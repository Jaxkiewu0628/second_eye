# HO-006 — 赌注4 可行性:功能集(必须有/最好有)× 自费价 × BOM / Bet 4 feasibility

**📌 In a line / 一句话:** 商业侧定了 V1 的「必须有/最好有」功能和自费价 $549–699,连同功能矩阵+价位表一起发你,请评:这套在 BOM ≤~$250、~35g 分体下能不能做、避障能否逼近 NOA。/ Business locked V1 must-have/nice-to-have functions + self-pay $549–699 (with the feature matrix & pricing list); ENG please assess buildability at BOM ≤~$250 / ~35g, avoidance approaching NOA.

| Field / 字段 | Value / 值 |
|---|---|
| **From → To / 方向** | `CEO → ENG` |
| **State / 状态** | 📤 OPEN |
| **Priority / 优先级** | normal(定产品方向用;不改 V1 排期) |
| **Created / 创建** | 2026-07-01 |
| **Updated / 更新** | 2026-07-01 |
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

## Resolution / 结论
_（待 ENG:BOM 粗估 + 避障 vs NOA + 可行性结论 → CEO 据此定自费价底线、close 赌注4 工程侧。）_
