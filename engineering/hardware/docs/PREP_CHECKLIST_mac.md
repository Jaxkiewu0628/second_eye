# Prep Checklist (macOS) — while the dev board ships

Goal: turn the shipping wait into a Phase-1 head start, so the board is pure validation.

## The Mac reality (read first)

Rockchip tooling is Windows / x86-Linux-centric. On a Mac you'll use **three environments**:

| Environment | Used for | Mac notes |
|---|---|---|
| **Native macOS** | CV algorithm + golf physics dev, video playback | easiest — do most prep here |
| **Docker (Ubuntu 22.04)** | Luckfox SDK build + RKNN-Toolkit2 | SDK toolchain is x86_64 → run `--platform linux/amd64`; RKNN has arm64 + x86_64 wheels |
| **`upgrade_tool` (macOS build)** | flashing the board to **eMMC** | SocToolKit is Windows-only, but the Ultra W has eMMC, so this works — no Windows, no SD-card flashing needed |

> Apple Silicon: the amd64 Docker container runs under Rosetta/QEMU — fine for compiling, just slower. If SDK builds feel too slow, a cheap x86 cloud Ubuntu VM is the low-friction alternative.

---

## Track A — Native macOS (the algorithm work — highest payoff)

1. **Install tools** (Homebrew):
   ```
   brew install ffmpeg python@3.11
   brew install --cask vlc
   ```
2. **Python env for vision:**
   ```
   python3 -m venv ~/venvs/glasses && source ~/venvs/glasses/bin/activate
   pip install opencv-python numpy matplotlib
   ```
3. **Collect test footage** — phone video of golf swings + ball flight (varied lighting/backgrounds). This is your dataset.
4. **Prototype ball detection** on that footage in OpenCV (background subtraction + blob/streak detection). Learn how hard moving-camera detection is *before* the NPU exists.
5. **Write the golf launch→trajectory physics model** in Python (launch speed/angle → parabola with drag). This is the core of the "send results, not pixels" feature and is pure software.

## Track B — Docker box (Rockchip toolchain)

1. **Install Docker Desktop** for Mac.
2. **Start an Ubuntu container** (amd64 for the SDK toolchain):
   ```
   docker run --platform linux/amd64 -it -v ~/glasses:/work ubuntu:22.04 bash
   apt update && apt install -y git build-essential python3 python3-pip wget
   ```
3. **Luckfox SDK + examples:**
   ```
   git clone https://github.com/LuckfoxTECH/luckfox-pico.git
   # clone the example you'll build on:
   git clone https://github.com/luckfox-eng29/luckfox_pico_rtsp_opencv.git
   ```
   Set up the cross toolchain (`arm-rockchip830-linux-uclibcgnueabihf`, per the SDK README) and **compile one example** — this flushes out toolchain issues now.
4. **RKNN-Toolkit2 (model conversion + simulator, no board needed):**
   ```
   pip install rknn-toolkit2        # or clone the repo for the version matching the SDK
   git clone https://github.com/airockchip/rknn_model_zoo.git
   ```
   Convert a **YOLO-nano** to `.rknn` targeting **`rv1106`** and run it in the **simulator** against your test footage.

## Track C — Flashing prep (stage it now, run it when the board lands)

1. Download the **macOS `upgrade_tool`** build and the **Buildroot eMMC image** for the Pico Ultra W from the Luckfox wiki.
2. Note the procedure (for arrival day): put the board in **loader/Maskrom mode** (BOOT button) → connect USB-C → `sudo ./upgrade_tool uf <buildroot-image>.img`.
3. Install a **millisecond stopwatch** app/page for the latency shot, and save the low-latency playback command:
   ```
   ffplay -fflags nobuffer -flags low_delay -framedrop rtsp://<board-ip>/live/0
   ```

---

## Day-the-board-arrives sequence (should take an afternoon)

1. Flash eMMC via `upgrade_tool` (Track C).
2. Boot, connect to WiFi/USB-net, find the board IP.
3. `ssh pico@<ip>` (password `luckfox`).
4. Open `rtsp://<board-ip>/live/0` with the `ffplay` command above.
5. **Record: resolution/fps, bitrate, glass-to-glass latency.** ← Phase 0 done.
6. Then deploy your already-built tracking model (Track B) — Phase 1 begins immediately.

---

## If you only do three things while waiting
1. **Track A #5** — the golf physics model (pure software, core feature).
2. **Track A #4** — ball detection on real footage (tells you if the vision is even feasible).
3. **Track B #4** — convert + simulate YOLO-nano so deployment is a copy step, not a project.
