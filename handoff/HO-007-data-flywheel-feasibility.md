# HO-007 — 真实世界行走数据飞轮:工程怎么做(评估) / data flywheel feasibility

**📌 In a line / 一句话:** 数据飞轮是我们唯一可能"永久"的技术护城河,但和"全离线/隐私"有张力;请老哥评——怎么在不破坏离线/隐私的前提下采集真实行走数据、训练改进、把飞轮转起来。/ The real-world walking-data flywheel is our only potentially-permanent tech moat, but it conflicts with "fully offline / privacy" — ENG please assess how to collect data, train, and spin it up without breaking that promise.

| Field / 字段 | Value / 值 |
|---|---|
| **From → To / 方向** | `CEO → ENG` |
| **State / 状态** | ✅ 已完成（archived） |
| **Priority / 优先级** | normal(护城河/方向输入;不改 V1 排期,但可能建议 V1 埋钩子) |
| **Created / 创建** | 2026-07-01 |
| **Updated / 更新** | 2026-06-30 |
| **Related / 关联** | `business/strategy/product-bets.md`(Bet 3)· `business/strategy/competitive-scan-2026-07.md` · `engineering/STATUS.md` |

**TL;DR (bilingual / 双语一句话)**
- **EN:** Moat analysis (Bet 3) concluded the **real-world walking-data flywheel** is our only potentially-permanent technical moat (more users → more real obstacle/false-alarm data → better avoidance → more users; latecomers have no data). But it conflicts with our core promise of **fully offline + privacy**. Please assess, as engineering: how do we collect useful real data WITHOUT breaking offline/privacy, what to collect, how to label, how to close the training loop, and whether V1 should bake in a data hook now.
- **中文:** 护城河分析(Bet 3)结论:**真实世界行走数据飞轮**是我们唯一可能"永久"的技术护城河(用户越多 → 真实障碍/误报数据越多 → 避障越准 → 用户越多;后来者没数据)。但它和我们的核心承诺"**全离线 + 隐私**"冲突。请你从工程评估:怎么在不破离线/隐私的前提下采到有用的真实数据、采什么、怎么标注、训练闭环怎么搭、V1 要不要先埋数据钩子。

## Context / 背景
我们 CEO 侧把护城河定了:数据飞轮是技术上唯一可能"别人抄不走"的(整合优势是时间型、专利弱)。但核心张力是——**我们卖点是"全离线、不联网、隐私",数据飞轮却要收集用户行走数据**,而盲人行走视频极敏感(隐私 + 位置)。这条请你评:**工程上怎么做,既转起飞轮、又不破离线/隐私承诺。**

## The ask / 需求(你要评估的)
1. **怎么采集又不破"离线/隐私"承诺?** 哪些方案可行、怎么取舍:
   - opt-in 自愿(默认离线,用户主动选"贡献数据"时、有 Wi-Fi 才传)?
   - 只传"难例/误报"的**少量元数据/关键帧**,不传全程视频?
   - **端侧/联邦学习**(模型在设备本地用用户数据微调,只回传模型更新、不传原始数据)——端侧算力够吗?
   - 上传前**脱敏**(去人脸、去位置、去声音)?
   - 和 **O&M 机构/试点**在受控同意下采训练数据(不依赖普通用户)?
2. **采什么最有价值?** 怎么让设备端**自动识别"这是个值得回传的难例"**(误报、漏报、没见过的障碍)?
3. **怎么标注?** 盲人自己标不了——O&M 老师?众包?半自动?
4. **训练改进闭环怎么搭?** V1 要不要**先埋"数据采集钩子"**(哪怕先不开启),免得以后回头改架构?
5. **规模 / 时间**:大概多少数据、多久能让飞轮转起来见效(避障可感知地变准)?

**Definition of Done / 完成标准**
- [ ] 一个"离线/隐私不破 + 能采到有用数据"的可行方案(或几个候选 + 取舍)
- [ ] V1 该不该埋数据钩子的建议
- [ ] 飞轮见效的规模/时间粗估
- [ ] 一句话结论:数据飞轮工程上 **可行 / 有条件 / 很难**

## Constraints & non-goals / 约束与非目标
- **不破"全离线 + 隐私"是硬约束**(这是我们的卖点 + 对盲人的承诺,绝不能为了数据牺牲)。
- 纸面方案即可;**不改 V1 排期**(但欢迎建议 V1 埋钩子)。

## References / 参考(你有 business/ 读权限,直接看)
- `business/strategy/product-bets.md` — Bet 3 护城河结论(数据飞轮是唯一可能永久的技术墙)
- `business/strategy/competitive-scan-2026-07.md` — S2 竞争/护城河分析
- `engineering/STATUS.md` — 端侧算力/链路现状

## Thread / 对话线
- **2026-07-01 [CEO]** — 护城河定了,数据飞轮是技术上最大那道墙,但和"全离线/隐私"冲突。请你评工程上怎么做、V1 要不要埋钩子。不急,纸面先行。

- **2026-06-30 [ENG]** — Assessed. **Feasible but conditional 🟡.** The way to keep the "fully offline + privacy" promise intact is a single principle: **the device is 100% offline by default; data is an opt-in side-channel, never collected silently.** A user who never opts in has a fully offline device — promise unbroken. On top of that, three collection tiers, ranked by privacy cost:

  | Tier | How | Privacy cost |
  |---|---|---|
  | **C — partner-collected** | O&M training centers / pilot users, under **explicit consent**, collect labeled walking data | none — doesn't touch the consumer promise |
  | **B — opt-in hard-example upload** | User opts in + WiFi-only + charging-only → upload **de-identified short clips/keyframes** (faces blurred, GPS stripped, audio stripped); **never full video** | low, controlled |
  | A — pure on-device (federated) | Local fine-tune, upload weight deltas not data | zero data leaves, but RK3576 can only do last-layer/adapter fine-tune, not full retrain — heavy, deferred |

  ### ✅ Decision (with Jackie): **C is the primary data source, B is the fallback.**
  - **C (partner data) = primary.** Cleanest fuel: doesn't touch the consumer privacy promise at all, and it comes **pre-labeled** (a sighted O&M instructor is right there). This is the realistic engine of the flywheel, especially early. **Action: we should go talk to O&M centers about a controlled, consented data-collection partnership.**
  - **B (opt-in de-identified upload) = fallback / scale-later.** Switched on once we have an install base; supplements C with real-world long-tail. Default OFF.
  - Pure on-device training (A) is a research nice-to-have, not the plan.

  ### What to collect + how the device auto-finds "hard examples"
  Not full video — only short snippets around **uncertainty events**, detected cheaply on-device:
  - YOLO confidence in the ambiguous band (~0.3–0.6) → model unsure
  - **Sensor disagreement**: ToF says obstacle but YOLO sees nothing (or vice-versa) → likely false-pos / miss
  - **User-correction signal**: sudden stop, repeated "what's ahead?" query → system probably got it wrong
  - **Near-miss**: ToF distance collapses with no prior warning → missed obstacle

  ### Labeling (blind users can't self-label)
  - **O&M instructors** (Tier C) — gold standard, sighted & present
  - **Semi-auto weak labels**: sensor fusion as the labeler (ToF/【V2】radar confirms an obstacle YOLO missed → auto-label "obstacle, class unknown")
  - **Active learning**: only label the hard examples the model is unsure about — efficient

  ### V1 data hook — **YES, bake it in (cheap insurance)**
  V1 builds the **device-side** pieces only (NOT the cloud training pipeline):
  - (a) on-device hard-example trigger logic
  - (b) local encrypted ring buffer (stores locally by default, uploads nothing)
  - (c) an opt-in upload path, **disabled by default**

  (a)+(b) are low-cost and stop us from having to re-architect later. Cloud training + OTA model update is a post-V1 build.

  ### Scale / time (no hand-waving)
  - Meaningfully improving the detector needs **thousands of labeled hard examples per failure mode**
  - Early wins come from **Tier C partner data** (10–50 pilot users × a few weeks → first improved model in a few months), **not** the consumer flywheel
  - A self-sustaining consumer opt-in flywheel needs **hundreds of users** → this is a **12–24 month** build, not instant

  ### Connection to HO-006
  The flywheel's payoff is **class-agnostic / unknown-obstacle coverage** — exactly V1's gap vs NOA. So it's the **software path** that narrows the NOA gap over time, complementing the **V2 hardware path** (mmWave radar + downward ToF). Two paths, same goal.

  ### One-line conclusion
  Data flywheel is **feasible but conditional 🟡**: the offline/privacy promise holds (default-offline + opt-in + de-identified + hard-examples-only + partner-data-primary); pure on-device training is hard so the real loop is C-primary/B-fallback → cloud train → OTA; **V1 should bake in the cheap device-side hook**; payoff is 12–24 months, partner data first. **Next step: go talk to O&M centers about a consented data-collection partnership.**

- **2026-07-01 [CEO]** — 方案很赞,**全采纳:** 默认离线 + opt-in 旁路 + **O&M 合作采集为主** + **V1 埋便宜数据钩子**。**下一步把"找 O&M 谈数据合作"排进任务**(正好和我们 O&M 渠道一举三得:渠道+数据+信任)。赌注3 护城河据此 close。**本条 ✅ 归档。**

## Resolution / 结论
数据飞轮可行但有条件 🟡:默认离线 + opt-in + O&M 合作为主 + V1 埋设备端钩子,离线/隐私承诺不破。收益 12–24 月,合作数据先行。下一步:谈 O&M 数据合作。✅ 归档。
