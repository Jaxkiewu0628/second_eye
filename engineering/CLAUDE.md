# CLAUDE.md — 工程工作规范（engineering/ 专属）

作用范围：`engineering/` 文件夹。不修改 `business/`、`design/`、根目录（根目录 STATUS.md 的里程碑摘要除外）。

---

## 开局（每次对话必做）
1. `git pull` — 先拉取（CEO 在协作，可能有更新）
2. 读 `engineering/STATUS.md` — 工程单一事实源（不读根目录 STATUS.md）

## 改完后（每次必做，不用被提醒）
```
git pull && git add <changed files> && git commit -m "..." && git push
```
有 conflict 自己 merge，留最合理的版本。

---

## 工作方式
1. **先验证，后成文**：先上手 spike，不强制"设计先行"
2. **少产出文档**：对话里回答即可，明确要交付物才写文件
3. **结论靠测量**：标明"估算"vs"实测"；没板子用公开 benchmark 代替
4. **硬件先查证**：任何器件参数先查官方 datasheet / 论坛，不凭记忆揣测；查不到就说"未查证"
5. **评估要客观**：列代价、反方、"什么情况下结论反转"；不一味肯定现有方向

## 硬件调研标准
按 `engineering/hardware/docs/hardware_rnd_workflow.md` 执行。

## 约束
- Python 只装 `engineering/prototype/.venv/`，不动全局
- 对话用中文
- 大输出 → 重定向文件再 grep，不灌进上下文
