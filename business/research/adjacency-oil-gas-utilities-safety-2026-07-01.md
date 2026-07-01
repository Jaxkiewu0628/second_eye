# Adjacency scan — Oil / Gas / Chemical / Power / Utilities worker-safety wearables (2026-07-01)

> Angle owner: CEO subagent. Question: does our "便宜 + 可穿戴 + 端侧离线个人级实时预警 + 数据飞轮" playbook
> have a real seam (护城河机会) in the high-hazard-industry safety-wearable market?
> Verdict: **LEAN-RED with one genuinely unclaimed angle.** See bottom.

## Scene / how the money actually works today
The dominant category here is **connected gas-detection + lone-worker telemetry** — a mature, consolidated,
**cloud + subscription** business. The wearable's job is (a) sniff gas (H2S/CO/O2/LEL) and (b) call for help
when a worker falls / stops moving. It is a **connectivity + monitoring** play, not an **on-device perception** play.

- Market: Lone-worker safety solutions ~$10.1B (2023) → ~$17B by 2031, ~15% CAGR (Verified Market Research).
- Connected worker installed base heading to ~17.5M devices / ~$2.8B revenue by 2034 (Transforma Insights).
- Blackline Safety (category leader) went **private April 2026, Francisco Partners, up to $850M**; ARR ~$90.5M
  (Q ending Jan 2026), targeting $145–149M ARR by Oct 2027. 40% rev CAGR since G7 launch. **This is a proven,
  well-capitalized, subscription-first market** — the opposite of a greenfield.

## Players (name / form / offline? / price)
| Player | Form | Offline? | Price | Note |
|---|---|---|---|---|
| **Blackline Safety** G7 / G7c / G8 / EXO | Clip-on puck (gas + lone-worker) | **No** — cloud-first (Blackline Live); device alarms locally but value = live monitoring/analytics | ~$38/mo multi-gas, ~$33/mo lone-worker (device+plan, 4-yr amortized) | Category leader. Fall = accelerometer/IMU. **No camera, no vision.** |
| **Honeywell** BW Solo / MicroClip X3 / BW Ultra | Clip-on gas detector | Partial — hardware-first, BLE, software optional | Hardware sale + optional SaaS | "Sells HW, hopes you adopt SW." No vision. |
| **MSA Safety / Industrial Scientific (Fortive) / Dräger** | Clip-on gas detectors | Mostly local + optional cloud (Dräger = no direct-cloud) | Hardware-centric | Together w/ Blackline ≈ 35% of multi-gas installed base. No vision wearable. |
| **Guardhat** HC1 Communicator | Smart hard hat (RTLS + gas + IMU) | Needs RTLS/UWB infra | from **$1,500** | Proximity = **UWB/RFID tags + beacons**, not vision. IECEx/ATEX Zone 1 certified. |
| **Spacebands** | Wristband + machine beacons | Needs beacons on machines | from **$32/wearable/mo** (US), £25/mo UK 36-mo | Collision = **BLE beacon** tag-and-zone. HAVS/noise/PPE. |
| **Modjoul** SmartBelt / HaloGuard / Watchdog | Belt + RFID | Needs RFID infra | Subscription bundle | Ergonomics + **RFID** proximity. No vision. |
| **SlateSafety** BAND V2 | Armband | Cloud dashboard | Subscription | Heat-stress / physiology only. No hazard perception. |
| **RealWear** Navigator Z1 / HMT-1Z1 | Head-mounted display (ATEX Zone 1) | AR/remote-assist, cloud | ~$2.5–5k class | Remote expert video, **not** autonomous hazard alerting. |
| **Vuzix** Shield / M400 / Blade 2 | AR safety glasses (ANSI Z87.1) | Cloud/AR | ~$1–2k+ | HD cam + "AI awareness" marketing; not a shipped offline personal hazard-warning product. |
| **Iristick** | ATEX smart glasses | AR/remote | ~$4–6k | Remote assist. Not autonomous perception. |
| Tag/radar PWAS (ShieldSensor, Reactec R-Link, radar vendors) | Worker tag + machine reader / radar-on-machine | Local RF | Project-priced | **Collision avoidance = RF/UWB/BLE/radar on the machine**, not egocentric vision on the worker. |

## The two structural facts that define our seam
1. **Perception in this vertical is chemical + inertial, not visual.** Everyone detects **gas** (electrochemical
   sensors) and **falls** (accelerometer/IMU). Nobody ships an on-body **camera that sees an untagged physical
   hazard** (moving vehicle, unguarded edge, energized gear) and warns the worker. Our camera+ToF+YOLO perception
   is orthogonal to what the incumbents do.
2. **Collision/proximity avoidance is infrastructure-based (tag + beacon / RTLS / UWB / radar).** It requires
   tagging every vehicle and instrumenting the site; it can't see a hazard that isn't tagged. The one academic
   "smart-glasses proximity" system (Kim et al., 2020, construction/mining) **also uses BLE beacons, not vision.**
   → A **self-contained, no-infrastructure, vision-based** personal collision/edge warning is essentially unclaimed
   commercially. **This is the seam our playbook uniquely fits.**

## Our gap (where "cheap + wearable + on-device offline personal warning + data flywheel" fits)
- **Fit:** infrastructure-free, egocentric **vision** hazard warning (untagged vehicle approach, unguarded
  edge / fall-from-height, "you're inside the swing radius") — no beacons to install, works on day one, offline.
  This is the exact thing the tag/beacon/radar incumbents structurally cannot do, and the exact thing our
  YOLO+ToF+bone-conduction stack already does for blind mobility. Highest-fit vertical: **fall-from-height /
  edge detection** (downward ToF — we already pulled drop-off detection into V1) and **vehicle/equipment
  proximity in yards** without site instrumentation.
- **Data flywheel fit:** strong — a fleet of camera wearables in one operator's sites is a near-miss video
  corpus nobody else has; that compounds.

## The wall (why LEAN-RED, not blue)
1. **Intrinsic safety (ATEX/IECEx Zone 1, NEC C1D1) is a hard gate, and cameras are the worst case.** Ex
   environments cap stored energy; a compute-heavy camera + battery is precisely what IS certification fights.
   Certified IS wearable cameras today are **$5,000–6,500**. This obliterates our "$141 BOM / cheap" edge for
   the *classified* areas of oil/gas/chem — our cost moat evaporates exactly where the hazard is.
2. **Incumbent lock is deep and subscription-funded.** Blackline/Honeywell/MSA/Dräger own the safety-manager
   relationship, compliance reporting, and 75-country service. A me-too "connected safety puck" = suicide (铁律①).
3. **Gas + man-down are table stakes we don't do.** Buyers here buy gas detection first; a vision-only device
   is a *complement*, not a replacement — narrows us to an add-on, not the primary purchase.
4. **B2B enterprise sale ≠ our current GTM.** Second Eye's traction path is grants/VA/direct-to-individual for
   blind users. Selling to EHS departments in energy majors is a long procurement, safety-certification,
   pilot-gated motion — a different company.

## Honest verdict
- **blue_or_red = lean-red.** The vertical is a mature, consolidated, subscription-first RED ocean for the
  *incumbent job* (gas + lone-worker telemetry). BUT there is **one un-occupied angle** that fits our unique
  edge: **infrastructure-free, on-device-vision personal hazard/edge/collision warning.** That angle is real
  (no shipped commercial product does it) — its blocker is **intrinsic-safety certification + cost**, not
  competition.
- **Where the seam is actually workable:** the **non-Ex / lower-classification** slices of these industries —
  **electric/gas utility field & line work, water/wastewater, construction-adjacent yards, solar/wind O&M** —
  where a body-worn camera does **not** need Zone-1 IS certification. There, our cheap+offline+vision+flywheel
  combo has a genuine, unclaimed lane (fall-from-height + untagged-vehicle proximity, no site instrumentation).
  **The classified core of oil/gas/chem is a trap** (IS cost wall).
- **Recommendation:** do NOT chase the gas-detection / lone-worker market head-on. If we probe this adjacency
  at all, probe the **infrastructure-free vision-based fall/edge/vehicle-proximity** wedge in **non-Ex field
  work** (utilities / water / renewables O&M), where our playbook's four properties all hold. Everything else
  here is red.

## Sources
- Blackline pricing/plans — blacklinesafety.com/solutions/services/pricing-plans
- Blackline take-private ($850M / Francisco Partners / ARR) — businesswire 20260408058099; pehub; betakit
- Connected-worker market structure — William Blair "Connected Worker Revolution" (Apr 2025, Sparenblek)
- Market size/CAGR — Verified Market Research (lone worker); Transforma Insights (17.5M devices/$2.8B by 2034)
- Honeywell BW / Blackline compare — rockallsafety.co.uk; shashi.co (Francisco Partners analysis)
- Guardhat $1,500 + UWB/RFID proximity, IECEx/ATEX — time.com (100 Best Inventions 2020); prnewswire IS cert
- Spacebands pricing + BLE collision — spacebands.com pricing + machine-collision
- Modjoul/SlateSafety — modjoul.com; slatesafety.com
- Fall detection = accelerometer/IMU — blacklinesafety.com blog; aware360.com; extronics.com
- Intrinsically-safe camera $5–6.5k + why cameras are worst-case for IS — intrinsicallysafestore.com; realwear.com blog
- Tag/beacon/radar PWAS infrastructure dependence — shieldsensor.sa; experttime.net; reactec.com
- Smart-glasses proximity = BLE beacons, academic, 2020 — Kim et al., PMC7068505
- PPE-compliance CV research (fixed/cloud, not wearable) — arxiv 2408.07146; PEC-YOLO arxiv 2501.13981
