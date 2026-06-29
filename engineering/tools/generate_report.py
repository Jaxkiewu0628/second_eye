"""
生成《AI 眼镜主板选型与参数报告 — 视频管道专项版》PDF
运行: .venv/bin/python generate_report.py
输出: AI眼镜主板选型与参数报告_RV1106_视频管道专项_2026-06-23.pdf
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── 字体注册 ──────────────────────────────────────────────────────────────────
FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"
pdfmetrics.registerFont(TTFont("AUnicode", FONT_PATH))

# ── 颜色 ─────────────────────────────────────────────────────────────────────
DARK_BLUE   = colors.HexColor("#1A3A5C")
MID_BLUE    = colors.HexColor("#2E6DA4")
LIGHT_BLUE  = colors.HexColor("#D6E8F7")
ACCENT_TEAL = colors.HexColor("#0D7377")
GREEN_OK    = colors.HexColor("#1E7A34")
RED_WARN    = colors.HexColor("#A62020")
GRAY_BG     = colors.HexColor("#F4F4F4")
GRAY_LINE   = colors.HexColor("#CCCCCC")
WHITE       = colors.white
BLACK       = colors.black

# ── 段落样式 ──────────────────────────────────────────────────────────────────
def S(name, parent_name="Normal", **kw):
    base = dict(fontName="AUnicode", fontSize=10, leading=16,
                textColor=BLACK, spaceAfter=4)
    base.update(kw)
    return ParagraphStyle(name, **base)

sTitle    = S("sTitle",    fontSize=22, leading=28, textColor=WHITE,
              spaceAfter=6, spaceBefore=0, alignment=1)
sSubtitle = S("sSubtitle", fontSize=12, leading=18, textColor=colors.HexColor("#C8DFF2"),
              alignment=1, spaceAfter=4)
sChip     = S("sChip",     fontSize=10, leading=14, textColor=colors.HexColor("#BBDDFF"),
              alignment=1, spaceAfter=2)
sVersion  = S("sVersion",  fontSize=9,  leading=13, textColor=colors.HexColor("#9AAFC4"),
              alignment=1, spaceAfter=0)

sH1  = S("sH1",  fontSize=14, leading=20, textColor=DARK_BLUE,
         spaceBefore=12, spaceAfter=4, fontName="AUnicode")
sH2  = S("sH2",  fontSize=12, leading=18, textColor=MID_BLUE,
         spaceBefore=10, spaceAfter=4)
sH3  = S("sH3",  fontSize=11, leading=16, textColor=ACCENT_TEAL,
         spaceBefore=8,  spaceAfter=3)
sBody= S("sBody",fontSize=10, leading=15, textColor=BLACK, spaceAfter=4)
sBullet= S("sBullet",fontSize=10, leading=15, textColor=BLACK,
           leftIndent=12, spaceAfter=3)
sNote= S("sNote",fontSize=8.5, leading=13, textColor=colors.HexColor("#555555"),
         spaceAfter=4)
sGreen = S("sGreen",fontSize=10, leading=15, textColor=GREEN_OK, spaceAfter=3)
sRed   = S("sRed",  fontSize=10, leading=15, textColor=RED_WARN,  spaceAfter=3)
sTH    = S("sTH",   fontSize=9,  leading=13, textColor=WHITE,
           alignment=1, fontName="AUnicode")
sTD    = S("sTD",   fontSize=9,  leading=13, textColor=BLACK)
sTDc   = S("sTDc",  fontSize=9,  leading=13, textColor=BLACK, alignment=1)

W, H = A4
COL  = W - 30*mm      # usable text width

# ── 表格通用样式 ──────────────────────────────────────────────────────────────
def header_row_style(ncols, bg=DARK_BLUE):
    return [
        ('BACKGROUND',  (0,0), (ncols-1, 0), bg),
        ('TEXTCOLOR',   (0,0), (ncols-1, 0), WHITE),
        ('FONTNAME',    (0,0), (-1,-1),        'AUnicode'),
        ('FONTSIZE',    (0,0), (-1,-1),        9),
        ('LEADING',     (0,0), (-1,-1),        14),
        ('TOPPADDING',  (0,0), (-1,-1),        4),
        ('BOTTOMPADDING',(0,0),(-1,-1),        4),
        ('LEFTPADDING', (0,0), (-1,-1),        5),
        ('RIGHTPADDING',(0,0), (-1,-1),        5),
        ('GRID',        (0,0), (-1,-1),        0.4, GRAY_LINE),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),       [WHITE, GRAY_BG]),
        ('VALIGN',      (0,0), (-1,-1),        'TOP'),
    ]

def make_table(data, col_widths, extra_style=None):
    ts = TableStyle(header_row_style(len(data[0])))
    if extra_style:
        for cmd in extra_style:
            if cmd is not None:
                ts.add(*cmd)
    t = Table([[Paragraph(str(c) if not isinstance(c, Paragraph) else c, sTH)
                if r == 0 else
                (c if isinstance(c, Paragraph) else Paragraph(str(c), sTD))
                for c in row]
               for r, row in enumerate(data)],
              colWidths=col_widths, repeatRows=1)
    t.setStyle(ts)
    return t

def P(text, style=None):
    return Paragraph(text, style or sBody)

def bullet(text):
    return Paragraph(f"• {text}", sBullet)

def section_rule():
    return HRFlowable(width="100%", thickness=0.8, color=MID_BLUE,
                      spaceAfter=6, spaceBefore=2)

# ── 封面 ─────────────────────────────────────────────────────────────────────
def cover_block():
    elems = []
    # 深蓝背景色块用 Table 模拟
    cover_data = [[
        Paragraph("AI 眼镜主板选型与参数报告", sTitle),
    ]]
    cover_table = Table(cover_data, colWidths=[COL])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_BLUE),
        ('TOPPADDING',  (0,0), (-1,-1), 20),
        ('BOTTOMPADDING',(0,0),(-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING',(0,0), (-1,-1), 10),
    ]))
    elems.append(cover_table)

    sub_data = [[
        Paragraph("视频管道专项版 — 面向运动 AR 场景（高尔夫弹道 / 生物特征感知）",
                  sSubtitle),
    ]]
    sub_table = Table(sub_data, colWidths=[COL])
    sub_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_BLUE),
        ('TOPPADDING',  (0,0), (-1,-1), 0),
        ('BOTTOMPADDING',(0,0),(-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING',(0,0), (-1,-1), 10),
    ]))
    elems.append(sub_table)

    chip_data = [[
        Paragraph("已淘汰", sChip),
        Paragraph("已评估", sChip),
        Paragraph("✓ 已选定", S("sBold", fontSize=11, textColor=colors.HexColor("#7EF0A0"), alignment=1)),
    ],[
        Paragraph("Seeed XIAO ESP32-S3", sChip),
        Paragraph("ESP32-P4 + ESP32-C6", sChip),
        Paragraph("Rockchip RV1106 / Luckfox Pico Ultra W", sChip),
    ]]
    chip_table = Table(chip_data, colWidths=[COL/3, COL/3, COL/3])
    chip_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#2A1A1A")),
        ('BACKGROUND', (1,0), (1,-1), colors.HexColor("#1A2A2A")),
        ('BACKGROUND', (2,0), (2,-1), colors.HexColor("#0D3320")),
        ('TOPPADDING',  (0,0), (-1,-1), 8),
        ('BOTTOMPADDING',(0,0),(-1,-1), 8),
        ('FONTNAME',   (0,0), (-1,-1), 'AUnicode'),
        ('FONTSIZE',   (0,0), (-1,-1), 9),
        ('GRID',       (0,0), (-1,-1), 0.5, colors.HexColor("#333333")),
    ]))
    elems.append(chip_table)
    elems.append(Spacer(1, 8))

    ver_data = [[
        Paragraph("版本 1.0  |  规格检索截至 2026 年 6 月 23 日  |  用途：视频管道原型选型 / 功耗预算 / 开发路线规划", sVersion),
    ]]
    ver_table = Table(ver_data, colWidths=[COL])
    ver_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0E2035")),
        ('TOPPADDING',  (0,0), (-1,-1), 8),
        ('BOTTOMPADDING',(0,0),(-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
    ]))
    elems.append(ver_table)
    elems.append(Spacer(1, 12))
    return elems

# ── 正文内容 ─────────────────────────────────────────────────────────────────
def build_story():
    story = []
    story += cover_block()

    # ── 页眉辅助标识 ─────────────────────────────────────────────────────────
    def page_header(section_title):
        hdr = Table([[Paragraph(f"AI眼镜主板选型与参数报告  |  视频管道专项版  |  {section_title}",
                                S("sHdr", fontSize=8, textColor=colors.HexColor("#666666")))
                      ]],
                    colWidths=[COL])
        hdr.setStyle(TableStyle([
            ('BOTTOMPADDING',(0,0),(-1,-1), 2),
            ('TOPPADDING',  (0,0),(-1,-1), 0),
        ]))
        return hdr

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 执行摘要
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(P("执行摘要", sH1))
    story.append(section_rule())

    story.append(P("核心结论", sH2))
    story.append(P(
        "视频管道是本项目的根本性瓶颈：将相机帧从微型眼镜移动到显示/手机，"
        "必须在极度受限的空间、功耗和发热约束下实现足够低的延迟。"
        "本报告评估三条路径后，最终选定 <b>Rockchip RV1106（Luckfox Pico Ultra W）</b>"
        "作为 V0/V1 原型平台，理由如下：", sBody))

    story.append(bullet("硬件 H.265 编码器：1080p30 仅需 2–5 Mbps，比无编码器的 MJPEG 方案节省约 6–15 倍带宽。"))
    story.append(bullet("板载 NPU（~0.5–1 TOPS）：可在设备端完成目标检测/追踪，向手机只发送结果（~kbps），彻底规避视频传输瓶颈。"))
    story.append(bullet("低功耗：~0.1–0.3 W 主动功耗，专为电池安防相机设计，与眼镜功耗预算吻合。"))
    story.append(bullet("完整 Linux：标准摄像头/推流/AI 工具链（V4L2、GStreamer、RKNN、OpenCV）开箱即用。"))
    story.append(bullet("尺寸路线清晰：开发板用于验证，SoM（Core1106，30×30 mm）用于 V1，裸芯片（~10–15 mm SiP）面向最终产品。"))
    story.append(Spacer(1, 6))

    story.append(P("一眼看懂的推荐", sH2))
    rec_data = [
        ["用途", "推荐平台", "原因"],
        ["现在做 V0 验证", "Luckfox Pico Ultra W\n(RV1106 开发板)", "30–45 USD；板载 WiFi 6 + eMMC；可直接运行 H.265 推流和 RKNN 推理。"],
        ["V1 原型嵌入眼镜", "Core1106 SoM\n(30×30 mm 邮票孔模块)", "焊接到自制窄板；去掉开发板上的 USB 排针和屏接口，只留相机 + 无线 + 电源。"],
        ["量产形态目标", "RV1106 裸芯片 (SiP ~10–15 mm)", "定制 rigid-flex PCB，穿过镜腿和铰链；与 Meta Ray-Ban 拆解路线一致。"],
        ["算法验证（不依赖硬件）", "macOS + prototype/ 文件夹\n(.venv)", "trajectory.py / ball_detect.py 可在无板时本地跑；NPU 模型在 RKNN-Toolkit2 Docker 中转换。"],
    ]
    rec_widths = [42*mm, 50*mm, COL - 92*mm]
    story.append(make_table(rec_data, rec_widths))
    story.append(Spacer(1, 8))

    story.append(P("最重要的工程提醒", sH2))
    story.append(bullet(
        "视频传输是<b>带宽受限问题</b>，不是算力问题。解法是在设备端压缩或分析，发送更少的数据，"
        "而不是提高无线速率。"))
    story.append(bullet(
        "Wi-Fi 标称速率（802.11ax 最高 574 Mbps）远高于实际应用吞吐。"
        "协议栈开销、内存复制和信号质量会将实际值压低到标称的 10–25%。"))
    story.append(bullet(
        "H.265 比 H.264 节省 30–50% 码率，但需要硬件编码器支持才能在功耗和延迟上实用。"
        "ESP32-S3 无硬件编码器，只能做 MJPEG，每帧开销比 H.264 大 6–15 倍。"))
    story.append(bullet(
        "NPU 的价值在于『不发送视频』——把弹道轨迹计算、目标检测全部在片内完成，"
        "BLE 发送几十字节的结果即可，延迟和功耗同时下降。"))
    story.append(bullet(
        "最终产品不会把完整开发板塞进镜腿。需要拆除 USB 接头、排针、显示接口和调试芯片，"
        "重新设计为 6–10 mm 宽的狭长 rigid-flex PCB。"))
    story.append(PageBreak())

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 报告范围
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(page_header("报告范围与参数解释"))
    story.append(P("1. 报告范围与参数解释", sH1))
    story.append(section_rule())
    story.append(P(
        "本报告聚焦<b>视频数据管道</b>——从相机传感器到手机/显示器的全链路带宽、延迟和算力预算。"
        "参数来源为制造商官方产品页、芯片数据手册及社区实测数据；"
        "『未公布』不代表为零，而是厂商未给出可直接引用的整板数据，需在实际条件下测量。", sBody))

    story.append(P("1.1 关键参数区别", sH2))
    kv_data = [
        ["参数", "含义"],
        ["实际 Wi-Fi 吞吐", "扣除协议栈开销、内存复制和信号损耗后的真实数据率（始终低于 PHY 标称值）。"],
        ["硬件编码器 vs MJPEG", "硬件 H.264/H.265 在硅片上完成压缩，不占 CPU，功耗低；MJPEG 用软件，每帧发完整 JPEG，码率高 6–15 倍。"],
        ["NPU TOPS", "每秒万亿次整数运算，衡量 AI 推理吞吐；0.5–1 TOPS 可实时运行 YOLOv5n/MobileNet 检测模型。"],
        ["『结果』模式码率", "NPU 在设备端检测后只发坐标/心率等结果，码率降至 ~kbps，比视频流低 3–4 个数量级。"],
        ["Glass-to-glass 延迟", "从相机曝光到显示器点亮的全链路时延；AR 覆盖层要求 <150 ms，头锁模式要求 <20 ms。"],
    ]
    story.append(make_table(kv_data, [52*mm, COL - 52*mm]))
    story.append(Spacer(1, 6))

    story.append(P("1.2 功耗数据四种类型", sH2))
    pw_data = [
        ["类型", "说明"],
        ["整板场景实测", "最有参考价值。例如 Luckfox 的 H.265 推流平均电流、NPU 满载电流。"],
        ["睡眠电流",       "说明待机潜力，不代表持续摄像时的续航。"],
        ["芯片最小值",     "例如 RV1106 ~100 mW 是裸芯片估算，不含外部相机、WiFi 和 LED。"],
        ["电源额定值",     "例如 5V 2A 是建议供电能力，不是持续消耗功率。"],
    ]
    story.append(make_table(pw_data, [40*mm, COL - 40*mm]))
    story.append(Spacer(1, 6))

    story.append(P("1.3 对眼镜嵌入最容易忽略的指标", sH2))
    story.append(bullet("PCB 宽度与连接器高度，而不只是长×宽——镜腿内部仅 6–10 mm 可用。"))
    story.append(bullet("相机能否通过 FPC 分离到前框；镜头能否锁焦以适应固定视角。"))
    story.append(bullet("WiFi 天线靠近人头、金属铰链和电池后的失谐——需要实测 RSSI 和吞吐退化。"))
    story.append(bullet("表面温升与皮肤接触安全——RV1106 ~0.1–0.3 W 主动功耗对应的热设计。"))
    story.append(bullet("启动时间、断电恢复和 OTA 更新——Linux 系统约需 3–8 秒启动，MCU 方案毫秒级。"))
    story.append(PageBreak())

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 参数总表
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(page_header("参数总表"))
    story.append(P("2. 参数总表", sH1))
    story.append(section_rule())

    story.append(P("2.1 处理器、AI、Memory 与 Storage", sH2))
    cpu_data = [
        ["平台", "处理器", "AI 能力", "运行内存", "程序/板载存储", "可更换存储", "本项目定位"],
        ["XIAO\nESP32-S3", "ESP32-S3R8\n双核 Xtensa LX7\n240 MHz",
         "向量指令/TinyML\n无独立 NPU",
         "8 MB PSRAM", "8 MB Flash", "microSD\n官方 32 GB FAT",
         "已淘汰：\n无硬件编码器\nMJPEG 码率过高"],
        ["ESP32-P4\n+ C6", "双核 RISC-V\n最高 400 MHz\n+ 低功耗核",
         "AI 指令流水线\nH.264 硬编\n无独立 NPU",
         "最高 32 MB PSRAM", "16 MB SPI Flash", "microSD\nSDIO/SPI",
         "已评估：\n无 H.265 无 NPU\n~1 W 偏高"],
        ["RV1106\n(Luckfox)\n★ 已选定", "ARM Cortex-A7\n~1 GHz\n+ RISC-V 协处理器",
         "~0.5–1 TOPS NPU\n(INT8)\n支持 YOLOv5/MobileNet",
         "256 MB DDR3L", "8 GB eMMC\n(板载)", "无（eMMC 已足够）",
         "当前选型：\n最佳压缩+AI\n低功耗 Linux"],
    ]
    cpu_widths = [22*mm, 30*mm, 30*mm, 22*mm, 28*mm, 22*mm, 32*mm]
    t = make_table(cpu_data, cpu_widths, extra_style=[
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#D6F0E0")),
    ])
    story.append(t)
    story.append(P("注：RV1106 eMMC 中系统占用约 2–3 GB，用户可用约 5 GB；无 microSD 槽但 eMMC 写入寿命远高于 SD。", sNote))
    story.append(Spacer(1, 8))

    story.append(P("2.2 摄像头、帧率与视频接口", sH2))
    cam_data = [
        ["平台", "相机", "最大分辨率", "相机接口", "视频/帧率能力", "码率 @ 1080p30"],
        ["XIAO ESP32-S3",
         "OV3660 ~3 MP\n(或 OV2640)",
         "2048×1536",
         "DVP 并行\n(旧总线)",
         "MJPEG 帧序列\n无 H.264 硬编\n最高可用 VGA 30fps",
         "❌ 不可行\n(需 15–50 Mbps)"],
        ["ESP32-P4 + C6",
         "2 MP 手动调焦\n(开发板)",
         "2 MP / MIPI 扩展",
         "MIPI-CSI\n芯片亦支持 DVP",
         "H.264 硬编\n最高 1080p @ 30fps",
         "4–8 Mbps (H.264)"],
        ["RV1106 ★",
         "MIPI-CSI 相机\n(最高 5 MP)",
         "5 MP\n2592×1944",
         "MIPI-CSI + ISP\n(2-lane)",
         "H.264 + H.265 硬编\n最高 5 MP @ 30fps\nISP 噪声/曝光处理",
         "2–5 Mbps (H.265)\n4–8 Mbps (H.264)"],
    ]
    cam_widths = [22*mm, 26*mm, 24*mm, 24*mm, 44*mm, 32*mm]
    story.append(make_table(cam_data, cam_widths, extra_style=[
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#D6F0E0")),
    ]))
    story.append(P(
        "注：最大分辨率是传感器能力上限；AR 覆盖层实际推理通常缩放至 320×320 或 640×640。"
        "滚动快门在高速运动场景（如高尔夫挥杆）可能产生几何变形，必要时可选全局快门模块。", sNote))
    story.append(Spacer(1, 8))

    story.append(P("2.3 无线、USB 与外设传输", sH2))
    wifi_data = [
        ["平台", "Wi-Fi", "Bluetooth", "USB", "WiFi/BLE 冲突", "本项目含义"],
        ["XIAO ESP32-S3",
         "2.4 GHz 802.11b/g/n\n实测 ~1.6–10 Mbps\n(极不稳定)",
         "BLE 5.0\n2 Mbps PHY",
         "USB Full-Speed\n12 Mbps",
         "❌ 共用一个天线\nBLE 激活时 WiFi\n吞吐降 30–50%",
         "不可用于视频传输\n仅适合轻量传感数据"],
        ["ESP32-P4 + C6",
         "WiFi 6 (2.4 GHz)\n经 C6 转发\n实测 SDIO 瓶颈 ~36 Mbps",
         "BLE 5",
         "USB 2.0 HS\ndevice",
         "✅ 独立芯片\n无共享天线税",
         "WiFi 够用；但\nSDIO 成为瓶颈\n~36 Mbps 上限"],
        ["RV1106 ★",
         "内置 WiFi 6\n(802.11ax, 2.4 GHz)\n实测数十 Mbps",
         "内置 BLE 5.2",
         "USB 2.0 OTG\nHS",
         "✅ 无冲突\n(电路板层隔离)",
         "WiFi 带宽充裕\nH.265 仅需 2–5 Mbps\n~10× 余量"],
    ]
    wifi_widths = [22*mm, 36*mm, 22*mm, 22*mm, 28*mm, 36*mm]
    story.append(make_table(wifi_data, wifi_widths, extra_style=[
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#D6F0E0")),
    ]))
    story.append(Spacer(1, 8))

    story.append(P("2.4 功耗、供电、尺寸与机械适配", sH2))
    size_data = [
        ["平台", "官方/场景功耗", "供电与充电", "尺寸/重量", "机械结论"],
        ["XIAO ESP32-S3",
         "Webcam: 5V ~140 mA 均值\n峰值 ~347 mA\n深睡最低 14 µA",
         "USB-C 5V /\n3.7V Li-Po\n板载充电",
         "21×17.8×15 mm\n(含 Sense 扩展板)",
         "主板极小，但 15 mm\n堆叠厚度需拆分\n相机与主板"],
        ["ESP32-P4 + C6",
         "整板 ~1 W 活跃\n(官方未给精确数据)",
         "USB-C 5V /\nLi 电池充电",
         "开发板非眼镜尺寸\n芯片可做定制窄板",
         "功耗偏高\n眼镜续航不理想"],
        ["RV1106 ★",
         "裸芯估算 ~0.1–0.3 W\n(设计用于电池安防相机)\nH.265 推流实测待测",
         "3.3V / 5V 系统\n外部 PMIC 供电\n(Luckfox 开发板有 USB-C)",
         "开发板: ~58×40 mm\nSoM Core1106: 30×30 mm\n裸芯片: ~10–15 mm SiP",
         "开发板验证用\nSoM 可焊接到窄板\n裸芯片适配最终镜腿"],
    ]
    size_widths = [22*mm, 40*mm, 34*mm, 36*mm, 34*mm]
    story.append(make_table(size_data, size_widths, extra_style=[
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#D6F0E0")),
    ]))
    story.append(P(
        "注：RV1106 的 ~0.1–0.3 W 是基于芯片规格推算的估算值，需在 Luckfox 开发板上实测"
        "（H.265 推流 + NPU 运行 + WiFi 发送的组合场景）。", sNote))
    story.append(PageBreak())

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 视频管道带宽分析
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(page_header("视频管道带宽分析"))
    story.append(P("3. 视频管道带宽与延迟分析", sH1))
    story.append(section_rule())

    story.append(P("3.1 三种方案带宽与视频能力对比", sH2))
    bw_data = [
        ["", "ESP32-S3", "ESP32-P4 + C6", "RV1106 ★"],
        ["实际 WiFi 带宽",    "1.6–10 Mbps\n(极不稳定)", "~36 Mbps\n(SDIO 瓶颈)", "数十 Mbps\n(充裕)"],
        ["最高可用分辨率",    "VGA (640×480)",          "1080p (1920×1080)",       "5 MP (2592×1944)"],
        ["最高 fps",          "25–30 fps @ VGA",        "30 fps @ 1080p",          "30 fps @ 5 MP"],
        ["1080p30 码率",      "❌ 不可行\n(需 15–50 Mbps)", "4–8 Mbps (H.264)",    "2–5 Mbps (H.265)\n4–8 Mbps (H.264)"],
        ["结果模式码率",      "❌ 无 NPU",              "❌ 无 NPU",               "~10–100 kbps\n(NPU 检测后发坐标)"],
        ["WiFi/BLE 冲突",     "❌ 共享天线\n损失 30–50%", "✅ 独立芯片",           "✅ 无冲突"],
        ["视频压缩格式",      "MJPEG only",             "H.264",                   "H.264 + H.265"],
        ["端到端延迟目标",    "❌ 帧序列高延迟",        "可达 <150 ms",            "目标 <150 ms\n(Phase 0 验证)"],
    ]
    bw_widths = [36*mm, 42*mm, 42*mm, 46*mm]
    story.append(make_table(bw_data, bw_widths, extra_style=[
        ('BACKGROUND', (3,0), (3,-1), colors.HexColor("#EBF7EE")),
        ('BACKGROUND', (0,0), (0,-1), DARK_BLUE),
        ('TEXTCOLOR',  (0,0), (0,-1), WHITE),
    ]))
    story.append(Spacer(1, 8))

    story.append(P("3.2 为什么 H.265 是决定性的", sH2))
    story.append(P(
        "1080p30 的未压缩 YUV420 码率约为 <b>1 Gbps</b>，任何无线接口都无法直接传输。"
        "压缩是唯一出路，而压缩效率决定了系统能否运行。", sBody))
    codec_data = [
        ["编码方式", "1080p30 典型码率", "RV1106 硬件支持", "结论"],
        ["未压缩 YUV420", "~1,000 Mbps",   "—",   "完全不可行"],
        ["MJPEG (帧内)", "~30–50 Mbps",    "否",   "ESP32-S3 极限，WiFi 不够"],
        ["H.264 (帧间)", "~4–8 Mbps",      "✅ 是", "可行，P4+C6 使用此方案"],
        ["H.265 (帧间)", "~2–5 Mbps",      "✅ 是", "最优解，RV1106 默认方案"],
        ["结果模式 (NPU)", "~0.01–0.1 Mbps","✅ 是","终极解，只传检测结果"],
    ]
    codec_widths = [40*mm, 36*mm, 36*mm, 54*mm]
    story.append(make_table(codec_data, codec_widths, extra_style=[
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor("#D6F0E0")),
        ('BACKGROUND', (0,5), (-1,5), colors.HexColor("#C8F0D6")),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#FFE8E8")),
        ('BACKGROUND', (0,2), (-1,2), colors.HexColor("#FFF0E0")),
    ]))
    story.append(Spacer(1, 8))

    story.append(P("3.3 延迟拆解", sH2))
    story.append(P(
        "Glass-to-glass 延迟目标：<b>&lt;150 ms</b>（Phase 0 验证目标）；"
        "头锁 AR 模式（画面跟随头部移动）需 <b>&lt;20 ms</b>。", sBody))
    lat_data = [
        ["环节", "典型延迟", "RV1106 可优化点"],
        ["相机曝光 + 读出", "~5–15 ms", "选低延迟 MIPI 传感器（1/30s 曝光 = 33ms 上限）"],
        ["ISP 处理",          "~5 ms",    "RV1106 ISP 流水线并行，不阻塞编码"],
        ["H.265 硬件编码",    "~5–15 ms", "RV1106 硬件编码，不占 CPU"],
        ["WiFi 传输 (局域网)", "~5–20 ms", "2–5 Mbps @ 802.11ax，每帧 ~67–165 KB"],
        ["手机解码 + 渲染",   "~10–30 ms", "手机硬解 H.265 可用"],
        ["合计估算",          "~30–80 ms", "Phase 0 目标：实测 <150 ms"],
    ]
    lat_widths = [40*mm, 28*mm, COL - 68*mm]
    story.append(make_table(lat_data, lat_widths, extra_style=[
        ('BACKGROUND', (0,7), (-1,7), colors.HexColor("#D6F0E0")) if len(lat_data) > 7 else None,
        ('BACKGROUND', (0,6), (-1,6), colors.HexColor("#EBF7EE")),
    ]))
    story.append(PageBreak())

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 功耗续航预算
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(page_header("功耗与续航预算"))
    story.append(P("4. 功耗与续航预算", sH1))
    story.append(section_rule())
    story.append(P(
        "以下按 3.7V Li-Po、仅使用标称能量的 80% 进行估算，不含升降压损耗和电池老化。", sBody))
    bat_data = [
        ["平均功耗", "300 mAh 续航", "500 mAh 续航", "接近哪个场景"],
        ["0.10 W", "~8.9 h", "~14.8 h", "超低功耗待机 / 传感器触发模式"],
        ["0.30 W", "~3.0 h", "~4.9 h",  "RV1106 轻载估算目标（待实测）"],
        ["0.50 W", "~1.8 h", "~3.0 h",  "RV1106 H.265 推流 + NPU 估算上限"],
        ["1.00 W", "~0.9 h", "~1.5 h",  "ESP32-P4+C6 整板水平"],
        ["2.25 W", "~0.4 h", "~0.7 h",  "MaixCAM 全速 AI（中小电池无法支撑）"],
    ]
    bat_widths = [28*mm, 30*mm, 30*mm, COL - 88*mm]
    story.append(make_table(bat_data, bat_widths, extra_style=[
        ('BACKGROUND', (0,2), (-1,2), colors.HexColor("#EBF7EE")),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#D6F0E0")),
    ]))
    story.append(Spacer(1, 6))
    story.append(P(
        "对本项目的功耗目标：V0 开发板可接受 0.3–0.5 W；真正的眼镜版本目标 0.1–0.3 W，"
        "通过低帧率、事件触发、WiFi 按需唤醒实现。<b>实测值以 Luckfox Pico Ultra W 上的"
        "场景电流为准，不能只依赖估算。</b>", sBody))
    story.append(PageBreak())

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 详细分析 — ESP32-S3
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(page_header("详细分析 — ESP32-S3"))
    story.append(P("5. Seeed XIAO ESP32-S3 Sense（已淘汰）", sH1))
    story.append(section_rule())
    story.append(P("一句话定位", sH3))
    story.append(P(
        "起点平台：体积极小、开发生态好、BLE 控制可行，"
        "但<b>无硬件视频编码器</b>，MJPEG 码率远超 WiFi 承载能力，无法完成 1080p 实时 AR 推流。", sBody))

    s3_spec = [
        ["参数", "数值 / 说明"],
        ["处理器",    "ESP32-S3R8，双核 Xtensa LX7，最高 240 MHz；支持向量指令和 TinyML。"],
        ["运行内存",  "8 MB PSRAM；芯片内部 SRAM 供系统和实时任务。"],
        ["程序存储",  "8 MB Flash。"],
        ["外部存储",  "Sense 扩展板 microSD；官方支持 32 GB FAT/FAT32。"],
        ["摄像头",    "OV3660 2048×1536 (~3 MP)，DVP 并行接口，可拆卸。"],
        ["视频编码",  "❌ 无硬件编码器——只能 MJPEG（每帧独立 JPEG，无帧间压缩）。"],
        ["无线",      "2.4 GHz WiFi 802.11b/g/n；BLE 5.0 / Mesh；共用天线（BLE 激活时 WiFi 降速 30–50%）。"],
        ["有线传输",  "USB Full-Speed 12 Mbps；UART、I2C、I2S、SPI。"],
        ["功耗",      "Webcam 场景：5V ~140 mA 均值，采图峰值 ~347 mA；深睡最低 14 µA。"],
        ["尺寸",      "主板 21×17.8 mm；含 Sense 扩展板约 21×17.8×15 mm。"],
        ["供电",      "USB-C 5V 或单节 Li-Po ~3.7V；板载充电管理。"],
        ["软件",      "Arduino / ESP-IDF / MicroPython；TensorFlow Lite Micro / Edge Impulse。"],
    ]
    story.append(make_table(s3_spec, [38*mm, COL - 38*mm]))
    story.append(Spacer(1, 6))

    story.append(P("淘汰原因（视频管道角度）", sH3))
    story.append(bullet("无硬件编码器：MJPEG 在 VGA 30fps 需 ~5–8 Mbps，1080p30 需 30–50 Mbps，超出 WiFi 实际吞吐上限。"))
    story.append(bullet("WiFi 实测仅 1.6–10 Mbps 且极不稳定；BLE 同时激活时进一步下降。"))
    story.append(bullet("8 MB PSRAM 不足以同时容纳视频帧缓冲、AI 模型权重和 WiFi 栈。"))
    story.append(Spacer(1, 4))
    story.append(P("保留价值", sH3))
    story.append(bullet("BLE 命令通道（手机 → 眼镜）在本方案中仍由 RV1106 内置 BLE 5.2 承担，逻辑相通。"))
    story.append(bullet("ESP-IDF / Arduino 上已验证的传感器驱动代码可部分迁移。"))
    story.append(PageBreak())

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 详细分析 — ESP32-P4 + C6
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(page_header("详细分析 — ESP32-P4 + C6"))
    story.append(P("6. ESP32-P4 + ESP32-C6（已评估）", sH1))
    story.append(section_rule())
    story.append(P("一句话定位", sH3))
    story.append(P(
        "强力的两芯片方案：P4 负责摄像头和 H.264 硬件编码，C6 作为专用 WiFi 6 无线 Modem，"
        "解决了 ESP32-S3 的全部三个瓶颈。但无 H.265、无 NPU、~1 W 功耗，不是最终选型。", sBody))

    p4_spec = [
        ["参数", "数值 / 说明"],
        ["P4 处理器",  "双核 RISC-V，最高 400 MHz + 低功耗协处理器核。"],
        ["运行内存",   "最高 32 MB PSRAM（芯片支持）；开发板依配置。"],
        ["摄像头接口", "MIPI-CSI 2-lane + 片内 ISP；亦兼容 DVP。"],
        ["显示接口",   "MIPI-DSI 2-lane（可驱动小型显示屏）。"],
        ["视频编码",   "✅ 硬件 H.264，最高 1080p @ 30 fps；❌ 无 H.265；无法硬件解码。"],
        ["AI",         "AI 指令加速（向量运算）；❌ 无独立 NPU，复杂目标检测受 CPU 限制。"],
        ["C6 无线",    "WiFi 6 (802.11ax, 2.4 GHz) + BLE 5；独立芯片，无与主处理器的频率竞争。"],
        ["P4↔C6 链路", "SDIO via ESP-Hosted；实测有效吞吐约 36 Mbps（C6 单核 CPU 为瓶颈）。"],
        ["功耗",       "整板估算 ~1 W 活跃（官方未给统一数据）；显著高于 RV1106。"],
        ["开发板",     "ESP32-P4-Function-EV-Board，约 ¥400 / $55；板尺寸不适合直接装眼镜。"],
        ["软件",       "ESP-IDF；ESP-Hosted 框架（C6 作为 WiFi Modem）；Arduino 有限支持。"],
    ]
    story.append(make_table(p4_spec, [38*mm, COL - 38*mm]))
    story.append(Spacer(1, 6))

    story.append(P("对比 RV1106 的差距", sH3))
    story.append(bullet("无 H.265：同质量视频码率约为 RV1106 H.265 的 2 倍，消耗更多 WiFi 带宽和存储。"))
    story.append(bullet("无 NPU：无法做设备端目标检测，必须传输视频帧才能在手机侧推理，带宽需求高。"))
    story.append(bullet("功耗 ~1 W vs RV1106 ~0.1–0.3 W：电池续航仅约 1/3–1/5。"))
    story.append(bullet("ESP-Hosted 生态仅限 Espressif 芯片，不能直接换用更好的无线 Modem 芯片。"))
    story.append(Spacer(1, 4))
    story.append(P("保留价值", sH3))
    story.append(bullet("SDIO + ESP-Hosted 的两芯片无线模型为未来自定义 PCB 提供参考架构。"))
    story.append(bullet("若未来需要 MIPI-DSI 驱动小型 LCD，P4 的 DSI 接口有参考价值。"))
    story.append(PageBreak())

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 详细分析 — RV1106
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(page_header("详细分析 — RV1106（已选定）"))
    story.append(P("7. Rockchip RV1106 / Luckfox Pico Ultra W（已选定）", sH1))
    story.append(section_rule())
    story.append(P("一句话定位", sH3))
    story.append(P(
        "本项目选定平台：Linux 摄像头 SoC，同类价位中最佳的视频压缩（H.265）和 AI 推理（NPU）组合，"
        "低功耗，软件生态成熟，尺寸路线从开发板到裸芯片全覆盖。", sBody))

    rv_spec = [
        ["参数", "数值 / 说明"],
        ["处理器",    "ARM Cortex-A7 ~1 GHz + RISC-V 低功耗协处理器；可运行完整 Linux（Buildroot / Ubuntu）。"],
        ["AI / NPU",  "~0.5–1 TOPS NPU（INT8）；支持 RKNN 运行时；可实时运行 YOLOv5n / MobileNetV2 目标检测。"],
        ["运行内存",  "256 MB DDR3L（板载）；系统 + 相机 + 编码器 + NPU 约占 80–120 MB，用户可用 ~130 MB。"],
        ["板载存储",  "8 GB eMMC（板载，非 microSD）；存放 Linux 系统、模型、日志；写入寿命优于 SD 卡。"],
        ["摄像头接口","MIPI-CSI 2-lane + 片内 ISP（自动曝光、白平衡、降噪）；支持最高 5 MP 传感器。"],
        ["视频编码",  "✅ 硬件 H.264 + H.265（HEVC）；最高 5 MP @ 30 fps；ISP → 编码器全硬件流水线。"],
        ["显示接口",  "RGB-LCD（适合小型 LCD）；⚠️ 不直接支持 AR 微显示器（需外部驱动 IC）。"],
        ["无线",      "板载 WiFi 6 (802.11ax, 2.4 GHz) + BLE 5.2；独立射频，无 WiFi/BLE 冲突。"],
        ["有线传输",  "USB 2.0 OTG High-Speed；UART、I2C、SPI、GPIO；PWM。"],
        ["功耗",      "芯片设计功耗 ~0.1–0.3 W（估算，待 Luckfox 实测）；为电池安防相机设计。"],
        ["开发板",    "Luckfox Pico Ultra W：约 ¥220–320 / $30–45；58×40 mm；USB-C 供电；WiFi 天线内置。"],
        ["SoM",       "Core1106：30×30 mm 邮票孔焊接模块；去掉开发板多余接口后嵌入定制 PCB。"],
        ["软件",      "V4L2 摄像头、GStreamer 推流、RKMPP 硬件编码、RKNN NPU 运行时、OpenCV、RTSP；"
                      "Buildroot（精简）或 Ubuntu（易开发）可选。"],
        ["生态",      "Luckfox / Rockchip 官方 SDK；资料完整程度低于树莓派，但远优于定制 FPGA。"],
    ]
    story.append(make_table(rv_spec, [30*mm, COL - 30*mm]))
    story.append(Spacer(1, 6))

    story.append(P("选定理由（视频管道角度）", sH3))
    story.append(bullet(
        "<b>H.265 编码器</b>：1080p30 仅需 2–5 Mbps，相比 ESP32-S3 MJPEG 节省 6–15 倍带宽，"
        "相比 P4+C6 H.264 节省 ~40%。"))
    story.append(bullet(
        "<b>NPU 结果模式</b>：弹道追踪、球体检测全在设备端完成，BLE 发送坐标 ~kbps，"
        "WiFi 完全空出来或关闭，电池续航大幅提升。"))
    story.append(bullet(
        "<b>低功耗</b>：~0.1–0.3 W 设计目标使 300 mAh 电池可支撑约 3–9 h，"
        "接近实际运动场景（一轮高尔夫 ~4–5 h）。"))
    story.append(bullet(
        "<b>完整 Linux</b>：标准摄像头/推流/AI 工具链开箱即用；"
        "调试方法和文档资源远多于裸 MCU 方案。"))
    story.append(bullet(
        "<b>明确的尺寸路线</b>：开发板（验证）→ Core1106 SoM 30×30 mm（V1 原型）"
        "→ 裸芯片 ~10–15 mm SiP（量产镜腿形态）。"))
    story.append(Spacer(1, 4))

    story.append(P("限制与风险", sH3))
    story.append(bullet("单 CPU 核（Cortex-A7）：H.265 编码 + NPU + WiFi + Linux 同时运行可能饱和，需做负载测试。"))
    story.append(bullet("RGB-LCD 显示接口：AR 微显示器（硅基 OLED / DLP）通常需要额外 MIPI-DSI 或 SPI 驱动 IC，需验证。"))
    story.append(bullet("文档质量：Luckfox/Rockchip 中文社区资料足够，但英文文档不如树莓派完整。"))
    story.append(bullet("启动时间：Linux 需 3–8 秒启动，不适合需要毫秒级上电响应的场景；MCU 辅助板可缓解。"))
    story.append(PageBreak())

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 分阶段开发路线
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(page_header("分阶段开发路线"))
    story.append(P("8. 分阶段开发路线", sH1))
    story.append(section_rule())

    phase_data = [
        ["阶段", "目标", "关键指标", "工具 / 硬件"],
        ["Phase 0\n等板期间",
         "本地算法验证（无需开发板）",
         "弹道模型误差 <5%\n球体检测 F1 >0.7（静态视频）",
         "MacBook + prototype/.venv\ntrajectory.py / ball_detect.py"],
        ["Phase 0\n收板后",
         "H.265 推流延迟基准测试",
         "1080p30 H.265 @ <5 Mbps\nGlass-to-glass 延迟 <150 ms",
         "Luckfox Pico Ultra W\nGStreamer + RKMPP\nRTSP → 手机播放"],
        ["Phase 1",
         "NPU 目标检测上板",
         "YOLOv5n 30fps @ 320×320\n端到端 <200 ms",
         "RKNN-Toolkit2 (Docker)\n模型转换 → .rknn 部署"],
        ["Phase 2",
         "结果模式：设备端检测 + 轻量传输",
         "BLE 发送坐标 <100 kbps\nWiFi 仅按需开启",
         "自定义 BLE 数据协议\n手机 App 接收坐标"],
        ["Phase 3",
         "SoM 集成到自制窄板",
         "Core1106 焊接到 <30×10 mm PCB\n电池续航实测 >3 h",
         "Core1106 SoM\nCustom rigid-flex PCB"],
        ["Phase 4",
         "AR 显示集成",
         "AR 覆盖层延迟 <20 ms\n（头锁模式）",
         "外部 MIPI/SPI 显示驱动 IC\n微显示器模块评估"],
    ]
    phase_widths = [22*mm, 44*mm, 48*mm, 52*mm]
    story.append(make_table(phase_data, phase_widths))
    story.append(Spacer(1, 8))

    story.append(P("Phase 0 成功标准（最近期目标）", sH2))
    story.append(P(
        "在 Luckfox Pico Ultra W 上通过 <b>GStreamer + RKMPP</b> 建立完整 H.265 推流管道，"
        "在局域网手机上实时播放，测量端到端延迟 <b>&lt;150 ms</b>，码率 <b>&lt;5 Mbps</b>。", sBody))

    cmd_data = [
        ["步骤", "命令（Luckfox 终端）"],
        ["1. 确认相机可见",
         "v4l2-ctl --list-devices"],
        ["2. 启动 H.265 RTSP 流",
         "gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw,width=1920,height=1080,framerate=30/1 ! "
         "mpph265enc ! rtph265pay ! udpsink host=<手机IP> port=5000"],
        ["3. 手机端播放（VLC）",
         "rtsp://<板IP>:8554/live 或 udp://@:5000"],
        ["4. 测量延迟",
         "用手机摄像头拍摄推流画面中的秒表，计算帧差即 glass-to-glass 延迟"],
    ]
    cmd_widths = [30*mm, COL - 30*mm]
    story.append(make_table(cmd_data, cmd_widths))
    story.append(Spacer(1, 8))

    story.append(P("等板期间可并行推进的工作", sH2))
    story.append(bullet("运行 trajectory.py：验证高尔夫弹道模型（已验证：巡回赛球手 260 码，业余选手 203 码）。"))
    story.append(bullet("运行 ball_detect.py：用手机拍摄的挥杆视频测试 OpenCV 检测 baseline。"))
    story.append(bullet("Docker 中安装 RKNN-Toolkit2：在模拟器上跑通 YOLOv5n 推理（无需实体板）。"))
    story.append(bullet("采购 MIPI-CSI 相机模块（推荐 SC3336 或 OV5647 可接 Luckfox）。"))
    story.append(PageBreak())

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 形态与尺寸
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(page_header("形态与尺寸"))
    story.append(P("9. 形态与尺寸", sH1))
    story.append(section_rule())

    form_data = [
        ["硬件形态", "尺寸", "用途", "机械可行性"],
        ["Luckfox Pico Ultra W\n（开发板）",
         "~58×40 mm",
         "Phase 0/1 功能验证；桌面台架测试",
         "不装眼镜；用于算法 / 延迟 / 功耗验证"],
        ["Core1106 SoM\n（邮票孔模块）",
         "30×30 mm\n（厚约 3–4 mm）",
         "V1 原型；焊接到自制 PCB",
         "可嵌入镜框背面或耳机臂顶端；需自制 PCB"],
        ["RV1106 裸芯片\n（SiP 封装）",
         "~10–15 mm",
         "量产镜腿形态",
         "配合 rigid-flex PCB 穿过铰链；与 Meta Ray-Ban 路线一致"],
    ]
    form_widths = [38*mm, 28*mm, 46*mm, COL - 112*mm]
    story.append(make_table(form_data, form_widths))
    story.append(Spacer(1, 6))

    story.append(P("参考：Meta Ray-Ban 拆解数据", sH2))
    story.append(bullet("总重：69 g；电池：960 mWh（左右两侧镜腿各含一块）。"))
    story.append(bullet("芯片：Qualcomm Snapdragon AR1 Gen 1（专用 AR 处理器）。"))
    story.append(bullet("PCB：rigid-flex，穿过铰链连接两侧镜腿。"))
    story.append(bullet("温升：铰链内最热点约 40–45°C（轻量级，无显示器 / 计算密度低）。"))
    story.append(bullet("结论：真正的『在镜腿里』方案必须使用 rigid-flex 和裸芯片，不是开发板。"))
    story.append(Spacer(1, 6))

    story.append(P("真正的尺寸瓶颈（不是 SoC）", sH2))
    story.append(P(
        "镜腿内部可用空间约 6–10 mm 宽，SoC 只是其中一个零件。"
        "真正决定眼镜笨重程度的是：", sBody))
    story.append(bullet("电池体积（能量密度决定续航，不能随意缩小）。"))
    story.append(bullet("光学模组（镜片、棱镜或波导占据大部分前框空间）。"))
    story.append(bullet("散热设计（无风扇散热需要铜箔、导热垫和足够的热扩散面积）。"))
    story.append(bullet("天线位置（WiFi / BLE 天线靠近金属铰链时需要净空区域）。"))
    story.append(PageBreak())

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 采购清单
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(page_header("采购清单"))
    story.append(P("10. 现阶段采购清单（可在中国采购）", sH1))
    story.append(section_rule())
    story.append(P("以下为 Phase 0/1 验证所需物料，均可从淘宝/京东/立创购买。", sBody))

    buy_data = [
        ["物料", "型号 / 规格", "参考价 (CNY)", "用途", "优先级"],
        ["开发板",      "Luckfox Pico Ultra W",           "¥220–320", "主控平台", "★ 立即购买"],
        ["MIPI 相机",   "SC3336（200万，适配 Luckfox）",  "¥30–60",   "视频输入", "★ 立即购买"],
        ["USB-C 线",    "5V 2A USB-C 数据线",             "¥10–20",   "供电/调试", "立即购买"],
        ["MicroSD",     "32 GB Class 10（备用存储）",      "¥20–40",   "临时数据存储", "可选"],
        ["Li-Po 电池",  "3.7V 300–500 mAh 带保护板",      "¥15–30",   "独立供电测试", "Phase 1"],
        ["散热铜箔",    "0.1 mm 导热铜箔 5×5 cm",         "¥5–15",    "芯片贴装散热", "Phase 1"],
    ]
    buy_widths = [26*mm, 44*mm, 24*mm, 34*mm, 28*mm]
    story.append(make_table(buy_data, buy_widths, extra_style=[
        ('BACKGROUND', (0,1), (-1,2), colors.HexColor("#EBF7EE")),
    ]))
    story.append(Spacer(1, 8))

    story.append(P("注意事项", sH2))
    story.append(bullet("Luckfox Pico Ultra W 必须购买含 WiFi 的版本（型号中含【W】），无 W 版本无板载无线。"))
    story.append(bullet("SC3336 是官方验证过的相机，OV5647 也可兼容但需检查 I2C 地址和驱动支持。"))
    story.append(bullet("电池在 Phase 0 台架测试中非必需——USB-C 直接供电即可；Phase 1 穿戴测试时再购。"))
    story.append(Spacer(1, 8))

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 风险与缓解措施
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    story.append(P("11. 风险与缓解措施", sH1))
    story.append(section_rule())
    risk_data = [
        ["风险", "概率", "影响", "缓解措施"],
        ["实测功耗超过估算（>0.5 W）",
         "中", "续航不足",
         "降低帧率至 15fps；关闭 WiFi 常开；NPU 结果模式下不传视频"],
        ["H.265 延迟超过 150 ms",
         "低–中", "AR 体验差",
         "调整编码器 GOP 和缓冲区大小；考虑 RTSP over TCP 换 UDP"],
        ["RV1106 CPU 饱和\n（H.265+NPU+Linux）",
         "中", "帧率下降 / 系统卡顿",
         "RKMPP 卸载编码到硬件；NPU 推理频率降至 10fps；非实时任务后台化"],
        ["AR 微显示器不支持 RGB-LCD",
         "高", "显示集成受阻",
         "Phase 2 前调研 MIPI-DSI 显示驱动 IC（如 SSD1963）；或选带 SPI/I2C 的微显示模块"],
        ["Luckfox 文档不完整",
         "低", "开发速度慢",
         "参考 Buildroot SDK；社区 GitHub issues；必要时用 UART 串口直接调试"],
    ]
    risk_widths = [44*mm, 16*mm, 22*mm, COL - 82*mm]
    story.append(make_table(risk_data, risk_widths))
    story.append(Spacer(1, 12))

    # 结尾
    story.append(HRFlowable(width="100%", thickness=1.2, color=DARK_BLUE,
                            spaceAfter=8, spaceBefore=4))
    story.append(P(
        "本报告基于公开规格和工程估算，所有功耗/延迟数据需在 Luckfox Pico Ultra W 实际场景下验证。"
        "版本 1.0 | 2026-06-23", sNote))

    return story


# ── 主函数 ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import os
    output_path = os.path.join(
        os.path.dirname(__file__),
        "AI眼镜主板选型与参数报告_RV1106_视频管道专项_2026-06-23.pdf"
    )
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=15*mm, rightMargin=15*mm,
        topMargin=15*mm, bottomMargin=15*mm,
        title="AI眼镜主板选型与参数报告 视频管道专项版",
        author="AR Sports Glasses Team",
    )
    story = build_story()
    doc.build(story)
    print(f"生成完成: {output_path}")
