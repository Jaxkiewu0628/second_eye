# Prototype workspace (Track A — native macOS)

Self-contained workspace for the algorithm work you can do **while the dev board ships**.
Everything here is **local to this folder** — a project venv at `.venv`, packages installed
only into it. Nothing global on your Mac was modified (no `brew`, no system pip).

## What's here

```
prototype/
├── .venv/                 # local Python env (gitignored) — NOT your system Python
├── requirements.txt       # opencv-python, numpy, matplotlib
├── physics/trajectory.py  # golf launch -> trajectory model (core "send results" feature)
├── vision/ball_detect.py  # OpenCV ball-detection skeleton (run on recorded footage)
└── footage/               # put your test videos here (gitignored)
```

## Activate the environment

```bash
cd prototype
source .venv/bin/activate         # leaves your global shell/Python untouched
# ...work...
deactivate
```

(Or run without activating, e.g. `.venv/bin/python physics/trajectory.py ...`.)

## Run the golf physics model

```bash
.venv/bin/python physics/trajectory.py --speed 70 --launch 12 --spin 2800
.venv/bin/python physics/trajectory.py --speed 55 --launch 14 --spin 3200 --save out/shot.png
```

Constants in `trajectory.py` (CD, CL_SLOPE, CL_MAX) are approximate — **calibrate them
against real shot data**. That calibration is itself a prototype task.

## Run ball detection on footage

1. Drop a clip into `footage/` (phone video of a golf swing + ball flight).
2. ```bash
   .venv/bin/python vision/ball_detect.py --video footage/shot1.mp4 --out out/annotated.mp4
   ```
3. Tune `--min-area / --max-area / --min-circularity` for your ball size.

The skeleton assumes a roughly **static** camera. The real challenge is a moving
(head-worn) camera + a small fast ball — this script is to measure how far the simple
approach gets before committing to IMU-stabilized CV or an NPU detector.

## Not set up here (on purpose)

**Track B (Luckfox SDK + RKNN-Toolkit2)** needs Docker / a Linux toolchain, which would
touch tooling outside this folder. To honor "no global changes," run those inside a
container when you're ready — see `../PREP_CHECKLIST_mac.md`, Track B.
