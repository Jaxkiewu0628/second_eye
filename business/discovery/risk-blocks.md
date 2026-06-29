# Second Eye — Risk Blocks (validation register)

> Living register of the risks that must be validated before we commit the spec and raise.
> Last updated 2026-06-30. Companion to `status.md` (what's validated/risky) and `interview-guide.md` (the instrument).
>
> **Principle:** every risk has its *own* validation instrument. We do not "do some discovery calls" generically — each block names the specific test, the kill condition, and the pass signal. A risk isn't retired until its own instrument clears it.

## Map

| # | Block | Risk in one line | Owner | Instrument |
|---|---|---|---|---|
| 1 | Mobility / detection-trust | Can glasses+ToF reliably catch hazards outdoors, and is it trusted after a miss? | Jackie's demo (we set the bar) | Instrumented sidewalk walk + O&M sign-off |
| 2 | Persistency / abandonment | Will they still wear it in week 3? | Discovery + loaner pilot | "Device graveyard" Q now; DAU logging later |
| 3 | Willingness-to-pay | Does real money appear at $400–700? | Discovery | Revealed preference (what they spent, who paid) |
| 4 | Reimbursement reality | Will a funder actually write the check for *our* niche? | Research (done) + 2 funder calls | Documented precedent of funding a comparable device |
| 5 | Segment / buyer fit | Blind (our audio wedge) vs low-vision (wants a display)? | Discovery | Quota of both + self-routing A/B fork |
| 6 | Coexistence & stigma | Worn alongside the cane? Camera on the face tolerated? | Discovery + O&M | O&M coexistence Q + face-camera reaction |

---

## BLOCK 1 — MOBILITY / DETECTION-TRUST
- **Risk:** Can glasses + ToF reliably catch curbs, drop-offs, poles, overhangs/low branches outdoors — and does a real walker still trust it *after it misses one*?
- **Kill:** sustained misses on torso-and-above + drop-off hazards, or O&M instructors say "I'd never let a client rely on it."
- **Instrument (a test, not a call):** define the pass bar *before* the board arrives, then run it. Fixed ~500 m mixed route (curbs, parked bikes, A-frame signs, low branches); score **every hazard hit/miss** across N runs; cap the false-alarm rate so it isn't annoying. Then hand it to 2–3 O&M instructors + 2–3 blind walkers and let them try to break it.
- **Pass signal:** an O&M instructor willing to put a client on it.
- **Graveyard rules folded in:** engineer for **false-negative-aversion** (a missed hazard is the unforgivable error); **prove curb/pole detection on a real sidewalk before believing any demo** (the ETA graveyard — UltraCane, Sonic Guide — all demoed fine and never displaced the cane); **bone-conduction is the correct audio** because it leaves the ears open for echolocation and traffic — the AT literature explicitly warns that audio which blocks the user's own senses drives abandonment (→ Block 2).

## BLOCK 2 — PERSISTENCY / ABANDONMENT
- **Risk:** ~29% of assistive tech is abandoned (mobility worst; 17–50% for blind optical AT). Will they still wear it in week 3?
- **Kill:** it becomes a drawer device — high purchase, low daily-active use.
- **Instrument (predictors now, behavior later):**
  - *Now (pre-device):* every call runs a **"device graveyard" pass** — *what assistive tech did you buy and stop using, and exactly why* (comfort, stigma, battery, too slow, didn't trust it, blocked my hearing). Past abandonments predict ours.
  - *Later:* loaner pilot measuring **actual daily-active minutes** over 2–4 weeks + a 30-sec daily voice diary — behavior, not satisfaction scores.
- **Pass signal:** their graveyard is *not* full of head-worn / audio devices killed for reasons our device shares.
- **Graveyard rules folded in:** position as a **cane complement, never a replacement** (no ETA ever beat the cane head-on); don't block the user's residual senses (ears-open audio); design the out-of-box so trust is earned in week 1, not assumed.

## BLOCK 3 — WILLINGNESS-TO-PAY
- **Risk:** does real money appear at $400–700, one-time, no subscription?
- **Kill:** neither individuals nor funders pay; only subsidized giveaways move units.
- **Instrument — revealed preference, never "would you pay?":** ask what they *actually spent* on cane / phone / apps / OrCam and **who paid.** Anchor against real prices (WeWALK $850 + subscription; .lumen ~€10k; OrCam $4,490 — *now dead*). The honest WTP test is not their mouth — it's whether a funder says yes (→ Block 4).
- **Pass signal:** a credible "my VA/voc-rehab would cover this" beats ten "sure, I'd pay."
- **Graveyard rules folded in:** OrCam ($4,490) and eSight ($9,995→$5,950, then sold to Gentex) prove the category punishes "priced for nobody." Our sub-$700 + no-subscription is the deliberate inverse — but it still has to clear a funded-or-self-pay bar.

## BLOCK 4 — REIMBURSEMENT REALITY (the funder)
- **Risk:** will VA / voc-rehab / grants actually pay for **our** device, through a real mechanism? (Our model is funded purchase, not out-of-pocket.)
- **Kill:** no funder has a process for an *obstacle/mobility* aid *and* it's too pricey to self-pay → no viable channel.
- **Instrument:**
  - *Done:* research pass (`../research/reimbursement-hcpcs-2026-06-30.md`). **Verified:** VA issues no-cost "electronic mobility devices" and funds eSight/IrisVision 100%; voc-rehab funds AT but is **employment-gated** (Individualized Plan for Employment). **Killed myth:** Medicare/private insurance excludes low-vision aids — eSight/IrisVision never won it; drop "insurance-covered."
  - *Two calls, one sharp ask each:* a VA VIST coordinator and a state VR counselor — *"Have you ever funded an OrCam / WeWALK / Envision for a client? Walk me through the exact process and the price ceiling."*
- **Pass signal:** one *documented precedent* of a funder buying a comparable device — worth more than the whole sizing deck.
- **The catch (ties to Block 5):** every *proven* funding precedent is a low-vision **display** device (eSight, IrisVision) — *the segment we're not building for.* VA funding of our **obstacle/mobility** niche is unconfirmed and is the **#1 VA-call question.** If "display only," we need a new funding wedge or Block 5 gets louder.

## BLOCK 5 — SEGMENT / BUYER FIT
- **Risk:** truly-blind core (43M global / ~0.4–1M US, wants our audio alerts) vs low-vision (295M MSVI / ~3:1 in the US, may want a *display* we're deliberately not building). We could be building for the smaller room.
- **Kill:** the people with funding are low-vision and want magnification, not obstacle audio.
- **Instrument:** recruit a **quota of both** (≈6 blind/heavy-cane, ≈4 low-vision) and watch whose pain is acute and unmet. The interview guide's **"Glasses A (path) vs Glasses B (reading)" forced choice** is the self-routing fork — capture the pick *and the verbatim why,* tallied by group.
- **Pass signal:** blind cane-users light up at obstacle audio while low-vision keeps asking for a screen → confirms wedge *and* segment. A clean split = a segmentation decision, not a single wedge.

## BLOCK 6 — COEXISTENCE & STIGMA
- **Risk:** will they wear it *alongside* the cane/dog (we supplement, never replace), and tolerate a camera on their face? (Consumer Google Glass died on the "glasshole"/privacy backlash.)
- **Kill:** "it conflicts with my cane technique" or "I won't wear a camera on my face."
- **Instrument:** O&M instructors are the expert proxy for cane coexistence — ask directly whether it interferes with technique and whether they'd train with it. For stigma, gauge the face-camera reaction in calls.
- **Pass signal:** instructor "yes, I'd train with it" + users don't flinch at the face camera.
- **Graveyard rule folded in:** assistive framing + ADA legitimacy partly shields us from the Glass stigma (a medical/assistive purpose reads differently than a consumer camera) — lean into that positioning.

---

## Validated moats — don't re-litigate (proven by the graveyard)
- **Offline / no-subscription = economic + survival moat.** On-device YOLO+ToF means marginal cost of "obstacle ahead" is ~$0 (the structural antidote to Aira, whose per-minute human labor never scaled — Aira shifted *emphasis* to B2B sponsorship, the consumer plan never closed its unit economics). And no cloud benefactor can brick us — Microsoft killed Soundscape's Azure backend and it died; Google EOL'd the Glass that Envision is built on.
- **Reading is a free bonus, never the pitch.** OrCam's own exit statement: LLMs on phones made its $4,490 reading device "unnecessary." We sell the job phones *can't* do (continuous, hands-free, safety-critical mobility).

## What validates what
- **Block 1** → Jackie's outdoor demo (we own the scorecard + pass bar).
- **Blocks 2, 3, 5, 6** → the discovery calls (`interview-guide.md`, tagged by block).
- **Block 4** → research (done) + 2 funder calls (VA VIST coordinator, state VR counselor).

## Research backing
- `../research/global-market-sizing-2026-06-30.md` — 43M blind / 295M MSVI; US blind core ~0.4–1M; TAM ~78M, SAM ~4M, SOM ~2–6k units/3 yrs.
- `../research/reimbursement-hcpcs-2026-06-30.md` — VA verified, our niche unproven, Medicare dead, voc-rehab employment-gated.
- `../research/failure-graveyard-2026-06-30.md` — kill patterns: abandonment/trust collapse, priced-for-nobody, charging-for-free, cloud dependency, face-camera stigma.
