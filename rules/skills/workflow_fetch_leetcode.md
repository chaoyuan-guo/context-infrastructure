# LeetCode 抓取技能 (Fetch LeetCode Skill)
## 1. 技能概览

`fetch-leetcode` 是一个用于抓取力扣中文站 AC 题目数据的 CLI 工具。所有确定性逻辑已经沉淀在 `tools/fetch-leetcode/` 中，包括：

- AC 题清单获取
- 题目详情抓取
- 全部提交记录抓取
- 最近一次 AC 代码抓取
- 断点续传与 cache
- `verify` 校验补抓
- `incremental` 增量更新

输出是一份完整 Markdown 快照，默认建议存放到 `formal_projects/leetcode/`。

### 1.1 何时使用

用户希望导出或同步自己的力扣刷题数据时使用，典型场景包括：

- 导出当前所有 AC 题目的完整记录
- 保存最近一次 AC 代码，避免只留在 LeetCode 平台
- 在已有导出文件基础上做日常增量同步
- 校验本地历史导出是否有遗漏或抓取失败的题目

### 1.2 触发建议

**直接执行**：
- 用户说 导出力扣题目
- 用户说 抓取 LeetCode 提交历史
- 用户说 生成我的 AC 题清单
- 用户说 更新 `formal_projects/leetcode/leetcode_submissions.md`

**优先选 incremental**：
- 已经存在上一版导出文件
- 用户说 同步最近新增提交
- 用户说 做增量更新

**优先选 verify**：
- 用户怀疑已有 cache 或导出结果有缺失
- 用户说 检查并补抓遗漏数据

---

## 2. 使用说明

### 2.1 核心命令
```bash
node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs \
    --output formal_projects/leetcode/leetcode_submissions.md
```

### 2.2 参数规范
- `--output <path>`：输出 Markdown 文件路径。默认 `./leetcode-cn-submitted-problems.md`。
- `--resume`：从 cache 断点续传。适合全量抓取中途中断后继续。
- `--verify`：与服务端逐题对比提交次数，只重抓有差异的题目。适合补抓和修复。
- `--incremental`：基于现有导出文件做增量更新，只重抓发生变化的题目，并自动补入新 AC 题。
- `--skip-code`：跳过最近一次 AC 代码抓取，只保留题目信息和提交记录。

约束：`--resume`、`--verify`、`--incremental` 三者互斥。

### 2.3 前置依赖
```bash
node --version
export LEETCODE_SESSION="<你的 session 值>"
```

`LEETCODE_SESSION` 获取方式：
- 登录 `https://leetcode.cn/`
- 浏览器开发者工具 → Application → Cookies
- 找到 `LEETCODE_SESSION` 的值

---

## 3. 标准工作流

1. **首次全量导出**：
   ```bash
   node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs \
       --output formal_projects/leetcode/leetcode_submissions.md
   ```

2. **日常增量同步**：
   ```bash
   node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs \
       --output formal_projects/leetcode/leetcode_submissions.md \
       --incremental
   ```
   这会读取现有导出文件头部的生成时间作为上次同步边界，再与服务端逐题对比提交次数，只刷新发生变化的题目。

3. **抓取中断后续跑**：
   ```bash
   node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs --resume
   ```

4. **校验并补抓**：
   ```bash
   node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs \
       --output formal_projects/leetcode/leetcode_submissions.md \
       --verify
   ```

5. **需要更快但不抓代码时**：
   ```bash
   node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs \
       --output formal_projects/leetcode/leetcode_submissions.md \
       --incremental \
       --skip-code
   ```

---

## 4. 数据口径与限制

- 数据口径以力扣中文站当前账号的 AC 题列表为准。
- 每道题保留：题目信息、全部提交记录、最近一次 AC 代码。
- `incremental` 通过服务端每题 `numSubmitted` 判断哪些题发生变化。
- `incremental` 能自动补入新 AC 题，也能刷新已有题的新提交和最新 AC 代码。
- `verify` 主要用于修复 cache 已覆盖范围内的数据差异；日常同步优先使用 `incremental`。
- 若代码接口被限流，个别题目可能显示 （暂无 AC 代码）。

---

## 5. 输出与缓存

- 推荐输出位置：`formal_projects/leetcode/leetcode_submissions.md`
- cache 路径：`tools/fetch-leetcode/cache/leetcode-fetch-cache.json`
- cache 中保存：AC 题清单、已抓取题目数据、生成时间、输出路径、抓取来源
- `incremental` 会优先复用与当前输出文件匹配的 cache
- 若 cache 不可用，会回退解析现有 markdown 作为基线

输出文件头部会包含：
- 生成时间
- AC 题目数
- 总提交数

---

## 6. 性能与稳定性

- 400+ 题全量抓取通常约 20 到 30 分钟
- 普通请求间隔约 300ms
- 代码抓取额外等待约 1000ms
- 并发数限制为 3
- 单次请求失败最多重试 4 次，并使用指数退避

---

**版本**: 1.1.0
**最后更新**: 2026-04-18
