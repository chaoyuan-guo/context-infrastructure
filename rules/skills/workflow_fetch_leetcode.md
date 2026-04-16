# Skill: Fetch LeetCode（力扣提交历史导出）

## 元数据
- 类型: Workflow
- 适用场景: 从力扣中文站导出账号所有已通过题目的详细信息（题目信息、提交记录、最近一次 AC 代码），输出为 Markdown 文件
- 脚本路径: `tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs`
- 创建日期: 2026-04-16
- 依赖: Node.js（`node` 命令可用）、`LEETCODE_SESSION` 环境变量

## When to Use

用户希望导出自己的力扣刷题记录时触发。典型触发词：
- "导出力扣题目"、"抓取 LeetCode 提交历史"
- "生成我的 AC 题清单"
- "把力扣的代码存下来"

## Prerequisites

1. 获取 `LEETCODE_SESSION`：
   - 登录 `https://leetcode.cn/`
   - 浏览器开发者工具 → Application → Cookies → 找到 `LEETCODE_SESSION` 的值
2. 设置环境变量：
   ```bash
   export LEETCODE_SESSION="<你的 session 值>"
   ```
3. 确认 `node` 可用：
   ```bash
   node --version
   ```

## 执行步骤

### 基本用法（默认输出到当前目录）
```bash
node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs
```

### 指定输出路径
```bash
node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs \
  --output formal_projects/leetcode/submissions.md
```

### 断点续传（中途失败后继续）
```bash
node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs --resume
```

### 跳过代码获取（只要题目列表，更快）
```bash
node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs --skip-code
```

### 校验并补抓（verify 模式）
```bash
node tools/fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs --verify
```

与服务端对比每题提交次数，只重新抓取有差异的题目，最后重新生成 markdown。适合在初次全量抓取后，检查并补全遗漏或错误数据。

**注意：**
- verify 默认会重新抓取 AC 代码（与普通模式一致），加 `--skip-code` 可跳过
- verify 只能修复缓存中已有题目的数据差异；若缓存中缺少新 AC 的题目，需重新全量抓取

## 参数速查

| 参数 | 简写 | 说明 |
|------|------|------|
| `--output <path>` | `-o` | 输出文件路径，默认 `./leetcode-cn-submitted-problems.md` |
| `--resume` | `-r` | 从缓存断点续传 |
| `--skip-code` | `-s` | 跳过代码获取，仅输出题目信息和提交记录 |
| `--verify` | `-v` | 与服务端对比，补抓提交次数有差异的题目后重新生成 markdown |

## 输出格式

```markdown
# LeetCode 提交汇总

- 生成时间：2026/04/13 14:09:37 CST
- AC 题目数：441
- 总提交数：2283

## 1. 两数之和 (`two-sum`)

- 题目链接：https://leetcode.cn/problems/two-sum/
- 难度：Easy
- 标签：Array, Hash Table
- 总提交次数：2
- 最近提交时间：2025/11/30 15:07:18 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 681664260 | 2025/11/30 15:07:18 CST | python | Accepted | 0 ms | 18.6 MB |

### 最近一次 AC 代码
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...
```
```

## 性能与限制

- **耗时**：400+ 题约 20-30 分钟
- **频率控制**：请求间隔 300ms，获取代码时额外等待 1000ms，并发数限制为 3
- **重试策略**：单次失败最多重试 4 次，指数退避（600ms → 1200ms → 2400ms...）
- **缓存**：每完成 10 道题自动保存到 `./leetcode-fetch-cache.json`，`--resume` 可续传

## 输出校验

- 正常情况：输出文件包含账号所有已通过题目
- 若部分代码因限流无法获取，显示"（暂无 AC 代码）"
- 异常时保留明确错误信息，不输出伪造结果

## 存放位置建议

导出结果建议存放到：`formal_projects/leetcode/`
