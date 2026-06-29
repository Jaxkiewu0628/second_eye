# Failure Graveyard — assistive-vision & smart-glasses products that died or stalled

> Post-mortem research for **Second Eye** (sub-$700, fully-offline, no-subscription AI glasses; wedge = MOBILITY: camera + on-device detection + ToF → bone-conduction "obstacle ahead").
> Compiled 2026-06-30. The lesson matters more than the obituary.
> Convention: **measured** = sourced/confirmed; *estimated* = inferred. Rumor is flagged explicitly. Full URLs + access date in **Sources**.

## How to read this
Each product: what it was → price → what happened → primary-source citation → **the lesson**.
Then **Kill patterns → our rules** maps every recurring failure mode to one explicit rule for us.
This is a graveyard on purpose: every entry is a way to die that we are choosing to avoid.

---

## The dead and the dying (verdict table)

| Product | Category | Price | Verdict (2026-06-30) | One-line cause of death |
|---|---|---|---|---|
| Toyota BLAID | Indoor nav, shoulder-worn | n/a (never priced) | **Never shipped** (quiet death) | Big-co side project; no obituary, no product |
| Horus (Eyra) | Reading + nav, bone-conduction headband | ~$2,000 (*pre-order, est.*) | **Dead** | Pivoted to eye-tracking (Eyeware); device never shipped |
| Google Glass (Explorer) | Consumer face camera/display | ~$1,500 | **Killed as consumer** (Jan 2015) | "Glasshole" stigma + camera-privacy backlash |
| OrCam MyEye | Clip-on reading device | $3,500–$4,490 | **Exited vision** (2024) | Free phone AI killed willingness-to-pay for reading |
| Envision Glasses | Reading/scene on Google Glass | $1,899–$3,500 | **Struggling / orphaned HW** | Google discontinued the Glass it was built on |
| Aira | Human-agent remote assist | Consumer subs + B2B | **Pivoted emphasis to B2B** | Consumer subscription couldn't scale on human-agent cost |
| eSight | Low-vision HMD (magnifier) | ~$4,950–$5,950 | **Acquired by Gentex** (2024) | Priced for nobody; no reimbursement; needed a manufacturer |
| Microsoft Soundscape | 3D-audio nav app (free) | Free | **Discontinued** (2023) | Side research project; killed despite being free + loved |
| Brainport V100 | Tongue electro-tactile display | ~$10,000 | **Marginal / abandoned** | Brutal learning curve + price; sensory substitution is hard |
| .lumen | Guide-dog-replacement headset | ~€10,000 retail | **Pre-commercial** (risk) | Years of funding, still not shipping at scale |
| Biped NOA | Shoulder-worn obstacle/nav | ~CHF 3,500 / sub | **Alive (small)** | Live mobility competitor; subscription + connectivity reliance |

(Detail and citations per product below.)

---

## 1. Toyota BLAID — _never shipped (death by silence)_

**What it was.** A horseshoe-shaped wearable worn around the neck/shoulders ("like a neck pillow") for **indoor** navigation. Cameras detected surroundings; output via speakers, headphone jack, Bluetooth bone-conduction headphones, and vibration motors. It identified indoor features — restrooms, escalators, stairs, doors — with voice recognition and physical buttons. Maps lived on-device, updated via Wi-Fi/SD card, with planned iBeacon integration.

**Price.** None ever announced — it never reached a commercial stage. *(measured: no price exists)*

**What happened (timeline, measured).** Toyota's **sole** official announcement was **7 Mar 2016** (an "early-stage" device in employee beta). An AFB AccessWorld profile followed (May 2016, still pre-product). Then: no further releases, no launch, **no discontinuation notice.** Toyota's own "Project BLAID" newsroom tag page lists exactly **one** item, dated 7 Mar 2016. Death by quiet abandonment.

**Why it died (root cause).** The fatal flaw was named at the time: BLAID depended on pre-mapped, continuously maintained interior maps for *"every building a blind person would want to visit"* — an unwinnable data-coverage problem for indoor positioning in the pre-LiDAR-phone, pre-modern-SLAM era. It read as a corporate-CSR R&D/PR project, not a funded product line; when the press cycle ended, so did the program.

**The lesson.** A wearable that depends on **infrastructure you don't control** (here: maintained indoor maps of every venue) has no path to scale. Build for the world as it is — **on-device perception that works in an unmapped building on day one.** This is precisely Second Eye's bet (on-device detection + ToF, **no map dependency**) — so we are on the right side of BLAID's grave.

## 2. Horus / Eyra — _took early interest, never shipped (under-capitalized)_

**What it was.** A two-piece head-worn AI assistant: a band around the back of the head with **two stereo cameras** and **bone-conduction** earpieces, tethered by a ~1 m cable to a smartphone-sized pocket unit holding the battery and an **NVIDIA Tegra K1** GPU running deep-learning vision. Functions: stereo obstacle/navigation cues, face recognition, object recognition, read-aloud, scene description. *(Note: this is almost exactly Second Eye's architecture — stereo cameras + on-device GPU + bone-conduction — a decade early and under-funded.)*

**Price.** ~**US$2,000** expected. *(estimated — press figure; never sold, so no final price was published)*

**Company / funding (measured).** Founders **Saverio Murgia** & **Luca Nardelli** (CV researchers, University of Genoa). Won a €15k EIT Digital grant; raised **~$900,000 from 5Lion Holdings**; both made Forbes 30 Under 30 Europe (2017). "Horus Technology" rebranded to **Eyra Ltd.** in Oct 2016.

**What happened (timeline).** **26 Oct 2016:** Eyra launches "early access," trials with the Italian Union of the Blind, units "expected by January 2017." That beta/launch never materialized at scale. By **~2019** the founders had moved on, Crunchbase noted it was *"doubtful Eyra will raise another funding round,"* and the product quietly disappeared.

**⚠️ Two premise corrections (honest flags).**
- **The "pivot to Eyeware self-driving" premise is NOT supported and appears to be a mix-up.** **Eyeware Tech SA** is a *separate* EPFL/Idiap spin-off (incorporated Sept 2016, led by **Kenneth Funes**) with **no Horus/Eyra lineage.** Eyra's founders later surface at a venture called *"Sungazer,"* not Eyeware. Treat "Eyra → Eyeware" as **incorrect / unconfirmed.**
- **No formal shutdown notice and no documented refund saga could be located** in company channels, r/Blind, AppleVis, or tech press. The product never reached documented commercial sale; the company stopped raising and vanished. **The early-access refund question is unverified — I will not assert it either way.** (AppleVis and the Wayback Machine were server-blocked to the fetcher — a known gap.)

**Why it failed (root cause).** Classic under-capitalized hardware death: ~$900K is far too little to industrialize, certify, and support a custom dual-camera + Tegra-GPU + tethered-computer wearable, shipping at ~$2,000 into a tiny, price-sensitive market, in a bulky two-piece tethered form factor. The team had CV talent but not the capital or manufacturing path.

**The lesson.** **Early-access sign-ups and press buzz ≠ fundable demand.** A novel sensor+compute wearable for a small, price-sensitive disability market needs either a far bigger raise *or* a far cheaper BOM before taking customer money — and **if you take deposits, have a refund plan**, because reputational damage in the tight-knit blind community outlives the company.

## 3. Google Glass (consumer Explorer Edition) — _killed as a consumer product_

**What it was.** Face-worn wearable with a forward-facing camera and a small prism display above the right eye; voice + touch control, photo/video, hands-free. The archetypal consumer face camera.

**Price (measured).** **$1,500** (Explorer Edition; £1,000 UK).

**What happened (timeline, measured).** Sold to developers from 27 Jun 2012; broad Explorer program through 2014; one-day US public sale 15 Apr 2014; UK launch Jun 2014. **29 Oct 2014:** MPAA + NATO advise theaters to ask patrons to remove Glass (recording fear). **15 Jan 2015:** Google ends the Explorer Program (last day to buy 19 Jan 2015). Reborn as **Glass Enterprise Edition (2017)** for workplaces — itself discontinued **15 Mar 2023**.

**Why it failed — the face-camera social-acceptability collapse.**
1. **The "Glasshole" stigma** (term emerged 2013, Urban Dictionary Mar 2014) — encoded both the wearer ignoring people *and* the bystander's sense of being surveilled.
2. **"Is it recording me?"** — a lens at eye level that bystanders couldn't tell was on or off. Consumer Watchdog called it *"a perfect stalker's tool"* (ABC News, 16 Jan 2015).
3. **Venue bans** (2013–14, mostly preemptive): bars ("No Google Glass Zone"), cinemas (Alamo Drafthouse; MPAA advisory), Las Vegas casinos, banks.
4. **Bystander hostility** — Mat Honan, *"I, Glasshole,"* WIRED, 30 Dec 2013: *"People get angry at Glass. They get angry at you for wearing Glass… It inspires the most aggressive of passive aggression."*

**Why Enterprise survived while consumer died — the load-bearing distinction.** In a factory/warehouse/OR, everyone present is an employee under a known policy, the camera serves a sanctioned task, and there is no random member of the public to feel surveilled. The exact objection that killed consumer Glass — *"a stranger pointed a camera at me and I can't tell if it's on"* — structurally doesn't arise. Bounded context + bystander consent = survival.

**The lesson for a face-worn assistive camera (us).** A legitimate accessibility purpose does NOT exempt you from the bystander reaction — the bystander cannot see your purpose, only your lens. Three implications, all of which Second Eye is positioned to win:
1. **Bystander legibility is a first-class design requirement.** The device must *read as* an assistive aid, not surveillance.
2. **"Fully offline / on-device, nothing stored or uploaded" is our single strongest privacy defense — but only if we communicate it.** It is the direct antidote to the fear that killed Glass; treat it as a marketing/policy asset, not just an engineering fact.
3. **Assistive framing earns goodwill Glass never had.** A mobility aid worn by a blind person carries ADA-backed social legitimacy a $1,500 lifestyle gadget never did. Foreground *disability accommodation*, never *consumer camera wearable.*

## 4. OrCam MyEye — _exited vision; the willingness-to-pay autopsy_

**What it was.** Wearable AI reading device — a small camera/speaker unit that clips magnetically to the temple of ordinary glasses, points where the user points, and reads printed/screen text aloud, recognizes faces, identifies products and money. Fully on-device, no phone required. The flagship product of OrCam Technologies (Jerusalem; founded 2010 by Amnon Shashua and Ziv Aviram, the Mobileye founders).

**Price (measured).** OrCam MyEye 2 / MyEye Pro: **$3,500–$4,490** depending on edition/era. This is the "$4,490 reading-hardware king" — the most capable dedicated reading wearable ever sold, at a price an individual had to self-fund.

**What happened (timeline).**
- Mar 2021: raised $50M at a **$1.5B valuation**, eyeing a New York IPO targeting **$2.5B+** (measured). The IPO **never happened**.
- Oct 2022: laid off **62 employees (~16% of staff)** as the market turned (measured).
- 2023–2024: further rounds; investor battle and last-ditch funding reported.
- 2024: laid off **100 in June, ~50 earlier**, then in **July 2024 closed its reading-glasses (Low Vision) development entirely** and pivoted to hearing tech (OrCam Hear). (measured)

**Why it died — in OrCam's own words.** OrCam stated that *"the technological progress in image processing by language models makes the need for further development of the Low Vision products unnecessary."* Calcalist: *"The development of generative artificial intelligence technologies that perform functions similar to OrCam's reading device for the blind using smartphones has harmed its bottom line."* (CTech, 28 Jul 2024 — measured.) The IPO freeze was compounded by the war and a freeze on Gulf-market sales, but the structural killer was **free phone AI eating the reading job.**

**The lesson (this is the central one for us).** OrCam built the best dedicated reading hardware on earth, priced it at $4,490, and **still could not sustain it once Seeing AI / Be My AI / Lookout made reading free on a phone the user already owns.** Willingness-to-pay for *reading hardware* collapsed to roughly zero. → **Reading is a free bonus on our stack, never the reason-to-buy.** If reading were our wedge, OrCam is our future.

## 5. Envision Glasses — _struggling; orphaned hardware_

**What it was.** AI glasses for the blind/low-vision **built on Google Glass Enterprise Edition 2** — reads text (Instant/Scan/Batch), describes scenes, recognizes faces/cash/colors, and can "Call a Companion" or "Call Aira." Netherlands-based Envision; also ships a well-regarded **free Envision App** for phones.

**Price (measured).** ~**$1,899–$3,500** across editions (Home / Professional). The free app does most of the same reading on a phone.

**What happened (measured).** Google **stopped selling Glass Enterprise Edition 2 on 15 Mar 2023** and **ended support 15 Sep 2023**, amid Google's ~12,000-person layoffs. Envision's entire hardware platform was discontinued *by its supplier.* Envision still sells and updates the glasses and leans on the free app, but its glasses business now rests on an EOL'd, unsupported device.

**Why it struggles.** Two squeezes at once: (a) the **platform-dependency** time bomb — you don't control your bill of materials when you build on someone else's hardware, and Google killed it; and (b) the **same free-phone-AI** pressure that killed OrCam (Envision's own free app, plus Seeing AI / Be My AI, do the reading job for $0).

**The lesson.** Don't build your hardware on a platform a bigger company can discontinue out from under you. **Own your BOM** (Second Eye does — Jackie's own RK3576/RV1126B + IMX415 + VL53L5CX stack), and don't let your paid hardware compete against your own free app on the job (reading) that phones already do free.

## 6. Aira — _consumer subscription couldn't scale; pivoted emphasis to B2B_

**What it was.** Live human agents who see through the user's phone/glasses camera and describe surroundings / navigate / read in real time. The premium "a trained human on demand" service.

**Price (measured).** Consumer plans historically tiered (~$30–$200+/mo); **retail rate escalated to ~$50/hr (2023) → ~$100/hr (2024).** Now ~**65%+ of revenue is the B2B "Aira Access" program** — 3,000+ geofenced "sponsored access" locations (60+ international airports, ~50% of top US airports, major retailers) where a partner pays so the blind user uses it **free** at that location.

**What happened (timeline).** Launched consumer-first; the **Jan 2023 pricing change** triggered a well-documented community backlash (Jonathan Mosen, *"Aira's astounding communications fail,"* 16 Jan 2023). Aira pivoted its *emphasis* to enterprise/sponsored access as the durable engine. **Consumer plans still exist** (Aira announced no 2025 price increase) — so this is a *pivot of emphasis*, not a shutdown.

**Why the consumer subscription couldn't carry the business.** The product *is trained human expertise* — a 24/7 distributed workforce (training + background checks) is the supply chain, and **human-labor cost per session does not fall with scale.** Mosen, plainly: *"where people costs are high and infrastructural costs are significant, finding a sustainable business model was always going to be a challenge"* (escalating labour costs + inflation). An individual blind user can't shoulder $50–100/hr; a payer (enterprise/airport/employer) had to step in.

**The lesson.** Human-in-the-loop assistance has an **irreducible marginal cost**; an individual can't carry it, and "cheaper subscription" can't fix labor economics. → Our value must be **marginal-cost-near-zero (on-device compute, no per-use human or cloud bill)**, and where money is needed, **find a payer (VA / voc-rehab), not a recurring consumer subscription.** This is also why "no subscription" is a real moat, not just a slogan.

## 7. eSight — _the tech worked; the price-and-reimbursement model didn't_

**What it was.** A head-mounted electronic low-vision *display* (an enhancement aid, not obstacle/navigation): a high-def camera feeds magnified, contrast-enhanced live video to dual OLED screens in front of each eye; tilt up to keep peripheral/mobility vision. For **low vision, not blindness** — it requires residual sight. Compatible with 20+ conditions (macular degeneration, Stargardt, diabetic retinopathy, glaucoma). Company-reported ~70% of trial users benefited.

**Price (measured — note it fell over time, a tell in itself).** eSight 3: launched **$9,995** (Feb 2017); earlier generations ran as high as ~$15,000 out of pocket. **eSight 4 (2020): cut to $5,950** (~40% reduction). **eSight Go (current): $4,950 / $6,600 CAD.** **Coverage:** eSight's own marketing admitted *"this cost is not covered by health insurance in the US."* Today the **VA covers 100% for US veterans**, but **CMS/Medicare does not cover/reimburse** — everyone else relies on financing, tax credits, charity, crowdfunding.

**What happened (timeline, measured).** Premium pricing forced down ($9,995→$5,950) while the reimbursement battle dragged; eSight built an entire "affordability program" (a tell that the price was unaffordable to its own users). **Jan 2022:** Gentex (NASDAQ: GNTX, auto dimming-mirror giant) partners + takes a ~20% stake. **2 Nov 2023:** Gentex **acquires eSight's technology assets** — total consideration **~$88.9M = ~$18.9M cash + assumption of a $9.4M note + an earn-out of up to $70M over 10 years.** **7 Jan 2024 (CES):** publicly announced.

**Distress vs. strategic? (verify, don't assert).** Officially **strategic** (Gentex CTO: *"leverage [automotive vision] expertise in health care"*). But the **deal structure reads like an asset-rescue / soft landing**: an *asset* purchase (not the whole company), a **small cash component (~$18.9M)** with the bulk (**up to $70M**) pushed into a **contingent 10-year earn-out** — the shape of a deal for a company that needed a manufacturing/balance-sheet parent after 15+ years and repeated price cuts. *Flagged as inference from terms, not a stated fact.*

**Why it struggled (root cause).** The high-priced low-vision HMD is squeezed from both sides: a **small addressable market** (low-vision users who benefit from a worn display) × a **medical-device price** ($5,950–$9,995) × **no Medicare/most-insurance reimbursement**, sold to a population skewing older and lower-income. The technology worked; the **business model (premium hardware with no payer) didn't.**

**The lesson.** For assistive wearables, **the payer is the product decision.** Price at medical-device levels and you must win reimbursement *or* engineer the BOM to a consumer price — doing neither traps you in a tiny cash-pay market that ends in price cuts, charity, and selling your assets. → For us: **keep the BOM low enough to be cash-pay-viable AND build the VA / voc-rehab / charitable case *before* scaling, not after.** (Note: the VA already covers eSight 100% — direct evidence our VA payer path is real.)

## 8. Others worth a line

**Microsoft Soundscape — DISCONTINUED (then open-sourced).** Free iOS 3D-spatial-audio ambient-awareness app from Microsoft Research. Pulled from download **3 Jan 2023**; existing installs **stopped working 30 Aug 2023** (per Microsoft's own support page); code open-sourced on GitHub. Community forked it (VoiceVista carries it forward). *Killed not for lack of love but because it was a research project with no P&L owner — and Microsoft shut the **Azure backend**, which is what actually bricked the app.* **Lesson:** a free, polished, big-company assistive app still dies when it's a benefactor's side project — and **cloud-backend dependency you don't control is a kill switch.** Second Eye's fully-offline design is the direct antidote.

**.lumen (Romania) — PRE-COMMERCIAL (closest analog; cautionary).** Guide-dog-replacement **headset** (forehead haptics + beamforming audio physically nudge the head; 6 cameras, 2 IR projectors, 3 IMUs, GPS). Heavily EU-funded: EIC Accelerator (~€9.7M) + €5M round (Jul 2024) + EIT Urban Mobility. **Price the red flag: ~€9,999 (~$11,800), reservations only as of Dec 2025**, with the launch roadmap slipping. **Lesson:** a head-worn mobility device *can* raise serious capital and patents — but a ~€10k "replace the guide dog" promise caps the market to grant-funded early adopters and invites timeline slip. Watch it as *validation* (demand + money are real) and *cautionary tale* (price/scope/timeline). Our sub-$700, "obstacle ahead, not full autonomy" framing is the deliberate opposite bet.

**Biped NOA (Switzerland) — ALIVE (live competitor).** Backpack-style harness, 170° obstacle detection + GPS + AI scene description via **bone-conduction 3D audio** (same audio channel we use). **€1,850–€2,750** (a CHF 129/mo subscription option existed in 2022). Distributed via national blindness orgs. **Lesson:** the obstacle + audio + nav bundle has paying customers, validating the category — but at ~€2k+ and cloud-leaning. Sub-$700 + offline undercuts NOA ~3–4× as a sharp wedge.

**Brainport V100 (Wicab) — effectively gone from Western markets.** Tongue electro-tactile display (camera → ~400-electrode "lollipop" paints images on the tongue). FDA De Novo cleared **18 Jun 2015**, ~**$10,000**, positioned as adjunct to the cane. Successor "Vision Pro" listed as **only available in China**; US/EU reintroduction promised "late 2022" is ~3.5 yrs lapsed. **Lesson:** steep sensory-substitution learning curve + five-figure price = adoption death. Our bone-conduction "obstacle ahead" must be learnable in **minutes, not months** — Brainport proves the opposite doesn't scale.

**Sunu Band — DEAD.** Sonar/echolocation haptic wristband (~16 ft), YC S17, ~**$299**, ~5,000 users. **Crunchbase lists it permanently closed; sunu.com now redirects to a domain-for-sale listing.** (Exact shutdown date unconfirmed; closure confirmed.) **Lesson:** a single-function $299 obstacle gadget — even with real users and YC — is a feature, not a company. Bare obstacle detection has too thin a value prop to carry hardware economics. Our obstacle cue must sit inside a defensible whole (offline platform, payer path, room to grow into a visual co-pilot).

**BuzzClip (iMerciv) — DISCONTINUED / pivoted.** Clip-on ultrasonic obstacle detector, ~**$249**. Toronto's iMerciv pivoted to **MapinHood** (pedestrian-nav app); imerciv.com now shows a "Maintenance" page; founders moved on. (Pivot confirmed; product death inferred.) **Lesson:** the team that built the detector concluded the *software/navigation* was the real business and abandoned the hardware. Same warning as Sunu.

**Maptic — CONCEPT ONLY (correct the record).** A 2017 **student industrial-design project** (Brunel University; haptic necklace + app). Frequently cited because it entered the **Cooper Hewitt (Smithsonian) collection** and won design press — but **never manufactured, sold, or priced.** **Lesson:** beware the *vaporware halo* — renders, museum placement, and design awards manufacture the illusion of a competitor that never shipped. Judge rivals by units and revenue, not awards.

**Project Guideline (Google) — RESEARCH-ONLY.** Pixel + chest harness + headphones keeps a blind *runner* on a painted line via on-device ML. Google **open-sourced it 21 Nov 2023** and never shipped a consumer product. **Lesson:** Google (like Soundscape) does assistive as research/PR — publishes a repo and walks away. Don't model Big Tech as a market-maker or assume a Google product is coming to compete; *do* harvest their open code. The lane for a focused, shipping, for-profit hardware startup stays open.

**Bonus — the older ETA graveyard (from the abandonment literature).** Sonic Torch, Sonic Guide (Leslie Kay, 1960s), Mowat Sensor, LaserCane, Sonic PathFinder, Polaron — *none survive today.* **UltraCane** won global innovation awards but needed ~50 units/month to survive, sold only 20–40, and shut down. Diagnosis (Prof. David Clark-Carter): engineers *"create something which has every possible bell and whistle … but don't consider what the visually impaired user will be able to do with the information."* Decades of electronic travel aids have failed to displace the white cane. **Lesson:** this is the deepest moat against us — the cane is cheap, reliable, and never gives a false "clear." Win by *complementing* it, not replacing it.

---

## Kill patterns → our rules

Seven recurring ways these products died, each mapped to one explicit rule. **Ranked by how much the pattern threatens *us specifically*** (1 = most lethal to Second Eye).

### 1. Trust collapse / abandonment — the deepest grave (mobility is the worst category)
**Evidence:** ~**29.3%** of all assistive devices abandoned, **mobility aids highest** (Phillips & Zhao 1993). For blind/low-vision *optical* AT, **17–50%** abandoned. Two cliffs: **Year 1 and Year 5**. The white-cane graveyard (Sonic Guide, LaserCane, Sonic PathFinder, UltraCane — *none survive*) proves decades of electronic travel aids couldn't displace the cane. The cane **never gives a false "clear."**
**Why it's #1 for us:** mobility is our wedge, so we enter the single highest-abandonment category against the most-trusted incumbent ever. Trust is binary and asymmetric: a device that occasionally misses an obstacle isn't "95% as good" — it can be *worse than useless.*
**→ Rules:**
- **Position as a complement to the cane, never a replacement.** (Replacement attempts fail; complement framing also lowers the safety-failure stakes.) .lumen/BLAID promised to replace the dog/cane — we don't.
- **Engineer for false-negative-aversion.** Better to over-warn than to miss. The board demo must stress *misses*, not best-case detections — one miss in front of a user kills trust permanently.
- **Don't break the user's own senses.** Bone-conduction (ours) is correct *because it leaves the ears open* for echolocation/traffic — keep alerts sparse and high-precision, never chatty.
- **Front-load training + professional fitting** (fitted/trained devices retain far better) and design for durability to survive the Year-5 cliff.
- **Involve users in selection/design** — the #1 abandonment predictor is users not being consulted. *Our discovery gate (`discovery/`) directly de-risks this.*

### 2. Priced for nobody / no payer
**Evidence:** eSight ($9,995→$5,950, no Medicare, rescued by acquisition); OrCam ($4,490, collapsed); Brainport (~$10k, gone from the West); .lumen (~€10k, pre-commercial). The cash-pay market for $5–10k assistive hardware is too small and too old/low-income to sustain a company.
**Why it's high for us:** we're a hardware company selling to an income-constrained population.
**→ Rules:**
- **Sub-$700 is a survival constraint, not a marketing number** — it makes the device cash-pay-viable *without* a reimbursement miracle. Hold the BOM.
- **Build the payer path BEFORE scaling, not after.** VA already covers eSight 100% and funds "electronic mobility devices"; voc-rehab funds smart glasses. Secure those channels early — don't price like a medical device and *hope* insurance comes.

### 3. Solved a job phones now do for free
**Evidence:** OrCam's own post-mortem: *"the technological progress in image processing by language models makes the need for further development of the Low Vision products unnecessary"* — free Seeing AI / Be My AI / Lookout ate reading. Envision's paid glasses now compete with its own free app.
**Why it's high for us:** reading/scene/faces are commoditized to $0; if we ever drift to selling them, we become OrCam.
**→ Rules:**
- **Mobility is the reason-to-buy; reading/scene is a free bonus, never the pitch.** Mobility is the one job a phone physically can't do (can't hold a phone scanning the sidewalk while caning) — the only durable hardware wedge.
- **Never let paid hardware compete with a free phone app on the same job.** Our paid value = real-time, hands-free, offline obstacle detection while walking.

### 4. Cloud / subscription dependency that died with the benefactor
**Evidence:** Microsoft killed the **Soundscape Azure backend** → the app bricked even though it was free and loved. Envision's hardware base (Google Glass EE2) discontinued by Google. Project Guideline / Soundscape = Big-Tech *research*, open-sourced and abandoned.
**Why it's medium-high for us:** any cloud or third-party-platform reliance is a kill switch we don't control.
**→ Rules:**
- **Fully offline / on-device is a moat, not just a feature** — nothing to shut off, no server bill, works in a dead zone. This directly answers the Soundscape failure mode.
- **Own your bill of materials.** Don't build on a platform a bigger company can EOL (Envision's mistake). *Jackie's own RK3576/RV1126B + IMX415 + VL53L5CX stack already does this.*
- Treat Big Tech as a *code* source (harvest their open-source), never as a market-maker or assumed partner.

### 5. Social stigma of a face camera
**Evidence:** Google Glass — "glasshole," venue bans, *"perfect stalker's tool,"* bystander hostility. Consumer Glass died; Enterprise (bounded context, no random bystanders) survived. Abandonment literature: aesthetics that *"draw attention to the disability"* drive users to quit.
**Why it's medium for us — and partly in our favor:** we wear a camera on the face, but assistive framing carries ADA-backed legitimacy Glass never had.
**→ Rules:**
- **Bystander legibility is a first-class design requirement** — the device must *read as* an assistive aid, not surveillance.
- **Make "fully offline, nothing recorded or uploaded" a loud comms/policy asset** — it's the direct antidote to the fear that killed Glass.
- **Foreground disability accommodation, never "consumer camera wearable."** The same form-factor discipline that calms bystanders also keeps the *user* willing to wear it daily.

### 6. Single-function gadget = a feature, not a company
**Evidence:** Sunu Band (DEAD), BuzzClip/iMerciv (pivoted to software). Bare ultrasonic obstacle detection at $249–$299 — even with real users and YC — couldn't carry hardware economics.
**Why it's medium for us:** "obstacle ahead" alone risks being a feature.
**→ Rules:**
- **The obstacle cue must sit inside a defensible whole:** offline platform + payer path + a roadmap to a broader offline visual co-pilot (so we're not a one-trick gadget). Our design doc already frames this as "architected to grow."

### 7. Hardware/thermal/battery/infra reality vs. the demo
**Evidence:** BLAID needed maintained indoor maps of *every* venue (infra it couldn't control) → never shipped. Horus = bulky two-piece tethered rig, ~$900K, never industrialized. Every serious obstacle-detector uses bulkier hardware (NOA vest, .lumen headset) for FOV + depth.
**Why it's medium for us:** thin-frame outdoor obstacle detection is our make-or-break physics question.
**→ Rules:**
- **No dependency on infrastructure we don't control** (no required pre-mapped venues) — on-device perception must work unmapped on day one. *(Our ToF + on-device detection does this.)*
- **Respect the physics:** the neck-hung compute box (Jackie's V1) is the right call — it solves thermal/battery/compute that a sub-50g standalone frame can't. Prove curb/pole/branch detection on a *real sidewalk* on the board before believing the demo.
- **Don't take deposits without a refund plan** (Horus's reputational lesson in a tight-knit community).

### The single most important rule
**If you remember one thing: do not sell reading — sell trustworthy mobility, and earn the trust.** The two largest graves here are (a) *charging for reading*, which is now free (OrCam, the $4,490 king, is dead), and (b) *abandonment from broken trust* in the highest-churn category we're entering. Our entire strategy — **mobility wedge, reading as free bonus, offline/no-subscription, sub-$700, complement-not-replace the cane, false-negative-averse, validated by real-sidewalk discovery** — is the precise inverse of how every product in this graveyard died. Stay on that line.

---

## Sources

All URLs accessed **2026-06-30**. Publish dates given where known. Primary sources (company/official, SEC, FDA, GitHub, journals) prioritized; secondary/community sources marked.

**Toyota BLAID**
- Toyota USA Newsroom, "Wearable Mobility Device for the Blind and Visually Impaired Being Developed by Toyota," 2016-03-07 — https://pressroom.toyota.com/wearable-mobility-visually-impaired-toyota/
- Toyota Newsroom "Project BLAID" tag archive (shows the lone 2016-03-07 entry — death-by-silence evidence) — https://pressroom.toyota.com/tag/project-blaid/
- AFB AccessWorld, J. Pauls, "Project BLAID: Toyota's Contribution to Indoor Navigation for the Blind," May 2016 — https://afb.org/aw/17/5/15333
- Engadget, "Toyota's wearable for the blind sees the world through cameras," 2016-03-07 — https://www.engadget.com/2016-03-07-toyota-project-blaid.html

**Horus / Eyra**
- PR Newswire / Eyra, "Horus Technology Launches Early Access Program… Rebrands Company as Eyra," 2016-10-26 — https://www.prnewswire.com/news-releases/horus-technology-launches-early-access-program-for-ai-powered-wearable-for-the-blind-rebrands-company-as-eyra-300351430.html
- New Atlas, "Horus wearable helps the blind navigate, remember faces and read books," 2016-10-31 (~$2,000 price, Tegra K1, bone-conduction) — https://newatlas.com/horus-wearable-blind-assistant/46173/
- Eyeware Tech "About" (establishes Eyeware = separate Sept-2016 EPFL/Idiap spin-off under Kenneth Funes — *refutes the "Eyra→Eyeware pivot" premise*) — https://eyeware.tech/about/
- Crunchbase, Eyra (formerly Horus Technology) — funding + "doubtful… another funding round" — https://www.crunchbase.com/organization/horus-technology
- *Flag: no formal shutdown notice or refund-program document found; AppleVis & Wayback Machine were server-blocked to the fetcher — a known gap.*

**Google Glass (consumer)**
- Mat Honan, "I, Glasshole: My Year With Google Glass," WIRED, 2013-12-30 (canonical bystander-reaction account; original paywalled — quotes corroborated via secondary coverage) — https://www.wired.com/2013/12/glasshole/
- A. Newcomb, "From 'Glassholes' to Privacy Issues: The Troubled Run of… Google Glass," ABC News, 2015-01-16 (Consumer Watchdog "perfect stalker's tool"; venue bans) — https://abcnews.go.com/Technology/glassholes-privacy-issues-troubled-run-edition-google-glass/story?id=28269049
- AndroidPolice, "Glass Explorer Program Will End January 19th As Glass 'Graduates' Google[x]," 2015-01-15 — https://www.androidpolice.com/2015/01/15/glass-explorer-program-will-end-january-19th-glass-graduates-googlex/
- "Google Glass," Wikipedia (timeline, $1,500, MPAA 2014-10-29 advisory, Enterprise 2017, discontinued 2023-03-15) — https://en.wikipedia.org/wiki/Google_Glass
- *Flag: "glasshole" coinage origin is disputed (2013 emergence; Urban Dictionary Mar 2014 confirmed). Venue bans were largely preemptive.*

**OrCam MyEye**
- CTech (Calcalist), "OrCam closing glasses department, cutting dozens of jobs in third round of layoffs this year," 2024-07-28 (the LLM-killed-us quote; glasses dept closed) — https://www.calcalistech.com/ctechnews/article/hy0rv6qya
- CTech, "OrCam lays off 16% of workforce," 2022 (62 employees) — https://www.calcalistech.com/ctechnews/article/ry5v11kgvo
- CTech, "OrCam cuts almost half of workforce in second round of layoffs in four months," 2024 — https://www.calcalistech.com/ctechnews/article/skd15oj4a
- CTech, "OrCam fights for survival as investor battle, layoffs and last-ditch funding push escalate" — https://www.calcalistech.com/ctechnews/article/rkp8w111nyg
- OrCam device, Wikipedia (Mar 2021 $50M raise at $1.5B; planned $2.5B+ NY IPO that never happened) — https://en.wikipedia.org/wiki/OrCam_device
- Product/price: https://www.orcam.com/en-us/orcam-myeye-3-pro

**Envision Glasses**
- 9to5Google, "Google has discontinued the Glass Enterprise Edition," 2023-03-15 (sales stop 2023-03-15; support ends 2023-09-15) — https://9to5google.com/2023/03/15/google-glass-enterprise-edition-discontinued/
- Envision Glasses (product/features) — https://www.letsenvision.com/glasses/home · store/pricing — https://shop.letsenvision.com/products/glasses-home

**Aira**
- J. Mosen, "Aira's astounding communications fail, or how to lose friends and alienate people," 2023-01-16 ($50/hr→$100/hr; "people costs… significant… sustainable business model was always going to be a challenge") — https://mosen.org/airapricing/
- Aira, Personal Subscriptions (consumer plans still exist) — https://aira.io/subscriptions/
- Aira, Access Partners (B2B "sponsored access," 3,000+ locations, airports) — https://aira.io/our-partners/

**eSight**
- Gentex IR / GlobeNewswire, "Gentex Announces eSight Acquisition, Set to Showcase Advanced Vision Tech at CES 2024," 2024-01-07 — https://www.globenewswire.com/news-release/2024/01/07/2805000/32299/en/Gentex-Announces-eSight-Acquisition-Set-to-Showcase-Advanced-Vision-Tech-at-CES-2024.html
- MarketScreener (citing Gentex SEC disclosure): "$88.9M… closed Nov 2, 2023" ($18.9M cash + $9.4M note + up to $70M earn-out/10yr) — https://www.marketscreener.com/quote/stock/GENTEX-CORPORATION-9464/news/Gentex-Corporation-acquired-Certain-Technology-Assets-of-eSight-Corporation-for-88-9-million-45689949/
- Display Daily, "The eSight 3 Headset…," 2017-02-18 ($9,995; "not covered by health insurance in the US") — https://displaydaily.com/the-esight-3-headset-offers-help-to-the-vision-impaired/
- eSight Go pricing ($4,950 / $6,600 CAD; VA 100%; financing) — https://www.esighteyewear.com/esight-go-pricing/
- AFB AccessWorld, "The New eSight 4 Wearable," Nov 2021 ($5,950) — https://afb.org/aw/21/11/17299
- CNBC, "Amazing electronic glasses help the legally blind see, but they are costly," 2017-09-20 (~$15k out-of-pocket for an earlier owner) — https://www.cnbc.com/2017/09/20/these-amazing-electronic-glasses-help-the-legally-blind-see.html

**Microsoft Soundscape**
- Microsoft Research, Soundscape support page (pulled 2023-01-03; installs stop 2023-08-30) — https://www.microsoft.com/en-us/research/product/soundscape/support/
- AppleVis, "Microsoft to Discontinue Its Soundscape App and Make the Code Available as Open-Source," Dec 2022 — https://www.applevis.com/blog/microsoft-discontinue-its-soundscape-app-make-code-available-open-source-software
- GitHub microsoft/soundscape — https://github.com/microsoft/soundscape

**.lumen**
- SeedBlink / .lumen, "lumen raises €5M for its glasses for the blind," 2024-07-17 — https://seedblink.com/press-room/2024-07-16-lumen-raises-eur-5m-for-its-glasses-for-the-blind
- New Atlas, ".lumen AI glasses…," 2025-12-23 (€9,999, reservations only, sensor spec) — https://newatlas.com/wearables/dotlumen-ai-glasses-blind-independence/
- Romania Insider, ".lumen closes €5M round led by Catalyst Romania," Jan 2025 — https://www.romania-insider.com/lumen-funding-catalyst-ro-jan-2025

**Biped NOA**
- biped.ai homepage (NOA, 170°, bone-conduction, pricing) — https://biped.ai/
- Startupticker, "biped secures CHF 1.2M to enter US market and expand in Europe" — https://www.startupticker.ch/en/news/biped-secures-chf-1-2m-to-enter-us-market-and-expand-in-europe

**Brainport V100 (Wicab)**
- FDA De Novo DEN130039 (cleared 2015-06-18) — https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN130039.pdf
- Federal Register classification, 2015-09-22 — https://www.federalregister.gov/documents/2015/09/22/2015-24026/medical-devices-ophthalmic-devices-classification-of-the-oral-electronic-vision-aid
- Wicab BrainPort Vision Pro ("only available in China"; lapsed US/EU date) — https://www.wicab.com/brainport-vision-pro

**Sunu Band / BuzzClip / Maptic**
- Crunchbase: Sunu (permanently closed) — https://www.crunchbase.com/organization/sunu · sunu.com → domain-for-sale listing — https://www.atom.com/name/SUNU
- U of T Engineering on iMerciv → MapinHood pivot — https://news.engineering.utoronto.ca/this-u-of-t-startup-aims-to-make-the-world-more-navigable-for-pedestrians/
- Dezeen, "Maptic," 2017-08-02 (student concept) — https://www.dezeen.com/2017/08/02/maptic-wearable-guidance-system-visually-impaired-design-products-wearable-technology-graduates/ · Cooper Hewitt collection record — https://collection.cooperhewitt.org/objects/1158794665/

**Project Guideline (Google)**
- Google Research, "Open-sourcing Project Guideline…," 2023-11-21 — https://research.google/blog/open-sourcing-project-guideline-a-platform-for-computer-vision-accessibility-technology/
- GitHub google-research/project-guideline — https://github.com/google-research/project-guideline

**Assistive-tech abandonment (the kill-pattern #1 evidence)**
- Phillips, B. & Zhao, H. (1993). "Predictors of Assistive Technology Abandonment." *Assistive Technology* 5(1):36–45. PMID 10171664 — **29.3% abandoned; mobility aids highest; Year-1 & Year-5 cliffs** — https://pubmed.ncbi.nlm.nih.gov/10171664/
- Barak Ventura, Hamilton-Fletcher & Rizzo (2026). "From abandonment to adoption…" *Frontiers in Digital Health*, DOI 10.3389/fdgth.2025.1719746 — **optical AT for blind/low-vision 17–50% abandoned**; ~29% overall — https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1719746/full
- Jiménez-Arberas & Ordóñez-Fernández (2021). *Rev Neurol*, PMID 34109998 — mobility AT 17.5% abandoned (neuro) — https://pubmed.ncbi.nlm.nih.gov/34109998/
- A. Lee, "The unimprovable white cane," Wellcome Collection, 2021-11-25 — ETA graveyard (Sonic Guide, LaserCane, UltraCane economics; cane endures) — https://wellcomecollection.org/stories/the-unimprovable-white-cane
- Khan, Khusro & Ullah (2018). "Technology-assisted white cane…" *PeerJ*, PMC6292384 — trust/reliability/echolocation design bar — https://pmc.ncbi.nlm.nih.gov/articles/PMC6292384/
- *Flag: "one missed obstacle → permanent cane reversion" is a well-grounded design **hypothesis** (supported by the abandonment literature + the ETA failure record), NOT a single quantified study. A targeted r/Blind / NFB verbatim-quote pull remains a follow-up.*

### Verification flags (summary)
- **BLAID:** no discontinuation notice exists; death *inferred* from total silence after the lone 2016-03-07 release (absence documented via Toyota's own tag page).
- **Horus/Eyra:** the **"pivot to Eyeware" premise is incorrect** (Eyeware = separate EPFL spin-off; Eyra's founders later at "Sungazer"); **no shutdown notice or refund saga found** — refund question unverified.
- **Aira:** consumer plans **still exist** (no 2025 price increase) — this is a *pivot of emphasis to B2B*, not a consumer shutdown. Do not overstate.
- **eSight:** "strategic vs. distress" is officially **strategic**; the distress read is *inferred* from deal structure (small cash + large 10-yr earn-out). Close = 2023-11-02; announce = 2024-01-07 (both dates correct, different events).
- **Envision:** alive and selling, but on an **EOL'd hardware platform** — "struggling/orphaned," not dead.
