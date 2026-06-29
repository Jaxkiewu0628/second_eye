"""
AR Glasses PCB Design Brief — RV1106 Platform
Generates a PDF with block diagrams and layout illustrations.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak)
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle, Polygon, Group
from reportlab.graphics import renderPDF

W, H = A4
DARK   = colors.HexColor('#1a1a2e')
BLUE   = colors.HexColor('#0f3460')
ACCENT = colors.HexColor('#e94560')
GRAY   = colors.HexColor('#555577')
LIGHT  = colors.HexColor('#eef0f5')
GREEN  = colors.HexColor('#27ae60')
ORANGE = colors.HexColor('#e67e22')
PURPLE = colors.HexColor('#8e44ad')
TEAL   = colors.HexColor('#16a085')

# ── helper: draw a labelled box ──────────────────────────────────────────────
def box(d, x, y, w, h, label, sublabel='', fill=BLUE, text_color=colors.white,
        font_size=7, sub_size=6):
    d.add(Rect(x, y, w, h, fillColor=fill, strokeColor=colors.white,
               strokeWidth=0.5, rx=2, ry=2))
    d.add(String(x + w/2, y + h/2 + (4 if sublabel else 0),
                 label, fontSize=font_size, fillColor=text_color,
                 textAnchor='middle', fontName='Helvetica-Bold'))
    if sublabel:
        d.add(String(x + w/2, y + h/2 - 5,
                     sublabel, fontSize=sub_size, fillColor=text_color,
                     textAnchor='middle', fontName='Helvetica'))

def arrow(d, x1, y1, x2, y2, color=GRAY, width=1):
    d.add(Line(x1, y1, x2, y2, strokeColor=color, strokeWidth=width))
    # arrowhead
    dx, dy = x2-x1, y2-y1
    length = (dx**2+dy**2)**0.5
    if length == 0: return
    ux, uy = dx/length, dy/length
    ax, ay = -uy*4, ux*4
    d.add(Polygon([x2, y2,
                   x2 - ux*6 + ax, y2 - uy*6 + ay,
                   x2 - ux*6 - ax, y2 - uy*6 - ay],
                  fillColor=color, strokeColor=color, strokeWidth=0))

def bidir(d, x1, y1, x2, y2, label='', color=GRAY):
    arrow(d, x1, y1, x2, y2, color)
    arrow(d, x2, y2, x1, y1, color)
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        d.add(String(mx+2, my+2, label, fontSize=5, fillColor=color,
                     textAnchor='start', fontName='Helvetica'))

# ═══════════════════════════════════════════════════════════════════════════════
# DRAWING 1 — System Block Diagram
# ═══════════════════════════════════════════════════════════════════════════════
def make_block_diagram():
    d = Drawing(170*mm, 120*mm)
    W2, H2 = 170*mm, 120*mm

    # background
    d.add(Rect(0, 0, W2, H2, fillColor=colors.HexColor('#0d0d1a'),
               strokeColor=None))
    d.add(String(W2/2, H2-8, 'RV1106 System Block Diagram',
                 fontSize=9, fillColor=colors.white, textAnchor='middle',
                 fontName='Helvetica-Bold'))

    # ── Central SoC ──────────────────────────────────────────────────────────
    cx, cy, cw, ch = 58*mm, 38*mm, 54*mm, 44*mm
    d.add(Rect(cx, cy, cw, ch, fillColor=colors.HexColor('#1a237e'),
               strokeColor=ACCENT, strokeWidth=1.2, rx=3, ry=3))
    d.add(String(cx+cw/2, cy+ch-10, 'RV1106 SoC', fontSize=9,
                 fillColor=colors.white, textAnchor='middle',
                 fontName='Helvetica-Bold'))

    internals = [
        ('ARM Cortex-A7', '1.2 GHz', cy+ch-24),
        ('NPU ~0.5 TOPS', 'RKNN', cy+ch-36),
        ('ISP 5MP 3A', 'rkaiq', cy+ch-48),
        ('HW H.265 Enc', 'venc540c', cy+ch-60),
        ('LPDDR4 256MB', 'on-package', cy+ch-72),
    ]
    for label, sub, yy in internals:
        if yy < cy: break
        d.add(Rect(cx+4, yy-7, cw-8, 11, fillColor=colors.HexColor('#283593'),
                   strokeColor=None, rx=1, ry=1))
        d.add(String(cx+8, yy-3, label, fontSize=5.5, fillColor=colors.white,
                     fontName='Helvetica-Bold'))
        d.add(String(cx+cw-8, yy-3, sub, fontSize=5, fillColor=colors.HexColor('#90caf9'),
                     textAnchor='end', fontName='Helvetica'))

    # ── Left side: inputs ────────────────────────────────────────────────────
    box(d, 4*mm, 82*mm, 32*mm, 14*mm, 'CSI Camera',  '12MP / SC3336', TEAL,    font_size=6.5)
    box(d, 4*mm, 62*mm, 32*mm, 14*mm, 'MIPI CSI-2',  '2-lane, 1.5Gbps', GRAY,  font_size=6.5)
    box(d, 4*mm, 42*mm, 32*mm, 14*mm, 'IMU',          'ICM-42688', PURPLE,      font_size=6.5)
    box(d, 4*mm, 22*mm, 32*mm, 14*mm, 'MIC',          'MEMS PDM', PURPLE,       font_size=6.5)

    arrow(d, 36*mm, 89*mm, cx, 76*mm, TEAL, 1.5)
    arrow(d, 36*mm, 69*mm, cx, 69*mm, GRAY, 1)
    arrow(d, 36*mm, 49*mm, cx, 55*mm, PURPLE, 1)
    arrow(d, 36*mm, 29*mm, cx, 48*mm, PURPLE, 1)

    # ── Right side: outputs ──────────────────────────────────────────────────
    rx0 = cx + cw + 12*mm
    box(d, rx0, 82*mm, 34*mm, 14*mm, 'MIPI DSI Display', '720p microLED', ACCENT, font_size=6)
    box(d, rx0, 62*mm, 34*mm, 14*mm, 'WiFi 6 + BLE 5.2', 'ATBM6012B', GREEN,     font_size=6.5)
    box(d, rx0, 42*mm, 34*mm, 14*mm, 'SPI Flash 16MB',   'NOR, 104MHz', ORANGE,   font_size=6.5)
    box(d, rx0, 22*mm, 34*mm, 14*mm, 'USB 2.0 OTG',      'Type-C', GRAY,          font_size=6.5)

    arrow(d, cx+cw, 76*mm, rx0, 89*mm, ACCENT, 1.5)
    arrow(d, cx+cw, 69*mm, rx0, 69*mm, GREEN, 1)
    arrow(d, cx+cw, 55*mm, rx0, 49*mm, ORANGE, 1)
    arrow(d, cx+cw, 48*mm, rx0, 29*mm, GRAY, 1)

    # ── Bottom: power ────────────────────────────────────────────────────────
    box(d, 58*mm, 6*mm, 54*mm, 12*mm, 'PMIC  RK816',
        '3.3V / 1.8V / 1.0V rails', DARK, font_size=6.5)
    arrow(d, 85*mm, 18*mm, 85*mm, cy, ORANGE, 1.2)

    return d


# ═══════════════════════════════════════════════════════════════════════════════
# DRAWING 2 — PCB Layout (top view, two variants)
# ═══════════════════════════════════════════════════════════════════════════════
def make_pcb_layout():
    d = Drawing(170*mm, 130*mm)
    W2, H2 = 170*mm, 130*mm
    d.add(Rect(0, 0, W2, H2, fillColor=colors.HexColor('#0d0d1a'), strokeColor=None))
    d.add(String(W2/2, H2-8, 'PCB Layout — Top View (1:1 scale approximation)',
                 fontSize=9, fillColor=colors.white, textAnchor='middle',
                 fontName='Helvetica-Bold'))

    # ── Variant A: Square 25×25mm ─────────────────────────────────────────────
    d.add(String(30*mm, H2-18, 'Variant A — Square Module  25 × 25 mm',
                 fontSize=7.5, fillColor=ACCENT, textAnchor='middle',
                 fontName='Helvetica-Bold'))
    ox, oy = 5*mm, 68*mm
    scale = 3.8  # 1mm → 3.8pt at this drawing size

    def s(v): return v * scale

    d.add(Rect(ox, oy, s(25), s(25), fillColor=colors.HexColor('#1b5e20'),
               strokeColor=colors.HexColor('#4caf50'), strokeWidth=1.2, rx=2, ry=2))

    # Grid lines (PCB copper texture hint)
    for i in range(1, 5):
        d.add(Line(ox, oy+s(i*5), ox+s(25), oy+s(i*5),
                   strokeColor=colors.HexColor('#2e7d32'), strokeWidth=0.3))
        d.add(Line(ox+s(i*5), oy, ox+s(i*5), oy+s(25),
                   strokeColor=colors.HexColor('#2e7d32'), strokeWidth=0.3))

    # Components on square board
    components_a = [
        (8.5, 8.5, 8, 8,   'RV1106',   'SoC+RAM', colors.HexColor('#1a237e')),
        (0.5, 16,  8, 8,   'WiFi',     'ATBM6012', colors.HexColor('#1b5e20').clone() if False else GREEN),
        (0.5, 0.5, 5, 5,   'PMIC',     'RK816',    ORANGE),
        (17,  0.5, 4, 4,   'Flash',    '16MB',     PURPLE),
        (17,  16,  5, 4,   'Crystal',  '24MHz',    GRAY),
        (0.5, 6,   5, 3,   'Caps',     'Decoup.',  GRAY),
    ]
    for rx, ry, rw, rh, lbl, sub, col in components_a:
        d.add(Rect(ox+s(rx), oy+s(ry), s(rw), s(rh),
                   fillColor=col, strokeColor=colors.white, strokeWidth=0.4,
                   rx=1, ry=1))
        d.add(String(ox+s(rx+rw/2), oy+s(ry+rh/2)+2,
                     lbl, fontSize=4.5, fillColor=colors.white,
                     textAnchor='middle', fontName='Helvetica-Bold'))
        d.add(String(ox+s(rx+rw/2), oy+s(ry+rh/2)-3,
                     sub, fontSize=3.5, fillColor=colors.HexColor('#cccccc'),
                     textAnchor='middle', fontName='Helvetica'))

    # FPC connectors
    d.add(Rect(ox+s(10), oy+s(23.5), s(7), s(1.5),
               fillColor=colors.HexColor('#f57f17'), strokeColor=colors.white, strokeWidth=0.3))
    d.add(String(ox+s(13.5), oy+s(24.2), 'Camera FPC', fontSize=4,
                 fillColor=colors.white, textAnchor='middle'))
    d.add(Rect(ox+s(18.5), oy+s(6), s(1.5), s(7),
               fillColor=colors.HexColor('#f57f17'), strokeColor=colors.white, strokeWidth=0.3))
    d.add(String(ox+s(21), oy+s(9.5), 'DSI', fontSize=4,
                 fillColor=colors.HexColor('#f57f17'), textAnchor='middle'))

    # Antenna keep-out
    d.add(Rect(ox+s(0.5), oy+s(20), s(8), s(4.5),
               fillColor=None, strokeColor=colors.HexColor('#ff6f00'),
               strokeWidth=0.6, strokeDashArray=[2,2]))
    d.add(String(ox+s(4.5), oy+s(22.2), 'Antenna', fontSize=3.5,
                 fillColor=colors.HexColor('#ff6f00'), textAnchor='middle'))

    # Dimension arrows
    d.add(Line(ox, oy-4, ox+s(25), oy-4, strokeColor=ACCENT, strokeWidth=0.8))
    d.add(String(ox+s(12.5), oy-7, '25 mm', fontSize=5.5, fillColor=ACCENT,
                 textAnchor='middle'))
    d.add(Line(ox-4, oy, ox-4, oy+s(25), strokeColor=ACCENT, strokeWidth=0.8))
    d.add(String(ox-10, oy+s(12.5), '25 mm', fontSize=5.5, fillColor=ACCENT,
                 textAnchor='middle'))

    # ── Variant B: Strip 55×8mm ───────────────────────────────────────────────
    d.add(String(120*mm, H2-18, 'Variant B — Temple Strip  55 × 8 mm',
                 fontSize=7.5, fillColor=GREEN, textAnchor='middle',
                 fontName='Helvetica-Bold'))

    bx, by = 88*mm, 82*mm
    scaleB = 1.5  # 1mm → 1.5pt
    def sb(v): return v * scaleB

    d.add(Rect(bx, by, sb(55), sb(8),
               fillColor=colors.HexColor('#1b5e20'),
               strokeColor=colors.HexColor('#4caf50'), strokeWidth=1, rx=1, ry=1))

    strip_parts = [
        (0.5,  0.5, 7, 7,   'RV1106', '',       colors.HexColor('#1a237e')),
        (8.5,  0.5, 7, 7,   'WiFi',   '',       GREEN.clone() if False else colors.HexColor('#00695c')),
        (16.5, 1,   4, 6,   'PMIC',   '',       ORANGE),
        (21.5, 1,   4, 6,   'Flash',  '',       PURPLE),
        (26.5, 0.5, 5, 7,   'Caps',   '',       GRAY),
        (32.5, 0.5, 5, 7,   'Caps',   '',       GRAY),
    ]
    for rx, ry, rw, rh, lbl, sub, col in strip_parts:
        d.add(Rect(bx+sb(rx), by+sb(ry), sb(rw), sb(rh),
                   fillColor=col, strokeColor=colors.white, strokeWidth=0.3, rx=0.5, ry=0.5))
        d.add(String(bx+sb(rx+rw/2), by+sb(ry+rh/2),
                     lbl, fontSize=4, fillColor=colors.white,
                     textAnchor='middle', fontName='Helvetica-Bold'))

    # FPC connectors on strip ends
    d.add(Rect(bx+sb(39), by+sb(2.5), sb(1.5), sb(5),
               fillColor=colors.HexColor('#f57f17'), strokeColor=colors.white, strokeWidth=0.3))
    d.add(Rect(bx+sb(42), by+sb(2.5), sb(1.5), sb(5),
               fillColor=colors.HexColor('#f57f17'), strokeColor=colors.white, strokeWidth=0.3))
    d.add(String(bx+sb(41.5), by+sb(-3), 'FPC', fontSize=4,
                 fillColor=colors.HexColor('#f57f17'), textAnchor='middle'))

    # Antenna at end
    d.add(Rect(bx+sb(45), by, sb(10), sb(8),
               fillColor=None, strokeColor=colors.HexColor('#ff6f00'),
               strokeWidth=0.6, strokeDashArray=[2,2]))
    d.add(String(bx+sb(50), by+sb(4), 'Ant.', fontSize=4,
                 fillColor=colors.HexColor('#ff6f00'), textAnchor='middle'))

    # Dimension arrows
    d.add(Line(bx, by-4, bx+sb(55), by-4, strokeColor=GREEN, strokeWidth=0.8))
    d.add(String(bx+sb(27.5), by-7, '55 mm', fontSize=5.5, fillColor=GREEN,
                 textAnchor='middle'))
    d.add(Line(bx-4, by, bx-4, by+sb(8), strokeColor=GREEN, strokeWidth=0.8))
    d.add(String(bx-10, by+sb(4), '8 mm', fontSize=5.5, fillColor=GREEN,
                 textAnchor='middle'))

    # ── Side profile ──────────────────────────────────────────────────────────
    d.add(String(W2/2, 54*mm, '— Side Profile (Z-axis) —',
                 fontSize=7.5, fillColor=colors.white, textAnchor='middle',
                 fontName='Helvetica-Bold'))

    px, py = 35*mm, 28*mm
    layers = [
        (40, 2.5, 'SMD top (BGA chips)',  colors.HexColor('#1a237e'), colors.white),
        (40, 8,   'PCB substrate 6L',     colors.HexColor('#1b5e20'), colors.white),
        (40, 2.5, 'SMD bottom (passives)',colors.HexColor('#4a148c'), colors.white),
    ]
    yc = py
    for lw, lh, lbl, col, tc in layers:
        lh_pt = lh * 1.5
        d.add(Rect(px, yc, lw*mm, lh_pt, fillColor=col,
                   strokeColor=colors.white, strokeWidth=0.5))
        d.add(String(px + lw*mm + 2, yc + lh_pt/2,
                     lbl, fontSize=5.5, fillColor=tc, fontName='Helvetica'))
        yc += lh_pt

    # Total height arrow
    total_z = sum(lh for _, lh, *_ in layers)
    d.add(Line(px - 5, py, px - 5, py + total_z*1.5,
               strokeColor=ACCENT, strokeWidth=0.8))
    d.add(String(px - 12, py + total_z*1.5/2,
                 '~2 mm', fontSize=5.5, fillColor=ACCENT, textAnchor='middle'))

    return d


# ═══════════════════════════════════════════════════════════════════════════════
# DRAWING 3 — Glasses Integration Sketch
# ═══════════════════════════════════════════════════════════════════════════════
def make_glasses_sketch():
    d = Drawing(170*mm, 90*mm)
    W2, H2 = 170*mm, 90*mm
    d.add(Rect(0, 0, W2, H2, fillColor=colors.HexColor('#0d0d1a'), strokeColor=None))
    d.add(String(W2/2, H2-8, 'Glasses Integration — Component Placement',
                 fontSize=9, fillColor=colors.white, textAnchor='middle',
                 fontName='Helvetica-Bold'))

    # ── Front frame ──────────────────────────────────────────────────────────
    fc = GRAY
    # Left lens
    d.add(Rect(18*mm, 38*mm, 34*mm, 22*mm, fillColor=colors.HexColor('#0a2a4a'),
               strokeColor=fc, strokeWidth=1.5, rx=4, ry=4))
    # Right lens
    d.add(Rect(58*mm, 38*mm, 34*mm, 22*mm, fillColor=colors.HexColor('#0a2a4a'),
               strokeColor=fc, strokeWidth=1.5, rx=4, ry=4))
    # Nose bridge
    d.add(Line(52*mm, 50*mm, 58*mm, 50*mm, strokeColor=fc, strokeWidth=2))
    # Frame top
    d.add(Line(18*mm, 60*mm, 92*mm, 60*mm, strokeColor=fc, strokeWidth=1.5))

    # Camera on nose bridge
    d.add(Rect(51*mm, 46*mm, 8*mm, 6*mm, fillColor=TEAL,
               strokeColor=colors.white, strokeWidth=0.6, rx=1, ry=1))
    d.add(Circle(55*mm, 49*mm, 2, fillColor=colors.HexColor('#1a1a1a'),
                 strokeColor=TEAL, strokeWidth=0.8))
    d.add(String(55*mm, 40*mm, 'Camera', fontSize=5.5, fillColor=TEAL,
                 textAnchor='middle'))
    d.add(Line(55*mm, 46*mm, 55*mm, 42*mm, strokeColor=TEAL, strokeWidth=0.6,
               strokeDashArray=[1,1]))

    # HUD overlay hints
    d.add(String(35*mm, 50*mm, 'HUD\nOverlay', fontSize=6,
                 fillColor=colors.HexColor('#00bcd4'), textAnchor='middle'))
    d.add(String(75*mm, 50*mm, 'HUD\nOverlay', fontSize=6,
                 fillColor=colors.HexColor('#00bcd4'), textAnchor='middle'))

    # ── Right temple arm (PCB) ────────────────────────────────────────────────
    d.add(Rect(92*mm, 47*mm, 55*mm, 8*mm, fillColor=colors.HexColor('#1b5e20'),
               strokeColor=GREEN, strokeWidth=1, rx=1, ry=1))

    arm_components = [
        (0.5, 0.5, 8, 7,   'RV1106', colors.HexColor('#1a237e')),
        (9,   0.5, 7, 7,   'WiFi',   colors.HexColor('#00695c')),
        (17,  1,   5, 5,   'PMIC',   ORANGE),
        (23,  1,   4, 5,   'Flash',  PURPLE),
    ]
    for rx, ry, rw, rh, lbl, col in arm_components:
        d.add(Rect(92*mm + rx*mm, 47*mm + ry*mm, rw*mm, rh*mm,
                   fillColor=col, strokeColor=colors.white, strokeWidth=0.3, rx=0.5))
        d.add(String(92*mm + (rx+rw/2)*mm, 47*mm + (ry+rh/2)*mm,
                     lbl, fontSize=3.5, fillColor=colors.white, textAnchor='middle',
                     fontName='Helvetica-Bold'))

    # Antenna zone
    d.add(Rect(133*mm, 47*mm, 14*mm, 8*mm,
               fillColor=None, strokeColor=colors.HexColor('#ff6f00'),
               strokeWidth=0.6, strokeDashArray=[2,2]))
    d.add(String(140*mm, 51*mm, 'WiFi\nAnt.', fontSize=4,
                 fillColor=colors.HexColor('#ff6f00'), textAnchor='middle'))

    d.add(String(119.5*mm, 42*mm, 'Right arm — PCB + compute  55 × 8 × 2 mm',
                 fontSize=6, fillColor=GREEN, textAnchor='middle'))

    # ── Left temple arm (battery) ─────────────────────────────────────────────
    d.add(Rect(18*mm - 55*mm, 47*mm, 55*mm, 8*mm,
               fillColor=colors.HexColor('#4a148c'),
               strokeColor=PURPLE, strokeWidth=1, rx=1, ry=1))
    d.add(String(18*mm - 55*mm/2, 51*mm, 'Battery  ~200 mAh  /  Speakers  /  Mic',
                 fontSize=5.5, fillColor=colors.white, textAnchor='middle'))
    d.add(String(18*mm - 55*mm/2, 42*mm, 'Left arm — power + audio  55 × 8 × 4 mm',
                 fontSize=6, fillColor=PURPLE, textAnchor='middle'))

    # Flex cable hint through hinge
    d.add(Line(18*mm, 51*mm, 18*mm - 0*mm, 51*mm,
               strokeColor=ORANGE, strokeWidth=1, strokeDashArray=[2,1]))
    d.add(Line(92*mm, 51*mm, 92*mm + 0*mm, 51*mm,
               strokeColor=ORANGE, strokeWidth=1, strokeDashArray=[2,1]))

    # Scale reference
    d.add(Line(20*mm, 15*mm, 70*mm, 15*mm, strokeColor=ACCENT, strokeWidth=1))
    d.add(String(45*mm, 11*mm, '50 mm', fontSize=6, fillColor=ACCENT,
                 textAnchor='middle'))
    d.add(Line(20*mm, 13*mm, 20*mm, 17*mm, strokeColor=ACCENT, strokeWidth=1))
    d.add(Line(70*mm, 13*mm, 70*mm, 17*mm, strokeColor=ACCENT, strokeWidth=1))

    return d


# ═══════════════════════════════════════════════════════════════════════════════
# BUILD PDF
# ═══════════════════════════════════════════════════════════════════════════════
def build_pdf(path):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=15*mm, rightMargin=15*mm,
                            topMargin=15*mm, bottomMargin=15*mm)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('Title', parent=styles['Title'],
                                 textColor=DARK, fontSize=18, spaceAfter=4)
    sub_style   = ParagraphStyle('Sub', parent=styles['Normal'],
                                 textColor=GRAY, fontSize=10, spaceAfter=12)
    h2_style    = ParagraphStyle('H2', parent=styles['Heading2'],
                                 textColor=BLUE, fontSize=11, spaceBefore=12, spaceAfter=4)
    body_style  = ParagraphStyle('Body', parent=styles['Normal'],
                                 textColor=DARK, fontSize=8.5, spaceAfter=4, leading=13)
    note_style  = ParagraphStyle('Note', parent=styles['Normal'],
                                 textColor=GRAY, fontSize=7.5, spaceAfter=4,
                                 leftIndent=8, leading=12)

    def cell(text, bold=False, color=DARK, bg=None, align='LEFT'):
        s = ParagraphStyle('c', parent=styles['Normal'], fontSize=7.5,
                           textColor=color, alignment=0 if align=='LEFT' else 1,
                           fontName='Helvetica-Bold' if bold else 'Helvetica',
                           leading=11)
        return Paragraph(text, s)

    story = []

    # ── Cover ─────────────────────────────────────────────────────────────────
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph('AR Sports Glasses', title_style))
    story.append(Paragraph('PCB Design Brief — RV1106 Platform', sub_style))
    story.append(Paragraph('For 3D Frame Design Reference · 2026-06-24', sub_style))
    story.append(HRFlowable(width='100%', thickness=1.5, color=BLUE, spaceAfter=8))

    story.append(Paragraph('Summary', h2_style))
    story.append(Paragraph(
        'This document provides PCB size, component placement, and integration '
        'dimensions for the RV1106-based compute module intended for AR sports '
        'glasses. Two form-factor variants are defined: a <b>square module (25×25 mm)</b> '
        'for modular testing, and a <b>temple strip (55×8 mm)</b> for final integration. '
        'The battery and audio subsystem occupy the opposite arm.',
        body_style))

    # ── Block diagram ─────────────────────────────────────────────────────────
    story.append(Paragraph('1. System Block Diagram', h2_style))
    story.append(Paragraph(
        'The RV1106 SoC integrates CPU, NPU, ISP, hardware H.265 encoder, and '
        '256 MB LPDDR4 in a single 8×8 mm package. External components are limited '
        'to WiFi/BT, PMIC, and NOR Flash.',
        body_style))
    bd = make_block_diagram()
    story.append(bd)
    story.append(Spacer(1, 4))

    # ── Component table ───────────────────────────────────────────────────────
    story.append(Paragraph('2. Bill of Materials (Minimum Viable PCB)', h2_style))

    bom = [
        [cell('Component', bold=True), cell('Part', bold=True),
         cell('Package / Size', bold=True), cell('Notes', bold=True)],
        [cell('RV1106 SoC + LPDDR4'), cell('RV1106'),
         cell('8×8 mm FCCSP'), cell('CPU+NPU+ISP+HW encoder+RAM, single chip')],
        [cell('WiFi 6 + BLE 5.2'), cell('ATBM6012B'),
         cell('8×8 mm LCC'), cell('2.4GHz; needs 15mm antenna clearance')],
        [cell('PMIC'), cell('RK816 / SY8827'),
         cell('3×3 mm QFN'), cell('3.3V, 1.8V, 1.0V rails')],
        [cell('SPI NOR Flash'), cell('W25Q128 (16MB)'),
         cell('4×4 mm SOIC-8'), cell('Boot storage')],
        [cell('Crystal — system'), cell('24 MHz TCXO'),
         cell('1.6×1.2 mm'), cell('PLL reference')],
        [cell('Crystal — RTC'), cell('32.768 kHz'),
         cell('1.6×1.2 mm'), cell('Low-power sleep')],
        [cell('Camera FPC connector'), cell('0.5mm pitch 30P'),
         cell('10×2 mm'), cell('MIPI CSI-2 to camera module')],
        [cell('Display FPC connector'), cell('0.5mm pitch 30P'),
         cell('10×2 mm'), cell('MIPI DSI to microLED panel')],
        [cell('USB-C'), cell('USB 2.0 OTG'),
         cell('8.94×6.5 mm'), cell('Dev/charge only; omit in final')],
        [cell('Battery connector'), cell('1.25mm pitch 2P'),
         cell('5×2 mm'), cell('Li-Po from left arm')],
        [cell('Decoupling caps'), cell('0402 / 0201 MLCC'),
         cell('0402: 1×0.5 mm'), cell('~80–100 pcs')],
        [cell('Inductors (power)'), cell('0402 ferrite'),
         cell('1×0.5 mm'), cell('~10 pcs for PMIC')],
    ]

    t = Table(bom, colWidths=[38*mm, 28*mm, 32*mm, 72*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BLUE),
        ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [LIGHT, colors.white]),
        ('GRID',       (0,0), (-1,-1), 0.4, colors.HexColor('#ccccdd')),
        ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING',   (0,0), (-1,-1), 4),
    ]))
    story.append(t)

    story.append(PageBreak())

    # ── PCB layout ────────────────────────────────────────────────────────────
    story.append(Paragraph('3. PCB Layout — Top View', h2_style))
    story.append(Paragraph(
        '<b>Variant A</b> (square, 25×25 mm): Recommended for prototyping — '
        'easier to rework and test. '
        '<b>Variant B</b> (strip, 55×8 mm): Target form factor for temple arm integration. '
        'Requires 6+ layer board; WiFi antenna at far end.',
        body_style))
    story.append(make_pcb_layout())
    story.append(Spacer(1, 4))

    # ── Dimension summary ─────────────────────────────────────────────────────
    story.append(Paragraph('4. Critical Dimensions', h2_style))

    dims = [
        [cell('Location', bold=True), cell('Item', bold=True),
         cell('X (mm)', bold=True), cell('Y (mm)', bold=True),
         cell('Z (mm)', bold=True), cell('Notes', bold=True)],
        [cell('Right arm'), cell('Main PCB — prototype'),
         cell('25'), cell('25'), cell('2.0'), cell('Square module, Variant A')],
        [cell('Right arm'), cell('Main PCB — production'),
         cell('55'), cell('8'), cell('2.0'), cell('Strip, Variant B; fits ≥8mm arm width')],
        [cell('Right arm'), cell('WiFi antenna clearance'),
         cell('15'), cell('5'), cell('—'), cell('No metal above; at strip far end')],
        [cell('Left arm'), cell('Li-Po battery + audio'),
         cell('50'), cell('8'), cell('4.0'), cell('~200 mAh; speaker + mic')],
        [cell('Front frame'), cell('Camera module'),
         cell('12'), cell('12'), cell('5.0'), cell('Nose bridge / center mount')],
        [cell('Front frame'), cell('Flex cable routing'),
         cell('—'), cell('—'), cell('1.0'), cell('Through hinge; 0.5mm pitch 30P')],
        [cell('Total glasses'), cell('PCB + battery + frame'),
         cell('~145'), cell('~50'), cell('~22'), cell('Target weight <50g incl. lenses')],
    ]

    dt = Table(dims, colWidths=[22*mm, 44*mm, 16*mm, 16*mm, 16*mm, 56*mm])
    dt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BLUE),
        ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [LIGHT, colors.white]),
        ('GRID',       (0,0), (-1,-1), 0.4, colors.HexColor('#ccccdd')),
        ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING',   (0,0), (-1,-1), 4),
        ('SPAN', (0,7), (-1,7)),
    ]))
    story.append(dt)

    # ── Glasses sketch ────────────────────────────────────────────────────────
    story.append(Paragraph('5. Glasses Integration Sketch', h2_style))
    story.append(Paragraph(
        'Compute PCB in right arm, battery + audio in left arm, camera centered '
        'on nose bridge. Flex cable routes through both hinges.',
        body_style))
    story.append(make_glasses_sketch())

    # ── Design notes ──────────────────────────────────────────────────────────
    story.append(Paragraph('6. Design Constraints & Notes', h2_style))
    notes = [
        '<b>Z-height limit:</b> PCB + tallest component (BGA) must stay ≤2.2 mm to fit inside a 3 mm internal arm depth.',
        '<b>WiFi antenna:</b> 15×5 mm keep-out zone at strip end — no copper pour, no metal frame above.',
        '<b>Thermal:</b> RV1106 TDP ~0.5–1 W; add thermal via array under SoC; contact with metal frame lid for passive cooling.',
        '<b>Flex hinge:</b> 0.1 mm flex PCB with 30-pin 0.5 mm pitch routed through hinge; rated 100k flex cycles.',
        '<b>Layer stack (strip):</b> 6-layer; signal / GND / power / power / GND / signal; finished thickness 0.6 mm.',
        '<b>Battery:</b> single-cell Li-Po 3.7V ~200 mAh; protection IC (DW01) on left arm PCB.',
        '<b>EMI:</b> shield can over RV1106 + PMIC recommended; do not share ground plane with antenna zone.',
        '<b>Camera mount:</b> 12×12 mm module with 4-point screw mount on nose bridge; M1.0 screws.',
    ]
    for n in notes:
        story.append(Paragraph(f'• {n}', note_style))

    # ── Phase 0 validation note ───────────────────────────────────────────────
    story.append(HRFlowable(width='100%', thickness=0.8, color=BLUE, spaceBefore=8))
    story.append(Paragraph(
        '<b>Phase 0 validation (2026-06-24):</b> Hardware H.265 encoding confirmed working on '
        'Luckfox Pico Ultra W (RV1106) with Buildroot. 1080p30 @ 4 Mbps, '
        'WiFi+RTSP end-to-end latency ~440 ms; estimated product latency (local display) ~80 ms. '
        'Architecture validated — proceeding to Phase 1 (on-device object detection / NPU).',
        note_style))

    doc.build(story)
    print(f'PDF written → {path}')

if __name__ == '__main__':
    out = '/Users/zizhengwu/Desktop/projects/2026_sports_glasses/AR_Glasses_PCB_Design_Brief_RV1106.pdf'
    build_pdf(out)
