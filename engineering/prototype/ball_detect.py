"""
Ball / moving-object detection skeleton (OpenCV).

Starting point for Phase-1 vision. Runs entirely on your Mac against recorded
footage — no dev board needed. Pipeline: background subtraction -> morphology
-> contour filtering by area + circularity -> track the largest moving blob.

IMPORTANT: this naive pipeline assumes a roughly STATIC camera. The hard part of
the real product is a HEAD-WORN (moving) camera + a small, fast ball. Use this to
measure how far the simple approach gets on your footage, then decide between
(a) IMU-stabilized classical CV and (b) an NPU detector (YOLO-nano via RKNN).
That feasibility read is exactly the point of running this now.

Usage:
    python vision/ball_detect.py --video footage/shot1.mp4
    python vision/ball_detect.py --video footage/shot1.mp4 --out out/annotated.mp4
"""

from __future__ import annotations
import argparse
import os
import cv2
import numpy as np


def detect(video_path, out_path="", min_area=10.0, max_area=2000.0, min_circularity=0.6):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise SystemExit(f"could not open {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer = None
    if out_path:
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        writer = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    bg = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=25, detectShadows=False)
    kernel = np.ones((3, 3), np.uint8)
    frame_idx = 0
    hits = 0

    while True:
        ok, frame = cap.read()
        if not ok:
            break
        frame_idx += 1

        mask = bg.apply(frame)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.dilate(mask, kernel, iterations=1)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        best = None
        for c in contours:
            area = cv2.contourArea(c)
            if area < min_area or area > max_area:
                continue
            perim = cv2.arcLength(c, True)
            if perim == 0:
                continue
            circ = 4 * np.pi * area / (perim * perim)   # 1.0 == perfect circle
            if circ < min_circularity:
                continue
            (x, y), r = cv2.minEnclosingCircle(c)
            if best is None or area > best[3]:
                best = (int(x), int(y), int(r), area, circ)

        if best:
            hits += 1
            x, y, r, area, circ = best
            cv2.circle(frame, (x, y), max(r, 4), (0, 255, 0), 2)
            cv2.putText(frame, f"f{frame_idx} ({x},{y}) circ={circ:.2f}",
                        (x + 8, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        if writer:
            writer.write(frame)

    cap.release()
    if writer:
        writer.release()
    print(f"frames: {frame_idx}, candidate detections: {hits}")
    if out_path:
        print(f"annotated video -> {out_path}")
    print("Tune --min-area/--max-area/--min-circularity for your footage and ball size.")


def main():
    ap = argparse.ArgumentParser(description="Ball/moving-object detection skeleton")
    ap.add_argument("--video", required=True, help="path to a recorded clip")
    ap.add_argument("--out", default="", help="optional annotated output mp4")
    ap.add_argument("--min-area", type=float, default=10.0)
    ap.add_argument("--max-area", type=float, default=2000.0)
    ap.add_argument("--min-circularity", type=float, default=0.6)
    args = ap.parse_args()
    detect(args.video, args.out, args.min_area, args.max_area, args.min_circularity)


if __name__ == "__main__":
    main()
