# HO-005 — 赌注1 技术验证:眼镜重量 + 续航(要技术证明,非估计) / Bet 1 tech proof: weight + battery

**📌 In a line / 一句话:** 请给"~35g 轻框 + 续航"的**有依据技术结果**(供电预算计算 + 零件重量分解),用来 close 产品走向赌注1——口头估计不算,要算式/依据。/ Need evidence-backed numbers (power-budget calc + per-part weight breakdown) to close product-bet 1; chat estimates don't count.

| Field / 字段 | Value / 值 |
|---|---|
| **From → To / 方向** | `CEO → ENG` |
| **State / 状态** | 🔧 IN PROGRESS |
| **Priority / 优先级** | normal(定产品方向用;不改 V1 排期) |
| **Created / 创建** | 2026-07-01 |
| **Updated / 更新** | 2026-06-30 |
| **Related / 关联** | `business/strategy/product-bets.md`(Bet 1)· `handoff/HO-003`· `engineering/STATUS.md` |

**TL;DR (bilingual / 双语一句话)**
- **EN:** We're locking product direction. Bet 1 = "split-body glasses: ~35g light frame + neck box, battery good enough." Your chat answer ("5–6h has headroom", "25–39g doable") pointed the right way, but the CEO requires **engineering conclusions to be backed by proof, not a verbal one-liner**. Please turn those two numbers into evidence-backed results so we can close Bet 1.
- **中文:** 我们在定产品走向。赌注1 = "分体眼镜:~35g 轻框 + 颈挂盒,续航够用"。你上次聊天说的"5–6h 有提升空间""25–39g 可达"方向对,但 CEO 要求**重大工程结论必须有依据,不能凭口头**。请把那两个数用有依据的方式算出来,我们才好 close 赌注1。

## Context / 背景
CEO 在收敛"最有希望的一条产品走向",赌注1(形态/重量/续航)是地基。上次你在聊天里口头给了方向,但那只是初步信号、不算数。这条要的是**纸面也行、但要有算式/datasheet/结构依据**的结果。

## The ask / 需求(两个数,各要依据)
1. **续航——供电预算(power budget)**:在实际"忙时全速 / 闲时省电"的调度下,5000mAh 到底能撑几小时?
   - 请列:各工作状态(① 全速避障 ② 慢走巡航 ③ 静止/等待)的**功耗估算(mW/W)** + **各状态时间占比假设** → 算出实际续航**区间**。
   - **关键问题:能不能到 8h+(够全天)?** 还是现实就 5–6h、必须靠充电盒?
2. **重量——零件分解(weight breakdown)**:眼镜框里每个零件各多重,加起来落多少?
   - 逐项:IMX415 相机 / VL53L5CX ToF / 骨传导振子 / 双麦 / ESP32-S3 / 线缆接口 / 外壳+结构 → 各重量(datasheet 或结构估算)→ **总重**。
   - **关键问题:能否 ≤35g?** 还是现实是 40–45g?
3. 这两个数直接定卖点:**"~35g 最轻" + "够用一天"** 这两张牌能不能写进对外定位。

**Definition of Done / 完成标准**
- [ ] 续航:供电预算(各状态功耗 + 占比 → 小时数),给区间 + 明确能否 8h+
- [ ] 重量:眼镜框零件重量分解 → 总重 + 明确能否 ≤35g
- [ ] 一句话结论:~35g / 8h+ 能否达到(能 / 不能 / 有条件)

## Constraints & non-goals / 约束与非目标
- **要有依据**(算式 / datasheet / 结构),不要拍脑袋;**纸面计算可以**,但标清哪些"待上板实测确认"。
- **非目标**:不改 V1 排期。这是定产品方向用的输入,不是工程任务变更。

## References / 参考
- `business/strategy/product-bets.md` — Bet 1(要 close 的赌注)
- `handoff/HO-003-roadmap-review.md` — 续航 5–6h 修正的来源(你之前的分析)
- `engineering/STATUS.md` — 架构图 + 已验证的功耗/性能数据

## Thread / 对话线
- **2026-07-01 [CEO]** — 上次聊天你给的方向对,但要落成**有依据的数**我们才好拍板。续航供电预算 + 重量分解,辛苦给一下,纸面先行、标清待实测项。

- **2026-06-30 [ENG]** — Done. Both numbers below are **paper calculations** (datasheet + structural estimates); items marked ⏳ need on-board confirmation once the validation board arrives (~2026-07-01). **Architecture note:** since the last chat, we did a chip R&D sweep and the glasses-frame MCU has moved from ESP32-S3 to a **Rockchip RV1106G3 module (Luckfox Core1106 SOM)** — RV1106G3 has a native MIPI-CSI camera interface + H.265 encoder + on-board WiFi/BT (AIC8800DC), which the ESP32-S3 lacks. The numbers below already reflect the RV1106G3 design. (RV1126B stays in the neck box for YOLO inference.)

  ---

  ### 1. Weight — glasses-frame breakdown

  | Component | Weight | Basis |
  |---|---|---|
  | IMX415 camera module | 3 g | compact module estimate |
  | VL53L5CX ToF + PCB | 0.5 g | ST datasheet (6.4×3.6×1.5 mm) |
  | Bone-conduction transducer | 3 g | small electromagnetic type |
  | 2× PDM mics | 0.4 g | MEMS mic × 2 |
  | **Core1106 SOM (RV1106G3 + AIC8800DC, 30×30 mm)** | **3.5 g** | FR4 substrate ~2.4 g + components ~1 g |
  | Cable interface + PCB | 0.8 g | JST-ZH connector (power+data only) |
  | Internal flex PCB + wiring | 1.5 g | thin FPC estimate |
  | Frame (TR90) + PC lenses + hinges | 14 g | TR90 ~10 g + lenses ~4 g |
  | **Total** | **~26.7 g** | |

  Switching from ESP32-S3 to the RV1106G3 SOM adds only ~0.2 g vs. the earlier estimate (the SOM replaces both the ESP32 and part of the MIPI cable harness, so it nets out roughly flat).
  - **Target ~27 g; V1 hand-built prototype ~32–35 g; custom production design ~25–28 g.**
  - **Can we hit ≤35 g? YES.** ✅ ⏳ (final number after the prototype frame is built)

  ---

  ### 2. Battery — power budget (5000 mAh)

  Three real-world duty states with a weighted average. RV1106G3 draws more than the ESP32-S3 did, but its **AOV (Always-On Video)** low-power mode keeps the still/idle state cheap.

  | State | Scenario | Neck box (RV1126B) | Frame (RV1106G3) | Total | Time share |
  |---|---|---|---|---|---|
  | A — Full speed | YOLO 10–15 fps continuous | 2.8 W | 1.0 W | 3.8 W | 15% |
  | B — Cruise | YOLO 3–5 fps | 1.5 W | 0.6 W | 2.1 W | 50% |
  | C — Idle/still | IMU-gated, AOV low-power | 0.8 W | 0.1 W | 0.9 W | 35% |

  - **Weighted avg:** `0.15×3.8 + 0.50×2.1 + 0.35×0.9 = 1.93 W ≈ 1.9 W`
  - **Usable energy:** `5000 mAh × 3.7 V × 0.88 (DC-DC) × 0.90 (usable SoC) × 0.98 (aging) = 14.4 Wh`
  - **Typical runtime:** `14.4 / 1.9 = 7.6 h` ⏳
  - **Worst case (continuous full speed):** `14.4 / 3.8 = 3.8 h`

  **Can we hit 8h+? Borderline — typical use lands ~7.5 h, not a guaranteed 8h.** The earlier chat figure of "5–6 h" was the worst-case (no scheduling); with the IMU/AOV duty cycling we get ~7.5 h typical. For external messaging I'd say **"all-day with the charging case; ~7–8 h on a single charge"** rather than claiming a flat 8h. ⏳ (real power numbers after board validation may move this ±0.5 h either way.)

  ---

  ### One-line conclusion
  - **≤35 g:** **YES** — realistic ~27 g (V1 prototype ~32–35 g). ✅
  - **8h+:** **conditional** — typical ~7.5 h, worst-case ~3.8 h; market it as "~7–8 h + charging case = all-day," not a hard 8h. 🟡
  - Both are **paper calcs**; ⏳-marked items get confirmed on the validation board (~2026-07-01).

## Resolution / 结论
_（待 ENG 技术证明 → CEO 据此 close 赌注1。）_
