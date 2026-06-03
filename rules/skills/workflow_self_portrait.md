# 自画像

## 元数据

- **类型**: Workflow
- **产出**: 多维度认知画像 → `contexts/thought_review/cognitive_<YYYY-MM-DD>.md`
- **依赖**: [并行 Subagent 工作流](./workflow_parallel_subagents.md)
- **频率**: 冷启动：全量 session 数据。后续增量运行规则另文定义。

---

## 步骤

### Phase 1: 采样

```bash
python tools/export_opencode_sessions.py --sync
```

读取 `contexts/agent_traces/.export_manifest.json`，提取全部 session 的 display_title、path、created_at。

生成文件列表：

```bash
python3 -c "
import json
d = json.load(open('contexts/agent_traces/.export_manifest.json'))
for v in d['sessions'].values():
    print(f'contexts/agent_traces/{v[\"path\"]}')
" | sort > tmp/session_files.txt
```

统计时间分布和活跃度：

```bash
python3 << 'PYEOF'
import json, re
from collections import Counter

d = json.load(open('contexts/agent_traces/.export_manifest.json'))

# 按日期统计 session 数
dates = Counter()
for v in d['sessions'].values():
    m = re.search(r'(\d{2})(\d{2})(\d{2})/', v['path'])
    if m:
        yr, mo, dy = m.groups()
        dates[f"20{yr}-{mo}-{dy}"] += 1

print("每日 session 数 (>8 = 马拉松日):")
for day, cnt in sorted(dates.items()):
    tag = " <<<" if cnt > 8 else ""
    print(f"  {day}: {cnt}{tag}")

# 空窗期
all_days = sorted(dates.keys())
gaps = []
for i in range(1, len(all_days)):
    from datetime import date
    d1 = date.fromisoformat(all_days[i-1])
    d2 = date.fromisoformat(all_days[i])
    gap = (d2 - d1).days
    if gap > 1:
        gaps.append(f"  {all_days[i-1]} → {all_days[i]} 空 {gap-1} 天")
if gaps:
    print("\n空窗期:")
    for g in gaps:
        print(g)
PYEOF
```

**确定维度和查询词**：

1. 读取全部 display_title，归纳为 5~8 个话题类别
2. 从话题中提炼 3~5 个认知维度，每个维度命名并划定范围
3. 为每个维度生成 full-round 和 user-only 查询词，从该维度下实际话题的标题和关键词中提炼

对每个维度跑语义检索，用命中结果补充聚类、形成该维度的采样列表：

```bash
# Full-round
python tools/semantic_search/main.py --file-list tmp/session_files.txt \
    --query "<查询词>" --top-k 15 --cache-dir .knowledge_cache

# User-only
python tools/semantic_search/main.py --file-list tmp/session_files.txt \
    --query "<查询词>" --top-k 15 --user-only --cache-dir .knowledge_cache_user_only
```

合并规则：
1. 聚类和检索都命中的 → 确认
2. 检索命中但聚类没覆盖的 → 按分数挑 top 3 补充
3. 聚类核心但检索完全未命中的 → 降优先级

**Phase 1 产出**：各维度的名称和采样文件列表。

### Phase 2: 并行深度采样

为每个维度启动 1 个 explore 子 agent，拿到该维度的采样列表后并行执行。

用 `call_omo_agent(subagent_type="explore", run_in_background=true)` 启动，prompt（`[DIMENSION]` = 维度名，`[PATHS]` = 采样文件绝对路径列表）：

```
You are analyzing the cognitive profile of user chaoyuan by reading their AI session logs.
Focus: [DIMENSION].

Read these files:
[PATHS]

For each session, first classify: emotional (feelings, validation, emotional processing) or rational (reasoning, debate, system design, technical problem-solving)?

Then extract patterns. Apply the framework that matches:
- Emotional → triggers, defense mechanisms, what need is being expressed, avoidance
- Rational → reasoning chains, cognitive biases, mental models, questions NOT asked

Output a concise summary organized by patterns (not by session). Quote key phrases verbatim. Note which file each finding comes from.
```

### Phase 3: 画像合成

拿到各子 agent 报告 + Phase 1 定量数据后：

1. **交叉收敛**：检查不同报告是否独立发现同一模式
2. **去冗余**：合并重复发现
3. **找缺失**：大量讨论 X 但几乎不提 Y？（如"大量讨论配置但很少提配置后的使用感受"）
4. **按维度撰写**：每个维度一篇，维度下拆分 2~3 个子节（子节名从该维度报告的实际内容中归纳，不预设）
5. **稀疏溯源**：核心结论后标注 `[MM-DD session描述 可选R##]`。日期格式 `MM-DD`，描述 ≤8 个字，有关键轮次加 `R##`
6. **置信度与盲区**：每维度标支撑强度（高/中/低），声明数据盲区
7. **启发式追问**：推导 5 个值得追问自己的问题

产出格式：

```markdown
# chaoyuan 个人认知画像 — YYYY-MM-DD

> 数据源：N 个会话（开始日期 → 结束日期），X/Y 天活跃
> 方法：全量元数据聚类 + 语义检索 + M 个核心会话深度解析（N 个 explore 子 agent 并行）
> 分析模型：<主 agent 模型> + deepseek-v4-flash（子 agent）
> 维度来源：冷启动，由话题聚类 + 语义归纳生成

---

## 一、[维度名 1]

### [子节名]
...

### [子节名]
...

## 二、[维度名 2]
...

## 核心公式
> 一句话总结认知操作系统

## 启发式追问
> 从数据中推导出的 5 个问题

---

**盲区声明**：(1) 人类协作模式缺失；(2) 情绪低谷期数据稀疏；(3) 非 AI 中介的决策与行为缺失
```

### Phase 4: 存档

写入 `contexts/thought_review/cognitive_<YYYY-MM-DD>.md`。

---

## 注意事项

- 子 agent 用 `new-api/deepseek-v4-flash`，执行前确认 `oh-my-openagent.jsonc` 中 explore 的 model
- 这是冷启动基线画像，不预编维度、不对比历史。后续增量运行规则另见独立文档
