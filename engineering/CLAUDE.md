# CLAUDE.md — Second Eye 工程规范

> 工作目录：`engineering/`（从这里启动 Claude，本文件自动生效）

## 开局（每次对话必做）
1. `git pull` — 先拉取最新内容（CEO 在协作）
2. 读 `STATUS.md`（本目录下的，工程单一事实源）
3. 看 `../handoff/index.md` —— 有没有 CEO 发给你的交接（方向 `CEO → ENG`、状态 `📤 OPEN`）；有就把那条 `HO-***.md` 完整读完再开工

## 改完后（每次必做，不用被提醒）
```
git pull
git add .                 # stage engineering/ 里的文件
git add ../handoff/       # 如果你处理/回复了交接，连 HO-***.md 和 index.md 一起 stage
git commit -m "..."
git push
```
有 conflict 自己 merge，留最合理的版本。

---

## 项目背景
**Second Eye** — 帮助视障人士独立出行的 AI 眼镜。
摄像头 + 端侧 YOLO11n + 骨传导语音，完全离线。
等待鲁班猫3到货 → 上板验证完整链路。

## 工作方式
- 这是**硬件项目**，不套 TDD / code-review 等软件流程
- 先验证，后成文；给推荐+理由，不做穷举
- 对话用中文
- 硬件参数先查 datasheet，不凭记忆揣测；查不到就说"未查证"
- Python 只装 `prototype/.venv/`，不动全局
- 大输出 → 重定向文件再 grep

## 目录结构
```
engineering/          ← 你在这里
├── CLAUDE.md         ← 本文件
├── STATUS.md         ← 工程状态（每次读这个）
├── DEV_LOG.md
├── hardware/         ← 芯片文档、BOM、3D 模型
├── firmware/         ← C 代码
├── prototype/        ← 开发板脚本
├── tools/            ← RKNN 转换、生成脚本
├── app/              ← Flutter 伴侣 App
└── reference/        ← 2023 YCane 原始资料
```

repo 根目录的 `business/`、`design/` 不归你管（只读参考）。**例外：`../handoff/` 是共享交接通道 —— 发给 ENG 的交接你要读、要回、要一起 commit。**

## 协作交接（Handoff）—— `../handoff/`
和 CEO（`business/` 那边的 Claude）传递复杂任务的唯一通道，**零残留**：每条交接是一个自包含文件，接收方（哪怕全新会话）只凭该文件就能干活；结论写回文件，不留在对话里。
- **收：** 开局看 `../handoff/index.md`，把发给你的（`CEO → ENG`、`📤 OPEN`）那条 `HO-***.md` 读完再动手。
- **回：** 在该文件 `Thread` 段追加回复（标 `[ENG]` + 日期），更新状态（`🔧 进行中`／`❓ 需澄清`／`✅ 已完成`）；完成就填 `Resolution`，并在 `index.md` 把它挪到归档表。
- **发：** 要主动找 CEO，复制 `_TEMPLATE.md` → `HO-<编号>-<slug>.md`，写成自包含，状态 `📤 OPEN`，在 index 登记一行；正文用英文（CEO 的语言），TL;DR 中英双语。
- **提交：** `../handoff/` 是共享目录，发或改交接后 `git add ../handoff/` 一起提交。

状态：📝草稿 · 📤待处理 · 🔧进行中 · ❓需澄清 · ✅已完成 · 🗄️已归档。
