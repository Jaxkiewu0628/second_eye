# AR 眼镜开发日志

---

## Phase 0 — 硬件 H.265 视频管道验证

**日期**：2026-06-24  
**执行人**：Zizheng Wu  
**目标**：验证 RV1106 硬件 H.265 编码管道可行性，端到端延迟 <150ms

---

### 硬件配置

| 参数 | 值 |
|---|---|
| 开发板 | Luckfox Pico Ultra W |
| SoC | Rockchip RV1106 (ARM Cortex-A7 @ 1.2GHz) |
| RAM | 256MB DDR3（系统可用 ~211MB） |
| 存储 | 16MB SPI NOR Flash |
| 摄像头 | CSI MIPI，SC3336（1/2.7"，2304×1296 max） |
| 网络 | WiFi 2.4GHz（802.11b/g/n） |
| 操作系统 | Buildroot Linux 5.10.160 |

---

### 软件环境

| 组件 | 版本/说明 |
|---|---|
| 固件 | `Luckfox_Pico_WebBee_Flash_250607`（Buildroot） |
| 媒体框架 | RKMPI（Rockit），uClibc 编译 |
| 视频管道 | VI → VENC（硬件 H.265） → RTSP |
| ISP | rkaiq（3A：自动曝光、自动白平衡、自动对焦） |
| 测试工具 | `simple_vi_bind_venc_rtsp` |
| 客户端 | VLC 3.x（macOS），`--rtsp-tcp` |

---

### 测试结果

#### 编码参数 & 延迟测量（秒表对比法，VLC `--network-caching=50`）

| 分辨率 | 码率 | 实测延迟 | 卡顿 |
|---|---|---|---|
| 1280 × 720（720p） | 2000 kbps | **~380ms** | 无 |
| 1920 × 1080（1080p） | 4000 kbps | **~440ms** | 无 |

测试方法：手机秒表置于摄像头前，截图对比 VLC 流内读数与实物读数之差。  
RTSP 地址：`rtsp://192.168.31.212/live/0`

#### 延迟拆解

| 组件 | 估算延迟 | 最终产品是否存在 |
|---|---|---|
| H.265 硬件编码 | ~50ms | ✓ 保留 |
| RTSP/RTP 封包 | ~10ms | ✗ 替换为本地显示 |
| WiFi 传输 | ~10ms | ✗ 本地显示无此路径 |
| VLC 缓冲 | 50ms | ✗ 替换为直接帧缓冲 |
| VLC H.265 解码 | ~15ms | ✗ 显示屏硬件解码 |
| 显示刷新 | ~16ms | ✓ 取决于屏幕规格 |
| **预计产品延迟** | **~80ms** | 目标 <150ms ✓ |

#### 画质评估（1080p）

| 指标 | 观察 |
|---|---|
| 分辨率 | 1080p，细节明显优于 720p，文字可读 |
| 色彩 | ISP 自动白平衡正常，色温中性偏暖 |
| 曝光 | ISP 自动曝光正常，室内光线下轻微欠曝 |
| 噪点 | 暗部有可见噪点，ISP 降噪参数未调优 |
| 帧率 | 目测流畅，约 25-30fps |
| 整体评级 | **满足 Phase 0 验证要求**，量产前需调优 ISP 参数 |

---

### 关键结论

1. **RV1106 硬件 H.265 编码正常工作**，720p 实时编码无压力
2. **Buildroot 固件是唯一可行路径**——Ubuntu（glibc）与 Rockchip 媒体库（uClibc）不兼容，无法使用硬件编码器
3. **端到端延迟可控**——WiFi+RTSP 测试链路约 380ms，去掉非产品路径组件后预计 <100ms，满足 <150ms 目标
4. **ISP 已启动**，自动 3A 正常，后续可通过调整 `rkipc.ini` 参数优化画质

---

### 遇到的问题与解决方案

| 问题 | 根本原因 | 解决方案 |
|---|---|---|
| Ubuntu 上 MPP 硬件编码 0 帧输出 | RV1106 硬件编码器不接受 CPU 分配内存，需 CMA buffer；Rockit 库为 uClibc 编译，Ubuntu glibc 不兼容 | 切换 Buildroot 固件 |
| DRM buffer 分配 `grp=NULL` | MPP 内部 DRM allocator 在 Ubuntu 上行为异常 | Buildroot 绕过此问题 |
| 摄像头画面黑暗（Ubuntu） | 无 rkaiq ISP 守护进程 | Buildroot 自动启动 rkaiq |
| 刷机后 SSH 指纹变化 | 固件重刷生成新 host key | `ssh-keygen -R 192.168.31.212` |

---

---

## Phase 0.5 — YOLO NPU 验证（2026-06-26，暂停）

**目标**：验证 RV1106 NPU 实时 YOLOv5 推理 + bounding box 叠加视频流

### 已完成
- ✅ YOLOv5 NPU 推理验证：控制台实时打印检测结果（person/laptop/cell phone 等 COCO 80类）
- ✅ 修改源码（`main.cc`）：640×480 分辨率，bbox 叠加后 raw BGR 输出到 stdout
- ✅ Docker 交叉编译成功（arm-rockchip830-linux-uclibcgnueabihf，uclibc）
- ✅ 二进制确认输出数据：15s 写入 94MB（约 102 帧，6~7fps）

### 遗留问题（暂停原因）
- RKMPI/RTSP pipeline 未集成（需重写为 VI→YOLO→VENC→RTSP，非 raw BGR stdout）
- h264_v4l2m2m 在 RV1106 上无效（需走 RKMPI API）
- 目前只能离线录制后播放，无法实时流式 demo

### 正确方向（下次接手）
- 用 `rk_mpi_vi.h` + `rk_mpi_venc.h`（已有头文件）替换 opencv-mobile capture
- 在 VI 回调中插入 RKNN 推理 + OpenCV 画框
- VENC 输出 → RKMPI RTSP server → VLC 打开 `rtsp://192.168.31.212/live/0`

---

### Phase 1 待办

- [ ] 提升分辨率至 1080p（1920×1080），验证编码性能
- [ ] 调优 ISP 参数（曝光、降噪、锐化）
- [ ] 测量实际 CPU 占用率（编码期间）
- [ ] 评估 H.264 vs H.265 在同画质下的码率差异
- [ ] 研究 MIPI DSI 显示输出路径（替代 WiFi RTSP）
- [ ] 评估在眼镜形态下的散热方案
