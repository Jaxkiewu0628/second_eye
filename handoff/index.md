<!-- 中文在下 / English first -->
# Second Eye — Handoff Channel / 协作交接中心

> The shared **CEO ⇄ Engineering** channel — the one place complex tasks cross between `business/` (CEO, English) and `engineering/` (Jackie, 中文), **with zero residual**: every handoff is a self-contained file, so the receiver — even a brand-new Claude session — can act from that file alone, and outcomes are written back here, never left in chat.
>
> 共享的 **CEO ⇄ 工程** 通道 —— 复杂任务在 `business/`（CEO，英文）与 `engineering/`（Jackie，中文）之间传递的唯一入口，**零残留**：每条交接是一个自包含文件，接收方（哪怕全新的 Claude 会话）只凭该文件就能执行；结论写回文件，绝不遗留在对话里。

## How it works / 运作方式
1. **Sender** copies `_TEMPLATE.md` → `HO-<NNN>-<slug>.md`, fills it self-contained, sets state `📤 OPEN`, and adds a row to **Active** below. / **发送方** 复制 `_TEMPLATE.md` → `HO-<NNN>-<slug>.md`，写成自包含，状态设 `📤 OPEN`，并在下方 **进行中** 登记一行。
2. **Receiver** checks this index at the **start of every session** and reads any `📤 OPEN` item addressed to them, in full, before acting. / **接收方** 每次对话开局先看本索引，把发给自己的 `📤 OPEN` 条目完整读完再动手。
3. All back-and-forth lives in the file's **`Thread`** section (dated, tagged `[CEO]` / `[ENG]`) — not in chat. Update the **state** as it moves. / 所有来回都写在文件的 **`Thread`** 段（带日期、标 `[CEO]`／`[ENG]`）—— 不写在对话里。状态随进展更新。
4. When resolved, fill **`Resolution`**, set `✅ DONE`, and move the row to **Archive**. / 完成后填 **`Resolution`**，置 `✅ DONE`，把行移到 **归档**。

**Language / 语言:** write the body in the **receiver's** working language (CEO→ENG: **中文**; ENG→CEO: **English**). Always keep the one-line **TL;DR bilingual**. Frankie reads both. / 正文用 **接收方** 的语言（CEO→ENG 用 **中文**；ENG→CEO 用 **英文**）；TL;DR 永远 **中英双语**。

**Example / 示例:** see [`HO-000-EXAMPLE.md`](HO-000-EXAMPLE.md) — a filled specimen showing every section (not a live task). / 看 `HO-000-EXAMPLE.md`，一条填好的示例（非真实任务）。

**Title / 标题约定:** each handoff's H1 is a short label, and directly under it an **`In a line / 一句话`** field gives a crystal-clear one-sentence summary (subject + ask). That one-liner fills the **Summary** column here and the handoff log in `business/status.md` — so each numbered HO is obvious at a glance, without opening it. / 每条交接的 H1 是简短标签，紧跟一行 **`In a line / 一句话`** 给出一句话清楚总结（主题 + 要做什么）；这句填进本表 **Summary** 列和 `business/status.md` 的 handoff log，一眼就懂。

## States / 状态
| State | Meaning / 含义 |
|---|---|
| 📝 DRAFT | Being written, not yet sent / 起草中，未发送 |
| 📤 OPEN | Sent, waiting on receiver / 已发送，待接收方处理 |
| 🔧 IN PROGRESS | Receiver has acknowledged & is working / 已接手，进行中 |
| ❓ NEEDS INFO | Blocked on a question back to the sender / 卡在一个回问上 |
| ✅ DONE | Resolved, outcome captured in `Resolution` / 已解决，结论已记录 |
| 🗄️ ARCHIVED | Closed & filed (row in Archive) / 关闭归档 |

## Active / 进行中
| ID | Summary / 一句话 | Dir / 方向 | State / 状态 | Ball in court / 当前在谁 | Updated | File |
|----|------|------|------|------|------|------|
| HO-004 | S1 已定板 + 前瞻医疗扩张机会（FYI 老哥）/ S1 decided + forward medical opportunity | `CEO → ENG` | 📤 OPEN | **ENG** | 2026-07-01 | [HO-004](HO-004-s1-decided-medical-opportunity.md) |
| HO-003 | 多版本产品 roadmap 同步，请工程核维度（→ `business/strategy/roadmap.md`）/ multi-version roadmap sync + eng review | `CEO → ENG` | 📤 OPEN | **CEO** | 2026-07-01 | [HO-003](HO-003-roadmap-review.md) |

## Archive / 归档
| ID | Summary / 一句话 | Dir / 方向 | Closed | File |
|----|------|------|------|------|
| HO-001 | 通道往返测试 + 到货同步 / channel round-trip test + parts-arrival sync | `CEO → ENG` | 2026-07-01 | [HO-001](HO-001-channel-test.md) |
| HO-002 | S1 平台决策（已拍板 🟢 平台+freemium+守视障核心）/ S1 platform decision (decided) | `CEO → ENG` | 2026-07-01 | [HO-002](HO-002-platform-roadmap.md) |
