# Second Eye — 工程状态

> 工程单一事实源。最后更新：2026-06-30
> Claude 每次对话读这个文件，不读根目录 STATUS.md。

## 一句话现状
项目更名 **Second Eye**，转向视障辅助设备。
**V1 芯片定板：眼镜框 RV1106G3 + 颈挂盒 RK3576。逼近 NOA 的传感器升级（雷达+朝下ToF）推到 V2。**
**鲁班猫3 + IMX415 + VL53L5CX ToF 预计 2026-07-01 到货，板到即开始验证。**

---

## 核心定位（北极星）
- **产品**：帮助视障人士独立出行的 AI 眼镜
- **核心功能**：YOLO11n 实时识别障碍物 → 骨传导语音"前方 1.5 米台阶"
- **硬约束**：完全离线可用（对视障用户是安全要求，非可选特性）
- **形态**：眼镜框（轻量，~27g，目标≤35g）+ 颈挂计算盒（V1 短线缆，V2 无线）

---

## 硬件决策

### V1 芯片方案（2026-06-30 拍板）
**眼镜框 RV1106G3 + 颈挂盒 RK3576。** 用手头的鲁班猫3（RK3576）做 V1 快速上市，量产成本优化（RV1126B）留后面。
- **眼镜框：RV1106G3**（原生 MIPI-CSI + H.265 编码 + AIC8800DC WiFi/BT），取代原 ESP32-S3——ESP32 没有相机接口/视频流能力。⚠️ 已知 Issue #359：NPU+ISP 同跑会争 AXI 总线 → 眼镜框**不在框内跑 NPU**，只做相机流+音频，YOLO 在颈挂盒，架构上规避。
- **颈挂盒：RK3576**（6 TOPS，已验证、零迁移），跑 YOLO11n + STT/TTS。

### 验证板（在途，预计 2026-07-01 到货）
- **野火鲁班猫3 LBC_3WB（4+32G，BTB）摄像头套餐**（含 IMX415 + 12V@2A）~¥600
- 即 RK3576，V1 颈挂盒就用它。

### 量产主控（V1 后优化，待上板功耗实测后定）
- **RK3576**：V1 用，6 TOPS、$30-40、~3-4W，BOM 偏高但最快上市
- **RV1126B**：量产成本优化候选（3 TOPS，~2.8W，更便宜），上板对比功耗后再决定是否切换
- ❌ AX630C（量产不可用：BSP 闭源/固件不稳）· ❌ Snapdragon AR1（NDA 拿不到）

### 传感器（V1）
- **VL53L5CX**（ST，8×8 ToF，±10mm，4m，60Hz）— 在途 ~¥40
- **ICM-42688** IMU — 省电门控 + 跌倒检测

### 传感器（V2，逼近 NOA，本期不做）
- **60GHz 毫米波雷达** + **第二颗朝下 ToF**（drop-off）— 详见 memory `project-v2-noa-sensors`；V1 BOM/重量不含

---

## 已验证（RK3576 公开实测，直接复用）
- ✅ STT：Paraformer RTF 0.29（实时 3.4×）
- ✅ TTS：Matcha+Vocos RTF 0.13，首音 ~320ms
- ✅ YOLO11n：RKNN 格式 ~10fps（99.5ms/帧），工具链跑通
- ✅ H.265 视频管道：1080p 实测，端到端预估 <200ms
- ✅ 占空比架构可行

## 上板验证计划（板到即执行，按序）

**Step 1 — 系统启动**
- 刷 Ubuntu 22.04，SSH 登录，确认 RKNN-Toolkit2 / Python 环境
- IMX415 摄像头 `/dev/video0` 出图

**Step 2 — YOLO11n 推理**
- 跑 `tools/rk3576_yolo_convert/` 转换脚本，生成 `.rknn`
- 连续推理 1 小时：记录 fps、CPU 温度、实际功耗（USB 电流计）
- 验收：≥10fps，温度 <80°C，功耗 <2.5W

**Step 3 — VL53L5CX ToF**
- I2C 驱动，读取 8×8 距离矩阵
- 与 YOLO bounding box 融合：输出"前方 X 米有障碍"

**Step 4 — 语音闭环**
- 复用 `prototype/ai_voice_loop.py`
- Paraformer STT → 规则推理 → Matcha TTS → 骨传导播报
- 记录 RTF，验收：STT RTF <1（实时）

**Step 5 — 完整链路 E2E**
- 摄像头 → YOLO → ToF 融合 → TTS → 骨传导
- 端到端延迟目标 <300ms
- 连续运行 1 小时，记录功耗，验证颈挂盒续航

**关键风险（上板后立刻测）**
- Paraformer 在 RK3576 上的 RTF 需实测（非从公开数据复用）
- VL53L5CX I2C 地址 + 驱动兼容性未验证

---

## 待采购清单
| 项 | 价格 | 用途 |
|----|------|------|
| 鲁班猫3 LBC_3WB 摄像头套餐 | ~¥600 | 主验证板 | **在途** |
| VL53L5CX ToF 模块 | ¥30-60 | 精确测距 | **在途** |
| ICM-42688 IMU 模块 | ¥20-40 | 运动补偿 + 跌倒检测 |
| USB 骨传导耳机（开发测试用）| ¥80-150 | 音频反馈验证 |
| 双麦克风阵列 | ¥50-100 | 降噪 |
| USB 电流计 | ¥30-60 | 连续功耗测量 |
| 5000mAh LiPo 模块 | ¥80-120 | 颈挂盒原型电池 |
| Luckfox Pico Ultra W（RV1106G3+AIC8800DC）| ~¥200 | 眼镜框芯片验证 + BT A2DP 实测 |

> 注：ESP32-S3 已从眼镜框方案移除（改 RV1106G3）。唤醒词放颈挂盒 RK3576 或 RV1106G3。

---

## 架构图（分体式）
```
眼镜框 (~27g, 目标≤35g)        颈挂计算盒 (~150g)
┌──────────────────┐  ~25cm   ┌────────────────────┐
│ IMX415 (MIPI-CSI)│ ──线缆── │ RK3576 (6 TOPS)    │
│ VL53L5CX ToF     │          │ 5000mAh 电池        │
│ 骨传导振子        │          │ WiFi + BT (App同步) │
│ 双麦克风          │          │ 颈挂/腰挂两用        │
│ RV1106G3+AIC8800 │          └────────────────────┘
└──────────────────┘
端到端延迟：RK3576 ~185ms（< 300ms 目标）
续航（HO-005 供电预算，待上板实测 ⏳）：
  加权功耗 ~1.9W（全速3.8W·巡航2.1W·静止0.9W）
  5000mAh→14.4Wh → 典型 ~7.5h，最坏全速 ~3.8h
  全天靠充电盒；旧"13.7h@1.1W"数字作废
重量（HO-005 零件分解，待样机实测 ⏳）：~26.7g，≤35g 可达
```

---

## 功能优先级

**V1（板到货即验证）**
- 障碍物检测 + 骨传导告警（YOLO11n + ToF 融合）— 必做核心
- 本地语音指令（STT → 规则推理 → TTS）— 必做核心
- 唤醒词（RK3576 或 RV1106G3 + WakeNet）
- 文字识别 OCR（按需触发，免费 bonus，硬件零增量）
- 数据飞轮设备侧钩子（难例触发器 + 本地环形缓冲 + 默认关闭的 opt-in 上传，见 HO-007）

**V1.5**
- 交通灯识别（红/绿）
- 斑马线检测
- 云端 LLM 场景描述（VLM 离线不可行，走云端 API，发文字不发图）

**V2**
- 完全无线（本地 WiFi P2P）
- 跌倒检测 + 紧急呼叫
- 单目深度估计（Depth Anything V2）
- **逼近 NOA 传感器升级**：60GHz 毫米波雷达（类别无关障碍+测速）+ 朝下 ToF（drop-off）— 有成本余量再上，见 memory `project-v2-noa-sensors`

---

## 文件索引
| 路径 | 内容 |
|------|------|
| `hardware/docs/architecture_brief.md` | 功耗/算力/续航分析 |
| `hardware/docs/glasses_chip_rnd.md` | 芯片全景调研 |
| `hardware/docs/ID_design_spec.md` | 外观结构规格书 |
| `hardware/docs/hardware_rnd_workflow.md` | 硬件调研标准流程 |
| `hardware/models/` | 3D 模型（glb/stl/png）|
| `firmware/` | C 代码（RV1106 MPP / Rockit）|
| `prototype/ai_voice_loop.py` | 语音闭环脚本（可直接复用）|
| `tools/rk3576_yolo_convert/` | YOLOv8/11→RKNN 转换工具链 |
| `reference/ycane_2023/` | 2023 YCane 专利 + PPT |

## 约束
- Python 只装 `prototype/.venv/`，不动全局
- 对话用中文
- 大输出 → 重定向文件再 grep
