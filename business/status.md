# Second Eye — CEO / Business Status

> Single source of truth for the business side. Last updated: 2026-06-30.
> (Repo-wide status lives in the monorepo's top-level `STATUS.md`, maintained jointly. This file is the CEO/business view.)

## One-liner
Affordable, offline, hands-free AI glasses that tell a blind person what's in their path. Jackie Wu's Conrad-winning "YCane," realized.

## Direction (decided)
- **Path A:** offline, sub-$700, **freemium** assistive glasses — the **full mobility core works offline, free, no subscription**; an **optional paid cloud tier** adds enhancements (scene description, a learning agent). Sold direct, funded via grants / VA / voc-rehab; architected to grow into a broader offline visual co-pilot. **(S1 🟢 decided 2026-07-01 — `strategy/product-direction.md`.)**
- **Wedge = MOBILITY** (real-time obstacle / path detection while walking) as the reason-to-buy; **reading / scene as a free bonus, never the pitch.**
- **Why:** reading is commoditized to free (Seeing AI, Be My AI, Lookout) and OrCam — the $4,490 reading-hardware king — collapsed proving you can't charge for it. Mobility is the one job phones can't do, so it's the only durable hardware wedge.

## Engineering alignment (from Jackie's new monorepo, 2026-06-30) — STRONG
Jackie's `engineering/` side independently converged on the same thesis (no coordination):
- Pivoted from AR sports glasses → visual assistance (2026-06-29).
- Core = obstacle detection + bone-conduction "step 1.5 m ahead." **Mobility-first — matches our wedge.**
- Cites OrCam $4,490 and WeWALK $850 as competitors — same framing as our teardown.
- **Added a ToF depth sensor (VL53L5CX)** — directly de-risks the "can a thin frame detect obstacles" physics concern I flagged.
- **Form factor: lightweight glasses + neck-hung compute box** (V1 short cable, V2 wireless). Updates our "sub-50 g standalone" assumption: compute lives in a neck box, solving thermal / battery / compute.
- Chips: RK3576 to validate; RV1126B leaning for production.
- Parts: LubanCat 3 + IMX415 (~¥600) + VL53L5CX ToF (~¥40) — **ordered, ETA ~2026-07-01** (per Jackie, `../handoff/` HO-001). Once they land, the parts blocker clears and V1 board bring-up can start.

## What's validated (market research, adversarially verified)
- Price + offline + no-subscription + glasses = real white space. Cheapest mobility wearable competitor is Ara $2,750; the only glasses-form mobility product (.lumen) is €9,999.
- Mobility is the defensible hardware wedge (funded category: NOA, .lumen, Ara, Glide, WeWALK).
- Offline / on-device is unique — the whole field leans cloud + subscription.
- Payer path **partly verified** (research 2026-06-30, `research/reimbursement-hcpcs-2026-06-30.md`): VA.gov confirms no-cost "electronic mobility devices" and funds eSight/IrisVision 100% — a real channel; voc-rehab is real but **employment-gated** (must serve an Individualized Plan for Employment). **Caveats:** every *proven* precedent is a low-vision **display** device — VA funding of our **obstacle/mobility** niche is *unconfirmed* (the #1 VA-call question); **Medicare/private insurance is a dead end** (statutory low-vision exclusion; eSight/IrisVision never won it — drop "insurance-covered"). Regulatory: FDA assistive/general-wellness off-ramp is favorable and does **not** block VA/voc-rehab (eSight is Class 1, yet VA-funded).

## What's risky / needs validation
1. **Form-factor physics** — can glasses + ToF detect curbs / poles / branches reliably outdoors? (ToF + neck box help; validate with a real-sidewalk demo on the board.)
2. **Will users pay $400–700 for mobility hardware?** (Discovery calls.)
3. **Abandonment** (~29%, mobility worst) and the **safety-trust bar** — one missed obstacle kills trust.
4. **Free-app floor** for the reading bonus; cheap "AI glasses" entrants coming (e.g. EchoVision).
5. **Market smaller / low-vision-skewed** — truly-blind core <1M US; low-vision (~3x bigger) may want a display we're not building.

## Competitive snapshot
OrCam (reading, $4,490) — DEAD / exited vision. Envision (reading, $2,499) — struggling. eSight (low-vision display, $4,950). Mobility field: .lumen €9,999, Ara $2,750, NOA £800 + sub, Glide $1,199 + sub, WeWALK $850–1,150. Free apps (Seeing AI / Be My AI / Lookout) own reading. Full teardown: `strategy/competitive-landscape.md`.

## IP status
Not a blocker. Jackie owns YCane (Conrad T&C). New tech is his own post-2023 build. Cleanups: check WFLA student-IP policy; get a no-claim note from old YCane teammates; drop "YCane" → "Second Eye"; clean US founder IP-assignment at incorporation. Details: `strategy/ip-status.md`.

## Document index (this folder)
- `strategy/second-eye-design-doc.md` — the plan (Path A, premises, approaches, assignment)
- `strategy/market-research-2026-06-29.md` — research synthesis
- `strategy/competitive-landscape.md` — full competitor teardown
- `strategy/ip-status.md` — IP / ownership
- `strategy/product-direction.md` — **Tier-1 strategic blockers (S1 ideology → S2 competition → S3 profit); the device-vs-platform decision**
- `discovery/interview-guide.md` — discovery-call script (the gate), tagged to risk blocks
- `discovery/recruiting-plan.md` — recruiting + outreach templates
- `discovery/risk-blocks.md` — **validation register: the 6 risk blocks, each with its own kill condition + instrument**
- `research/global-market-sizing-2026-06-30.md` — global sizing (43M blind / 295M MSVI; TAM/SAM/SOM)
- `research/reimbursement-hcpcs-2026-06-30.md` — payer reality (VA verified, our niche unproven, Medicare dead)
- `research/failure-graveyard-2026-06-30.md` — post-mortems + kill patterns → design/GTM rules
- `research/deep-research-raw-2026-06-29.json` — raw research archive
- `todo.md` — action items

## Org / folder structure (migration in progress, 2026-06-30)
- **NEW monorepo:** github.com/Jaxkiewu0628/second_eye → cloned to `~/dev/second_eye_repo/`. Structure: `engineering/` (Jackie), `business/` (CEO — us), `design/` (shared), top-level `STATUS.md` (joint).
- **This folder** (`~/dev/second_eye/ceo/`) is our CEO work; it moves INTO the monorepo's `business/` folder.
- The old `~/dev/second_eye/` scaffold (with the legacy `ar-sports-glasses` clone) is superseded by the monorepo's `engineering/` and can be retired after the move.

## Handoff log (CEO ⇄ Jackie) — what each HO is about
> HO titles are just numbers; this maps each to its subject so we know which to check when working a topic. Full channel + threads: `../handoff/index.md`.

| HO | Subject / why it exists | State | Latest |
|----|----|----|----|
| HO-000 | Example specimen (format demo) | 🗄️ example | not a real task |
| HO-001 | Channel round-trip test (+ parts-arrival sync) | ✅ done | system verified; parts ordered, ETA ~2026-07-01 |
| HO-002 | **S1 platform decision** — future-functions roadmap + eng feasibility/architecture | ✅ done (archived) | S1 拍板 🟢 platform + freemium + blind-core; Jackie: modular engine ✅, split-body required, scene-desc needs cloud |
| HO-003 | **Roadmap sync** — multi-version product roadmap (`strategy/roadmap.md`), eng review | ✅ done (archived) | Jackie confirmed order/split-body/thermal; 3 fixes backfilled — **battery 13.7h→5–6h**, V2 wireless needs HW rev, OCR de-duped |
| HO-004 | **S1 decided + medical opportunity** — notify Jackie of the 3 decisions + the caregiver/vitals expansion idea | 📤 ball in **ENG** | FYI / 前瞻；未来方向不影响 V1；医疗机会为未验证假设 |

## Next (the gate) — see `todo.md`
Outdoor obstacle-detection demo on the board + 8–10 discovery calls. Everything waits on these.
