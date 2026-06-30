# Second Eye — 全球竞品扫描 (pivot 后) / Global Competitor Scan

> 多 agent 全球扫描，2026-07-01。覆盖 **157 个竞品**（23 高威胁 · 36 巨头 · 24 已死），8 路角度/地域并行 + 对抗式核实 + 完整性补漏。
> 服务 S2（竞争/护城河）讨论。原始数据：workflow `global-competitor-scan`。评估框架（科技铁律）：① 不蹈前辈覆辙 ② 不和巨头硬抢 ③ 不做同质化 ④ 只有没见过的新组合才做得起来。

## ⭐ 核心结论（诚实，会让人不舒服但必须面对）
**我们今天没有"功能"护城河，只有"组合 + 时机 + 渠道"的潜在护城河，窗口以 12–24 个月计。** 我们原来的四条差异化主张，三条已被抹平：
- **"离线"** = 已是 table stakes，**不是 moat**：NOA、.lumen、Ara、Apple Magnifier、大量学术栈（YOLO+depth）全都离线。最可信的对手 .lumen CEO 明确说"过街不能容忍云延迟"——**离线=mobility 安全，这点是对的，但人人都懂，守不住**。
- **"无订阅/一次性付费"** = 已被抹平：NOA、Ara、.lumen、WeWALK、EchoVision 免费层都有。我们只在**"免费完整安全基线"**上还差异。
- **"云端自学习 agent"** = **最脆弱、不可守**：Brilliant Labs Halo（Narrative 记忆）、Rabbit LAM、OpenAI io（"Sweetpea"，40–50M 量级）都在做"越用越懂你"，巨头在定义这层。
- **唯一还空着的**：`mobility-safety-grade + sub-$700 + 30g 分体轻形态` 的**组合**。

## 竞争格局（7 桶）
1. **巨头红海 — 消费 AI 眼镜（避开正面）**：Meta Ray-Ban/Oakley + Be My Eyes + Live AI（$299–799，~80% 市占，EssilorLuxottica 全渠道）、Google Android XR/Astra + Aira、Apple（传闻）、华为/小米/字节/百度/Rokid。→ **绝不在"读字/识物/场景描述/叫志愿者"上正面抢**；这是巨头用免费+全渠道占的地盘。
2. **视障 mobility 在位者（真正战场）**：biped **NOA**（最强功能对手，$3k+背心/可选订阅，Honda IP，已发货 20+ 国）、**.lumen**（€9,999 头盔，最强 mobility，离线，但 1kg+16x 价）、WeWALK 智能拐杖、Ara/Strap（胸挂触觉 $2,750）、Glide（轮式机器人 $1,499+$30/mo）、TAMI（瑞士雷达眼镜）。
3. **中国低价 mobility 眼镜（形态+价格最贴近，高威胁）**：**瞳行科技**（¥3,399/~$470，Qwen-VL，300ms 避障，45g，已发货）、**KRETA 克里特**（3 代避障眼镜）、SHG India Aura（离线+避障+OCR，~$590）、视氪（已死同架构）、启明（$95 雷达眼镜，最低价锚）。→ 多为**云依赖/中国残联渠道专属**，是缝隙，但窗口在收窄。
4. **死掉的前辈（教训，非对手）**：OrCam（$4,490 读字王，关闭视觉部门）、Toyota BLAID、Horus/Eyra（~$2k，几乎我们的架构，融 $900K 死掉）、BrainPort、Microsoft Soundscape（免费受爱戴，关 Azure 后端即 bricked）、Google Glass EE/Guideline。
5. **免费 app 地板（commodity 压顶）**：Seeing AI、Google Lookout、Be My Eyes/Be My AI、Apple Magnifier（LiDAR 离线检测门/人，但**自述"不可用于导航"**——主动让出 mobility-safety）。→ 读字/场景/找东西被永久 $0 化，我们只能当**免费 bonus**。
6. **医疗护理 + 体征（扩张方向，远期）**：Vuzix（医院 AR 平台）、Masimo/BioIntelliSense/VitalConnect（体征数据层）、**护士-体征 AR overlay（学术，2025 已原型，~30% 文档时间↓，high/high）**。→ 我们的"护工看体征"已被抢跑；**phase-2，今天不碰**；体征巨头是未来整合伙伴非对手。
7. **AI 可穿戴新贵 / 学习 agent（借鉴 + 警示）**：Brilliant Labs Halo（最接近技术配方：眼镜+骨传导+边缘AI+记忆 agent，但 sighted）、Plaud（freemium 范本）、Rabbit、OpenAI io。

## Top threats（排序）
| # | 竞品 | 为什么危险 | 级别 |
|---|---|---|---|
| 1 | **Meta Ray-Ban + Be My Eyes + Live AI** | ~80% 市占、$299 起、免费助盲层、全渠道；正把品类心智锚成"AI 助盲=免费"；Live AI 走向连续免提=我们 wedge 方向。产品重叠仍低（无 ToF/非安全级/云依赖），但**威胁是战略级**。盯防=Meta 上 ToF / 连续 watch mode。 | 高 |
| 2 | **biped NOA** | 最强功能对手、最接近我们 wedge：同骨传导、同离线核+云可选、同平台路线，Honda 自驾 IP，同行评审数据，O&M 训练师渠道。**抹平了我们"离线""无订阅"两条主张**。 | 高 |
| 3 | **瞳行 / KRETA 中国低价群** | 形态（眼镜）+价格（~$420–590）几乎与我们重叠，已发货，**直接削弱"没人做过的新组合"**。多为云依赖/中国渠道——缝隙，但若走真离线+出海则升为正面冲突。 | 高 |
| 4 | **Google Android XR + Aira** | 巨头+Warby Parker 全渠道+明确点名盲人（与 Aira 合作）；Aira 已有视障关系与**报销足迹**（正是我们要建的渠道）。 | 高 |
| 5 | **EchoVision $599 / Ally Solos $699** | **形态+价格最接近我们**的可负担眼镜；但云依赖、reading/scene-first、**无实时避障 wedge**——留出我们 mobility-safety 缝隙。 | 高 |
| 6 | **护士-体征 AR overlay + Vuzix** | 我们护工扩张方向**已被抢跑**（学术原型）；phase-2 红旗。 | 中 |
| 7 | **iFlytek 科大讯飞** | 中国 AI 巨头+国家级残联(CDPF)渠道，点名盲人眼镜；今日还是 R&D，但渠道无敌——"不要把中国当 beachhead"的结构性理由。 | 中 |
| 8 | **Halo / OpenAI io** | 专门威胁我们"自学习 agent"差异化；让投资人问"为什么 OpenAI/Meta 不直接做"。agent **不是可守护城河**。 | 中 |

## 我们的 whitespace（framework ④，诚实版）
单点功能几乎全被做过（离线✓ 避障✓ 眼镜形态✓ 骨传导✓ freemium✓ ToF✓ agent✓）。**真正空白 = 这个五元组的交集，无一家同时占满**：
> **sub-$700 + 真·完整离线免费安全基线 + 30g 分体眼镜(轻框+颈挂盒) + 安全级(ToF+端侧YOLO+骨传导)实时 mobility + 西方支付渠道(VA/voc-rehab)**

逐一点破最近的占位者：NOA 占了离线+mobility+平台**但 $3k+背心/订阅/欧美高端**；.lumen 占了最强 mobility **但 €9,999 头盔**；瞳行/KRETA 占了便宜眼镜**但云依赖+中国渠道**；EchoVision/Ally 占了 $599–699 眼镜**但云依赖+reading-first+无避障**；Halo 占了技术配方**但 sighted**。**结论：whitespace 不是任何单一功能，而是"把 NOA 的能力做到瞳行的价格、SHG 的离线，装进比所有人都轻的分体眼镜，走 Meta 让出的 mobility-safety 角落，用 Aira 尚未锁死的西方报销渠道"——这个交集现在空着，每条边都有人逼近，窗口 12–24 个月。**

## 护城河评级（诚实）
- **最耐久 = 分发/信任/支付渠道**：VA/voc-rehab 报销 + 盲人社区信任 + O&M 训练师网络。这是 NOA 领先我们的地方，也是我们能建的真壁垒。（参照：AT&T CarePlus $6k/终身已覆盖 Aira/eSight/NuEyes/OrCam——**要么进这个名单，要么被锁在外**。）
- **中等 = 安全级工程可靠性 + 真端侧**：实时深度避障的 lab-to-field 稳定性、分钟可学、信号无关。
- **最弱 = 技术配方本身**：开源 YOLO+depth、Mentra 开放眼镜 OS、学术论文证明整套架构可 cheap 复制。**配方不是 moat。**
- **本质：护城河 = 执行速度 × 渠道深度 × 组合完整性，不是任何单一 feature。**

## 前辈覆辙（framework ①，对应我们的设计纪律）
- **Reading 不能是 reason-to-buy** — OrCam 关闭整个视觉部门，自述"LLM 让低视力开发没必要"。→ OCR/场景只能免费 bonus、绝不收费、绝不当头条。
- **不依赖别人的硬件平台或云后端** — Envision 建在 Google Glass 被 EOL 孤儿化；Soundscape 关 Azure 即 bricked。→ 自有 BOM、真端侧、**无云 kill-switch**（这正是 freemium 基础必须完整离线的存在理由）。
- **$2k+ 进小市场需厚资本或极低 BOM** — Horus 几乎是我们的架构（立体相机+端侧+骨传导）十年前，只融 $900K，never industrialized。→ 要么 sub-$700 低 BOM、要么大融资。
- **感知替代必须分钟内学会** — BrainPort（$10k 舌电极）被数月学习曲线杀死。
- **单功能可穿戴是 feature 不是公司** — BuzzClip/Sunu/Humane Pin/Bee 反复证明（多被巨头吸收）。→ mobility 单点必须能扩成平台。
- **freemium 正面教材 = Plaud**（专注单一 job + 干净免费阶梯，商业健康）；反面 = Friend（me-too 情感陪伴遭 backlash）。

## S2 给 CEO 的 8 条可执行结论
1. **重写 messaging 层级**：头条只讲 **"安全级实时避障(ToF+骨传导，无信号也工作) + sub-$700 + 比所有人都轻的分体眼镜"**。**立即从对外卖点删掉"离线""无订阅""自学习 agent"作为独立主张**——已同质化，会显得 me-too。离线只作为"安全级 mobility 的必要条件"来讲。
2. **头号盯防 = NOA(功能基准) + Meta(分发/品类定义)**，不是 .lumen 或中国群。季度 watch：Meta 上 ToF/连续 watch mode、NOA 出眼镜形态、瞳行/KRETA 走真离线+出海——任一触发=威胁升级。
3. **渠道是真护城河，优先于功能**：尽早启动 VA/voc-rehab 报销路径（进 AT&T CarePlus 那类名单）+ 盲人社区信任共建（NFB/ACB，对标 EchoVision）。比多加一个功能更耐久。
4. **不要把中国当 beachhead**：iFlytek 国家级渠道 + 瞳行/KRETA 低价群，硬碰必输；用西方+真离线+支付渠道在他们弱的市场建壁垒。
5. **护工体征 = phase-2，今天不碰**：护士 AR overlay 已抢跑 + Vuzix 医院在位 + 体征巨头数据链；先在盲人 mobility 站稳。
6. **self-learning agent 降级**为 wedge 内增强（"越用越懂你的常走路线/障碍"），绝不对外定位成通用 agent。
7. **速度是一切**：组合护城河窗口 12–24 个月，每条边都有人逼近。与其追功能完整，不如最快在"西方 mobility-safety + 支付渠道信任"建立不可逆领先。
8. **借 graveyard 守纪律**：自有 BOM、无云 kill-switch、分钟可学、reading 永远免费 bonus——这些是 pivot 后定位的生死线。
