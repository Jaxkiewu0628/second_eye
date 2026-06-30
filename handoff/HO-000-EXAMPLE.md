<!--
⚠️ EXAMPLE ONLY — a filled specimen to show the format. NOT a live task; do not action.
⚠️ 仅为示例 —— 展示一条交接填好后长什么样。非真实任务，勿执行。
（真实交接：复制 _TEMPLATE.md → HO-<编号>-<slug>.md）
-->

> ⚠️ **EXAMPLE / 示例** — 展示格式用的填好样例，**非真实任务，勿执行**。真实交接请复制 `_TEMPLATE.md`。

# HO-000 — EXAMPLE：户外避障 demo 的验收标准 / outdoor obstacle-detection pass-bar

**📌 In a line / 一句话:** 【示例·非真实任务】交接填好后长什么样的格式样板。/ [Example, not a real task] a filled specimen showing how a handoff looks.

| Field / 字段 | Value / 值 |
|---|---|
| **From → To / 方向** | `CEO → ENG` |
| **State / 状态** | 🗄️ ARCHIVED（示例） |
| **Priority / 优先级** | high |
| **Created / 创建** | 2026-06-30 |
| **Updated / 更新** | 2026-06-30 |
| **Related / 关联** | `business/discovery/risk-blocks.md`（Block 1）· `engineering/STATUS.md` |

**TL;DR (bilingual / 双语一句话)**
- **EN:** Lock the measurable pass-bar the outdoor obstacle demo must hit (zero misses on drop-offs + torso-and-above), so "it works" is a number, not a vibe.
- **中文：** 定死户外避障 demo 必须达到的可量化验收标准（落差和齐胸以上障碍零漏检），让"能用"是一个数字，而不是感觉。

## Context / 背景
鲁班猫3 + ToF 上板后，第一个 demo 是"走真实人行道、按方向播报障碍"。这是 `risk-blocks.md` 的 **Block 1（避障信任）**：避障一旦漏检一次，用户就再也不信，永久退回白手杖。所以在上板前就得把"多可靠才算过"定成可测的数字——这条交接就是定这个标准。

## The ask / 需求
给出一份"逐障碍物计分"的测试协议，并在真实人行道上跑到达标。

**Definition of Done / 完成标准**
- [ ] 固定 ~500m 混合路线（下沿台阶、停放的自行车、A 字招牌、低垂树枝）
- [ ] **落差类**（下台阶、站台边缘）跨 ≥10 次：**零漏检**
- [ ] **齐胸以上**（杆子、招牌、低树枝）：**零漏检**（手杖扫不到——这正是我们存在的理由）
- [ ] 地面障碍（垃圾桶、地桩）：**>90% 检出**
- [ ] 误报 **< ~1 次/分钟**，且无"幽灵急停"
- [ ] 预警在步速下留 **≥1.5m** 反应距离
- [ ] 1 位 O&M 指导师试过后愿意让学员用

## Constraints & non-goals / 约束与非目标
- 骨传导播报，**不堵耳朵**（要留给回声定位和车流）。
- 定位为白手杖的**补充**，不是替代。
- 全程**离线**，端侧跑。
- 非目标：这条不碰阅读/场景描述，只管避障。

## References / 参考
- `business/discovery/risk-blocks.md` — Block 1 的 kill condition 和 instrument
- `engineering/STATUS.md` — 当前硬件/链路状态

## Thread / 对话线
- **2026-06-30 [CEO]** — 标准如上。先确认这些数字在 ToF 量程内是否现实；不现实就回 `❓ NEEDS INFO` 提出你的反案。
- **2026-06-30 [ENG]**（示例回复）— VL53L5CX 在 ~2–3m 内可覆盖落差和齐胸障碍；齐胸以上需确认眼镜俯仰角。地面障碍 >90% 可行。建议误报阈值上板后实测再定。状态置 `🔧 进行中`。

## Resolution / 结论
（示例）标准确认可行，落差/齐胸零漏检为硬门槛；误报阈值上板后用真实数据回填。后续：上板实测 → 若需要再开 **HO-00X** 跟踪调参。
