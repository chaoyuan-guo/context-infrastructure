---
name: fetch-leetcode
description: 使用 LEETCODE_SESSION 调用力扣中文站接口，导出或增量同步账号的 AC 题目详细信息。
---

# Fetch LeetCode Skill

这个目录存放 `fetch-leetcode` 的工具实现。

workspace 级的完整 skill 真源在：`rules/skills/workflow_fetch_leetcode.md`

## 目录定位

- `scripts/export_leetcode_cn_submitted_problems.mjs`：CLI 主入口
- `cache/leetcode-fetch-cache.json`：抓取 cache
- `agents/openai.yaml`：工具元数据

## 使用入口

常用命令：

```bash
node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs \
  --output formal_projects/leetcode/leetcode_submissions.md \
  --incremental
```

详细的触发场景、参数语义、标准工作流和使用约束，请查看：

`rules/skills/workflow_fetch_leetcode.md`
