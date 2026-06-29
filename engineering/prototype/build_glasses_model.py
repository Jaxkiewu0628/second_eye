#!/usr/bin/env python3
"""
AR 运动眼镜简化 3D 模型生成器（块状概念模型，尺寸=真实 mm）
==========================================================
按 docs/shell_design_blade_temple.md 的尺寸搭建：
  - 包裹前框 + 单片镜
  - 左右扁平刀锋镜腿（blade temple）
  - 右刀锋内的计算岛（高亮）
输出：
  models/ar_glasses.glb   实体文件（带颜色，可发外观组/任意3D软件打开）
  models/ar_glasses.stl   实体文件（通用网格）
  models/ar_glasses.png   多视图渲染图（放幻灯片用）

坐标系：X=左右(宽)  Y=前后(深,前为负,镜腿向后+)  Z=上下(高)
（采用 Z 轴朝上，与 matplotlib 默认一致，眼镜直立显示）
单位：mm
"""
import os
import numpy as np
import trimesh
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

OUT = os.path.join(os.path.dirname(__file__), "..", "models")
os.makedirs(OUT, exist_ok=True)

# ── 部件定义：(名称, 中心xyz, 尺寸xyz, 颜色RGB) ──────────────────
DARK   = (0x44, 0x44, 0x41)   # 框架深灰
LENS   = (0x37, 0x55, 0x6e)   # 镜片蓝灰
CORAL  = (0xD8, 0x5A, 0x30)   # 计算岛高亮
GRAY   = (0x88, 0x87, 0x80)   # 电池侧
AMBER  = (0xEF, 0x9F, 0x27)   # 摄像头

# 中心(x宽, y深, z高)  尺寸(宽, 深, 高)
PARTS = [
    # ── 前框 ──
    ("brow_bar",     (   0,   0,  18), (140,  9, 10), DARK),   # 眉梁
    ("lens_shield",  (   0,   2,   0), (134,  5, 34), LENS),   # 包裹单片镜
    ("camera",       (  22,  -6,  14), ( 12,  8, 12), AMBER),  # 摄像头(前凸)
    ("nose_pad",     (   0,  -2, -16), ( 10,  6,  8), DARK),   # 鼻托

    # ── 右镜腿（计算侧）── 向后(+Y)延伸
    ("R_hinge",      (  70,   9,  14), (  8, 12, 12), DARK),
    ("R_compute",    (  71,  38,   6), (  6, 46, 26), CORAL),  # 计算刀锋(高亮,高26)
    ("R_arm",        (70.5, 105,   6), (  5, 90, 14), DARK),
    ("R_eartip",     (70.5, 150,   1), (  5, 12, 12), DARK),

    # ── 左镜腿（电池侧，外形对称）──
    ("L_hinge",      ( -70,   9,  14), (  8, 12, 12), DARK),
    ("L_battery",    ( -71,  38,   6), (  5, 46, 26), GRAY),   # 电池刀锋
    ("L_arm",        (-70.5, 105,   6), (  5, 90, 14), DARK),
    ("L_eartip",     (-70.5, 150,   1), (  5, 12, 12), DARK),
]

# ── 构建 trimesh 场景并导出实体文件 ──────────────────────────────
scene = trimesh.Scene()
for name, ctr, size, color in PARTS:
    box = trimesh.creation.box(extents=size)
    box.apply_translation(ctr)
    box.visual.face_colors = list(color) + [255]
    scene.add_geometry(box, geom_name=name)

glb_path = os.path.join(OUT, "ar_glasses.glb")
stl_path = os.path.join(OUT, "ar_glasses.stl")
scene.export(glb_path)
scene.dump(concatenate=True).export(stl_path)
print("实体文件已导出：")
print("  ", os.path.normpath(glb_path))
print("  ", os.path.normpath(stl_path))

# ── matplotlib 多视图渲染（无需 GL，稳定出图）────────────────────
def box_faces(ctr, size):
    cx, cy, cz = ctr; sx, sy, sz = (s / 2 for s in size)
    c = np.array([[cx-sx,cy-sy,cz-sz],[cx+sx,cy-sy,cz-sz],[cx+sx,cy+sy,cz-sz],[cx-sx,cy+sy,cz-sz],
                  [cx-sx,cy-sy,cz+sz],[cx+sx,cy-sy,cz+sz],[cx+sx,cy+sy,cz+sz],[cx-sx,cy+sy,cz+sz]])
    idx = [[0,1,2,3],[4,5,6,7],[0,1,5,4],[2,3,7,6],[1,2,6,5],[0,3,7,4]]
    return [c[i] for i in idx]

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Hiragino Sans GB", "STHeiti", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

views = [("等轴测", 22, -55), ("侧视(看刀锋轮廓)", 8, 0), ("俯视", 88, -90)]
fig = plt.figure(figsize=(16, 5.2))
for n, (title, elev, azim) in enumerate(views):
    ax = fig.add_subplot(1, 3, n + 1, projection="3d")
    for _, ctr, size, color in PARTS:
        polys = box_faces(ctr, size)
        fc = (color[0] / 255, color[1] / 255, color[2] / 255)
        pc = Poly3DCollection(polys, facecolor=fc, edgecolor="#222", linewidths=0.4, alpha=1.0)
        ax.add_collection3d(pc)
    ax.set_xlim(-90, 90); ax.set_ylim(-20, 160); ax.set_zlim(-90, 90)
    ax.set_box_aspect((180, 180, 180))
    ax.view_init(elev=elev, azim=azim)
    ax.set_title(title, fontsize=13)
    ax.set_xlabel("X 宽"); ax.set_ylabel("Y 前后(深)"); ax.set_zlabel("Z 高")
    try:
        ax.set_proj_type("ortho")
    except Exception:
        pass

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Hiragino Sans GB", "STHeiti", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False
fig.suptitle("AR 运动眼镜简化模型（刀锋镜腿，尺寸=真实 mm）", fontsize=15)
png_path = os.path.join(OUT, "ar_glasses.png")
plt.tight_layout()
plt.savefig(png_path, dpi=130, bbox_inches="tight")
print("  ", os.path.normpath(png_path))
