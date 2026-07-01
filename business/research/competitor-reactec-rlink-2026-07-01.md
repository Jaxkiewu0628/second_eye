# Competitor verify — Reactec R-Link (worker-safety wearable)

**Date:** 2026-07-01 · **Method:** adversarial verification vs primary sources (default = distrust the given blurb)
**Camp:** B (wearable / UWB proximity + exposure monitoring) — same as the input hypothesis.
**Verdict:** ✅ **Real; input blurb CONFIRMED and sharpened.** Leaves our gap wide open.

---

## What it actually is
Third-gen workplace wearable **smartwatch** (launched July 2022). Two bundled functions:
1. **HAVS / MSD monitoring** — hand-arm vibration exposure (HSE points), real-time on-wrist display + alert when personal threshold exceeded. This is Reactec's 20-yr core.
2. **Proximity warning** — **UWB** (ultra-wideband) alert when the worker gets too close to **beacon-tagged** vehicles/plant, or an **RFID-tagged** restricted zone. Watch vibrates/alerts.

Worker device = **smartwatch only** (no GPS, "does not track location" per Levitt-Safety). Hazards must be **instrumented**: you place **R-Link beacons** on vehicles/plant and **RFID tags** on zones. Data → single **gateway at the charging area** → **cloud (Reactec Analytics)** every 15 min for supervisor dashboards.

## Offline? → **PARTIAL** (matches input's "partial")
- The **real-time proximity alert is local UWB** peer radio: watch ↔ beacon, triggers on-wrist without needing the cloud in the moment. So the *safety alert itself* is not cloud-gated. Primary/distributor pages imply local triggering; **not explicitly stated** that it works fully offline — the value proposition ("eco-system... dependent only on an internet connection through a public mobile network or local wifi") is framed around connectivity, and the analytics/visibility layer is **cloud-mandatory**.
- Net: alert = edge/local; **product = cloud-tethered** (analytics, config, fleet visibility, the thing you actually buy). Not an offline product.

## Is it "personal real-time danger warning"? → **YES, but only tag-relative, not environmental**
- It DOES give the individual worker a real-time on-body warning (unlike pure after-the-fact PPE-compliance/analytics tools). So the input's framing is fair.
- **BUT the warning is relative distance to a pre-placed radio tag** — "you are near beacon #7." It has **no perception of the world**: no camera, no vision/YOLO, no depth/ToF. It cannot warn about an **un-tagged** hazard, a static obstacle, a hole/edge (**no fall detection**), an untagged moving object, or anything nobody bolted a beacon onto. Scope = people↔tagged-vehicle/zone proximity + arm-vibration. That's it.

## Price / model → subscription + separate hardware
- **shop.reactec.com** sells it as an **annual subscription**, hardware bought separately. HAV+Proximity subscription is listed **POA** (price on application / "request a quote"), £ (USD option at checkout).
- Visible tiered per-watch annual figures on the shop: **£30 (41–100 watches) → £46 → £50 → £54 (501–5000)** — i.e. **volume DISCOUNTS as you buy MORE**, per-watch/yr, before adding the watch hardware cost. Enterprise fleet motion, not an individual purchase. (Exact single-unit price + hardware cost still gated behind a quote.)

## Funding / corporate
- **Acquired by Ideagen on 2025-08-18** (undisclosed sum) — Ideagen's 6th acquisition of 2025, folding Reactec into its EHS/GRC compliance suite. Support email is now `@ideagen.com`, confirming the deal. **No longer independent.**
- Pre-acquisition: University of Edinburgh spin-out (2001). Total funding modest (~£1.4M–$8.3M depending on source; Archangel Investors + Scottish Enterprise). Revenue ~**$5.9M / ~£3.9M**, ~47 employees. A mature, small, niche EHS-hardware company — now a compliance-software feature line.

---

## leaves_gap_for_us → **YES — wide.** Different problem, different physics.
Reactec R-Link is the archetype of **camp B**: it protects workers by **instrumenting the environment** (beacons + RFID) and having a **radio bracelet feel proximity to those tags**, then selling the **cloud compliance dashboard**. It is:
- **Not cheap for the buyer** — per-watch annual subscription + hardware + you must buy & deploy beacons on every vehicle and RFID tags on every zone (infrastructure cost/labor). Enterprise fleet economics.
- **Not environment-aware** — zero vision/depth; blind to any hazard nobody pre-tagged; **no fall/edge/obstacle detection**.
- **Not an offline product** — safety ping is local, but the product you pay for is cloud-tethered.
- **Not truly "personal-scene" perception** — it's relative-distance-to-a-tag, not "understand what's in front of this worker."

**Our open lane (unchanged / reinforced):** cheap (~$141 BOM), ~30g wearable, **on-device offline vision (camera+ToF+YOLO)** that perceives the **actual environment** and gives an **instant bone-conduction/haptic warning** for **un-instrumented** hazards — moving machinery, danger zones, collisions, **falls/edges**, isolated work — **without bolting beacons onto every vehicle or wiring a site**, and **without a cloud subscription** to get the alert. Reactec needs you to tag the world first and pay a fleet SaaS; we read the world as-is. **No overlap on the wedge.**

## Sources
- https://www.reactec.com/products/r-link/proximity/
- https://www.reactec.com/products/r-link/
- https://www.reactec.com/products/r-link/havs/
- https://shop.reactec.com/shop/subscriptions/r-link-annual-subscription-hav-proximity/
- https://www.levitt-safety.com/specialty-products/sound-vibration/rlink
- https://www.reactec.com/about/news/proximity-detection/ (July 2022 launch)
- https://www.ideagen.com/company/news/ideagen-expands-safety-solutions-with-reactec-acquisition (acquisition 2025-08-18)
- https://www.businesswire.com/news/home/20250817122865/en/Ideagen-Expands-Safety-Solutions-With-Reactec-Acquisition
- https://getlatka.com/companies/reactec (revenue $5.9M / ~47 staff)
- https://tracxn.com/d/companies/reactec/ (funding / acquisition data)
