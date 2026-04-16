---
name: fetch-leetcode
description: 使用 LEETCODE_SESSION 调用力扣中文站接口，导出账号的已通过题目清单及详细信息（题目信息、提交记录、最近一次 AC 代码），输出为 Markdown 文件。
---

# Fetch LeetCode Skill

## 目标
在力扣中文站导出"已通过题目的详细信息清单"，输出格式包含：
- 题目基本信息（链接、难度、标签）
- 提交记录表格（包含所有提交：Accepted、Wrong Answer、Runtime Error 等）
- **最近一次 AC 代码**

## 前置条件
- 环境变量 `LEETCODE_SESSION` 已设置。
- 本机可执行 `node`。
- 运行时允许访问力扣中文站 `https://leetcode.cn/`。

## 执行方式

### 基本用法
```bash
node fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs
```

### 指定输出文件
```bash
node fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs --output ./my-leetcode.md
```

### 断点续传
抓取 400+ 题约需 20-30 分钟，若中途失败可使用断点续传：
```bash
node fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs --resume
```

### 跳过代码获取
若仅需题目信息而不需要代码（更快）：
```bash
node fetch-leetcode/scripts/export_leetcode_cn_submitted_problems.mjs --skip-code
```

## 输出格式示例

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
| 681222981 | 2025/11/28 08:44:34 CST | python | Accepted | 0 ms | 18.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target-num], i]
            hash_map[num] = i
        return []
```
```

## 工作流
1. 校验 `LEETCODE_SESSION` 是否存在。
2. 通过 REST API 获取用户所有 AC 题目的基础信息（题目 slug、题号等）。
3. 对每个 AC 题目：
   - 获取题目详情（中文标题、难度、标签）
   - 获取该题目的全部提交记录
   - 提取最近一次 AC 提交的代码
4. 结果按题号排序后写入 Markdown 文件；纯数字题号排前面，特殊编号（如"剑指 Offer"）随后输出。

## 数据口径
- 以力扣中文站用户的 AC 题目列表为准。
- 目标是与用户的实际 AC 题数保持一致。
- 每道题只保留最近一次 AC 的代码，不单独列出未通过的提交代码。

## 参数说明

| 参数 | 简写 | 说明 |
|------|------|------|
| `--output <path>` | `-o` | 指定输出文件路径，默认为 `./leetcode-cn-submitted-problems.md` |
| `--resume` | `-r` | 从缓存断点续传，避免重复抓取 |
| `--skip-code` | `-s` | 跳过代码获取，仅输出题目信息和提交记录（更快） |

## 频率控制
- 普通请求间隔约 `300ms`。
- 获取代码时额外等待 `1000ms` 以减少限流。
- 并发数限制为 `3`，过高会导致请求被拒绝。
- 单次请求失败时做最多 `4` 次重试，并使用指数退避策略（600ms → 1200ms → 2400ms...）。

这套频率对常见规模的已通过题列表通常足够快，也比无节制轮询更不容易触发限流。

## 缓存机制
- 每完成 10 道题自动保存缓存到 `./leetcode-fetch-cache.json`。
- 若中途失败，使用 `--resume` 可从缓存继续。
- 缓存包含题目列表和已抓取数据。
- 若缓存文件损坏，会自动忽略并重新开始。

## 输出校验
- 正常情况下，输出文件应包含账号的所有已通过题目。
- 每道题包含：题目信息、提交记录表格、最近一次 AC 代码。
- 若部分代码因限流无法获取，会显示"（暂无 AC 代码）"，并在控制台输出统计。
- **不输出**未通过的提交代码详情。

## 异常处理
- `LEETCODE_SESSION` 缺失时，直接报错并停止。
- 登录失效、接口返回错误、网络失败、接口限流时，保留明确错误信息，不输出伪造结果。
- 题目详情或提交记录获取失败时，使用基础信息继续，不阻断整个流程。
- 代码获取受限于接口限流，部分题目可能显示"暂无 AC 代码"。
