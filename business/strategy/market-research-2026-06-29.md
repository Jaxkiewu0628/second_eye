# Second Eye — Market Research Synthesis

_Source: /deep-research run (111 agents, 28 sources fetched, 127 claims, 25 adversarially verified with 3-vote checks). 2026-06-29. Raw output: `../research/deep-research-raw-2026-06-29.json`._

## Verdict: CONDITIONAL GO — but our wedge premise failed verification

We had committed to "mobility (obstacle detection) is the painkiller, reading is commoditized." The evidence does not support that, and the only signal that exists leans the other way. The product direction (offline cheap glasses) survives; the **feature wedge** is now open and must be settled with users.

## What is validated (the real assets)
- **Price + offline + one-time = genuine white space.** Every incumbent sits far above our band: Envision Glasses $2,499; Glide $1,199 + mandatory $30/mo; Aira $26–$1,160/mo human-service subscription. A sub-$700, offline, no-subscription device is differentiated. Caveat: we must beat "free phone app + white cane," not just the expensive players.
- **Open positioning lane.** Envision (best-funded glasses player) does reading only, zero obstacle detection. Glide does mobility but is a handheld wheeled robot, not glasses. "Obstacle detection on light audio glasses" is not directly occupied.
- **Real cane gap.** Peer-reviewed: the white cane gives no information about head-level obstacles; ~40% of blind users report head-level accidents yearly. A camera wearable cut collisions in a trial — but that trial was competitor-funded (Biped), lab-only, n=13, chest vest not glasses. Promising, not proof.
- **Payer path exists.** VA provides blind veterans "electronic mobility devices" at no out-of-pocket; vocational rehab funds smart glasses + OCR readers. (Medicare excludes low-vision aids via the "eyeglass exclusion"; consumer health insurance generally won't pay.)
- **Regulatory looks manageable.** FDA "general wellness" off-ramp if positioned as assistive (not medical); precedent that even a vision-substitution aid cleared as the lighter Class II. OrCam/Envision stay out of FDA scope this way. Don't market it as "medical treatment."

## What got challenged
1. **Mobility-first is NOT validated.** The one direct blind-user preference study ranked Text Recognition #1, Scene Query #2, Obstacle Detection #3. Those numbers failed adversarial verification (can't cite as fact), but they don't flip to support us either — the question is genuinely open and the only signal tilts toward reading.
2. **Market is smaller and more low-vision-skewed than assumed.** ~1M Americans legally blind; the truly-no-vision core that fits an audio-only/no-display device best is under 1M. Low-vision (retains sight, may want a display we are not building) outnumbers them ~3:1. "No display" keeps us cheap but caps the initial market.
3. **Abandonment is the kill-risk.** ~29% of assistive devices get abandoned, driven by lack of user buy-in and poor real-world performance. Lab demos don't count; outdoor performance + blind-user co-design decide viability.

## Top 3 risks
1. **Wrong wedge** — building obstacle-first when users want reading-first. Mitigate with the discovery calls before any spec.
2. **Abandonment** — real outdoor performance can't match a lab; users drop it and keep the cane. Mitigate with co-design and cane-complement (not cane-replacement) positioning.
3. **The free floor** — Seeing AI and Be My Eyes are free and good. Hands-free + offline + instant must be 10x better than pulling out a phone.

## The 5 things to validate next (the gate)
1. Mobility vs. reading vs. both — structured interviews + willingness-to-pay with 8–10 blind users and 3 O&M instructors.
2. Would they actually keep wearing it alongside a cane/dog (esp. guide-dog users)?
3. The free-app comparison — watch them use Seeing AI; what does it fail at that hands-free offline would nail?
4. The payer path — one call each to a VA VIST coordinator and a state voc-rehab counselor: would you fund this, and how?
5. Outdoor performance reality — repoint Jackie's detector into a "hear obstacles by direction" demo and walk a real sidewalk.

## Honest gaps (budget-dropped, NOT "no signal" — for a future research pass)
Global WHO sizing; full competitor teardown (OrCam, eSight, WeWALK, .lumen, Ara, and the free-app floor in detail); the failure graveyard (Toyota BLAID, Horus, Google Glass products); exact reimbursement/HCPCS codes.

## Key sources
- Population: NEI/NIH, JAMA Ophthalmology (Varma/Chan et al.) — https://pmc.ncbi.nlm.nih.gov/articles/PMC5833607/
- User preference: ASSETS 2023 / arXiv 2505.19325 — https://arxiv.org/html/2505.19325v1
- Cane gap / wearable efficacy: Scientific Reports 2026 (Pittet/Biped) — https://www.nature.com/articles/s41598-026-37578-9
- Abandonment: Phillips & Zhao 1993 — https://pubmed.ncbi.nlm.nih.gov/10171664/
- Competitor pricing: Envision (shop.letsenvision.com), Glide (glidance.io), Aira (aira.io/subscriptions)
