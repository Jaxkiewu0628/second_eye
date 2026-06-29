# AI 眼镜芯片选型简报

> 针对会议问题的调研结论 · 2026-06-26

---

## 一、有哪些芯片和 Snapdragon AR1 类似？

| 芯片 | 厂商 | NPU | WiFi/BT | 可及性 | 代表产品 |
|------|------|-----|---------|--------|---------|
| **Snapdragon AR1 Gen 1** | Qualcomm | ~4-6 TOPS | WiFi 6 + BT 5.3（集成） | ❌ 需 NDA/合作关系 | Ray-Ban Meta、RayNeo X2 Lite |
| **Snapdragon AR1+ Gen 1** | Qualcomm | 6 TOPS+ | WiFi 6E + BT 5.3 | ❌ 同上，2025新款 | 下一代眼镜产品 |
| **Snapdragon AR2 Gen 1** | Qualcomm | 更高 | 集成 | ❌ | Snap Spectacles 5（双芯） |
| **MediaTek（Meta下代）** | MediaTek | 4-8 TOPS | 集成 | ❌ 尚未公开发布 | Ray-Ban Gen 4+（2026-27） |
| **Unisoc W517** | 紫光展锐 | ~2-4 TOPS | WiFi 5 + BT 5.2 | ⚠️ 淘宝可买，生态弱 | 闪极 AI 拍拍镜 |
| **Rockchip RK3576** | 瑞芯微 | **6 TOPS** | WiFi 6 + BT 5.3（需外挂模组） | ✅ 立创¥165，生态成熟 | 野火鲁班猫3 等开发板 |
| **BES2800** | 恒玄科技 | 无 | BT only | ✅ 易购 | 纯音频协处理器（千问眼镜副芯片） |

**结论：** 市面上真正可及且算力达标的 AR1 替代只有 **RK3576**。MediaTek 路线是趋势但暂不可用，Unisoc 算力不足。

---

## 二、为什么竞品都选 Snapdragon AR1？

### 核心原因排序

#### 🥇 第一：Always-On 低功耗架构（决定性）

这是 AR1 真正不可替代的能力，也是其他通用 ARM 芯片无法直接复制的。

```
通用 ARM（如 RK3576）：
  主 CPU 待机 → 整个 SoC 耗电 50-100mW
  要检测唤醒词 → 必须唤醒全部 CPU → 500mW 峰值，延迟 2-3 秒

Snapdragon AR1：
  主 CPU 完全关闭 → 内置 Hexagon DSP 独立运行，仅 10-20mW
  持续监听麦克风 + 检测唤醒词 → 响应 <200ms
```

**实际意义：** 49g 眼镜配 210mAh 电池能待机 5-6 小时（Rokid 实测），这是 always-on 架构的直接结果。

#### 🥈 第二：Qualcomm "Aware" 参考平台（商业优势）

- Qualcomm 向 OEM 提供完整参考原理图 + 中间件（SNPE 推理引擎、音频 DSP 固件）
- Ray-Ban、RayNeo、Rokid 都是拿这套东西直接做产品，**出货时间 6-9 个月**
- 自研方案需要 **12-18 个月**

#### 🥉 第三：WiFi/BT/ISP 集成（方便，但非独家）

- AR1 集成 WiFi 6E + BT 5.3 + 摄像头 ISP
- **RK3576 同样可以做到**（通过外挂模组）
- 这个维度 AR1 没有独特优势

### 一句话总结

> AR1 被选中的核心是 **always-on 低功耗架构**，而不是 WiFi/BT/摄像头集成。集成生态只是加分项，真正的壁垒是 10-20mW 的传感器枢纽设计。

---

## 三、V1 选哪款芯片？

### V1 功能需求

- 通用 LLM 对话（云端 API）
- 本地 STT（语音转文字）
- 本地 TTS（文字转语音）
- 小视觉模型（YOLOv8 目标检测，~20fps）

### 算力需求估算

| 任务 | 所需算力 |
|------|---------|
| STT（Paraformer-small / Whisper tiny） | ~0.3-0.5 TOPS |
| TTS（Piper 等） | ~0.1-0.2 TOPS |
| YOLOv8n @ 20fps | ~0.3-0.5 TOPS |
| 三者同时运行合计 | ~0.7-1.2 TOPS |
| × 5 倍 headroom | **需要 ~5-6 TOPS** |

### 芯片选择：Rockchip RK3576

| 维度 | 评估 |
|------|------|
| NPU | **6 TOPS** ✅ 恰好满足 5× headroom |
| 系统 | Ubuntu 22.04 / Debian 12，glibc ✅ |
| STT | Sherpa-ONNX 直接 pip install，无需交叉编译 ✅ |
| 视觉 | RKNN-Toolkit2 支持 YOLOv5/v8 ✅ |
| WiFi | 外挂模组可达 WiFi 6 + BT 5.3 ✅ |
| 芯片单价 | ¥165（立创商城，可直接采购） ✅ |
| 量产路径 | 同款 SoC 有 SoM 模块，可直接设计底板嵌入眼镜 ✅ |

### 为什么不选 AR1？

1. **无法购买**：需要 Qualcomm 合作协议，初创团队不可及
2. **成本过高**：AR1 占整机 BOM 的 37-50%，连 Meta 都因此换 MediaTek
3. **V1 不需要 always-on**：验证阶段用按键/手势触发即可，always-on 是 V2 的事

### 开发板选择：野火 鲁班猫3（已采购）

- **型号：** LBC_3WB，4GB + 32GB，BTB 接口
- **配套：** IMX415 MIPI 摄像头（Sony，8MP）
- **补充：** USB 麦克风（¥30-50）+ 小音箱（¥20-30）
- **总成本：** ≈ ¥700 以内，完成 STT + TTS + YOLO 全链路验证

### V1 量产 BOM 估算（百片）

| 元件 | 单价 |
|------|------|
| RK3576 芯片 | ¥165 |
| 内存 4GB LPDDR4 | ¥60 |
| 存储 32GB eMMC | ¥40 |
| 摄像头（Sony IMX681） | ¥100 |
| 音频功放 + 麦克风 | ¥30 |
| IMU（TDK ICM-42688） | ¥25 |
| PMIC + 电源 | ¥25 |
| 电池（450mAh × 3节） | ¥40 |
| PCB 打板 + 贴片 | ¥150 |
| **合计** | **≈ ¥635/片（$88）** |

> 对比：Ray-Ban Meta 零售 $299（≈¥2100），有充足利润空间。

---

## 附：AR1 的 always-on 如何在 RK3576 方案中补齐（V2）

RK3576 本身无 always-on DSP，但可外挂低功耗 MCU 实现同等效果：

- **NationalChip GX8002**（闪极方案，70µW 待机，¥5-8）
- **Nordic nRF5340**（行业主流，BT 5.4，¥20-30）

这是 ¥20-30 的成本增量，V2 硬件迭代时加入即可。
