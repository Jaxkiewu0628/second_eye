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
| ID | Title / 标题 | Dir / 方向 | State / 状态 | Ball in court / 当前在谁 | Updated | File |
|----|------|------|------|------|------|------|
| _–_ | _(none)_ | | | | | |

## Archive / 归档
| ID | Title / 标题 | Dir / 方向 | Closed | File |
|----|------|------|------|------|
| HO-001 | 交接通道连通性测试 / channel round-trip test | `CEO → ENG` | 2026-07-01 | [HO-001](HO-001-channel-test.md) |
