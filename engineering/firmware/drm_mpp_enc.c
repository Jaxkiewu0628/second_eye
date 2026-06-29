#define MODULE_TAG "drm_enc"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <drm/drm.h>
#include <drm/drm_mode.h>

/* Rockchip-specific CMA GEM allocation (not in public headers) */
struct drm_rockchip_gem_create { __u64 size; __u32 flags; __u32 handle; };
#define ROCKCHIP_BO_CONTIG   (1 << 0)
#define ROCKCHIP_BO_CACHABLE (1 << 1)
#define DRM_ROCKCHIP_GEM_CREATE 0x00
#define DRM_IOCTL_ROCKCHIP_GEM_CREATE \
    DRM_IOWR(DRM_COMMAND_BASE + DRM_ROCKCHIP_GEM_CREATE, \
             struct drm_rockchip_gem_create)
#include "rk_mpi.h"
#include "mpp_frame.h"
#include "mpp_packet.h"
#include "mpp_buffer.h"
#include "rk_venc_cfg.h"

#define WIDTH    640
#define HEIGHT   480
#define FPS      15
#define FRAMES   45
#define BITRATE  1000000

static long ms_now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1000L + ts.tv_nsec / 1000000L;
}

static int drm_alloc(int drm_fd, size_t size,
                     unsigned int *handle_out, int *dma_fd_out, void **ptr_out)
{
    unsigned int gem_handle;

    /* Try Rockchip CMA allocation first (physically contiguous — required for HW encoder) */
    struct drm_rockchip_gem_create rk = {
        .size  = (__u64)size,
        .flags = ROCKCHIP_BO_CONTIG | ROCKCHIP_BO_CACHABLE
    };
    if (ioctl(drm_fd, DRM_IOCTL_ROCKCHIP_GEM_CREATE, &rk) == 0) {
        gem_handle = rk.handle;
        printf("Rockchip CMA handle=%u\n", gem_handle);
    } else {
        perror("ROCKCHIP_GEM_CREATE (fallback to dumb)");
        struct drm_mode_create_dumb cd = { .width = (unsigned int)size, .height = 1, .bpp = 8 };
        if (ioctl(drm_fd, DRM_IOCTL_MODE_CREATE_DUMB, &cd)) { perror("CREATE_DUMB"); return -1; }
        gem_handle = cd.handle;
        printf("Dumb handle=%u (not CMA — encoder may fail)\n", gem_handle);
    }

    struct drm_prime_handle ph = { .handle = gem_handle, .flags = O_RDWR | O_CLOEXEC };
    if (ioctl(drm_fd, DRM_IOCTL_PRIME_HANDLE_TO_FD, &ph)) { perror("PRIME_TO_FD"); return -1; }
    printf("dma_fd=%d\n", ph.fd);

    struct drm_mode_map_dumb md = { .handle = gem_handle };
    if (ioctl(drm_fd, DRM_IOCTL_MODE_MAP_DUMB, &md)) { perror("MAP_DUMB"); return -1; }
    void *ptr = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_SHARED, drm_fd, md.offset);
    if (ptr == MAP_FAILED) { perror("mmap"); return -1; }

    *handle_out = gem_handle;
    *dma_fd_out = ph.fd;
    *ptr_out    = ptr;
    return (int)size;
}

int main(void) {
    /* ----- 1. Open DRM ----- */
    int drm_fd = open("/dev/dri/renderD128", O_RDWR | O_CLOEXEC);
    if (drm_fd < 0) { perror("open drm"); return 1; }
    printf("DRM opened fd=%d\n", drm_fd);

    size_t frame_sz = WIDTH * HEIGHT * 3 / 2;
    unsigned int gem_handle;
    int dma_fd;
    void *yuv_ptr;

    int alloc_sz = drm_alloc(drm_fd, frame_sz, &gem_handle, &dma_fd, &yuv_ptr);
    if (alloc_sz < 0) { close(drm_fd); return 1; }
    printf("DRM buffer mapped OK ptr=%p\n", yuv_ptr);

    /* Fill grey NV12 test frame */
    memset(yuv_ptr, 128, WIDTH * HEIGHT);
    memset((char *)yuv_ptr + WIDTH * HEIGHT, 128, WIDTH * HEIGHT / 2);

    /* ----- 2. Init MPP encoder ----- */
    MppCtx ctx   = NULL;
    MppApi *mpi  = NULL;
    MppEncCfg cfg = NULL;

    if (mpp_create(&ctx, &mpi)) { fprintf(stderr, "mpp_create\n"); return 1; }
    if (mpp_init(ctx, MPP_CTX_ENC, MPP_VIDEO_CodingHEVC)) { fprintf(stderr, "mpp_init\n"); return 1; }

    mpp_enc_cfg_init(&cfg);
    mpi->control(ctx, MPP_ENC_GET_CFG, cfg);
    mpp_enc_cfg_set_s32(cfg, "prep:width",        WIDTH);
    mpp_enc_cfg_set_s32(cfg, "prep:height",       HEIGHT);
    mpp_enc_cfg_set_s32(cfg, "prep:hor_stride",   WIDTH);
    mpp_enc_cfg_set_s32(cfg, "prep:ver_stride",   HEIGHT);
    mpp_enc_cfg_set_s32(cfg, "prep:format",       MPP_FMT_YUV420SP);
    mpp_enc_cfg_set_s32(cfg, "rc:mode",           MPP_ENC_RC_MODE_CBR);
    mpp_enc_cfg_set_s32(cfg, "rc:bps_target",     BITRATE);
    mpp_enc_cfg_set_s32(cfg, "rc:fps_in_flex",    0);
    mpp_enc_cfg_set_s32(cfg, "rc:fps_in_num",     FPS);
    mpp_enc_cfg_set_s32(cfg, "rc:fps_in_denorm",  1);
    mpp_enc_cfg_set_s32(cfg, "rc:fps_out_flex",   0);
    mpp_enc_cfg_set_s32(cfg, "rc:fps_out_num",    FPS);
    mpp_enc_cfg_set_s32(cfg, "rc:fps_out_denorm", 1);
    mpp_enc_cfg_set_s32(cfg, "rc:gop",            FPS * 2);
    mpp_enc_cfg_set_s32(cfg, "codec:type",        MPP_VIDEO_CodingHEVC);
    if (mpi->control(ctx, MPP_ENC_SET_CFG, cfg)) { fprintf(stderr, "set_cfg\n"); return 1; }
    printf("Encoder configured\n");

    FILE *out = fopen("/tmp/drm_enc_test.h265", "wb");
    if (!out) { perror("fopen"); return 1; }

    /* ----- 3. Encode loop ----- */
    long t0 = ms_now();
    int encoded = 0;

    for (int i = 0; i < FRAMES; i++) {
        /* Import DRM buffer as external DMA */
        MppBuffer ext_buf = NULL;
        MppBufferInfo binfo;
        memset(&binfo, 0, sizeof(binfo));
        binfo.type = MPP_BUFFER_TYPE_EXT_DMA;
        binfo.size = frame_sz;
        binfo.fd   = dma_fd;
        if (mpp_buffer_import(&ext_buf, &binfo)) {
            fprintf(stderr, "mpp_buffer_import failed frame %d\n", i); break;
        }

        MppFrame frame = NULL;
        mpp_frame_init(&frame);
        mpp_frame_set_buffer(frame, ext_buf);
        mpp_frame_set_width(frame, WIDTH);
        mpp_frame_set_height(frame, HEIGHT);
        mpp_frame_set_hor_stride(frame, WIDTH);
        mpp_frame_set_ver_stride(frame, HEIGHT);
        mpp_frame_set_fmt(frame, MPP_FMT_YUV420SP);
        mpp_frame_set_pts(frame, (long long)i * 1000 / FPS);
        if (i == FRAMES - 1) mpp_frame_set_eos(frame, 1);

        /* encode_put_frame takes ownership of frame+buffer — do NOT deinit them */
        int ret = mpi->encode_put_frame(ctx, frame);
        if (ret) { fprintf(stderr, "encode_put_frame %d: %d\n", i, ret); break; }

        /* first frame (IDR) can take longer — wait up to 2s */
        int max_tries = (i == 0) ? 1000 : 100;
        MppPacket pkt = NULL;
        for (int t = 0; t < max_tries && !pkt; t++) {
            mpi->encode_get_packet(ctx, &pkt);
            if (!pkt) usleep(2000);
        }
        if (pkt) {
            void *data = mpp_packet_get_pos(pkt);
            size_t len  = mpp_packet_get_length(pkt);
            fwrite(data, 1, len, out);
            printf("Frame %d: %zu bytes\n", i, len);
            mpp_packet_deinit(&pkt);
            encoded++;
        } else {
            fprintf(stderr, "timeout getting packet for frame %d\n", i);
            break;
        }
    }

    long elapsed = ms_now() - t0;
    fclose(out);
    printf("Encoded %d/%d in %ldms (%.1f fps)\n",
           encoded, FRAMES, elapsed, encoded * 1000.0 / elapsed);

    struct stat st;
    if (stat("/tmp/drm_enc_test.h265", &st) == 0 && elapsed > 0)
        printf("Output %ld bytes  bitrate %.0f kbps\n",
               (long)st.st_size,
               st.st_size * 8.0 / (elapsed / 1000.0) / 1000.0);

    /* Cleanup */
    mpp_enc_cfg_deinit(cfg);
    mpp_destroy(ctx);
    munmap(yuv_ptr, alloc_sz);
    close(dma_fd);
    struct drm_gem_close gc = { .handle = gem_handle };
    ioctl(drm_fd, DRM_IOCTL_GEM_CLOSE, &gc);
    close(drm_fd);
    return 0;
}
