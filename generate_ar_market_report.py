"""
生成《市售AR眼镜显示方案技术报告》PDF
运行: prototype/.venv/bin/python generate_ar_market_report.py
输出: AR眼镜市场技术报告_2026-06-23.pdf
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── 字体 ──────────────────────────────────────────────────────────────────────
pdfmetrics.registerFont(TTFont("AU", "/Library/Fonts/Arial Unicode.ttf"))

# ── 颜色 ─────────────────────────────────────────────────────────────────────
C_DARK   = colors.HexColor("#1A2E44")
C_MID    = colors.HexColor("#2E6DA4")
C_TEAL   = colors.HexColor("#0D7377")
C_GREEN  = colors.HexColor("#1A6B3C")
C_AMBER  = colors.HexColor("#8B5E00")
C_RED    = colors.HexColor("#8B1A1A")
C_LGRAY  = colors.HexColor("#F5F5F5")
C_MGRAY  = colors.HexColor("#DDDDDD")
C_BGBLUE = colors.HexColor("#EAF2FB")
C_BGGRN  = colors.HexColor("#EBF7EE")
C_BGYEL  = colors.HexColor("#FFFBEA")
C_BGRED  = colors.HexColor("#FFF0F0")
WHITE    = colors.white
BLACK    = colors.black

W, H  = A4
MARGIN = 14 * mm
COL   = W - 2 * MARGIN

# ── 样式工厂 ──────────────────────────────────────────────────────────────────
def sty(name, size=10, lead=15, color=BLACK, bold=False, align=0,
        sb=0, sa=4, li=0):
    return ParagraphStyle(name, fontName="AU", fontSize=size,
                          leading=lead, textColor=color,
                          spaceBefore=sb, spaceAfter=sa,
                          leftIndent=li, alignment=align)

S_H1    = sty("h1",  14, 20, C_DARK,  sb=14, sa=4)
S_H2    = sty("h2",  12, 17, C_MID,   sb=10, sa=4)
S_H3    = sty("h3",  11, 16, C_TEAL,  sb=8,  sa=3)
S_BODY  = sty("bd",  10, 15)
S_BULL  = sty("bl",  10, 15, li=10,   sa=3)
S_NOTE  = sty("nt",   8, 12, colors.HexColor("#555"), sa=4)
S_URL   = sty("url",  8, 12, C_MID,   sa=2)
S_TH    = sty("th",   9, 13, WHITE,   align=1)
S_TD    = sty("td",   9, 13, BLACK)
S_TDC   = sty("tdc",  9, 13, BLACK,   align=1)
S_TITLE = sty("ti",  20, 28, WHITE,   align=1, sb=0, sa=4)
S_SUB   = sty("su",  11, 17, colors.HexColor("#B8D4F0"), align=1, sa=3)
S_VER   = sty("ve",   9, 13, colors.HexColor("#8AAFC6"), align=1)
S_BADGE = sty("bd2", 10, 14, colors.HexColor("#7FDFB0"), align=1)
S_SPEC_KEY = sty("sk", 9, 13, colors.HexColor("#333"))
S_SPEC_VAL = sty("sv", 9, 13, BLACK)

def P(t, s=None): return Paragraph(t, s or S_BODY)
def B(t): return Paragraph(f"• {t}", S_BULL)
def HR(): return HRFlowable(width="100%", thickness=0.7,
                             color=C_MID, spaceAfter=5, spaceBefore=2)

# ── 表格辅助 ──────────────────────────────────────────────────────────────────
BASE_TS = [
    ('FONTNAME',       (0,0), (-1,-1), 'AU'),
    ('FONTSIZE',       (0,0), (-1,-1),  9),
    ('LEADING',        (0,0), (-1,-1), 13),
    ('TOPPADDING',     (0,0), (-1,-1),  4),
    ('BOTTOMPADDING',  (0,0), (-1,-1),  4),
    ('LEFTPADDING',    (0,0), (-1,-1),  5),
    ('RIGHTPADDING',   (0,0), (-1,-1),  5),
    ('GRID',           (0,0), (-1,-1), 0.4, C_MGRAY),
    ('VALIGN',         (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND',     (0,0), (-1, 0), C_DARK),
    ('TEXTCOLOR',      (0,0), (-1, 0), WHITE),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, C_LGRAY]),
]

def tbl(data, widths, extra=None):
    rows = []
    for r, row in enumerate(data):
        cells = []
        for c in row:
            if isinstance(c, Paragraph):
                cells.append(c)
            elif r == 0:
                cells.append(P(str(c), S_TH))
            else:
                cells.append(P(str(c), S_TD))
        rows.append(cells)
    ts = TableStyle(BASE_TS[:])
    if extra:
        for cmd in (extra or []):
            if cmd: ts.add(*cmd)
    t = Table(rows, colWidths=widths, repeatRows=1)
    t.setStyle(ts)
    return t

def spec_block(items, w1=42*mm):
    """Two-column key/value table, no header."""
    rows = [[P(k, S_SPEC_KEY), P(v, S_SPEC_VAL)] for k, v in items]
    ts = TableStyle([
        ('FONTNAME',      (0,0),(-1,-1),'AU'),
        ('FONTSIZE',      (0,0),(-1,-1), 9),
        ('LEADING',       (0,0),(-1,-1),13),
        ('TOPPADDING',    (0,0),(-1,-1), 3),
        ('BOTTOMPADDING', (0,0),(-1,-1), 3),
        ('LEFTPADDING',   (0,0),(-1,-1), 5),
        ('RIGHTPADDING',  (0,0),(-1,-1), 5),
        ('GRID',          (0,0),(-1,-1), 0.3, C_MGRAY),
        ('ROWBACKGROUNDS',(0,0),(-1,-1),[WHITE, C_LGRAY]),
        ('VALIGN',        (0,0),(-1,-1),'TOP'),
        ('TEXTCOLOR',     (0,0),(0,-1),  C_TEAL),
    ])
    t = Table(rows, colWidths=[w1, COL-w1])
    t.setStyle(ts)
    return t

def colored_badge(text, bg):
    t = Table([[P(text, sty("b2", 9, 13, WHITE, align=1))]],
              colWidths=[COL])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('TOPPADDING',(0,0),(-1,-1),5),
        ('BOTTOMPADDING',(0,0),(-1,-1),5),
        ('LEFTPADDING',(0,0),(-1,-1),8),
        ('FONTNAME',(0,0),(-1,-1),'AU'),
    ]))
    return t

def hdr(section):
    t = Table([[P(f"AR眼镜市场技术报告  2026-06-23  |  {section}",
                  sty("ph", 8, 11, colors.HexColor("#888")))]],
              colWidths=[COL])
    t.setStyle(TableStyle([
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),2),
    ]))
    return t

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 封面
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def cover():
    def band(content, bg, pt=10, pb=10):
        t = Table([[content]], colWidths=[COL])
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,-1),bg),
            ('TOPPADDING',(0,0),(-1,-1),pt),
            ('BOTTOMPADDING',(0,0),(-1,-1),pb),
            ('LEFTPADDING',(0,0),(-1,-1),12),
            ('RIGHTPADDING',(0,0),(-1,-1),12),
            ('FONTNAME',(0,0),(-1,-1),'AU'),
        ]))
        return t
    out = []
    out.append(band(P("市售 AR 眼镜显示方案技术报告", S_TITLE), C_DARK, 22, 6))
    out.append(band(P("涵盖：显示引擎 / 光学方案 / SoC 主控 / 协议 / 详细参数 / 产品链接", S_SUB),
                    C_DARK, 0, 12))
    cats = Table([[P("有线挂接型", S_BADGE), P("一体式 AR", S_BADGE), P("研究原型", S_BADGE)]],
                 colWidths=[COL/3, COL/3, COL/3])
    cats.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0), colors.HexColor("#0D3A5C")),
        ('BACKGROUND',(1,0),(1,0), colors.HexColor("#0D4030")),
        ('BACKGROUND',(2,0),(2,0), colors.HexColor("#3A200D")),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('FONTNAME',(0,0),(-1,-1),'AU'),
        ('GRID',(0,0),(-1,-1),0.5,colors.HexColor("#111")),
    ]))
    out.append(cats)
    out.append(band(P("版本 1.0  |  数据截至 2026-06-23  |  含产品官网 / 评测来源链接", S_VER),
                    colors.HexColor("#0D1F30"), 8, 8))
    out.append(Spacer(1, 10))
    return out

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 主函数
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def story():
    s = []
    s += cover()

    # ── 1. 技术背景 ──────────────────────────────────────────────────────────
    s.append(hdr("技术背景"))
    s.append(P("1. AR Overlay 技术背景", S_H1)); s.append(HR())

    s.append(P("1.1 两种根本不同的 AR 模式", S_H2))
    mode_data = [
        ["模式", "原理", "用户感知", "主要产品"],
        ["光学透视\nOptical See-Through",
         "真实世界直接穿过透明镜片到达眼睛\n显示屏图像通过光学元件叠加在视野上",
         "直接看真实世界\n虚拟图像漂浮其上\n无延迟感",
         "Rokid Glasses\nRayNeo X3 Pro\nINMO AIR3\nMeta Orion"],
        ["摄像头透视\nVideo See-Through",
         "相机拍摄真实世界\n主机合成视频帧+图形\n用户看合成后的屏幕",
         "看屏幕，不看真实世界\n有 80-200ms 延迟\n需要遮挡眼睛",
         "Meta Quest 3\nApple Vision Pro\n（非眼镜形态）"],
    ]
    s.append(tbl(mode_data, [30*mm, 62*mm, 44*mm, 40*mm]))
    s.append(P("本报告产品均为光学透视方案（Optical See-Through）。", S_NOTE))
    s.append(Spacer(1,6))

    s.append(P("1.2 三种主流光学方案对比", S_H2))
    opt_data = [
        ["光学方案", "原理", "优点", "缺点", "典型亮度", "代表产品"],
        ["Birdbath\n(鸟浴式半透镜)",
         "显示屏 → 45° 半透\n半反镜 → 反射入眼\n同时透过真实世界",
         "光效高(~20%)\n色彩好\n成本低\nFOV 大(40-55°)",
         "机身较厚\n镜片偏暗\n不够通透",
         "500-600 nits",
         "XREAL Air 2/Ultra\nRokid Max 2"],
        ["衍射波导\nDiffractive Waveguide",
         "光通过平面镜片内的\n衍射光栅全反射\n传导至眼睛",
         "镜片超薄(1-3mm)\n透明度高(90%+)\n接近普通眼镜外观",
         "光效低(1-5%)\n色彩均匀性差\n有彩虹纹\n视场角小(20-36°)",
         "1500-6000 nits\n(需MicroLED补偿损耗)",
         "RayNeo X3 Pro\nRokid Glasses\nINMO AIR3"],
        ["碳化硅波导\nSiC Waveguide",
         "与衍射波导相似\n但基材用碳化硅\n折射率更高",
         "彩虹纹极低\nFOV 大(~70°)\n散热好",
         "极贵\n量产难\n仅Meta掌握",
         "未公布",
         "Meta Orion (原型)"],
    ]
    s.append(tbl(opt_data, [24*mm, 40*mm, 36*mm, 36*mm, 22*mm, 30*mm]))
    s.append(Spacer(1,6))

    s.append(P("1.3 显示引擎：Micro-OLED vs MicroLED", S_H2))
    eng_data = [
        ["显示引擎", "像素发光原理", "亮度上限", "对比度", "功耗", "制造难度", "户外可用性"],
        ["Micro-OLED\n(OLEDoS/硅基OLED)",
         "有机发光二极管\n直接在硅晶圆上制造",
         "500-2000 nits", "100,000:1+", "中",
         "低", "⚠️ 户外勉强"],
        ["MicroLED",
         "无机 LED 阵列\n像素尺寸 < 50 µm",
         "1500-10,000 nits", "10,000:1+", "低",
         "极高", "✅ 户外可用"],
        ["LCoS\n(液晶硅)",
         "LCD 调制反射光\n（较老方案）",
         "100-500 nits", "1000:1", "高",
         "低", "❌ 室外不足"],
    ]
    s.append(tbl(eng_data, [26*mm, 42*mm, 24*mm, 22*mm, 14*mm, 22*mm, 22*mm]))
    s.append(P(
        "关键结论：户外强光（高尔夫球场）使用要求 >1000 nits，只有 MicroLED 方案能满足。"
        "Micro-OLED + Birdbath 的 500-600 nits 在室内/阴天尚可，直射阳光下基本不可见。", S_NOTE))
    s.append(PageBreak())

    # ── 2. 参数总览表 ─────────────────────────────────────────────────────────
    s.append(hdr("参数总览"))
    s.append(P("2. 市售产品参数总览", S_H1)); s.append(HR())

    s.append(P("2.1 有线挂接型（Tethered）", S_H2))
    s.append(P("无板载主控和电池，通过 USB-C 连接手机/电脑获取视频信号和电源。光学通常用 Birdbath，亮度和色彩更好。", S_BODY))
    s.append(Spacer(1,4))
    t1 = [
        ["", "XREAL Air 2", "XREAL Air 2 Ultra", "Rokid Max 2"],
        ["显示引擎",     "Sony Micro-OLED × 2",     "Sony Micro-OLED × 2",     "Sony 0.68\" Micro-OLED × 2"],
        ["光学方案",     "Birdbath 半透镜",           "Birdbath 半透镜",           "Birdbath 半透镜"],
        ["单眼分辨率",   "1920 × 1080",              "1920 × 1080",              "1920 × 1080"],
        ["峰值亮度",     "500 nits",                  "500 nits",                  "600 nits"],
        ["刷新率",       "120Hz (2D) / 90Hz (3D)",   "120Hz (2D) / 90Hz (3D)",   "90Hz"],
        ["视场角 FOV",   "46°",                       "52°",                       "50°"],
        ["对比度",       "未公布",                    "未公布",                    "100,000:1"],
        ["色域",         "108% sRGB",                 "108% sRGB",                 "sRGB 106%"],
        ["跟踪",         "无",                        "6DoF 内向外 (2摄像头)",     "无"],
        ["主控 SoC",     "无 (纯显示设备)",           "无 (纯显示设备)",           "无 (纯显示设备)"],
        ["电池",         "无 (USB-C 供电)",           "无 (USB-C 供电)",           "无 (USB-C 供电)"],
        ["无线协议",     "无",                        "无",                        "无 (glasses 本身)"],
        ["有线接口",     "USB-C",                     "USB-C",                     "USB-C"],
        ["重量",         "72g",                       "80g",                       "75g"],
        ["音频",         "双扬声器",                  "双扬声器 + 双麦",           "扬声器 + 麦克风"],
        ["认证",         "CE, TUV 低蓝光",            "CE, TUV 低蓝光",            "CE, RoHS"],
        ["官方售价",     "~$399",                     "~$699",                     "~$449"],
    ]
    s.append(tbl(t1, [32*mm, 54*mm, 54*mm, 46*mm], extra=[
        ('BACKGROUND',(0,0),(0,-1), colors.HexColor("#1A3A5C")),
        ('TEXTCOLOR', (0,0),(0,-1), WHITE),
    ]))
    s.append(Spacer(1,4))
    s.append(P("注：Rokid Max 2 配合 Rokid Station 2 底座使用时，底座含 Snapdragon SoC + 8GB RAM + 128GB + 5000mAh + WiFi 6 + BT 5.2。", S_NOTE))
    s.append(Spacer(1,10))

    s.append(P("2.2 一体式 AR（Standalone）", S_H2))
    s.append(P("自带 SoC、电池和操作系统，无需连线使用。光学通常用衍射波导，需要 MicroLED 补偿波导损耗。", S_BODY))
    s.append(Spacer(1,4))
    t2 = [
        ["", "RayNeo X3 Pro", "Rokid Glasses", "INMO AIR3"],
        ["显示引擎",     "全彩 MicroLED × 2",         "单色绿 MicroLED × 2",       "Sony Micro-OLED × 2"],
        ["光学方案",     "双目衍射波导",               "双目衍射波导",               "全彩 RGB 1D 衍射波导"],
        ["单眼分辨率",   "640 × 480",                  "480 × 398",                  "1920 × 1080"],
        ["峰值亮度",     "6000 nits (典型 3500 nits)", "1500 nits",                  "600 nits"],
        ["刷新率",       "60Hz",                       "未公布",                     "60Hz / 120Hz"],
        ["视场角 FOV",   "30°",                        "30°",                        "36°"],
        ["清晰度 PPD",   "未公布",                     "未公布",                     "62 PPD"],
        ["色域",         "未公布",                     "单色绿 (单波长)",            "100% sRGB"],
        ["镜片透过率",   "90%",                        "未公布",                     "未公布"],
        ["主控 SoC",     "Snapdragon AR1 Gen 1",       "Snapdragon AR1 Gen 1\n+ NXP RT600 MCU", "Snapdragon 8核 (型号未公布)"],
        ["RAM",          "4GB",                        "2GB",                        "8GB"],
        ["存储",         "32GB ROM",                   "32GB",                       "128GB"],
        ["操作系统",     "RayNeo AI OS",               "未公布",                     "Android 14"],
        ["电池容量",     "245mAh",                     "210mAh",                     "660mAh"],
        ["续航",         "录制5h / 音乐3h / 视频36min","待机 8h",                    "待机7h / 音乐3h / 视频1.5h"],
        ["充电速度",     "38分钟充满",                 "磁吸充电",                   "30分钟充至59%，1小时充满"],
        ["Wi-Fi",        "WiFi 6 (2.4/5GHz)",          "WiFi 6",                     "未公布"],
        ["Bluetooth",    "BT 5.2",                     "BT 5.3",                     "BT (标准未公布)"],
        ["USB",          "USB-C",                      "USB-C",                      "USB-C"],
        ["摄像头",       "12MP Sony IMX681\n+ OV 空间相机 (6DoF用)", "12MP Sony IMX681\nF2.25, FOV H77/V94/D109°", "16MP 120° 超广角\n1080p EIS 防抖"],
        ["音频",         "双扬声器 + 3麦\n方向性拾音+降噪",         "2× AAC扬声器\n4方向性麦克风",              "双扬声器 + 4麦"],
        ["传感器",       "6DoF SLAM 定位\n加速度+陀螺仪",           "加速度计+陀螺仪+磁力计\n环境光传感器",      "3轴加速度+陀螺仪+磁力计\n环境光传感器"],
        ["跟踪",         "6DoF 内向外 SLAM",           "IMU 辅助",                   "IMU辅助; 手势追踪(Beta)"],
        ["输入方式",     "5向触摸键\n语音控制",        "语音控制",                   "触摸板 + 实体按键\n智能戒指 / 语音(Beta)"],
        ["AI 引擎",      "Gemini AI",                  "未公布",                     "内置 AI 助手"],
        ["镜腿材质",     "铝合金+钛合金铰链",          "镁铝合金+TR90",              "未公布"],
        ["防水等级",     "IPX2",                       "IPX4",                       "未公布"],
        ["重量",         "76g",                        "49g",                        "135g"],
        ["外形尺寸",     "153 × 46 × 169mm",           "155 × 49 × 44mm",            "未公布"],
        ["眼距调节",     "未公布",                     "瞳距 18mm 眼距",             "未公布"],
        ["处方镜片",     "支持 (合作眼镜商)",          "支持",                       "支持"],
        ["官方售价",     "$1,299",                     "$699 (原$799)",              "众筹中 ~$400-600"],
    ]
    s.append(tbl(t2, [34*mm, 54*mm, 52*mm, 46*mm], extra=[
        ('BACKGROUND',(0,0),(0,-1), colors.HexColor("#1A3A5C")),
        ('TEXTCOLOR', (0,0),(0,-1), WHITE),
        ('BACKGROUND',(0,4),(0,4), colors.HexColor("#1A3A5C")),
    ]))
    s.append(PageBreak())

    # ── 3. 各产品详细页 ───────────────────────────────────────────────────────
    # ─ 3-1 XREAL Air 2 Ultra ─
    s.append(hdr("产品详情 — XREAL Air 2 Ultra"))
    s.append(P("3. 各产品详细页", S_H1)); s.append(HR())
    s.append(P("3.1  XREAL Air 2 Ultra", S_H2))
    s.append(P("一句话定位：目前 Birdbath 方案中功能最全的有线 AR 眼镜，支持 6DoF 空间追踪，面向开发者和专业用户。", S_BODY))
    s.append(spec_block([
        ("显示引擎",       "Sony Micro-OLED × 2，0.55英寸"),
        ("光学方案",       "Birdbath 半透半反镜"),
        ("单眼分辨率",     "1920 × 1080 (Full HD)"),
        ("峰值亮度",       "500 nits"),
        ("刷新率",         "120Hz (2D) / 90Hz (3D / 侧边3D)"),
        ("视场角 FOV",     "52°"),
        ("色域",           "108% sRGB，16位色深，1600万色"),
        ("Passthrough",    "支持（摄像头透视，2个视觉传感器）"),
        ("6DoF 跟踪",      "内向外 6DoF 位置追踪（2个 CV 传感器）"),
        ("手势跟踪",       "支持手势识别"),
        ("主控 SoC",       "无（纯显示设备，算力来自外接设备）"),
        ("内置电池",       "无，USB-C 直接供电"),
        ("无线协议",       "无 WiFi / BT（纯 USB-C 连接）"),
        ("有线接口",       "USB-C（视频信号 + 供电）"),
        ("外壳材质",       "铝合金"),
        ("重量",           "80g"),
        ("外形尺寸",       "148.6 × 48 × 161.6mm（展开）"),
        ("认证",           "CE, TUV Rheinland 低蓝光 + 无频闪"),
        ("兼容性",         "Android / iOS / PC / Mac / 游戏主机（USB-C DP 输出）"),
        ("定价",           "~$699 USD"),
    ]))
    s.append(Spacer(1,4))
    s.append(B("核心价值：Birdbath 方案中最好的视场角（52°）+ 6DoF 追踪，适合开发空间 AR 应用。"))
    s.append(B("局限：500 nits 在户外强光下不够用；无板载计算，完全依赖外接设备。"))
    s.append(P("官网：https://us.shop.xreal.com/products/xreal-air-2-ultra", S_URL))
    s.append(P("规格参考：https://vr-compare.com/headset/xrealair2ultra  |  https://unboundxr.com/xreal-air-2-ultra", S_URL))
    s.append(Spacer(1,10))

    # ─ 3-2 XREAL Air 2 ─
    s.append(P("3.2  XREAL Air 2", S_H2))
    s.append(P("一句话定位：入门级 Birdbath AR 眼镜，性价比最高的有线接屏方案。", S_BODY))
    s.append(spec_block([
        ("显示引擎",       "Sony Micro-OLED × 2，0.55英寸"),
        ("光学方案",       "Birdbath 半透半反镜"),
        ("单眼分辨率",     "1920 × 1080 (Full HD)"),
        ("峰值亮度",       "500 nits"),
        ("刷新率",         "120Hz (2D) / 90Hz (3D)"),
        ("视场角 FOV",     "46°"),
        ("色域",           "108% sRGB"),
        ("跟踪",           "无 6DoF"),
        ("主控 SoC",       "无（纯显示设备）"),
        ("内置电池",       "无，USB-C 直接供电"),
        ("无线协议",       "无 WiFi / BT"),
        ("有线接口",       "USB-C"),
        ("音频",           "双立体声扬声器"),
        ("重量",           "72g"),
        ("外形尺寸",       "148 × 51.4 × 56.4mm（折叠）"),
        ("认证",           "CE, TUV Rheinland 低蓝光 + 无频闪"),
        ("定价",           "~$399 USD"),
    ]))
    s.append(P("官网：https://us.shop.xreal.com/products/xreal-air-2", S_URL))
    s.append(Spacer(1,10))

    # ─ 3-3 Rokid Max 2 ─
    s.append(P("3.3  Rokid Max 2", S_H2))
    s.append(P("一句话定位：亮度最高的 Birdbath 有线眼镜（600 nits），配合 Rokid Station 2 底座可独立使用。", S_BODY))
    s.append(spec_block([
        ("显示引擎",       "Sony 0.68\" Micro-OLED × 2"),
        ("光学方案",       "Birdbath 半透半反镜"),
        ("单眼分辨率",     "1920 × 1080 (Full HD)"),
        ("峰值亮度",       "600 nits"),
        ("刷新率",         "90Hz"),
        ("视场角 FOV",     "50°"),
        ("对比度",         "100,000:1"),
        ("色域",           "sRGB 106%"),
        ("主控 SoC (glasses)", "无（纯显示设备）"),
        ("内置电池 (glasses)", "无，USB-C 供电"),
        ("无线协议 (glasses)", "无"),
        ("有线接口",       "USB-C"),
        ("重量",           "75g"),
        ("配套底座 Station 2", "Snapdragon SoC, 8GB RAM, 128GB,\n5000mAh, WiFi 6, BT 5.2, USB-C"),
        ("定价",           "~$449 USD (glasses only)"),
    ]))
    s.append(P("官网：https://global.rokid.com/pages/rokid-max-2", S_URL))
    s.append(P("Amazon：https://www.amazon.com/dp/B0DKX1WSQ3", S_URL))
    s.append(PageBreak())

    # ─ 3-4 RayNeo X3 Pro ─
    s.append(hdr("产品详情 — RayNeo X3 Pro"))
    s.append(P("3.4  RayNeo X3 Pro（TCL 雷鸟）", S_H2))
    s.append(colored_badge("★ 目前户外可用性最强的量产 AR 眼镜 — 6000 nits MicroLED + 衍射波导", C_DARK))
    s.append(Spacer(1,4))
    s.append(P("一句话定位：唯一在量产 AR 眼镜中用 MicroLED + 波导实现户外强光可见的产品，代价是分辨率低（640×480）和高售价（$1299）。", S_BODY))
    s.append(spec_block([
        ("显示引擎",       "全彩 MicroLED 双目投影仪"),
        ("光学方案",       "双目衍射波导"),
        ("单眼分辨率",     "640 × 480"),
        ("峰值亮度",       "6,000 nits（典型 3,500 nits）"),
        ("刷新率",         "60Hz"),
        ("视场角 FOV",     "30°"),
        ("镜片透过率",     "90%"),
        ("主控 SoC",       "Qualcomm Snapdragon AR1 Gen 1"),
        ("AI 引擎",        "Google Gemini 集成"),
        ("RAM",            "4GB"),
        ("存储",           "32GB ROM"),
        ("操作系统",       "RayNeo AI OS"),
        ("电池容量",       "245mAh（眼镜内置）"),
        ("续航",           "录制 5h / 播音乐 3h / 看视频 ~36min"),
        ("充电",           "USB-C，38分钟充满"),
        ("WiFi",           "WiFi 6（802.11ax），2.4GHz + 5GHz 双频"),
        ("Bluetooth",      "BT 5.2"),
        ("USB",            "USB-C Type-C"),
        ("摄像头 (RGB)",   "12MP Sony IMX681，F2.2，16mm 超广角"),
        ("摄像头 (空间)",  "OV Spatial Camera，F2.0，6DoF 空间定位用"),
        ("跟踪",           "6DoF 内向外 SLAM 定位"),
        ("音频",           "双腔体立体声扬声器 + 3麦\n窄波束指向拾音 + 噪声消除"),
        ("输入",           "5向触摸按键；语音控制；Apple Watch 兼容"),
        ("传感器",         "加速度计 + 陀螺仪 + 磁力计"),
        ("防水等级",       "IPX2"),
        ("重量",           "76g"),
        ("外形尺寸",       "153.16 × 45.65mm"),
        ("镜腿材质",       "铝合金 + 钛合金铰链"),
        ("认证",           "CE, IPX2, RoHS"),
        ("开发支持",       "Unity ARDK + Android ARDK 开发者模式"),
        ("处方镜片",       "支持（RayNeo 全球合作眼镜商）"),
        ("官方售价",       "$1,299 USD"),
    ]))
    s.append(Spacer(1,4))
    s.append(B("核心优势：6000 nits 是目前量产眼镜中唯一在高尔夫球场直射阳光下可见的方案。"))
    s.append(B("核心劣势：640×480 分辨率是 2004 年手机水平；$1299 售价偏贵；电池续航视频仅 36 分钟。"))
    s.append(P("官网：https://www.rayneo.com/products/x3-pro-ai-display-glasses", S_URL))
    s.append(P("评测 (Tom's Hardware)：https://www.tomshardware.com/peripherals/wearable-tech/rayneo-x3-pro-ar-glasses-review", S_URL))
    s.append(P("评测 (Notebookcheck)：https://www.notebookcheck.net/TCL-RayNeo-X3-Pro-debut-as-cutting-edge-new-microLED-AR-glasses.1025368.0.html", S_URL))
    s.append(PageBreak())

    # ─ 3-5 Rokid Glasses ─
    s.append(hdr("产品详情 — Rokid Glasses"))
    s.append(P("3.5  Rokid Glasses", S_H2))
    s.append(colored_badge("★ 目前最轻的一体式 AR 眼镜 — 49g，对标 Meta Ray-Ban 外形", C_TEAL))
    s.append(Spacer(1,4))
    s.append(P("一句话定位：全球最轻的一体式 AR 智能眼镜之一（49g），单色绿 MicroLED 节省功耗，用 Snapdragon AR1 + WiFi 6 + BT 5.3 实现完整无线连接。", S_BODY))
    s.append(spec_block([
        ("显示引擎",       "双目单色绿 MicroLED（波长单一 = 功耗极低）"),
        ("光学方案",       "双目衍射光波导"),
        ("单眼分辨率",     "480 × 398"),
        ("峰值亮度",       "1,500 nits（可调光）"),
        ("视场角 FOV",     "30°"),
        ("眼距",           "18mm 眼距"),
        ("显示色彩",       "单色绿（非全彩）"),
        ("主控 SoC",       "Qualcomm Snapdragon AR1 Gen 1"),
        ("辅助 MCU",       "NXP RT600 (MIMXRT685SFAWBR) — 语音唤醒/低功耗任务"),
        ("RAM",            "2GB"),
        ("存储",           "32GB"),
        ("电池容量",       "210mAh"),
        ("续航",           "最长约 8 小时（轻量使用）"),
        ("充电方式",       "磁吸充电线"),
        ("WiFi",           "WiFi 6（802.11ax）"),
        ("Bluetooth",      "BT 5.3"),
        ("USB",            "USB-C"),
        ("摄像头",         "12MP Sony IMX681, F2.25 光圈\n相机 FOV: H77° / V94° / D109°\n焦距 1.9m, 景深 34cm~∞\n1680p 视频录制"),
        ("音频",           "2× AAC 0920 扬声器 + 4 方向性麦克风\n具备 AI 降噪"),
        ("传感器",         "3轴加速度计 + 陀螺仪 + 磁力计 + 环境光"),
        ("镜框材质",       "镁铝合金"),
        ("镜腿材质",       "TR90 工程塑料"),
        ("防水等级",       "IPX4"),
        ("重量",           "49g"),
        ("外形尺寸",       "155 × 49 × 44mm"),
        ("处方镜片",       "支持"),
        ("官方售价",       "$699 USD（原价 $799）"),
    ]))
    s.append(Spacer(1,4))
    s.append(B("为什么用单色绿 MicroLED：单波长比全彩 MicroLED 功耗低 60%+，维持 49g 重量和 8h 续航的关键。代价是无法显示彩色内容。"))
    s.append(B("NXP RT600 的作用：专门处理语音唤醒词识别和始终在线的低功耗任务，AR1 主芯片可以深度休眠——这是双芯片设计在 AR 眼镜上的典型应用。"))
    s.append(P("官网：https://global.rokid.com/products/rokid-glasses", S_URL))
    s.append(P("发布公告：https://global.rokid.com/blogs/news/rokid-glasses-are-lightweight-ar-smart-glasses-with-micro-led-displays-and-a-499-price-tag", S_URL))
    s.append(P("评测 (Tom's Guide)：https://www.tomsguide.com/computing/smart-glasses/rokid-glasses-review", S_URL))
    s.append(PageBreak())

    # ─ 3-6 INMO AIR3 ─
    s.append(hdr("产品详情 — INMO AIR3"))
    s.append(P("3.6  INMO AIR3（影目）", S_H2))
    s.append(colored_badge("★ 目前分辨率最高的一体式 AR 眼镜 — 1080p + 全彩波导 + Android 14", colors.HexColor("#1A5C3A")))
    s.append(Spacer(1,4))
    s.append(P("一句话定位：自称全球首款量产 1080p 全彩一体式 AR 眼镜，用 Micro-OLED 做光源配合全彩 RGB 波导，但代价是重量（135g）和短续航（1.5h 视频）。", S_BODY))
    s.append(spec_block([
        ("显示引擎",       "Sony Micro-OLED × 2"),
        ("光学方案",       "全彩 RGB 1D 阵列光波导"),
        ("单眼分辨率",     "1920 × 1080 (Full HD)"),
        ("峰值亮度",       "600 nits（可调）"),
        ("刷新率",         "60Hz / 最高 120Hz"),
        ("视场角 FOV",     "36°"),
        ("清晰度",         "62 PPD (Pixels Per Degree)"),
        ("色域",           "100% sRGB"),
        ("主控 SoC",       "Qualcomm Snapdragon 8核（具体型号未公布）"),
        ("RAM",            "8GB"),
        ("存储",           "128GB"),
        ("操作系统",       "Android 14"),
        ("电池容量",       "660mAh"),
        ("续航",           "待机 7h / 音乐 3h / 视频 1.5h"),
        ("快充",           "30分钟充至 59%，1小时充满"),
        ("WiFi",           "未公布"),
        ("Bluetooth",      "支持 BT（标准未公布）"),
        ("USB",            "USB-C"),
        ("摄像头",         "16MP, 120° 超广角, 1080p EIS 防抖视频"),
        ("音频",           "双扬声器 + 4 麦克风"),
        ("传感器",         "3轴加速度计 + 陀螺仪 + 磁力计 + 环境光"),
        ("输入方式",       "右镜腿触摸板 + 2音量键 + 电源键\n配套触摸板鼠标（随附）\n智能戒指控制器（随附）\n语音控制(Beta) + 手势追踪带(Beta)"),
        ("随附配件",       "触摸板、充电线、太阳镜夹片、清洁布"),
        ("重量",           "135g"),
        ("处方镜片",       "支持"),
        ("众筹平台",       "Kickstarter，众筹破百万美元"),
        ("官方售价",       "众筹约 $400-600 USD"),
    ]))
    s.append(Spacer(1,4))
    s.append(B("1080p + 全彩波导的技术路径：用 Micro-OLED 驱动全彩 RGB 波导，分辨率最高但亮度被波导损耗限制在 600 nits，户外可见性不足。"))
    s.append(B("135g 是明显劣势：是 Rokid Glasses(49g) 的 2.75 倍，长时间佩戴体验差。根本原因是电池（660mAh）比其他产品大得多。"))
    s.append(P("官网：https://www.inmoxr.com/products/inmo-air3-ar-glasses-all-in-one-full-color-waveguide", S_URL))
    s.append(P("规格页：https://www.inmoxr.com/pages/inmo-air3-specs", S_URL))
    s.append(P("评测：https://www.geeky-gadgets.com/inmo-air-3-waveguide-display/", S_URL))
    s.append(PageBreak())

    # ─ 3-7 Meta Orion ─
    s.append(hdr("产品详情 — Meta Orion（原型）"))
    s.append(P("3.7  Meta Orion（研究原型，暂不销售）", S_H2))
    s.append(colored_badge("技术天花板参照物 — SiC 波导 + 70° FOV，量产目标 2027", colors.HexColor("#5C1A1A")))
    s.append(Spacer(1,4))
    s.append(P("一句话定位：目前人类造出的 FOV 最大的 AR 眼镜原型（70°），用碳化硅波导消除彩虹纹，计算放在独立无线计算包里。每副成本约 $10,000，量产计划 2027 年。", S_BODY))
    s.append(spec_block([
        ("显示引擎",       "Meta 定制 uLED（MicroLED 变体），波长级最小像素密度"),
        ("光学方案",       "硅基碳化硅（SiC）全息衍射波导（Meta 自研）"),
        ("视场角 FOV",     "~70°（目前量产形态最大，接近自然视野下限 ~120°）"),
        ("彩虹纹",         "极低（SiC 高折射率消除彩虹纹）"),
        ("镜片材质",       "碳化硅（SiC）— 高折射率、高热导率"),
        ("主控 SoC",       "Meta 定制 AI/图形专用芯片（规格未公开）"),
        ("辅助 MCU",       "11 颗定制微控制器（专用热管理）"),
        ("计算形态",       "主算力在独立无线计算包（Puck）中，非眼镜内置"),
        ("电池",           "计算包提供"),
        ("眼镜重量",       "~100g（镁合金镜框）"),
        ("跟踪/感知",      "眼动追踪 + 手势追踪 + EMG 腕带（肌电图输入）"),
        ("输入方式",       "眼动 + 手势 + 语音 + EMG 腕带"),
        ("感知摄像头",     "多个微型相机环绕镜框边缘（手势+眼部+空间感知）"),
        ("WiFi/BT",        "通过计算包无线连接"),
        ("制造成本",       "~$10,000/副（内部测试用，非零售价）"),
        ("量产计划",       "消费级目标 2027 年"),
        ("发货状态",       "不对外销售，仅内部研究"),
    ]))
    s.append(Spacer(1,4))
    s.append(B("SiC 波导的核心价值：碳化硅折射率比玻璃高（n≈2.65 vs n≈1.5），同样厚度能实现更大 FOV；热导率高（490 W/m·K）帮助散热；密度相对低，控制重量。"))
    s.append(B("双芯片 + 计算包架构：眼镜只留光学+传感器，算力在口袋包里——这和我们项目的「眼镜 + 拴绳计算包」架构高度一致。"))
    s.append(P("官网：https://www.meta.com/emerging-tech/orion/", S_URL))
    s.append(P("深度分析 (KGOnTech)：https://kguttag.com/2024/10/06/meta-orion-ar-glasses-pt-1-waveguides/", S_URL))
    s.append(P("IEEE Spectrum 成本分析：https://spectrum.ieee.org/meta-ar-glasses-expense", S_URL))
    s.append(PageBreak())

    # ── 4. 横向对比 ──────────────────────────────────────────────────────────
    s.append(hdr("横向对比与项目关联"))
    s.append(P("4. 横向对比与对我们项目的意义", S_H1)); s.append(HR())

    s.append(P("4.1 关键参数横向对比", S_H2))
    cmp = [
        ["指标",           "XREAL Air 2 Ultra", "Rokid Max 2",     "RayNeo X3 Pro", "Rokid Glasses", "INMO AIR3",    "Meta Orion"],
        ["形态",           "有线挂接",           "有线挂接",         "一体机",         "一体机",         "一体机",        "原型+计算包"],
        ["光学方案",       "Birdbath",           "Birdbath",         "衍射波导",       "衍射波导",       "衍射波导",      "SiC 全息波导"],
        ["显示引擎",       "Micro-OLED",         "Micro-OLED",       "MicroLED",       "MicroLED(单色)", "Micro-OLED",   "uLED(定制)"],
        ["单眼分辨率",     "1920×1080",          "1920×1080",        "640×480",        "480×398",        "1920×1080",    "640×480"],
        ["峰值亮度",       "500 nits",           "600 nits",         "6000 nits",      "1500 nits",      "600 nits",     "未公布"],
        ["视场角 FOV",     "52°",                "50°",              "30°",            "30°",            "36°",          "~70°"],
        ["主控 SoC",       "无",                 "无",               "Snapdragon AR1", "Snapdragon AR1\n+NXP RT600", "Snapdragon 8核", "Meta 定制"],
        ["WiFi",           "无",                 "无(glasses)",      "WiFi 6",         "WiFi 6",         "未公布",       "通过计算包"],
        ["BT",             "无",                 "无(glasses)",      "BT 5.2",         "BT 5.3",         "BT",           "通过计算包"],
        ["重量",           "80g",                "75g",              "76g",            "49g",            "135g",         "~100g"],
        ["电池续航(视频)", "无内置电池",          "无内置电池",        "~36 min",        "未公布",         "~1.5h",        "计算包供电"],
        ["户外强光可用",   "⚠️ 勉强",            "⚠️ 勉强",          "✅ 6000 nits",   "⚠️ 1500 nits",  "❌ 600 nits",  "未知"],
        ["OS",             "N/A",                "N/A",              "RayNeo AI OS",   "未公布",         "Android 14",   "Meta OS"],
        ["开发者支持",     "USB-C DP",           "USB-C DP",         "Unity ARDK",     "未公布",         "Android SDK",  "无(非商品)"],
        ["参考售价",       "$699",               "$449",             "$1,299",         "$699",           "$400-600",     "不售"],
    ]
    s.append(tbl(cmp, [28*mm, 28*mm, 26*mm, 26*mm, 26*mm, 24*mm, 24*mm], extra=[
        ('BACKGROUND',(0,0),(0,-1), C_DARK),
        ('TEXTCOLOR', (0,0),(0,-1), WHITE),
        ('BACKGROUND',(0,4),(0,4), C_DARK),
    ]))
    s.append(Spacer(1,8))

    s.append(P("4.2 对我们项目（RV1106 运动 AR 眼镜）的直接含义", S_H2))
    rel = [
        ["我们的阶段", "参照产品", "关键参数意义", "行动"],
        ["Phase 3-I\n(SPI+棱镜)", "XREAL Air 2 的光学原理", "Birdbath 500 nits 已够室内/阴天 HUD；棱镜成本 ¥50–150", "验证 SPI OLED + 棱镜能否在眼镜上做 HUD 显示"],
        ["Phase 3-II\n(AMOLED+改良)", "Rokid Max 2 同类方案", "600 nits + 50° FOV 是 Birdbath 的上限；进一步提升需换波导", "提升画质，验证高尔夫轨迹弧线在 AMOLED 上的体验"],
        ["Phase 3-III\n(波导+MicroLED)", "RayNeo X3 Pro (6000 nits)", "户外球场必须 >1000 nits；唯一量产解法是 MicroLED + 波导", "评估 MicroLED 波导模块供应商，预算 ¥3000–20000+"],
        ["最终产品目标", "Rokid Glasses (49g 架构)", "双芯片 (AR1+MCU) + 磁充 + IPX4 是眼镜级产品的设计范式", "参考 Rokid Glasses 的重量分配和双芯片架构"],
        ["技术天花板", "Meta Orion (70° FOV)", "SiC 波导是 FOV 突破的路径；眼镜+计算包是算力解耦的验证", "长期关注，2027 年量产后评估商用 SiC 模组可及性"],
    ]
    s.append(tbl(rel, [26*mm, 34*mm, 60*mm, 56*mm]))
    s.append(Spacer(1,8))

    s.append(P("4.3 户外强光（高尔夫）亮度要求分析", S_H2))
    s.append(spec_block([
        ("晴天直射阳光亮度", "~100,000 lux（环境背景极亮）"),
        ("人眼适应后感知阈", "显示内容需 >1,000 nits 才能与背景竞争可见"),
        ("Birdbath 方案上限", "500–600 nits → 晴天室外基本不可见，仅适合阴天/室内"),
        ("衍射波导 + Micro-OLED", "600 nits → 同上，不够用"),
        ("衍射波导 + MicroLED 1500 nits", "（Rokid Glasses）阴天/背阴处可见，强阳光下仍吃力"),
        ("衍射波导 + MicroLED 6000 nits", "（RayNeo X3 Pro）户外晴天可见，是目前唯一量产解法"),
        ("SiC 波导 + uLED", "（Meta Orion）理论上更优，但非商品"),
        ("结论",
         "我们的 Phase 3-I/II 用 Birdbath 在室内/阴天 HUD 验证是合理的；"
         "最终户外产品必须用 MicroLED + 衍射波导（参照 RayNeo X3 Pro 技术路线）"),
    ]))
    s.append(Spacer(1,12))

    # ── 5. 来源链接 ──────────────────────────────────────────────────────────
    s.append(P("5. 完整来源链接", S_H1)); s.append(HR())
    links = [
        ["产品 / 资料", "链接"],
        ["XREAL Air 2 官网",          "https://us.shop.xreal.com/products/xreal-air-2"],
        ["XREAL Air 2 Ultra 官网",    "https://us.shop.xreal.com/products/xreal-air-2-ultra"],
        ["XREAL Air 2 Ultra 规格",    "https://vr-compare.com/headset/xrealair2ultra"],
        ["XREAL Air 2 Ultra UnboundXR","https://unboundxr.com/xreal-air-2-ultra"],
        ["Rokid Max 2 官网",          "https://global.rokid.com/pages/rokid-max-2"],
        ["Rokid Max 2 Amazon",        "https://www.amazon.com/dp/B0DKX1WSQ3"],
        ["Rokid Glasses 官网",        "https://global.rokid.com/products/rokid-glasses"],
        ["Rokid Glasses 发布公告",    "https://global.rokid.com/blogs/news/rokid-glasses-are-lightweight-ar-smart-glasses-with-micro-led-displays-and-a-499-price-tag"],
        ["Rokid Glasses 评测 Tom's Guide","https://www.tomsguide.com/computing/smart-glasses/rokid-glasses-review"],
        ["Rokid Glasses MicroLED分析","https://www.microled-info.com/rokid-announces-new-smart-ar-glasses-microled-microdisplays"],
        ["RayNeo X3 Pro 官网",        "https://www.rayneo.com/products/x3-pro-ai-display-glasses"],
        ["RayNeo X3 Pro 规格 UnboundXR","https://unboundxr.com/rayneo-x3-pro"],
        ["RayNeo X3 Pro 评测 Tom's Hardware","https://www.tomshardware.com/peripherals/wearable-tech/rayneo-x3-pro-ar-glasses-review"],
        ["RayNeo X3 Pro 评测 Notebookcheck","https://www.notebookcheck.net/TCL-RayNeo-X3-Pro-debut-as-cutting-edge-new-microLED-AR-glasses.1025368.0.html"],
        ["RayNeo X3 Pro 评测 Tom's Guide","https://www.tomsguide.com/computing/smart-glasses/tcl-rayneo-x3-pro-smart-glasses-review"],
        ["INMO AIR3 官网",            "https://www.inmoxr.com/products/inmo-air3-ar-glasses-all-in-one-full-color-waveguide"],
        ["INMO AIR3 规格页",          "https://www.inmoxr.com/pages/inmo-air3-specs"],
        ["INMO AIR3 评测 Geeky Gadgets","https://www.geeky-gadgets.com/inmo-air-3-waveguide-display/"],
        ["INMO AIR3 评测 ARMDevices", "https://armdevices.net/2026/01/09/inmo-air3-1080p-waveguide-ar-glasses-snapdragon-ring-control-36-fov/"],
        ["Meta Orion 官网",           "https://www.meta.com/emerging-tech/orion/"],
        ["Meta Orion SiC 波导博客",   "https://www.meta.com/blog/orion-silicon-carbide-waveguides-ar-glasses-large-field-of-view/"],
        ["Meta Orion 波导深度分析",   "https://kguttag.com/2024/10/06/meta-orion-ar-glasses-pt-1-waveguides/"],
        ["Meta Orion 成本分析 (IEEE)", "https://spectrum.ieee.org/meta-ar-glasses-expense"],
        ["Birdbath vs 波导对比",      "https://www.metavisi.cc/post/the-two-main-optical-solutions-in-consumer-ar-devices-birdbath-and-waveguide-technologies"],
        ["CES 2026 AR 光学趋势",      "https://en.ubiresearchnet.com/ces-2026-ar-glasses-optics-technology-waveguide-dimming/"],
        ["AR 市场 H2 2025 出货量",    "https://www.communicationstoday.co.in/ar-smart-glasses-shipments-grow-148-yoy-in-h2-2025/"],
        ["雷鸟 vs 影目对比 (知乎)",    "https://zhuanlan.zhihu.com/p/1917980128685822769"],
    ]
    s.append(tbl(links, [60*mm, COL-60*mm]))

    s.append(Spacer(1,10))
    s.append(HRFlowable(width="100%", thickness=1.0, color=C_DARK, spaceAfter=6))
    s.append(P("本报告数据来源于各品牌官网、第三方评测及公开规格表，截至 2026-06-23。"
               "部分参数（尤其 INMO AIR3 WiFi 标准、RayNeo X3 Pro 温升）尚未被厂商公开，标注为【未公布】。", S_NOTE))
    return s


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(__file__),
                       "AR眼镜市场技术报告_2026-06-23.pdf")
    doc = SimpleDocTemplate(out, pagesize=A4,
                            leftMargin=MARGIN, rightMargin=MARGIN,
                            topMargin=13*mm, bottomMargin=13*mm,
                            title="市售AR眼镜显示方案技术报告",
                            author="AR Sports Glasses Team")
    doc.build(story())
    print(f"生成完成: {out}")
