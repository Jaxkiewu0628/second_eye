#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sys/stat.h>

#include "rk_mpi_sys.h"
#include "rk_mpi_mb.h"
#include "rk_mpi_venc.h"
#include "rk_comm_venc.h"
#include "rk_comm_video.h"
#include "rk_comm_mb.h"
#include "rk_type.h"

#define WIDTH    1280
#define HEIGHT   720
#define FPS      30
#define FRAMES   90   /* 3 seconds */
#define BITRATE  2000 /* kbps */

static long ms_now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1000L + ts.tv_nsec / 1000000L;
}

int main(void) {
    RK_S32 ret;

    /* 1. System init */
    ret = RK_MPI_SYS_Init();
    if (ret != RK_SUCCESS) {
        fprintf(stderr, "RK_MPI_SYS_Init failed 0x%x\n", ret);
        return 1;
    }
    printf("SYS init OK\n");

    /* 2. Create MB pool for input frames */
    MB_POOL_CONFIG_S poolCfg;
    memset(&poolCfg, 0, sizeof(poolCfg));
    poolCfg.u64MBSize   = WIDTH * HEIGHT * 3 / 2;  /* NV12 */
    poolCfg.u32MBCnt    = 4;
    poolCfg.enRemapMode = MB_REMAP_MODE_CACHED;
    poolCfg.enAllocType = MB_ALLOC_TYPE_DMA;
    poolCfg.enDmaType   = MB_DMA_TYPE_CMA;
    poolCfg.bPreAlloc   = RK_FALSE;

    MB_POOL pool = RK_MPI_MB_CreatePool(&poolCfg);
    if (pool == MB_INVALID_POOLID) {
        fprintf(stderr, "RK_MPI_MB_CreatePool failed\n");
        RK_MPI_SYS_Exit();
        return 1;
    }
    printf("MB pool created\n");

    /* 3. Create VENC channel (H.265 CBR) */
    VENC_CHN_ATTR_S stAttr;
    memset(&stAttr, 0, sizeof(stAttr));
    stAttr.stVencAttr.enType         = RK_VIDEO_ID_HEVC;
    stAttr.stVencAttr.enPixelFormat  = RK_FMT_YUV420SP;
    stAttr.stVencAttr.u32PicWidth    = WIDTH;
    stAttr.stVencAttr.u32PicHeight   = HEIGHT;
    stAttr.stVencAttr.u32VirWidth    = WIDTH;
    stAttr.stVencAttr.u32VirHeight   = HEIGHT;
    stAttr.stVencAttr.u32StreamBufCnt = 4;
    stAttr.stVencAttr.u32BufSize     = WIDTH * HEIGHT * 3 / 2;
    stAttr.stVencAttr.enMirror       = MIRROR_NONE;
    stAttr.stRcAttr.enRcMode         = VENC_RC_MODE_H265CBR;
    stAttr.stRcAttr.stH265Cbr.u32BitRate = BITRATE;
    stAttr.stRcAttr.stH265Cbr.u32Gop    = FPS * 2;

    ret = RK_MPI_VENC_CreateChn(0, &stAttr);
    if (ret != RK_SUCCESS) {
        fprintf(stderr, "RK_MPI_VENC_CreateChn failed 0x%x\n", ret);
        RK_MPI_MB_DestroyPool(pool);
        RK_MPI_SYS_Exit();
        return 1;
    }
    printf("VENC channel created\n");

    VENC_RECV_PIC_PARAM_S stRecvParam;
    memset(&stRecvParam, 0, sizeof(stRecvParam));
    stRecvParam.s32RecvPicNum = -1;
    RK_MPI_VENC_StartRecvFrame(0, &stRecvParam);

    FILE *out = fopen("/tmp/rockit_test.h265", "wb");
    if (!out) { fprintf(stderr, "open output failed\n"); return 1; }

    long t0 = ms_now();
    int encoded = 0;

    for (int i = 0; i < FRAMES; i++) {
        /* Get MB and fill with grey NV12 */
        MB_BLK blk = RK_MPI_MB_GetMB(pool, WIDTH * HEIGHT * 3 / 2, RK_TRUE);
        if (blk == MB_INVALID_HANDLE) {
            fprintf(stderr, "GetMB failed at frame %d\n", i);
            break;
        }

        void *ptr = RK_MPI_MB_Handle2VirAddr(blk);
        memset(ptr, 128, WIDTH * HEIGHT);
        memset((char*)ptr + WIDTH * HEIGHT, 128, WIDTH * HEIGHT / 2);

        /* Build VIDEO_FRAME_INFO_S */
        VIDEO_FRAME_INFO_S stFrame;
        memset(&stFrame, 0, sizeof(stFrame));
        stFrame.stVFrame.pMbBlk         = blk;
        stFrame.stVFrame.u32Width       = WIDTH;
        stFrame.stVFrame.u32Height      = HEIGHT;
        stFrame.stVFrame.u32VirWidth    = WIDTH;
        stFrame.stVFrame.u32VirHeight   = HEIGHT;
        stFrame.stVFrame.enPixelFormat  = RK_FMT_YUV420SP;
        stFrame.stVFrame.u64PTS         = (RK_U64)i * 1000000 / FPS;

        ret = RK_MPI_VENC_SendFrame(0, &stFrame, 200);
        RK_MPI_MB_ReleaseMB(blk);
        if (ret != RK_SUCCESS) {
            fprintf(stderr, "SendFrame %d failed 0x%x\n", i, ret);
            break;
        }

        /* Get encoded packet */
        VENC_STREAM_S stStream;
        stStream.pstPack = malloc(sizeof(VENC_PACK_S));
        ret = RK_MPI_VENC_GetStream(0, &stStream, 500);
        if (ret == RK_SUCCESS) {
            void *data = RK_MPI_MB_Handle2VirAddr(stStream.pstPack->pMbBlk);
            fwrite(data, 1, stStream.pstPack->u32Len, out);
            if (encoded == 0)
                printf("First packet: %u bytes\n", stStream.pstPack->u32Len);
            RK_MPI_VENC_ReleaseStream(0, &stStream);
            encoded++;
        } else {
            fprintf(stderr, "GetStream %d failed 0x%x\n", i, ret);
        }
        free(stStream.pstPack);
    }

    long elapsed = ms_now() - t0;
    fclose(out);

    printf("Encoded %d/%d frames in %ldms (%.1f fps)\n",
           encoded, FRAMES, elapsed, encoded * 1000.0 / elapsed);

    struct stat st;
    if (stat("/tmp/rockit_test.h265", &st) == 0)
        printf("Output: %ld bytes  avg bitrate: %.0f kbps\n",
               (long)st.st_size, st.st_size * 8.0 / (elapsed / 1000.0) / 1000.0);

    RK_MPI_VENC_StopRecvFrame(0);
    RK_MPI_VENC_DestroyChn(0);
    RK_MPI_MB_DestroyPool(pool);
    RK_MPI_SYS_Exit();
    return 0;
}
