# CLAUDE.md — Second Eye 工作规范

## 开局（每次对话必做）
1. `git -C /Users/zizhengwu/Desktop/projects/2026_second_eye/ar-sports-glasses pull` — 先拉取（CEO 在协作）
2. 读 `engineering/STATUS.md` — 工程单一事实源

## 改完后（每次必做，不用被提醒）
```
git pull && git add <files> && git commit -m "..." && git push
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
- Python 只装 `engineering/prototype/.venv/`，不动全局
- 大输出 → 重定向文件再 grep

## 目录职责
| 路径 | 维护人 |
|------|--------|
| `engineering/` | Zizheng + Claude |
| `business/` | CEO |
| `design/` | 共同 |

详细工程规范 → `engineering/CLAUDE.md`
