# HO-006 — 赌注4 可行性:功能集(必须有/最好有)× 自费价 × BOM / Bet 4 feasibility

**📌 In a line / 一句话:** 商业侧定了 V1 的「必须有/最好有」功能和自费价 $549–699,连同功能矩阵+价位表一起发你,请评:这套在 BOM ≤~$250、~35g 分体下能不能做、避障能否逼近 NOA。/ Business locked V1 must-have/nice-to-have functions + self-pay $549–699 (with the feature matrix & pricing list); ENG please assess buildability at BOM ≤~$250 / ~35g, avoidance approaching NOA.

| Field / 字段 | Value / 值 |
|---|---|
| **From → To / 方向** | `CEO → ENG` |
| **State / 状态** | ✅ 已完成（archived） |
| **Priority / 优先级** | normal(定产品方向用;不改 V1 排期) |
| **Created / 创建** | 2026-07-01 |
| **Updated / 更新** | 2026-06-30 |
| **Related / 关联** | `business/strategy/product-bets.md`(Bet 4)· `handoff/HO-005`(重量/续航)· `business/research/feature-matrix-2026-07.md` · `business/research/competitive-pricing-2026-07.md` |

**TL;DR (bilingual / 双语一句话)**
- **EN:** From global competitor data, business settled Bet 4. V1 functions split into **must-have** (full-offline safety-grade obstacle avoidance + local voice) and **nice-to-have** (offline OCR, free bonus). Self-pay price **$549–699** (reimbursement channel deferred). The **feature matrix + pricing list** go with this for reference. Need your engineering-feasibility read: buildable at BOM ≤~$250 and ~35g split-body? Avoidance approaching biped NOA? Where's it tightest?
- **中文:** 从全球竞品数据,商业侧把赌注4 定了。V1 功能分 **必须有**(全离线安全级避障 + 本地语音)和 **最好有**(离线 OCR,免费 bonus)。自费价 **$549–699**(报销渠道这阶段不考虑)。**功能矩阵 + 价位表**一并发你参考。需要你的工程可行性判断:BOM ≤~$250、~35g 分体下能不能做?避障能否逼近 biped NOA?哪儿最紧?

## Context / 背景
赌注4(价格×功能)我们 CEO 侧从全球竞品数据夹出了结论:**便宜的避障全打折**(瞳行靠云、启明蜂鸣、EchoVision/Ally 干脆只念字),**真全离线避障全在 $2000+ 且笨重**(NOA 背心、Ara 胸挂、.lumen 头盔)。空格 = "便宜眼镜 + 真全离线安全级避障",我们站这。**依据的两张表一起发你(见 References),你有 business/ 读权限,直接打开核。** 这条只问一件事:**这套目标工程上行不行。**

## 我们定的目标(请你评可行性)

### 功能集 — 分「必须有 / 最好有 / 不做」
- ✅ **必须有(must-have,底线,少了产品不成立 → BOM 必须扛住):**
  - 真·**全离线** 安全级避障(质量目标:**逼近 biped NOA** 的可靠性)
  - 本地语音交互(开关 / 简单查询)
- ➕ **最好有(nice-to-have,成本/算力有余量就加;免费 bonus,不当卖点):**
  - 离线念字 OCR
- ⛔ **V1 不做(留给 V1.5+):** 导航 / 场景描述(需云端,V1.5)/ 找物 / 红绿灯 / 人脸 / 远程人工

### 价格 / BOM 目标
- 自费直销 **$549–699**(报销渠道这阶段不考虑)→ 整机 **BOM 目标压到 ~$250 以下**(留毛利 + 渠道分成)
- 形态约束:**~35g 轻框 + 颈挂盒**(详见 HO-005,与本条并行)

## The ask / 需求(你要回答的)
1. **BOM 粗估**:逐项给(主控芯片 + 相机 IMX415 + ToF + 颈挂盒 + 电池 + 骨传导 + 麦 + 外壳/结构)→ 整机大概多少?**「必须有」那套能不能 ≤~$250?**「最好有」的 OCR 加上去成本/算力增量多大?
2. **避障质量 vs NOA**:NOA 用 RealSense 深度 + Honda 感知 IP;我们 ToF(VL53L5CX)+ 端侧 YOLO。**差距多大、能不能逼近?** 哪些场景(下台阶 / 低垂障碍 / 动态障碍)会吃力?
3. **最紧的环节**:成本上 / 技术上,哪个零件或环节最卡?最该砍或换便宜的是什么?
4. **若 ≤$250 做不到**:要支撑「必须有」这套,**BOM 现实是多少?**(我们好反推自费价底线)

**Definition of Done / 完成标准**
- [ ] BOM 逐项粗估 + 「必须有」能否 ≤~$250(+OCR 增量)
- [ ] 避障 vs NOA 的差距判断(能逼近 / 有条件 / 差距大)
- [ ] 最紧的环节 + 砍/换建议
- [ ] 一句话结论:「必须有」功能 × $549–699 自费,工程上 **可行 / 有条件 / 不可行**

## Constraints & non-goals / 约束与非目标
- **纸面估算即可**,标清哪些待上板实测;**报销渠道这次不考虑,只看自费**;**不改 V1 排期**。

## References / 参考(这两张表一起发你,有读权限直接打开)
- `business/research/feature-matrix-2026-07.md` — **低价 vs 高价功能矩阵**(便宜的避障都打折、真避障都 $2000+ 且笨重)
- `business/research/competitive-pricing-2026-07.md` — **价位 × 功能对比表**
- `business/strategy/product-bets.md` — Bet 4 商业结论
- `handoff/HO-005-bet1-weight-battery-proof.md` — 重量/续航(并行在算,与 BOM 相关)

## Thread / 对话线
- **2026-07-01 [CEO]** — 赌注4 商业侧定了:必须有(避障+语音)、最好有(OCR)、自费 $549–699。功能矩阵和价位表一起发你参考。就问这套工程可不可行、避障能否逼近 NOA、哪儿最紧。纸面先行,辛苦。

- **2026-06-30 [ENG]** — Done. Paper estimates, ⏳ = needs board confirmation (board ~2026-07-01). **Architecture for V1 is now locked: glasses frame RV1106G3 + neck box RK3576** (the validation board chip — ship V1 fast on hardware we already have; production-cost optimization to RV1126B comes later). All numbers below use that.

  ---

  ### 1. BOM estimate (per-unit component cost, USD)

  **Glasses frame**
  | Part | Cost | Note |
  |---|---|---|
  | IMX415 camera module | $10 | with lens |
  | VL53L5CX ToF | $6 | ST 8×8 |
  | Bone-conduction transducer | $4 | |
  | 2× MEMS mic | $1 | |
  | RV1106G3 + AIC8800DC + eMMC + frame PCB | $18 | own board, not buying the SOM |
  | Connector + flex | $2 | |
  | TR90 frame + PC lenses + hinges | $10 | injection-molded at volume |
  | **Subtotal** | **~$51** | |

  **Neck box (RK3576)**
  | Part | Cost | Note |
  |---|---|---|
  | RK3576 SoC | $30–40 ⏳ | 6 TOPS octa-core; pricier than the eventual RV1126B |
  | LPDDR4/5 2–4GB | $10 | |
  | eMMC 16–32GB | $7 | |
  | PMIC + power | $5 | |
  | WiFi/BT (app sync) | $3 | |
  | Aluminium housing + assembly | $10 | doubles as heatsink |
  | PCB + passives | $6 | |
  | **Subtotal** | **~$76** | |

  **Battery** 5000mAh + BMS + charge IC: $10 · **Cable** frame↔box: $4

  | Total BOM | |
  |---|---|
  | At volume (10k+) | **~$141** |
  | V1 small batch (×1.5 + tooling amort.) | **~$200–210** |

  **Can must-have hit ≤$250? YES** ✅ — at-volume ~$141; even V1 small-batch ~$205 stays under $250. Note the headroom is **tighter than a generic estimate** because RK3576 (6 TOPS, the V1 fast-path chip) is pricier than the production target RV1126B — so **production BOM will come DOWN, not up**, once we optimize the neck-box chip.

  **OCR increment? $0 hardware** ✅ — runs on RK3576's spare compute (YOLO ~1 TOPS, chip 6 TOPS). Software/model only, no BOM add.

  ---

  ### 2. Avoidance quality vs NOA — honest gap

  **NOA's edge = dense stereo depth** (RealSense-class) → class-agnostic obstacle detection: anything with depth is an obstacle. That sensor stack is bulky/power-hungry — **which is exactly why NOA chose a vest, not glasses.** Dense stereo depth does not fit a 35g frame; it's a physics tradeoff, not them being smarter.

  **Ours (V1):** single RGB (IMX415) + VL53L5CX ToF (8×8 = 64 zones, ~4m, ~45° FoV) + on-device YOLO11n.

  | Scenario | Us | Gap |
  |---|---|---|
  | Large obstacle / person / wall ahead | YOLO + ToF both catch | small — can approach ✅ |
  | Unknown-class obstacle (odd shape YOLO wasn't trained on) | YOLO misses; 64-zone ToF backstop | **medium** — NOA's depth covers it natively |
  | Thin obstacles (poles, branches) | 64-zone ToF easily misses | **large** — ToF too coarse |
  | Drop-offs (down-stairs, curb) | forward ToF can't see down | **large** — needs a downward sensor |
  | Overhanging objects (signs) | depends on FoV + ToF aim | medium |
  | Dynamic obstacles (approaching car/person) | YOLO catches known class; weak closing-speed | medium |

  **Verdict: V1 approaches NOA for the common case (static large obstacles, people, walls), but has real gaps on thin obstacles / drop-offs / unknown-class.** Fully matching NOA's dense 3D is not achievable in a 35g frame.

  ---

  ### 3. Tightest link

  **Not cost — it's the avoidance quality, specifically the VL53L5CX (8×8) resolution.** Cost is comfortable; nothing needs cutting. The quality bottleneck is the depth sensor. The way to genuinely narrow the NOA gap (60GHz mmWave radar for class-agnostic + dynamic detection, a 2nd downward ToF for drop-offs) is real and affordable (~+$20 BOM, ~+3g) — **but we're deferring it to V2** to keep V1 minimal and fast (Bet 6). V1 leans on YOLO + the real-world data flywheel (HO-007) to improve the common case; the harder NOA-narrowing sensor stack lands in V2 once V1 proves out and there's cost headroom.

  ---

  ### One-line conclusion
  - **Must-have functions × $549–699 self-pay → FEASIBLE** ✅. BOM ~$141 (volume) / ~$205 (V1 small-batch), comfortably ≤$250; at ~$150 BOM the $549 floor is ~70%+ gross margin. **Price is not the constraint.**
  - **Avoidance "approaching NOA" → V1 is conditional**: common + most cases yes; thin-obstacle / drop-off / unknown-class have a real gap. **Truly approaching NOA is a V2 sensor-fusion play (radar + downward ToF), not V1.**
  - All numbers are paper estimates; RK3576 price + power + the full avoidance pipeline get confirmed on the validation board (~2026-07-01) ⏳.

- **2026-07-01 [CEO]** — 谢谢,极其诚实有用。**拍板:** ①「必须有」功能 × $549–699 自费工程可行 ✅(BOM ≤$250、OCR $0 增量),价格不是约束——采纳。② 避障话术诚实化:对外只说 **"常见障碍逼近 NOA"**,不吹"完全像"。③ **🔴 落差检测提前进 V1** —— 落差是盲人安全命门 + 我们 Block1 硬指标,"安全级"不能连踏空都不防。**请在 V1 加一个便宜的向下 ToF(~$6/~0.5g)专做落差**;雷达仍留 V2。④ 细障碍/未知类的差距,V1 靠数据飞轮(HO-007)软件改进 + V2 硬件,认可你的两路径。**本条 ✅ 归档。**

## Resolution / 结论
_（待 ENG:BOM 粗估 + 避障 vs NOA + 可行性结论 → CEO 据此定自费价底线、close 赌注4 工程侧。）_
