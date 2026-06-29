"""
Golf ball launch -> trajectory physics model.

First-order flight model: gravity + quadratic aerodynamic drag + Magnus lift
from backspin. The constants are physically reasonable but APPROXIMATE — they
should be calibrated against real measured shots (that calibration is part of
the prototype work).

Why this matters: this is the core of the "send results, not pixels" feature.
From a few launch parameters measured at impact, the glasses compute the whole
arc locally and transmit only the trajectory (~bytes), instead of streaming
video of the ball flight.

Usage:
    python physics/trajectory.py --speed 70 --launch 12 --spin 2800
    python physics/trajectory.py --speed 55 --launch 14 --spin 3200 --save out/shot.png
"""

from __future__ import annotations
import argparse
import math
import os
import numpy as np

# --- Physical constants (golf ball, sea level) --------------------------------
G = 9.81                       # gravity (m/s^2)
RHO = 1.225                    # air density (kg/m^3)
MASS = 0.04593                 # ball mass (kg), USGA max
DIAMETER = 0.04267             # ball diameter (m), USGA min
RADIUS = DIAMETER / 2.0
AREA = math.pi * RADIUS ** 2   # cross-sectional area (m^2)

# Aerodynamic coefficients — APPROXIMATE; tune against measured shots.
CD = 0.25                      # drag coefficient (typical 0.21–0.27)
CL_SLOPE = 1.5                 # lift coeff per unit spin factor S = r*omega/v
CL_MAX = 0.30                  # cap on lift coefficient


def _spin_vector(spin_rpm: float, azimuth_rad: float) -> np.ndarray:
    """Backspin vector (rad/s): horizontal axis perpendicular to the launch
    direction, oriented so the Magnus force lifts the ball."""
    omega = spin_rpm * 2.0 * math.pi / 60.0
    fwd = np.array([math.cos(azimuth_rad), math.sin(azimuth_rad), 0.0])
    up = np.array([0.0, 0.0, 1.0])
    # Backspin axis = fwd x up, so that Magnus force (omega x v) points UP (lift).
    axis = np.cross(fwd, up)                 # horizontal, perpendicular to forward
    n = np.linalg.norm(axis)
    axis = axis / n if n > 1e-9 else np.array([0.0, -1.0, 0.0])
    return omega * axis


def _accel(vel: np.ndarray, omega: np.ndarray) -> np.ndarray:
    """Acceleration from gravity + drag + Magnus lift (z is up)."""
    speed = float(np.linalg.norm(vel))
    a = np.array([0.0, 0.0, -G])
    if speed < 1e-6:
        return a
    fd = -0.5 * RHO * AREA * CD * speed * vel          # drag opposes velocity
    cross = np.cross(omega, vel)                       # Magnus direction ~ omega x v
    cmag = float(np.linalg.norm(cross))
    if cmag > 1e-9:
        S = RADIUS * float(np.linalg.norm(omega)) / speed     # spin factor
        cl = min(CL_MAX, CL_SLOPE * S)
        fl = 0.5 * RHO * AREA * cl * speed * speed * (cross / cmag)
    else:
        fl = np.zeros(3)
    return a + (fd + fl) / MASS


def simulate(speed, launch_deg, spin_rpm=2800.0, azimuth_deg=0.0,
             tee_height=0.0, dt=0.001, max_t=15.0):
    """RK4 integration until the ball lands (z < 0). Returns trajectory + stats."""
    launch = math.radians(launch_deg)
    azim = math.radians(azimuth_deg)
    omega = _spin_vector(spin_rpm, azim)

    vh = speed * math.cos(launch)
    vel = np.array([vh * math.cos(azim), vh * math.sin(azim), speed * math.sin(launch)])
    pos = np.array([0.0, 0.0, tee_height])

    pts = [pos.copy()]
    t = 0.0
    while pos[2] >= 0.0 and t < max_t:
        k1v = _accel(vel, omega);                k1x = vel
        k2v = _accel(vel + 0.5*dt*k1v, omega);   k2x = vel + 0.5*dt*k1v
        k3v = _accel(vel + 0.5*dt*k2v, omega);   k3x = vel + 0.5*dt*k2v
        k4v = _accel(vel + dt*k3v, omega);       k4x = vel + dt*k3v
        vel = vel + (dt/6.0)*(k1v + 2*k2v + 2*k3v + k4v)
        pos = pos + (dt/6.0)*(k1x + 2*k2x + 2*k3x + k4x)
        t += dt
        pts.append(pos.copy())

    pts = np.array(pts)
    carry = float(math.hypot(pts[-1, 0], pts[-1, 1]))
    apex = float(pts[:, 2].max())
    return {"points": pts, "carry_m": carry, "apex_m": apex, "flight_s": t}


def main():
    ap = argparse.ArgumentParser(description="Golf launch -> trajectory model")
    ap.add_argument("--speed", type=float, default=70.0, help="ball speed at launch (m/s)")
    ap.add_argument("--launch", type=float, default=12.0, help="launch angle (deg)")
    ap.add_argument("--spin", type=float, default=2800.0, help="backspin (rpm)")
    ap.add_argument("--azimuth", type=float, default=0.0, help="left/right angle (deg)")
    ap.add_argument("--tee", type=float, default=0.0, help="tee height (m)")
    ap.add_argument("--save", type=str, default="", help="save plot to this PNG path")
    args = ap.parse_args()

    r = simulate(args.speed, args.launch, args.spin, args.azimuth, args.tee)
    print(f"ball speed   : {args.speed:.1f} m/s ({args.speed*2.237:.0f} mph)")
    print(f"launch angle : {args.launch:.1f} deg")
    print(f"backspin     : {args.spin:.0f} rpm")
    print("--- result ---")
    print(f"carry        : {r['carry_m']:.1f} m ({r['carry_m']*1.094:.0f} yd)")
    print(f"apex height  : {r['apex_m']:.1f} m")
    print(f"flight time  : {r['flight_s']:.2f} s")

    if args.save:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        pts = r["points"]
        downrange = np.hypot(pts[:, 0], pts[:, 1])
        plt.figure(figsize=(8, 3))
        plt.plot(downrange, pts[:, 2])
        plt.xlabel("downrange (m)"); plt.ylabel("height (m)")
        plt.title(f"carry {r['carry_m']:.0f} m, apex {r['apex_m']:.0f} m, {r['flight_s']:.1f} s")
        plt.grid(True, alpha=0.3); plt.tight_layout()
        os.makedirs(os.path.dirname(args.save) or ".", exist_ok=True)
        plt.savefig(args.save, dpi=120)
        print(f"saved plot   : {args.save}")


if __name__ == "__main__":
    main()
