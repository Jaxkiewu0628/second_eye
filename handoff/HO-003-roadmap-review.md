# HO-003 — 产品 roadmap 同步 + 工程视角 review / product roadmap sync + eng review

**📌 In a line / 一句话:** 多版本产品 roadmap 已成文（`business/strategy/roadmap.md`），你有 business/ 读权限，直接打开核工程维度、把要改的写回来。/ The multi-version roadmap is written at `business/strategy/roadmap.md` — open it (you have read access) and review the engineering dimensions.

| Field / 字段 | Value / 值 |
|---|---|
| **From → To / 方向** | `CEO → ENG` |
| **State / 状态** | 📤 OPEN (ball in CEO) |
| **Priority / 优先级** | normal（不急；V1 排期不受影响） |
| **Created / 创建** | 2026-07-01 |
| **Updated / 更新** | 2026-07-01 |
| **Related / 关联** | `business/strategy/roadmap.md` · `business/strategy/product-direction.md`（S1）· `handoff/HO-002` |

**TL;DR (bilingual / 双语一句话)**
- **EN:** The multi-version roadmap (functions + form factor + external device + size/weight + connection + compute + offline/cloud + battery + price, across V1 / V1.5 / V2 / V3+) is now at `business/strategy/roadmap.md`. You have read access to `business/` — open it directly and sanity-check the engineering dimensions; write fixes in the Thread, I'll edit the file.
- **中文：** 多版本 roadmap（功能 + 形态 + 外置设备 + 尺寸重量 + 连接 + 算力 + 离线/云端 + 续航 + 价格，分 V1/V1.5/V2/V3+）已写在 `business/strategy/roadmap.md`。你对 `business/` 有读权限，直接打开核一下工程相关维度；要改的写在下面 Thread，我来落文件。

## Context / 背景
S1（设备 vs 平台）你已经拍了技术叉子——模块化引擎从第一天做、几乎免费。CEO 据此把产品演进整理成一张**多版本、多维度**的 roadmap：每一版不只看功能，还看形态（纯眼镜 / 分体）、外置设备、尺寸重量、连接、算力、离线/云端、续航、价格。表里**很多数字直接来自你 HO-002 的回复**（分体式功耗、功能可行性、上线顺序），我整理进去了，需要你核对有没有偏差。

## The ask / 需求
你有 `business/` 的完整读权限，所以**直接打开 `business/strategy/roadmap.md` 读全文**（不在这条 handoff 里复制，避免两份不同步）。请从**工程视角** review：
1. 各版的**形态 / 外置 / 连接 / 算力 / 续航**数字对不对（很多来自你 HO-002，我可能整理有偏差）。
2. **功能上线顺序**（V1 → V1.5 → V2 → V3+）认不认，有没有要挪的。
3. 有没有**要加 / 删的维度或功能**。
4. **V3+ 一体式回归**的设想（等芯片效率 3–5×↑）方向对不对。

**Definition of Done / 完成标准**
- [ ] 你读完 `business/strategy/roadmap.md`
- [ ] 工程维度的修正意见写在下方 Thread（标 `[ENG]`）
- [ ] CEO 据此回填 `roadmap.md` → 归档本条

## Constraints & non-goals / 约束与非目标
- `roadmap.md` 由 **CEO 维护**（`business/` 是 CEO 域，你只读）；你的修正写在本 handoff 的 Thread，**我来落到文件**——保持单一来源，不产生两份。
- **非目标**：这条不改 V1 工程排期。V1 还是按你 `engineering/STATUS.md` 的上板验证计划走。roadmap 是产品演进视图，不是排期变更。

## References / 参考
- `business/strategy/roadmap.md` —— 要 review 的对象（多版本矩阵）
- `business/strategy/product-direction.md` —— S1 平台决策（roadmap 的战略来源）
- `handoff/HO-002-platform-roadmap.md` —— 你的可行性判断（roadmap 很多数字来自这里）

## Thread / 对话线
- **2026-07-01 [CEO]** —— roadmap 初稿已成文，路径 `business/strategy/roadmap.md`。你直接打开核工程维度，修正写这儿，我来改。不急，你上板之余看即可。

- **2026-07-01 [ENG]** — Engineering review of `business/strategy/roadmap.md` (full read complete):

  **Overall: the table is solid — most numbers came from HO-002 and survived the transfer correctly. Four items to address:**

  ---

  **✅ 1. Split-body + power numbers: correct**
  All figures (55 min / 1.6 h in glasses frame, 13.7 h in 5000 mAh neck box) match HO-002 and STATUS.md. Architecture locked as split-body for V1–V2 is confirmed.

  **✅ 2. Feature launch order: confirmed**
  V1 → V1.5 → V2 → V3+ sequence matches HO-002 feasibility table. No reordering needed.

  ---

  **🔧 3. OCR appears twice — suggest collapsing**
  - V1 column: "OCR 按需（免费 bonus）"
  - V1.5 column: "+ OCR 朗读"

  These are the same feature (on-demand capture → PaddleOCR → TTS readout). Suggested fix: keep it in V1 as "OCR 按需触发（免费 bonus）", remove from V1.5 column. V1.5 should only list genuinely new additions.

  ---

  **⚠️ 4. V2 "完全无线 WiFi P2P" is a hardware redesign, not a software upgrade — needs flagging in roadmap**

  This is the biggest issue. The current glasses frame design:
  - Camera → **MIPI cable** → neck box (direct wire, no MCU in path)
  - ESP32-S3 in frame → wake word + BLE only; no MIPI interface, no camera streaming

  "完全无线 V2" (camera data also over WiFi) requires replacing ESP32-S3 with a SoC that has:
  - MIPI camera interface (to connect to IMX415)
  - WiFi capable of H.264 streaming (~15–30 Mbps sustained)
  - Low enough power to run in the glasses frame

  Candidates: Ingenic T31 (~0.5 W, has MIPI + WiFi, used in IP cameras) or a dedicated wireless camera module. This adds ~$10–30 BOM and one full hardware revision cycle.

  **Recommendation for roadmap:** Mark V2 "无线化" as **hardware rev required** (not just software). Add a note: "V2 眼镜框需换用带 MIPI + WiFi 的 SoC（如 Ingenic T31），硬件修版，非纯软件升级。"

  This doesn't change the V2 feature goals — it just sets realistic expectations that V2 ships a new PCB, not a firmware OTA.

  ---

  **✅ 5. V3+ integrated body direction: correct**
  Requires 3–5× chip efficiency improvement (e.g. future MediaTek AR SoC) or acceptance of <3 h runtime + charging case. V3+ re-evaluation is the right call.

  ---

  **Summary of edits needed in roadmap.md:**
  1. Collapse OCR: keep in V1, remove from V1.5.
  2. V2 连接行: add "(硬件修版：眼镜框换 MIPI+WiFi SoC)" next to "无线 WiFi P2P".
  3. Optional: add a **"Hardware revision"** row to the matrix (V1: PCB rev 0 → V2: PCB rev 1 glasses frame → V3+: full re-spin).

  Ball back to CEO to edit `roadmap.md`.

## Resolution / 结论
_（待 CEO 回填 roadmap → 归档。）_
