# Sports AR Glasses — Prototype Plan Overview

_A hand-off summary. Goal: prove the video pipeline cheaply before spending on optics._
_Date: 2026-06-22_

---

## TL;DR

We're building AR sports glasses (heart rate + golf-tracer-style overlays). The hard part of the *electronics* is moving live video through a tiny board fast and smoothly. The ESP32-S3 we started on can't do it because it has **no hardware video compressor** and a weak shared radio. The fix is a small **Linux camera SoC (Rockchip RV1106 / "Luckfox" board, ~$50)** that compresses video in hardware and can even do the tracking on-device. **Phase 0 = buy the board, stream 1080p video over WiFi, measure latency.** If that number is good, the whole architecture is proven.

---

## The one idea that drives everything

> **Don't transmit raw pixels. Compress or analyze on the device, then send very little.**

| Strategy | What we send | Bandwidth | When |
|---|---|---|---|
| **Send results only** | ball position, trajectory, heart rate | **~10–100 kbps** | best — BLE is enough |
| **Compress on-device** | H.265 video stream | **2–5 Mbps** | when the phone needs the picture |
| ~~Send raw / MJPEG~~ | uncompressed frames | 50–1000 Mbps | ❌ what the ESP32 was forced to do |

The RV1106 can do all three. The ESP32-S3 could only do the bad one.

---

## Platform at a glance

| Parameter | Value | Plain meaning |
|---|---|---|
| Board | **Luckfox Pico Ultra W** | the dev board, ~**$30–45** |
| Chip | Rockchip **RV1106** | the same class of chip inside $20–30 security cameras |
| CPU | 1× ARM Cortex-A7 (~1 GHz) + RISC-V helper | runs real Linux |
| **NPU (AI)** | **~0.5–1 TOPS** | runs small object-detection models on-device |
| **ISP** | 3rd-gen, up to **5 MP** | turns raw sensor data into a clean image |
| **HW video encoder** | **H.264 / H.265, up to ~5 MP @ 30 fps** | the key feature — compresses video in hardware |
| RAM | 256 MB DDR3L (on-package) | |
| Storage | 8 GB eMMC | |
| Radio | onboard **2.4 GHz WiFi 6 + BLE 5.2** | enough for compressed video; no ESP32-style WiFi/BLE conflict |
| Camera in | MIPI-CSI (bundled 3 MP or 5 MP module) | |
| Display out | RGB-LCD (small panels) | ⚠️ *not* built for AR microdisplays — see risks |
| Power | ~**0.1–0.3 W** active | sips power; built for battery cameras |

---

## Form factor & dimensions — will it fit in glasses?

**Short answer: the *chip* fits; the *dev board* and *module* do not.** Getting into glasses is custom-PCB work, and the real size/weight limits are battery, optics, and heat — not the SoC.

**Size ladder:**

| What | Size | Fits in a temple arm? |
|---|---|---|
| Luckfox dev board | several cm + headers/connectors | ❌ bench only |
| Core1106 SoM (module) | **30 × 30 mm** | ❌ too big (made for compact cameras/IoT) |
| Bare RV1106 chip | **~10–15 mm** SiP (chip + RAM in one package) | ✅ only on a **custom flex PCB** |

_(A temple arm is only ~6–10 mm wide internally, even on a chunky smart-glasses arm.)_

**How real glasses do it (Meta Ray-Ban Display teardown):**
- Components **split across both arms** — one arm = battery + speaker + mic; the other = motherboard (Snapdragon AR1 + flash).
- **Flex PCB routes through the hinges** to the front frame.
- Battery = **960 mWh (~260 mAh)**; total weight = **69 g** (plain Ray-Ban Meta ~49 g; comfort target ~40–50 g).

**The real "clumsiness" drivers (not the SoC):**
1. **Battery** — ~0.5–1 W active video on a ~960 mWh budget ≈ **1–2 h** runtime.
2. **Display engine + optics** dominate the front-frame volume.
3. **Thermal** — ~0.5–1 W in a sealed arm gets warm against skin.
4. **Weight balance** vs the ~50 g comfort budget.

**The architecture decision this forces — where does compute live?**
- **Standalone** (compute + battery + display all in frame): heaviest, hottest, ~1–2 h battery.
- **Glasses + tethered puck (recommended to evaluate):** put the RV1106 + big battery in a **pocket/clip puck**; glasses hold only camera + microdisplay + sensors + a thin cable → much lighter & cooler. Good fit for outdoor sport.
- **Glasses + phone:** lightest in-frame footprint; adds wireless latency.

---

## The numbers that matter

**Bandwidth needed, by video format** (this is *why* we switch off the ESP32):

| Format | 720p @30 | 1080p @30 |
|---|---|---|
| Raw (uncompressed) | 442 Mbps | ~1 Gbps |
| MJPEG (ESP32's only option) | 12–24 Mbps | 30–50 Mbps |
| **H.264** (RV1106 hardware) | 1–4 Mbps | 4–8 Mbps |
| **H.265** (RV1106 hardware) | 1–3 Mbps | 2–5 Mbps |

→ With H.265, **1080p fits in less bandwidth than the ESP32 spent on VGA.**

**Latency target (glass-to-glass):** **< 150 ms** for streaming. A golf-tracer arc is forgiving; a head-locked overlay would need < ~20 ms (not our Phase 0 concern).

**Radio reality:** real WiFi throughput is the wall, not the chip. Compressed H.265 (2–5 Mbps) leaves large headroom; raw video never fits any wearable radio.

---

## The data path

```
Camera ──MIPI-CSI──> [ ISP: clean image ] ──> [ HW H.265 encoder ] ──> WiFi ──> phone/laptop
                                          └──> [ NPU: detect ball / track ] ──> send coords (~kbps)
```

The left side (camera→ISP→encode→WiFi) is **off-the-shelf, works in an afternoon.**
The NPU branch (on-device tracking) is **Phase 1.**

---

## Build phases & success criteria

| Phase | Goal | Done when… | Time |
|---|---|---|---|
| **0. Pipeline proof** | stream HW-compressed video over WiFi | **1080p30 H.265 @ 2–5 Mbps, <150 ms latency** measured | 1–2 wk |
| **1. On-device tracking** | detect ball / object on the board | classical CV then NPU (YOLO-nano) gives stable detections; golf = capture launch + compute arc from physics | 3–4 wk |
| **2. Heart rate** | PPG sensor at temple/nose + motion filtering | reads within tolerance vs a Polar H10 chest strap during movement | parallel |
| **3. AR display** | put the overlay in front of the eye | overlay visible & readable (start by using off-the-shelf AR glasses as a monitor) | 6–12 wk |
| **4. Form factor** | shrink onto a wearable board | RV1106 SoM on a custom PCB, battery, thermal OK | month 4+ |

---

## Bill of materials (prototype)

| Item | ~Cost |
|---|---|
| Luckfox Pico Ultra W + camera | $40–60 |
| Heart-rate (PPG) sensor + IMU | $15–40 |
| AR display — *prototype hack* (use Xreal/Rokid glasses as a monitor) | $200–400 |
| AR display — *real integrated module* (birdbath or waveguide+microLED) | $300–3000+ |
| Battery / power / misc | $20–50 |

**Electronics prototype (no display): ~$80–150.** The **display/optics dominates cost**, not the computer. (The SoC is ~$8–15 of a production BOM — choosing Linux does *not* make the product expensive.)

---

## Key risks (ranked)

1. **AR display/optics** — sourcing, cost, and outdoor sunlight brightness. Biggest unknown. *Mitigation: a simple monochrome microLED HUD (text + tracer arc) is cheap and sunlight-readable — we likely don't need full-color AR.*
2. **Head-worn ball tracking** is genuinely hard (small, fast, moving camera). *Mitigation: capture the launch moment + physics, don't video-track the whole flight.*
3. **RV1106 CPU saturation** if doing CV + encode + stream + display at once (single A7 core).
4. **Vendor SDK maturity** — Rockchip docs are thinner than Raspberry Pi.
5. **Thermal / battery** in a glasses temple.

---

## Software stack (for reference)

- **OS:** Luckfox **Buildroot** image (lean; ships with the RTSP camera demo). Ubuntu image only if we want `apt`.
- **Video encode:** Rockchip MPP (hardware H.264/H.265)
- **Streaming:** built-in `rkipc` RTSP (`rtsp://<board-ip>/live/0`), or GStreamer/WebRTC
- **On-device AI:** RKNN-Toolkit2 (convert a model → run on NPU)
- **Vision:** OpenCV

---

## First action (this week)

1. Order **Luckfox Pico Ultra W + matching MIPI camera** (~$50).
2. Flash the **Buildroot** image (SocToolKit → select RV1106 → SD card).
3. Boot, SSH in (`pico` / `luckfox`), open `rtsp://<board-ip>/live/0` in a player.
4. **Measure and write down: resolution/fps, bitrate, glass-to-glass latency.**

That latency + bitrate number decides whether the architecture works — and it costs $50 to find out.
