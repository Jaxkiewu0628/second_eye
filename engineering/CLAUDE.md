# CLAUDE.md — Second Eye 工程规范

> 工作目录：`engineering/`（从这里启动 Claude，本文件自动生效）

## 开局（每次对话必做）
1. `git pull` — 先拉取最新内容（CEO 在协作）
2. 读 `STATUS.md`（本目录下的，工程单一事实源）

## 改完后（每次必做，不用被提醒）
```
git pull
git add .          # 只 stage engineering/ 里的文件
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

repo 根目录其他文件夹（business/、design/）不归 Claude 管。
