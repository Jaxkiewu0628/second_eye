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

- **2026-07-01 [ENG]** — Full review complete. Organizing by what's locked vs. what needs a correction in `roadmap.md`.

  ---

  ### ✅ Confirmed — no changes needed

  **Functions (V1 → V3+):** Sequence confirmed. The key insight: these functions are **event-driven, not concurrent** — YOLO runs continuously in the background, everything else (voice commands, OCR, scene description) is triggered one at a time. Peak concurrent compute is ~1 TOPS (YOLO + one active task). Our chip has 3–6× headroom. All features through V3+ are feasible on the planned hardware.

  **Form factor — split-body locked 🟢:** Confirmed necessary and correct (from HO-002 analysis). Glasses frame ~30g target is achievable with camera + ToF + bone conduction + mic + ESP32-S3. No change needed.

  **Thermal:** Neck box has no thermal concern — natural convection in a large aluminium housing handles any SoC we'd use. This is not a risk for V1–V2.

  **V3+ integrated body direction:** Correct. Requires 3–5× efficiency improvement in chip technology. V3+ re-evaluation is the right call.

  ---

  ### ⚠️ Three corrections needed in `roadmap.md`

  **Correction 1 — Battery life figure is wrong (important)**

  The "5000mAh ≈ 13.7h" figure in the roadmap came from an earlier power estimate that turned out to be incorrect. Post-research revision:
  - Production SoC actual active power: ~2.8W (not the 0.7W used previously)
  - 5000mAh at ~3W total system → **~5–6h**, not 13.7h

  This is still borderline-acceptable (competitor EchoVision at $599 offers 6–9h with a charging case), but the number in the roadmap is materially wrong. Suggest updating to: "5000mAh ≈ 5–6h (V1 estimate); full-day target requires either ~8000mAh battery or charging case." Chip selection is not yet final — deferring to post-board-validation — so the exact figure will sharpen after we measure real power on the hardware.

  **Correction 2 — V2 wireless requires a hardware revision to the glasses frame**

  "无线 WiFi P2P (V2)" is not a software upgrade. The current glasses frame design streams camera data via MIPI cable directly to the neck box. The ESP32-S3 in the frame handles only wake-word detection and cannot stream camera video over WiFi. Making V2 truly wireless requires replacing the ESP32-S3 with a SoC that has both a MIPI camera interface and WiFi streaming capability — that's a new PCB for the glasses frame. Suggest adding a note to the V2 row: "glasses frame hardware rev required (MIPI + WiFi SoC)."

  **Correction 3 — OCR appears in both V1 and V1.5 (duplicate)**

  V1 lists "OCR 按需（免费 bonus）" and V1.5 lists "+ OCR 朗读" — these are the same feature (on-demand capture → OCR → TTS readout). Suggest: keep it in V1 as "OCR 按需触发", remove from V1.5 to avoid implying it's a new V1.5 addition.

  ---

  ### Chip / compute row: intentionally leaving vague for now

  We did a full chip R&D sweep and have two serious candidates for production. Deferring final selection until the validation board (arriving ~2026-07-01) gives us real power and performance measurements. The roadmap row "RK3576 验证 → RV1126B 量产" is fine as-is — just know that "RV1126B" may be revised after validation. Will send a separate handoff once we have board data.

  Ball in CEO to update `roadmap.md` with the three corrections above.

## Resolution / 结论
_（待 CEO 回填 roadmap.md 三处修正 → 归档。）_
