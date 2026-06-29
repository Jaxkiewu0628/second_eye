#define MODULE_TAG "enc_test"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sys/stat.h>
#include "rk_mpi.h"
#include "mpp_frame.h"
#include "mpp_packet.h"
#include "mpp_buffer.h"
#include "mpp_task.h"
#include "mpp_meta.h"
#include "rk_venc_cfg.h"

#define WIDTH    1280
#define HEIGHT   720
#define FPS      30
#define FRAMES   90
#define BITRATE  2000000

static long ms_now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1000L + ts.tv_nsec / 1000000L;
}

int main(void) {
    MppCtx ctx = NULL;
    MppApi *mpi = NULL;
    MppEncCfg cfg = NULL;
    int ret;

    ret = mpp_create(&ctx, &mpi);
    if (ret) { fprintf(stderr, "mpp_create failed %d\n", ret); return 1; }

    ret = mpp_init(ctx, MPP_CTX_ENC, MPP_VIDEO_CodingHEVC);
    if (ret) { fprintf(stderr, "mpp_init failed %d\n", ret); return 1; }

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
    ret = mpi->control(ctx, MPP_ENC_SET_CFG, cfg);
    if (ret) { fprintf(stderr, "set_cfg failed %d\n", ret); return 1; }
    printf("Encoder configured OK\n");

    FILE *out = fopen("/tmp/mpp_test.h265", "wb");
    if (!out) { fprintf(stderr, "open output failed\n"); return 1; }

    long t0 = ms_now();
    int encoded = 0;

    for (int i = 0; i < FRAMES; i++) {
        /* --- INPUT: dequeue input task, get pre-allocated frame --- */
        ret = mpi->poll(ctx, MPP_PORT_INPUT, MPP_POLL_BLOCK);
        if (ret) { fprintf(stderr, "poll input %d: %d\n", i, ret); break; }

        MppTask task = NULL;
        ret = mpi->dequeue(ctx, MPP_PORT_INPUT, &task);
        if (ret || !task) { fprintf(stderr, "dequeue input %d: %d\n", i, ret); break; }

        MppFrame frame = NULL;
        mpp_task_meta_get_frame(task, KEY_INPUT_FRAME, &frame);
        if (!frame) { fprintf(stderr, "no frame in input task %d\n", i); break; }

        /* fill the pre-allocated buffer with grey NV12 */
        MppBuffer buf = mpp_frame_get_buffer(frame);
        if (buf) {
            void *ptr = mpp_buffer_get_ptr(buf);
            if (ptr) {
                memset(ptr, 128, WIDTH * HEIGHT);
                memset((char*)ptr + WIDTH * HEIGHT, 128, WIDTH * HEIGHT / 2);
                if (i == 0) printf("Frame buffer OK: %p\n", ptr);
            }
        } else {
            fprintf(stderr, "frame %d has no buffer\n", i);
        }

        mpp_frame_set_width(frame, WIDTH);
        mpp_frame_set_height(frame, HEIGHT);
        mpp_frame_set_hor_stride(frame, WIDTH);
        mpp_frame_set_ver_stride(frame, HEIGHT);
        mpp_frame_set_fmt(frame, MPP_FMT_YUV420SP);
        mpp_frame_set_pts(frame, (long long)i * 1000 / FPS);
        if (i == FRAMES - 1) mpp_frame_set_eos(frame, 1);

        mpp_task_meta_set_frame(task, KEY_INPUT_FRAME, frame);
        ret = mpi->enqueue(ctx, MPP_PORT_INPUT, task);
        if (ret) { fprintf(stderr, "enqueue input %d: %d\n", i, ret); break; }

        /* --- OUTPUT: get encoded packet --- */
        ret = mpi->poll(ctx, MPP_PORT_OUTPUT, MPP_POLL_BLOCK);
        if (ret) { fprintf(stderr, "poll output %d: %d\n", i, ret); break; }

        task = NULL;
        ret = mpi->dequeue(ctx, MPP_PORT_OUTPUT, &task);
        if (ret || !task) { fprintf(stderr, "dequeue output %d: %d\n", i, ret); break; }

        MppPacket pkt = NULL;
        mpp_task_meta_get_packet(task, KEY_OUTPUT_PACKET, &pkt);
        if (pkt) {
            void *data = mpp_packet_get_pos(pkt);
            size_t len  = mpp_packet_get_length(pkt);
            fwrite(data, 1, len, out);
            if (encoded == 0) printf("First packet: %zu bytes\n", len);
            encoded++;
        }
        mpi->enqueue(ctx, MPP_PORT_OUTPUT, task);
    }

    long elapsed = ms_now() - t0;
    fclose(out);

    printf("Encoded %d/%d frames in %ldms  %.1f fps\n",
           encoded, FRAMES, elapsed, encoded * 1000.0 / elapsed);

    struct stat st;
    if (stat("/tmp/mpp_test.h265", &st) == 0 && elapsed > 0)
        printf("Output: %ld bytes  avg bitrate: %.0f kbps\n",
               (long)st.st_size, st.st_size * 8.0 / (elapsed / 1000.0) / 1000.0);

    mpp_enc_cfg_deinit(cfg);
    mpp_destroy(ctx);
    return 0;
}
