# Video Pipeline — Three Hardware Approaches (Meeting Brief)

_For the team meeting. Covers the path we took: **ESP32-S3** (where we started) →
**ESP32-P4 + C6** (the upgrade we evaluated) → **RV1106 / Luckfox** (what we're using now).
Every technical term is explained in the **Glossary** at the bottom._

---

## The story in one paragraph

We need to move **live video** from a tiny camera through a small board and out to a
display/phone, fast and smoothly enough for an AR overlay. Our first board, the
**ESP32-S3**, can't do it — it has **no hardware video compressor**, so it sends bloated
images over a weak, shared radio. We looked at the **ESP32-P4 + C6**, which adds a real
camera input and a hardware H.264 compressor and fixes most of the problem. We then chose
the **RV1106 (Luckfox)** — a small Linux camera chip that compresses even better (H.265),
*and* can run AI on the device itself, so we can send tiny "results" (ball position, heart
rate) instead of video at all.

> **The single key idea:** the problem is *moving data*, not *computing*. The winning move
> is to **compress or analyze on the device** so we transmit very little.

---

## Approach 1 — ESP32-S3 (where we started)

A popular, cheap **microcontroller (MCU)**. Great for sensors and audio; not built for video.

**Data path:**
```
Camera (OV2640) ──DVP (parallel)──> ESP32-S3 ──MJPEG over WiFi──> host
                                          └── BLE ──> phone (commands)
```

| Spec | Value | Plain meaning |
|---|---|---|
| CPU | dual-core **Xtensa LX7 @ 240 MHz** | a small processor, ~the speed of a 2005 phone |
| Memory | 8 MB **PSRAM** | scratch space to hold a few frames |
| Camera in | **OV2640** over **DVP** | a 2-megapixel sensor on an old-style parallel wire bus |
| Video codec | **none** → **MJPEG** only | can't do modern compression; sends each frame as a full JPEG |
| Radio | **2.4 GHz WiFi (b/g/n)** + **BLE**, one shared antenna | WiFi and Bluetooth fight over the same radio |

**Why it's slow — three ceilings at once:**
1. **No hardware codec.** It can only do **MJPEG**, which sends every frame whole with *no
   inter-frame compression* → huge bitrate.
2. **Weak, erratic WiFi.** Real-world throughput is ~**1.6–10 Mbps**, sometimes dropping to
   0.2 Mbps. Below VGA it manages 25–30 fps; at higher resolutions it collapses to a few fps.
3. **WiFi + BLE coexistence tax.** One radio is time-shared between WiFi and Bluetooth,
   cutting WiFi throughput by **30–50%**. A fast BLE command channel can nearly starve WiFi.

**Bandwidth & video capability:**

| Metric | Number | Notes |
|---|---|---|
| Real WiFi bandwidth | **1.6–10 Mbps** (erratic) | Can drop to 0.2 Mbps; halved when BLE is active |
| Max resolution | **VGA (640 × 480)** | Highest that still moves at usable fps |
| Max fps at VGA | **25–30 fps** | Falls apart above VGA |
| 720p / 1080p? | **Not feasible** | Would need ~15–50 Mbps MJPEG; radio can't deliver it |
| Codec overhead | MJPEG ≈ **10–15× larger** than H.264 at same quality | No hardware compressor → huge bitrate |

**Verdict:** Excellent for stills, audio, and light telemetry. **Not viable for live HD video.**

---

## Approach 2 — ESP32-P4 + ESP32-C6 (the upgrade we evaluated)

A **two-chip** system: the **P4** does the heavy work (camera, video, compute), the **C6**
is a dedicated **radio modem** bolted on (the P4 has no built-in wireless).

**Data path:**
```
Camera ──MIPI-CSI──> [P4: ISP → H.264 encoder] ──SDIO──> [C6: WiFi 6 radio] ──> host
                                └──MIPI-DSI──> display
```

| Spec | Value | Plain meaning |
|---|---|---|
| P4 CPU | dual-core **RISC-V up to 400 MHz** | a much faster modern processor |
| Camera in | **MIPI-CSI (2-lane) + ISP** | proper high-speed camera bus + image cleanup |
| Video codec | **hardware H.264, 1080p @ 30 fps** | the key upgrade — compresses video in silicon |
| Display out | **MIPI-DSI (2-lane)** | can drive a screen directly |
| AI | **vector extensions, no NPU** | can do some math fast, but no dedicated AI engine |
| C6 radio | **WiFi 6 (2.4 GHz) + BLE 5**, single 160 MHz core | a separate chip just for wireless |
| P4↔C6 link | **SDIO**, via **ESP-Hosted** | the wire and software between compute and radio |

**The number that matters:** real measured WiFi throughput over the P4↔C6 link is
**~36 Mbps** (headline rate is 143 Mbps; ~25% is achievable). The bottleneck is the C6's
single small CPU core, not the wire.

**Does it work?** Yes. Hardware **H.264 at 1080p30 needs only 4–8 Mbps**, which fits in
36 Mbps with ~5× headroom. And because the radio is a *separate chip*, there's **no
coexistence tax**. It fixes all three ESP32-S3 problems.

**Bandwidth & video capability:**

| Metric | Number | Notes |
|---|---|---|
| Real WiFi bandwidth | **~36 Mbps** | P4↔C6 SDIO bottleneck; headline rate is 143 Mbps |
| Max resolution | **1080p (1920 × 1080)** | Hardware H.264 encoder hard limit |
| Max fps at 1080p | **30 fps** | H.264 encoder ceiling |
| Stream bitrate at 1080p30 | **4–8 Mbps** | Well inside the 36 Mbps radio budget |
| Headroom | **~5×** | 36 Mbps available vs 8 Mbps used; ample margin |

**Limits:** **H.264 only** (no H.265), **no NPU** (weak on-device AI), **encode-only** (can't
hardware-decode), and ~**1 W** power. Dev kit: **ESP32-P4-Function-EV-Board ≈ $55**.

**Verdict:** A strong prototype / tethered-compute brain. But no AI engine + ~1 W heat mean
it's **not the final in-glasses chip.**

---

## Approach 3 — RV1106 / Luckfox (what we're using now)

A small **Linux camera chip** — the same class of part inside $20–30 security cameras. It
compresses better than the P4 *and* runs AI on-device.

**Data path (two modes):**
```
Camera ──MIPI-CSI──> [ISP → H.265 encoder] ──WiFi──> phone        (compress: 2–5 Mbps)
                          └──> [NPU: detect ball] ──BLE──> phone   (results only: ~kbps)
```

| Spec | Value | Plain meaning |
|---|---|---|
| CPU | **ARM Cortex-A7 (~1 GHz)** + RISC-V helper | runs **full Linux**, like a tiny computer |
| AI | **~0.5–1 TOPS NPU** | a real AI engine — can detect/track objects on the device |
| Camera in | **MIPI-CSI + ISP (up to 5 MP)** | high-speed camera bus + image cleanup |
| Video codec | **hardware H.264 *and* H.265**, up to 5 MP @ 30 fps | best compression of the three |
| Display out | **RGB-LCD** | drives small screens (⚠️ not built for AR microdisplays) |
| Memory/storage | **256 MB DDR3L** + **8 GB eMMC** | enough RAM and onboard storage for Linux |
| Radio | onboard **2.4 GHz WiFi 6 + BLE 5.2** | wireless built in; **no coexistence problem** |
| Power | ~**0.1–0.3 W** | sips power — designed for battery cameras |

**Why it wins for us:**
- **H.265** compresses ~30–50% smaller than H.264 → even lower bitrate.
- **NPU** lets us run **on-device tracking** → send *results, not pixels* (~kbps), which makes
  the data problem nearly disappear.
- It's **Linux**, so standard tools work (camera, streaming, AI, any WiFi card "just works").
- Tiny and low-power, sold as a **30 × 30 mm SoM** or a bare **~10–15 mm chip**.

**Bandwidth & video capability:**

| Metric | Number | Notes |
|---|---|---|
| Max resolution | **5 MP (2592 × 1944)** | H.264 or H.265, hardware encoder limit |
| Max fps at 5 MP | **30 fps** | Hardware encoder ceiling |
| Max fps at 1080p | **30 fps** | Smooth video; the typical operating mode |
| Stream bitrate at 1080p30 (H.265) | **2–5 Mbps** | ~40% less than H.264 for same quality |
| Stream bitrate at 1080p30 (H.264) | **4–8 Mbps** | Same as P4, but H.265 is the better default |
| "Results only" mode | **~10–100 kbps** | NPU sends ball position / HR numbers, not pixels |
| WiFi bandwidth available | **tens of Mbps** (ample) | Built-in WiFi 6; no shared-radio problem |

**Limits:** single CPU core (can saturate if doing everything at once), display output is
for small LCDs (not AR optics), and the vendor's software/docs are less polished than a
Raspberry Pi. Dev board: **Luckfox Pico Ultra W ≈ $30–45**.

**Verdict:** Best fit for both **prototype and early product** — best compression, on-device
AI, low power, Linux flexibility.

---

## Head-to-head

| | ESP32-S3 | ESP32-P4 + C6 | **RV1106 (current)** |
|---|---|---|---|
| Class | MCU | MCU + radio | **Linux camera SoC** |
| Camera bus | DVP (old) | MIPI-CSI | **MIPI-CSI** |
| Hardware codec | ❌ MJPEG only | H.264 | **H.264 + H.265** |
| **Real WiFi bandwidth** | **1.6–10 Mbps (erratic)** | **~36 Mbps** | **tens of Mbps (ample)** |
| **Max video quality** | **VGA (640×480)** | **1080p (1920×1080)** | **5 MP (2592×1944)** |
| **Max fps** | **25–30 fps @ VGA** | **30 fps @ 1080p** | **30 fps @ 5 MP** |
| **Stream bitrate @ 1080p30** | ❌ not feasible | **4–8 Mbps (H.264)** | **2–5 Mbps (H.265)** |
| **"Results only" bitrate** | ❌ no NPU | ❌ no NPU | **~10–100 kbps** |
| On-device AI (NPU) | ❌ | ❌ | **✅ ~0.5–1 TOPS** |
| WiFi/BLE conflict | ❌ shares one radio | ✅ separate radio | ✅ fine |
| Power (active) | low | ~1 W | **~0.1–0.3 W** |
| Runs Linux | ❌ | ❌ | **✅** |
| Dev board cost | ~$10 | ~$55 | ~$30–45 |
| Our verdict | rejected | good prototype brain | **chosen** |

---

## What to tell the room (30 seconds)

"Our first board, the ESP32-S3, can't stream live video because it has no hardware video
compressor and a weak shared radio. The ESP32-P4 fixes that with a real camera input and a
hardware H.264 compressor. We chose the RV1106 instead because it compresses even better
(H.265), runs AI on the device so we can send tiny results instead of video, sips power, and
runs Linux. Next step is a $50 board to measure real video latency and confirm it."

---

## Glossary — every technical term

**Compute & chips**
- **SoC (System-on-Chip):** a whole computer's main parts (CPU, memory controller, I/O) on one chip.
- **MCU (Microcontroller):** a tiny, low-power computer-on-a-chip for simple control tasks (the ESP32s are MCUs).
- **Application processor / Linux SoC:** a more powerful chip that can run a full operating system like Linux (the RV1106).
- **CPU core / dual-core:** the part that runs instructions; "dual-core" = two of them.
- **RISC-V:** a modern, open processor design (used by the P4 and parts of the RV1106).
- **Xtensa LX7:** the older processor design inside the ESP32-S3.
- **ARM Cortex-A7:** the processor design inside the RV1106 — powerful enough for Linux.
- **Clock speed (MHz / GHz):** how many cycles per second the CPU runs; higher = faster. 1 GHz = 1000 MHz.
- **NPU (Neural Processing Unit):** a dedicated AI engine that runs neural networks (object detection) efficiently.
- **TOPS (Tera-Operations Per Second):** a measure of AI compute. ~0.5–1 TOPS can run small detection models in real time.
- **ISP (Image Signal Processor):** hardware that turns raw sensor data into a clean image (exposure, color, noise).
- **PPA (Pixel Processing Accelerator):** hardware that scales/rotates/blends images cheaply (useful for overlays).

**Memory & storage**
- **SRAM:** fast on-chip memory, small.
- **PSRAM:** add-on RAM, larger but slower than SRAM (used to hold video frames).
- **DDR3L:** a type of low-voltage RAM (the RV1106's main memory).
- **eMMC:** flash storage soldered on the board (like a built-in SD card) — holds the OS.
- **Flash:** non-volatile storage that keeps data without power.

**Camera & video**
- **Image sensor (OV2640, SC3336):** the chip that captures light into pixels.
- **Resolution:** image size in pixels. QVGA ≈ 320×240, VGA ≈ 640×480, 720p = 1280×720, 1080p = 1920×1080. "MP" = megapixels.
- **fps (frames per second):** how many images per second; 30 fps looks smooth.
- **Rolling vs global shutter:** rolling reads the image line-by-line (fast objects smear); global captures all at once (better for a fast ball).
- **Codec:** **co**der/**dec**oder — software/hardware that compresses (encode) and decompresses (decode) video.
- **H.264:** a widely used modern video compression standard (efficient).
- **H.265 (HEVC):** the newer standard — ~30–50% smaller files than H.264 for the same quality.
- **MJPEG (Motion JPEG):** "compression" that just sends each frame as a separate JPEG — simple but very wasteful.
- **Inter-frame vs intra-frame:** inter-frame (H.264/H.265) only sends what *changed* between frames (efficient); intra-frame/MJPEG sends every frame whole (wasteful).
- **YUV420 / YUV422:** ways of storing image color data; YUV420 uses less data.
- **Bitrate (Mbps / kbps):** data per second. **Mbps** = megabits/s, **kbps** = kilobits/s (1 Mbps = 1000 kbps). Lower bitrate = less to transmit.
- **Raw video:** uncompressed frames — enormous (1080p30 ≈ 1 Gbps), never sent wirelessly.

**Buses & interfaces (the "wires" between chips)**
- **MIPI-CSI:** the modern high-speed camera input bus (Camera Serial Interface).
- **MIPI-DSI:** the matching high-speed display output bus (Display Serial Interface).
- **DVP:** an old, slow parallel camera bus (what the ESP32-S3 uses).
- **Lane:** one differential wire pair in a MIPI link; more lanes = more bandwidth.
- **RGB-LCD interface:** a simple bus for driving small LCD screens.
- **SDIO:** a fast bus (same family as SD cards) — used to connect the P4 to its C6 radio.
- **SPI:** a simpler, slower chip-to-chip bus.
- **USB 2.0 OTG / HS:** USB that can act as host or device; "HS" = High Speed (~480 Mbps).
- **Ethernet:** wired networking.

**Wireless**
- **WiFi (802.11 b/g/n/ac/ax):** the wireless-LAN standards; later letters = faster/newer. **WiFi 6 = 802.11ax**.
- **2.4 GHz / 5 GHz:** the two WiFi radio bands; 2.4 GHz is more crowded, 5 GHz is cleaner/faster but shorter range.
- **BLE (Bluetooth Low Energy):** low-power Bluetooth for small data (commands, sensor readings); ~1–2 Mbps.
- **802.15.4:** a low-power radio standard for mesh protocols (Thread/Zigbee).
- **Coexistence:** when WiFi and Bluetooth share one radio and have to take turns — hurts WiFi speed.
- **Throughput:** the *actual* useful data rate achieved (always lower than the headline "PHY" rate).
- **PHY:** the physical-layer raw radio rate (the optimistic headline number).
- **ESP-Hosted:** Espressif's software that lets a main chip (P4) use a separate chip (C6) as its WiFi/Bluetooth modem.

**Latency**
- **Latency:** delay between something happening and you seeing it.
- **Glass-to-glass latency:** total delay from the camera lens to the display — what the user actually feels.
- **Motion-to-photon:** delay from your head/eye moving to the screen updating; must be very small (<~20 ms) for head-locked AR.

**Software (RV1106 / Linux side)**
- **Linux:** the operating system the RV1106 runs (the ESP32s have no real OS).
- **Buildroot / Ubuntu:** two Linux "images"; Buildroot is small and lean, Ubuntu is bigger with more convenience.
- **BSP (Board Support Package):** the vendor's kernel + drivers for a specific chip.
- **RTSP:** a standard protocol for streaming live video over a network.
- **GStreamer:** a toolkit for building video pipelines.
- **RKMPP:** Rockchip's library to use the chip's hardware video encoder.
- **RKNN / RKNN-Toolkit2:** Rockchip's tools to convert and run AI models on the NPU.
- **OpenCV:** a popular computer-vision software library.
- **V4L2:** the standard Linux way to talk to cameras.

**Form factor**
- **SoM (System-on-Module):** a small ready-made board with the chip + memory, meant to be soldered onto your own board (Core1106 = 30×30 mm).
- **Flex / rigid-flex PCB:** a bendable circuit board — needed to route electronics through thin glasses arms and hinges.
- **Castellated pins:** the half-holes along a module's edge that let it be soldered down like a stamp.
- **Maskrom mode:** a special boot mode used to flash firmware onto the chip.
