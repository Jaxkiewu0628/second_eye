# AR 运动眼镜项目当前状态

> 单一事实源。最后更新：2026-06-29

## 一句话现状
软件能力验证(查公开基准)完成,**准备采购 RK3576 开发板做验证**;外观设计已出;下一步买板→搭环境→真机验证四项功能。**量产主芯片未定**(见下,RK3576 只是验证平台)。

## 核心定位与原则(北极星,开发/选材/设计都从此出发)
- **产品定位**:户外离线端侧眼镜(golf/登山/跑步/骑行/钓鱼…);**V1 楔子=高尔夫码数替代测距仪**,愿景=户外离线平台。
- **核心竞争优势:端侧优先,云端增强**——核心功能离线全可用,云端只做增强永不依赖(对手断网就废,我们不)。详见 [[edge-cloud-positioning]]。
- **硬约束**:主控必须有足够端侧算力跑核心功能离线(W517 NPU 够不够=硬门槛);离线优雅降级;功耗扛住占空比突发。

---

## 硬件决策

### RK3576 的真实角色(2026-06-29 诚实修正)
- ⚠️ **RK3576 不是量产镜框芯片**,是**验证平台**。客观核实:无任何眼镜用 RK3576;它定位是**边缘盒子/工业平板/NVR/车载**,功耗正常 1.2W、峰值 8.4W([T-Firefly](https://download.t-firefly.com/Spec/Mainboards/ROC-RK3576-PC_Specification_EN.pdf)),功耗/散热/封装不符合 <50g 一体式。
- ✅ **它能干的**:跑通软件(STT/TTS/YOLO/唤醒/联网)、给投资人演示、或放进**分体计算盒**(盒里功耗散热不是问题)。
- 早期"开发板直接嫁接量产 PCB"的说法**只在分体/盒子路线成立**,一体式镜框不成立。

### 量产镜框芯片:候选与倾向(待定)
- **关键认知:芯片不是差异化。** Ray-Ban/RayNeo/Rokid/Lenskart 全用同一颗 AR1,靠品牌/UX/垂直区分。我们的差异化在**高尔夫垂直 + 测距仪替代体验**,不在硅片。
- **Unisoc W517(倾向)**:可穿戴芯片(原 AI 手表平台),有**开放平台+免费SDK**(展锐×影目),中国方案商现成,成本低 → **可得性对无融资团队碾压 AR1**。弱点:NPU 弱(2-4 TOPS)、always-on 需外挂 GX8002、生态弱。([展锐W517](https://www.unisoc.com/cn_zh/home/TZNCD-W517-0))
- **Snapdragon AR1**:功耗/always-on 最佳,但 **NDA+ODM+MOQ+占BOM 37-50%**,无融资拿不到;且用它=站巨头同款平台被商品化。**仅获投+有ODM+要全程always-on全功能时才考虑。**
- **候选扩充(2026-06-29 检索)**:**RV1126B**(3 TOPS,1mW AOV 待机,**同 RKNN 生态→验证可迁移**,Luckfox Aura 可买)⭐、**爱芯 AX630C**(3.2 TOPS,<1.5W)、W517、AR1(❌NDA)。
- **"默认端侧"可行性结论**:算力够;连续满载无可及芯片塞进镜框;**"唤醒+主控常睡"占空比下成立**(全行业做法)。前提:**默认端侧=触发/突发,非连续全速**。
- **倾向**:量产主控倾向 **RV1126B 或 W517 类**(RV1126B 因 RKNN 生态可迁移、1mW 待机,可能更优)。
- **待验证**:RV1126B/AX630C 镜框内突发散热;W517 NPU 实测能力;方案商 MOQ。详见 [[chip-strategy]]。

### 验证板(已定)
- **野火鲁班猫3 LBC_3WB(4+32G,BTB)摄像头套餐**(含 IMX415 + 12V@2A),待采购
- 旧板 RV1106:STT 57× 慢于实时,仅历史参考
- 详见 [[project-hardware-decision]]、[[chip-strategy]]、全芯片调研 `docs/glasses_chip_rnd.md`

## 已验证(基于真实 RK3576 公开实测,非外推)
- ✅ STT：Paraformer hybrid RTF 0.29(快 3.4×)——避开 RV 陷阱。详见 [[stt-tts-validation]]
- ✅ TTS：Matcha+Vocos RTF 0.13,首音 ~320ms
- ✅ YOLO：YOLOv8n 真机 ~30fps / 纯推理 90fps;1080p 单路保守 25-40fps
- ✅ YOLOv8n→RKNN 工具链跑通(模型兼容,算子全过),**唯量化需 x86**(Mac QEMU 跑 SIGILL,改 Colab/真机)
- ⏸️ 云端 LLM 延迟脚本就绪(`prototype/llm_latency_bench.py`),待填 key 在真实网络测 TTFT

## 待采购清单
| 项 | 价 | 用途 |
|----|----|------|
| 鲁班猫3 LBC_3WB 摄像头套餐 | ~¥600 | 主板+IMX415+电源 |
| USB 麦克风 | ¥30-50 | STT/降噪 |
| USB 小音箱 | ¥20-30 | TTS |
| ESP32-S3 开发板 | ¥40-60 | 唤醒词+错峰架构验证 |
| USB 电流/功率计 | ¥30-60 | 错峰功耗测量(关键) |
| 杜邦线 | ¥10 | ESP32↔主板 |
| (可选)USB转TTL串口 | ¥10 | 首次点亮排错 |
| (可选)双麦阵列 | ¥50-100 | 降噪 beamforming |
| **不用买** | | DAP仿真器(Linux SoC不需要)、WiFi6模组(板载WiFi5够) |

## 板到货后验证四项功能
1. 本地降噪算法
2. 本地单独跑 YOLO
3. YOLO 与云端通用模型错峰(功耗 + 调度)
4. 本板直接联网

## 外观/结构设计(方案已出)
- 形态：包裹运动墨镜 + **扁平刀锋镜腿(Oakley 风格)**
- 主板位置：**右铰链刀锋宽体**(非细镜腿臂);计算岛净空 C1 = 30×24×5mm
- 摄像头：**右铰链角**(紧邻主板,走线短;单眼 HUD 同侧对齐)
- 散热：刀锋外侧铝合金平面迎风
- 续航：占空比模型,触发式 14h+,连续重载 ~2h(交给可选计算盒)
- 文档：见下

## 文档索引(docs/)
| 文件 | 内容 |
|------|------|
| chip_selection_brief.md | 芯片选型(会议用) |
| architecture_brief.md | 功耗/算力/唤醒/续航 |
| product_plan_draft.md | 双模架构产品方案 |
| rk3576_fit_and_voice_workflow.md | RK 契合度 + 本地 STT/TTS 流程优缺点 |
| shell_design_blade_temple.md | 刀锋镜腿设计方案(尺寸) |
| ID_design_spec.md (+.pdf) | 给设计团队的结构交接规格书 |
| models/ar_glasses.glb/.stl/.png | 简化 3D 模型 |

## 关键代码
| 文件 | 说明 |
|---|---|
| prototype/ai_voice_loop.py | 语音闭环(arecord→STT→Claude→TTS) |
| prototype/llm_latency_bench.py | 云端 LLM TTFT 延迟基准 |
| prototype/build_glasses_model.py | 3D 模型生成器 |
| rk3576_yolo_convert/ | YOLOv8n→RKNN 转换(x86 Docker,Mac 不能跑量化) |

## 开发约束(⚠️ 待与用户重新约定,见对话)
- Python 只装 `prototype/.venv/`,不改全局
- 对话中文(不用韩语)
- 大输出→重定向文件再 grep
- 每次对话开始只读本文件
