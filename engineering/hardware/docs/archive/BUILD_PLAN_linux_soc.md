# Build Plan — AR Sports Glasses (Linux SoC / RV1106 approach)

_Last updated: 2026-06-23_

## 0. Architecture thesis (why this approach)

The core problem is **transfer-bound, not compute-bound** — but it's transfer-bound *because* the ESP32-S3 has no hardware video codec and a weak shared radio. The fix is to move compute onto the device so you transmit far less:

- **Lever ladder** (cheapest-power first):
  1. **Send results, not pixels** (~10–100 kbps) — track on-device, transmit ball coords / HR / trajectory. BLE is enough.
  2. **Compress on-device** (H.265, 2–5 Mbps) — stream video the phone processes.
  3. Brute-force raw/MJPEG over a fat radio (avoid — melts a wearable).

The RV1106 supports **all three** because it has an ISP + hardware H.264/H.265 encoder + ~1 TOPS NPU + Linux (radio freedom). This plan front-loads the cheap pipeline wins and pushes the **AR optics** (the hard, expensive part) to a decoupled track.

## 1. Core platform

| Role | Part | Notes |
|---|---|---|
| Dev board | **Luckfox Pico Ultra W** (~$30–45) | RV1106G3: Cortex-A7 + RISC-V MCU + ~1 TOPS NPU + ISP3.2, 256 MB DDR3L, 8 GB eMMC, onboard 2.4 GHz WiFi 6 + BT5.2, MIPI-CSI, RGB-LCD, USB |
| Camera | bundled 5 MP MIPI-CSI (SC530AI) | for golf, evaluate a **global-shutter** sensor to avoid rolling-shutter smear on a fast ball |
| Production target | **Luckfox Core1106 SoM** | solderable, 112 castellated pins — drops onto your own carrier PCB |

## 1b. Form factor & dimensions — decide *where compute lives* early (not in Phase 4)

The dev board proves the pipeline but never ships. Size reality:

| Form | Size | Fits a temple arm (~6–10 mm internal width)? |
|---|---|---|
| Luckfox Pico Ultra W dev board | several cm + headers/connectors | ❌ bench only |
| Core1106 SoM (module) | **30 × 30 mm** | ❌ too big — it's a camera/IoT module, not eyewear |
| Bare **RV1106** SiP (chip + DDR in one package) | **~10–15 mm** | ✅ only on a **custom rigid-flex PCB** |

**Reference — Meta Ray-Ban Display teardown:** components split across **both arms** (one = battery + speaker + mic; the other = motherboard w/ Snapdragon AR1 + flash), **flex PCB routed through the hinges**, **960 mWh** battery, **69 g** total (comfort target ~40–50 g).

**Architecture fork — pick before Phase 4:**
- **Standalone in-frame:** heaviest/hottest; ~1–2 h battery at ~0.5–1 W active video.
- **Glasses + tethered puck (recommended to evaluate):** RV1106 + big battery in a pocket/clip puck; glasses carry only camera + microdisplay + PPG + IMU + a thin cable.
- **Glasses + phone:** lightest in-frame; pays a wireless-latency cost.

**Implication:** the SoC is *not* the size blocker — **battery + optics + thermal are.** The highest-leverage slimming decision is keeping the heavy compute and the big battery **off the frame**. This is an *early architecture decision*; Phase 4 only executes it.

## 2. Software stack

| Layer | Tool |
|---|---|
| OS | Luckfox SDK (Buildroot or Ubuntu), Rockchip BSP kernel |
| Camera / ISP | V4L2 + Rockchip `rkaiq` |
| HW video encode | **Rockchip MPP** (H.264 / H.265) |
| Streaming | GStreamer + RTSP, or **WebRTC** for low latency; or just push results over MQTT/BLE |
| On-device AI | **RKNN-Toolkit2** (convert ONNX/YOLO → `.rknn`), rknn runtime on NPU |
| Classical CV | OpenCV |
| Display | DRM/KMS + panel driver (Phase 3) |

## 3. Phased plan

### Phase 0 — Bench bring-up & pipeline proof (Week 1–2)
**Goal:** definitively kill the ESP32 bottleneck.
- Boot Linux, get camera as `/dev/video0`.
- Pipeline: camera → ISP → **HW H.265** → RTSP → laptop (ffplay/VLC).
- Measure sustained fps, bitrate, **glass-to-glass latency**.
- ✅ Success = **1080p30 H.265 @ 2–5 Mbps, <150 ms** over WiFi (vs the S3's erratic VGA).

### Phase 1 — On-device tracking (Week 3–6)
**Goal:** "send results, not pixels."
- Start with **classical CV** (OpenCV): background subtraction + blob/streak detection; ArUco markers for early dev.
- Then **NPU**: convert YOLO-nano / YOLOX-nano via RKNN, run on the 1 TOPS NPU.
- **Golf-specific insight:** don't video-track the ball across the sky. Capture the **launch/impact moment** (needs high local fps — 120–240 fps on a cropped window) and **compute the trajectory from launch parameters (physics)**. Output = an arc (a few floats), ~kbps.
- ⚠️ Risk: head-worn fast-ball tracking is genuinely hard. De-risk with a fixed/tee-relative capture first; add an IMU for stabilization.

### Phase 2 — Heart rate / biometrics (Week 4–6, parallel)
- PPG AFE: **MAX86141** (2-ch, wearable-grade) or **MAX30101/30102** (cheap) over I2C/SPI.
- Mount at **temple arm** or **nose bridge** (good perfusion).
- **Motion artifacts** are the whole challenge during sport — add an **IMU (ICM-42688 / LSM6DSO)** and do accelerometer-based adaptive filtering.
- Validate against a **Polar H10 chest strap** as ground truth.
- Low bandwidth → trivial to send over BLE.

### Phase 3 — AR display (Week 6–12, the hard/expensive track — decouple it)

#### 3a. Two fundamentally different AR modes — pick one early

| Mode | How it works | Latency (real world) | For us |
|---|---|---|---|
| **Optical see-through** | Real world passes through optics directly; display adds a floating overlay | Zero (you see the real world directly) | ✅ Target — Google Glass / Rokid style |
| **Video passthrough** | Camera → RV1106 composites frame + graphics → display | 80–200 ms added | ❌ Too bulky, latency too high for glasses |

**We want optical see-through.** The user sees the real world unmodified; the RV1106 only needs to render simple 2D graphics (arc, numbers) onto a small display that a prism or waveguide injects into the field of view. This is far simpler than compositing full camera video.

#### 3b. Key insight — sports overlay does not require camera passthrough

Common misconception: "we need to video-track the ball across the sky and draw a line on top of the video."

What we actually do:
```
Impact moment detected by NPU
  → launch params (speed, angle, spin) captured
  → trajectory.py computes full arc from physics (~ms)
  → display shows predicted arc as a few line segments
```
The ball tracer is a **pre-computed overlay on top of the real world**, not a real-time annotation on camera video. The RV1106 only pushes a handful of coordinates to the display, not frames. This makes everything simpler and removes the latency problem.

#### 3c. RV1106 display interface and what it can drive

RV1106's native output is **RGB-LCD parallel**, not MIPI-DSI. Options in order of difficulty:

| Sub-phase | Display module | Interface | Resolution | Optics | Cost | Status |
|---|---|---|---|---|---|---|
| **3-I** (do first) | SPI TFT / OLED (ST7789, SSD1351) | SPI | 240×240 ~ 320×240 | 45° half-mirror prism | ¥50–150 | Feasible now |
| **3-II** | Round AMOLED (RM67162 454×454) | SPI / QSPI | 454×454 | Birdbath prism | ¥200–400 | Medium effort |
| **3-III** | MIPI-DSI Micro-OLED (Sony ECX, Himax) | RGB→MIPI bridge IC (SSD2828 / TC358764) | 1280×720+ | Waveguide | ¥3000+ | Phase 4 territory |

The 3-I sub-phase is the **minimum viable AR overlay** and is achievable as soon as Phase 2 is stable. The bridge-IC route (3-III) requires additional PCB design but is electrically solvable — it is not a fundamental blocker.

Two sub-tracks, run in parallel:
- **Prototype path (cheap, fast):** use off-the-shelf **birdbath AR glasses (Xreal One / Rokid Max / Viture)** as a 1080p external display over USB-C DisplayPort. Render the overlay on a host (laptop/phone) that receives tracking data from the RV1106 over BLE. Validates overlay UX now with zero optics engineering.
- **Integration path (real product):** source an AR display module — birdbath (Micro-OLED) or waveguide + microLED — from a module vendor. Sub-phase 3-I → 3-II → 3-III progression above.

⚠️ **Outdoor/sunlight brightness** (golf is outdoors) demands high-nit microLED or birdbath — a real constraint. This is where cost jumps from a ~¥200 hack to ¥3k–20k+ modules. **Biggest program risk/cost.**

### Phase 4 — Integration & form factor (Month 4+)
- Move to **Core1106 SoM** on a custom rigid-flex PCB sized for a temple arm.
- Power: small LiPo (~150–300 mAh per temple), PMIC, USB-C charging.
- Thermal: ~0.3–1 W continuous → heat-spread, duty-cycle, accept limited runtime.
- This is **custom hardware** — the end of "off-the-shelf."

## 4. Prototype BOM (rough)

| Item | Part | ~Cost |
|---|---|---|
| SoC board | Luckfox Pico Ultra W | $30–45 |
| Camera | 5 MP MIPI (SC530AI) / global-shutter option | $10–25 |
| HR sensor | MAX86141 / MAX30101 module | $10–30 |
| IMU | ICM-42688 | $5–15 |
| AR display (proto) | Xreal/Rokid as external display | $200–400 |
| AR display (integration) | waveguide/birdbath module | $300–3000+ |
| Battery / PMIC / misc | — | $20–50 |

**Prototype ex-display ≈ $80–150.** With display path: **$300–3000+** (dominated by optics).

## 5. Honest feasibility verdict

- **Off-the-shelf today:** camera → ISP → HW H.265 → stream, on-device NPU tracking, PPG HR, WiFi/BLE — all genuinely buildable on the Luckfox in **weeks**.
- **Needs real engineering:** AR optics (sourcing + driving + outdoor brightness + eyebox/alignment), the glasses-form-factor PCB, thermal/battery, and robust head-worn ball tracking.
- **RV1106 fit:** strong *prototype + possibly early-product* brain, but single A7 + RGB-oriented display output + vendor BSP = great for the pipeline, weak for rich AR compositing. If the AR display becomes central, graduate to **RK3566/RK3588-class** or **Snapdragon AR**.

## 6. Critical risks (ranked)

1. **AR display** sourcing / cost / outdoor brightness (biggest).
2. Head-worn **fast-ball tracking** accuracy.
3. RV1106 **CPU saturation** doing CV + encode + stream + display at once.
4. **Sunlight readability** for outdoor sports.
5. Vendor **BSP / documentation** maturity.
6. **Thermal / battery** in a temple-arm form factor.

## 7. Immediate next action

Buy the **Luckfox Pico Ultra W + camera** (~$50) and execute **Phase 0**. The single number that validates the entire architecture: **sustained 1080p30 H.265 bitrate and glass-to-glass latency over WiFi.** Get that, and the "transfer-bound" problem is solved before you spend a cent on optics.
