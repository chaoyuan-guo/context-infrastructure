# Skills Index

本索引指向可复用的 Skills（技能）—— AI 可以调用的工具、流程和最佳实践。

- **想使用某个能力** → 浏览下方分类，找到对应的 skill 文件
- **想添加新 skill** → 参考现有文件格式，添加到对应分类

---

## 分类索引

### Workflow（工作流）

- [Web Article Scraper](./workflow_web_article_scraper.md) ✅ — Circle.so 等 SPA 社区帖子抓取，保存为 Markdown（含图片/链接/视频/评论）
- [Fetch LeetCode](./workflow_fetch_leetcode.md) ✅ — 从力扣中文站导出所有已通过题目（题目信息、提交记录、最近一次 AC 代码），输出为 Markdown

### BestPractice（最佳实践）

通用的最佳实践和经验教训。

- [AI 编程核心方法论](./bestpractice_ai_programming_mindset.md) ✅ — 70%问题、成功标准、可验证性
- [API Key 管理与调用](./bestpractice_api_key_management_1password_cli.md) ✅ — 使用 1Password CLI 安全管理密钥
- [AI 辅助调试诊断](./bestpractice_ai_debugging_diagnosis.md) ✅ — "代码改不好"的根因诊断决策树
- [AI 产品设计原则](./bestpractice_ai_product_design.md) ✅ — 线性聊天 vs 知识工作、感知规则解耦

---

## 如何添加你自己的 Skill

1. 参考现有 skill 文件的格式（元数据、核心说明、使用步骤、示例）
2. 以 `<category>_<name>.md` 命名（例如 `workflow_my_process.md`、`bestpractice_my_insight.md`）
3. 在 INDEX.md 对应分类下添加一行

Skill 格式参考（最简版）：
```markdown
# Skill: 名称

## When to Use
什么情况下触发这个 skill

## Prerequisites
需要什么工具/配置

## 步骤
1. 步骤一
2. 步骤二
```

## Progressive Disclosure

Skills 采用渐进式披露原则：
- **INDEX.md** 提供概览，快速定位
- **具体 skill 文件** 包含完整的操作步骤和示例
