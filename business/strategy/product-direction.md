# Second Eye — Product Direction (Tier-1 strategic blockers)

> The strategic decisions that shape product direction, worked in dependency order **S1 → S2 → S3**.
> These sit ABOVE the execution/validation gates in `../discovery/risk-blocks.md`. Started 2026-06-30.
> Status legend: 🟢 decided · 🟡 leaning, needs confirmation · ⚪ open.

## Why these come first
`risk-blocks.md` answers "can we build it and will they keep wearing it." This file answers the prior questions: **what are we, can we win, will it make money.** You don't perfect the demo for a game you shouldn't enter. Order is a dependency chain: ideology is the denominator for profit; competition decides if the game is winnable; profit decides if it's worth winning.

---

## S1 — IDEOLOGY: are we a *device* or a *platform*?  🟢 DECIDED

**The question:** is Second Eye a single-purpose blind-mobility aid, or the beachhead of an offline visual-AI platform with mobility as the wedge? This sets every other denominator — pricing, roadmap, cap table, hiring, how we read competition.

### Path A — The Device (single-purpose mobility aid)
- **What it is:** best-in-class obstacle/path detection, hands-free, offline. One job, done superbly. Reading is a free bonus.
- **Roadmap:** depth over breadth — lighter, cheaper, longer battery, more reliable detection.
- **Business shape:** honest SOM ~2–6k units / ~$1–3M over 3 yr (per sizing research). A small business or grant/mission-funded social enterprise. **Not venture-scale on its own.**
- **Fundraising:** grants, disability-tech funds, impact investors, VA/voc-rehab channel. Hard to raise traditional VC — TAM too small for venture math.
- **Competition exposure:** narrow surface; big tech won't build a dedicated blind device (too small for them). But vulnerable to a $300 general AI-glasses entrant adding an "obstacle mode."
- **Risk:** the graveyard's verdict — *"a single-function gadget is a feature, not a company"* (Sunu died, BuzzClip pivoted to software). You build a beloved tool that can't sustain a company, or stay forever grant-dependent.
- **Strength:** focus = you actually nail the safety-critical job, which IS the trust game (Block 1). Mission clarity. Easiest path to being genuinely best at the one thing.

### Path B — The Platform (offline visual co-pilot; mobility is the wedge)
- **What it is:** an offline, on-device visual-AI engine worn on the face. Mobility is the *reason-to-buy* and the safety-critical hook, but the architecture (camera + on-device models + audio, fully offline, no subscription) is a general "perceive and narrate the physical world" stack.
- **Roadmap:** breadth on one hardware base — obstacle detection → indoor nav → object/text/scene → contextual assistance → later optional low-vision SKU. Software-upgradeable; the offline AI stack + real-world walking data are the compounding asset.
- **Business shape:** TAM expands past blind-mobility (low-vision 3× bigger; aging/eldercare adjacent). The $0-marginal-cost offline moat compounds. **Venture-scale story becomes tellable.**
- **Fundraising:** "the offline visual cortex — landing in the highest-pain, most-defensible beachhead (blind mobility) first." Classic narrow→broad (Tesla Roadster→Model 3; Amazon books→everything).
- **Competition exposure:** bigger surface, nearer Meta/Apple/Google roadmaps — but offline + no-subscription + safety-grade latency is a real wedge vs cloud incumbents, and a *stack* survives a big-tech feature-add where a *gadget* doesn't.
- **Risk:** **focus dilution** — in a safety-critical product, "do everything, nail nothing" = dead on Block 1 trust. Premature platform-itis. And the obvious expansion segment (low-vision) wants a *display* we said we won't build → could force a hardware fork early.
- **Strength:** the only version that's venture-scale; the version where the offline moat (triple-proven: OrCam reading, Aira per-minute, Soundscape Azure shutdown) actually pays off; the version that survives commoditization.

### Comparison
| | Path A — Device | Path B — Platform |
|---|---|---|
| Scale | Small business / social enterprise | Venture-scale |
| Capital | Grants, impact | VC-fundable |
| Moat over time | Erodes (it's a feature) | Compounds (it's a stack) |
| Focus risk | Low (focused) | High (must resist sprawl) |
| Trust/safety execution | Easiest to nail | Must protect from distraction |
| Mission clarity | Highest | Risk of drift |

### What "platform" concretely means (the articulation that landed with Frankie)
**One line:** the same glasses, whose *abilities grow over time through software* — the blind user's **offline "eyes"** that launch with the most dangerous job (what's in your path) and expand to more jobs on the **same hardware**.

The enabling fact: the hardware (camera + ToF + on-device AI + bone conduction) is **general-purpose perception**. "Obstacle ahead" is only the first thing we teach it to see. Same device, new offline software:

| Capability | What the user hears | Ships |
|---|---|---|
| **Obstacle / path** (the wedge) | "pole ahead, step down in 1.5 m" | **V1 — only this** |
| Indoor wayfinding | "door on your left, elevator ahead" | later |
| Text reading (free bonus) | "the sign says EXIT" | later |
| Find my things | "keys on the table, to your right" | later |
| Scene / person | "a kitchen; someone seated at a table" | later |

None require new hardware — they're more offline software on the same glasses.

**Device vs platform — the difference is *underneath*, not in V1:**
- **Device:** ships obstacle detection, then iterates *on obstacle detection*. One axis; saturates the small blind-mobility SOM.
- **Platform:** ships the **identical** mobility V1, but builds the general offline-perception engine underneath — so each later capability is a new reason-to-wear, a new adjacent user, on the same hardware + moat. **Platform is a sequence, not a bigger V1.**

**Why that's a company (and a single-purpose device isn't):**
1. **Fights abandonment (Block 2)** — glasses useful in many daily moments stay on the face; a walk-only gadget gets drawered.
2. **Compounds the moat** — offline models + real-world data across many tasks; each capability makes the next cheaper / harder to copy.
3. **Revenue without a subscription** (moat kept) — more daily value supports the price; more SKUs/segments; **offline B2B/institutional** (the Aira-Access sponsorship model, but $0 marginal cost = actually profitable); eventually licensing the offline engine.

**What it is NOT** (so the word doesn't mislead): ❌ a developer SDK / app store · ❌ consumer AR for everyone (Meta's game — we'd lose) · ❌ a cloud/subscription platform (kills the entire moat).

### The core tension — the synthesis
**Build like A, story like B.** V1 must be a ruthlessly focused, best-in-class *mobility device* (the trust game punishes distraction; the wedge is the only way in), but the *company thesis, architecture, and capital strategy* must be *platform*, or the math can't support a venture and we die as a feature. **The fatal mistake is doing it backwards** — building broad/unfocused (mediocre detection) while the market only rewards a device that nails the one job.

### Mission-drift caveat (a product-ideology line, not just strategy)
This is assistive tech for blind people. "Platform/venture ambition" must never become "abandon the hardest-to-serve core for the bigger non-disabled market." **Blind mobility is not a stepping-stone we leave behind — it's the proving ground and the soul.** Expansion must be *adjacent and downstream of* the core users, never *at the expense of* them. This boundary is a values call to set explicitly.

### Recommendation (🟡 leaning) — **Platform, executed through a Device-grade V1 wedge** ("wedge-first platform")
Why: the standalone-device version is a near-certain *small* business (the sizing math says so) and the graveyard says single-function gadgets die; meanwhile the offline/$0-marginal-cost moat is exactly what a *platform* compounds on. So adopt the platform thesis, but enforce device-grade focus on V1.

### What this means for product direction NOW (if confirmed)
1. **Architecture (note for Jackie's repo — we plan, he builds):** build the offline visual stack as a *modular general engine* where obstacle-detection is module 1 — not a hardcoded beeper. The generality is the asset.
2. **V1 scope:** ONLY mobility, nailed. Reading stays a free bonus, off the pitch. Resist all feature creep until detection clears the Block-1 bar.
3. **Hardware:** keep V1 display-free and cheap for the blind wedge; a low-vision *display variant* is a future SKU, never V1.
4. **Story vs ship:** pitch the platform, sell the device. Keep both honest.
5. **Moat to protect:** offline models + accumulated real-world walking data = the compounding asset; guard it.

### Decision — 🟢 DECIDED (2026-07-01, Frankie)
All three sub-questions settled / 三个子问题全部拍板：

**1. Identity = Platform（会长大的产品，设备级 V1 为楔子）🟢.**
Build the modular general engine from V1 (Jackie confirmed ~1–2 days, zero V1 risk); V1 still ships mobility-only, generality lives underneath. / 从 V1 就搭模块化通用引擎；V1 仍只做避障，通用性在底层。
- **Frankie's vision add:** a future **cloud agent** that self-updates its memory & architecture — learns each user's habits, gets more tailored the more it's used. / 未来云端 agent：自更新记忆与架构，越用越贴合用户习惯。

**2. Model = freemium（基础免费离线 + 可选付费云端）🟢.**
- **Base = full offline core, free, no subscription** — works completely without paying or connecting; the moat + the blind-safety guarantee. / 基础 = 完整离线核心，免费、无订阅，不付费/不联网也能正常用。
- **Optional = paid subscription unlocks cloud** (scene description, the learning agent…) — **never required, opt-in.** / 可选 = 付月费打通云服务，不强制、可选。
- **Hard line:** safety/mobility core **always offline**; the no-subscription promise holds for the base. This freemium split *is* the fusion mechanism for expansion (decision 3). / 保命/避障核心永远离线；基础无订阅承诺不变；这个 freemium 切分就是扩张的融合机制。

**3. Mission = blind-core fixed; expansion welcome via the freemium fusion 🟢.**
- Core users **stay visually-impaired** (the start). Expansion to other domains is **embraced** but routes through the optional-cloud layer — so it never diverts the free blind-core product. / 核心服务对象不变 = 视障；扩张走可选云端层，绝不挤占免费的盲人核心。
- **Sequence:** first prove tech + idea + demand on the blind wedge → then port to adjacent domains (easy, no drift). / 先用第一轮证明技术+想法+需求，再移植到别的领域，不跑偏。

### 🌟 Standout expansion opportunity (Frankie) — for the investor story · ⚠️ UNVALIDATED
**Arc / 大故事:** blind wedge → **hospital caregivers / 护工** → **medical-industry smart glasses / 医疗行业智能眼镜.**
- **Hypothesized pain (NOT researched — verify in discovery):** critically-ill / at-risk patients need **real-time vital-sign monitoring**; if a caregiver could see those numbers **right on their glasses**, response is faster & easier. / 假设痛点（未调查，待 discovery 验证）：危重/濒危病人需实时体征监控；护工若能在眼镜上随时看数值，更及时方便。
- Worth pre-building a stronger story around this; flagged as a hypothesis to validate (verify-don't-assert). **Notified to Jackie → HO-004.**

**S1 = 🟢 closed.** HO-002 → CEO decision replied + archived. Next block: **S2 (competition)** — other blocks later per Frankie.

---

## S2 — COMPETITION: moat or commoditization?  🟡 (扫描完成 2026-07-01；待 CEO 拍 messaging/渠道)
> 全球扫描 157 竞品（23 高威胁 · 36 巨头 · 24 死）→ 详见 `strategy/competitive-scan-2026-07.md`。

**核心结论（诚实）：今天没有"功能"护城河，只有"组合 + 时机 + 渠道"护城河，窗口 12–24 个月。**
- 四条原始差异化里**三条已同质化**：**离线**（NOA/.lumen/Ara/Apple 都离线 = table stakes）、**无订阅**（NOA/Ara/EchoVision 都有）、**自学习 agent**（Halo/Rabbit/OpenAI io 在做 = 不可守）。
- **唯一还空着的** = `mobility-safety-grade + sub-$700 + 30g 分体轻形态 + 西方支付渠道(VA/voc-rehab)` 的**组合交集**——每条边都有人逼近，没人占满。

**头号盯防：NOA（功能基准）+ Meta（分发/品类定义，正把"AI 助盲=免费"钉进心智）。** Meta/Apple 主动让出 mobility-safety（Apple Magnifier 自述"不可导航"）——这是我们的角落。

**待 CEO 拍的三件（S2 收尾）：**
1. **messaging 重写**：头条改成"**安全级实时避障 + sub-$700 + 最轻分体眼镜**"；把离线/无订阅/agent 退为支撑，不再当独立卖点（否则显 me-too）。
2. **渠道 = 真护城河，优先于功能**：尽早启动 **VA/voc-rehab 报销** + 盲人社区信任（NFB/ACB）。比加功能更耐久。
3. **agent 降级**为 wedge 内增强（"越用越懂你的路线"）；**医疗护工 = phase-2**（护士 AR overlay 已抢跑），今天不碰。

## S3 — PROFIT: is there a business, and what kind?  ⚪ (after S2)
