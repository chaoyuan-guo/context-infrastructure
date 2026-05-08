# 在Industry的思考与沉淀 | 把 Agent 真正用好的4个 Pattern

> 来源：<https://www.superlinear.academy/c/share-your-insights/ai-pattern>
> 作者：Franco Sun
> 发布日期：2026-04-16
> 平台：Superlinear Academy

---

> 这不是综述，也不是谁的框架搬运。是我每天高强度用 Claude Code、Cursor 和内部工具，在几个大型项目、流程和复杂 codebase 里反复踩坑之后，自己沉淀下来的几个 pattern。有一部分思考来自鸭哥的启蒙。欢迎讨论与指教。
> 
> ---

## Pattern 1 — 能 deterministic 的就别让 agent 来

给 agent 一个 skill 让它"自由发挥"是非常脆弱的。我的第一反应永远是：能不能把它退化成一个 **script / CLI / MCP tool**？这三种形态差别不大，本质都是把原本 LLM reasoning 承担的事交给确定性执行。

除了代码形态的确定化，agent 之外的 **harness** 同样是 determinism 的重要来源——尤其是 **Hooks**：它被 lifecycle 强制触发，不依赖 agent 自己选择调用。"被强制执行"本身就是对抗熵增的力量。

> 一个朴素的判断：**凡是能用代码基本解决的事，都不应该交给 LLM**。

---

## Pattern 2 — 用预处理好的 context 喂 agent，而不是 runtime 现抓

任何一个真正有意义的 skill 或 agent，背后几乎都挂着一个 **pre-ingested / curated** 的 context source，几乎是为这个 agent 量身定制的。

举个例子：你想要一个"追踪最新技术动态"的 skill。最差的做法是 runtime 去抓 raw HTML、塞给模型现场总结——慢、贵、脆、格式飘。正确的做法是有一个 pipeline 每天把感兴趣的源抓下来，用便宜的 LLM 做一轮结构化，按 agent 友好的 schema 存到本地。Skill 调用时直接读已经 curated 好的片段，效果经常是 *day and night*。

这里有个容易被忽略的点：**schema 是为消费者设计的**。不是所有处理过的数据都算 curated——一个 10K 字的长 summary 对 agent 来说还是 blob，它还要再消化一遍。真正有用的 pre-ingested 数据应该是：

- **scannable**（有清晰锚点，不用整段读）
- **结构化**（字段明确，可以直接用工具按需 extract——又回到了 Pattern 1）
- **短段落**（一次取用几百 token 就够做决策）

pipeline 的存在只完成了一半，schema 设计是另一半，而且往往是决定效果的那一半。

---

## Pattern 3 — 没有 evaluation 的 skill / agent，一定不是好 skill / agent

**evaluation 是 the single most important thing**。没有 eval，谁都没法真正说哪个 skill 好、哪个 agent 差——尤其现在造一个 skill 只需要一句话，更需要 eval 去筛掉"感觉还行"。

但一上来就做 test-oriented development 也不对，因为你还没 explore 出 solution 的形状。合理的节奏是三段：

1. **Manual exploration**：先用起来，看 feedback 是什么样子，做一堆 judgment call。这个阶段 test 太早反而会把形状锁死。
2. **沉淀 test set**：慢慢把反复出现的 pattern 抽成小而稳定的 test cases。不需要大而全，需要的是能区分"这次改动是进步还是退步"。
3. **嵌入 lifecycle**：最终目标是把 evaluation 变成 **runtime feedback loop**——比如 SessionEnd 钩子记录成功率、失败的 skill 自动降权、把新发现的 edge case 自动加进 test set。让优化 compounding。

或许哪天有个 meta-agent 能替我做这层判断，那我大概就真的可以"失业"了——也或许它已经有了，只是我还没用上。

---

## Pattern 4 — 减 noise，但要留呼吸

Context window 不是瓶颈，**signal density** 才是。

> 70K 里有全量相关信息 + 一点发散  >  50K 全是相关信息  »  200K 里散布着有用碎片

Noise 主要来自三处：

- **Registration overhead**：过多的 MCP、过多的 schema、一堆"什么都没做就已经 load 进去"的 instruction。典型 setup 光 MCP tool definitions 就能吃掉 ~25% 的 context。
- **Tool output**：要 agent 搜一条信息，不要把整页 HTML 回来当 output——只返回真正相关的那一段。Tool 的 responsibility 是 filter，不是 dump。
- **Over-filtering 的反噬**（容易被忽略的一条）：不能为了减 noise 什么都不 load。有些"对人来说是 noise"的信息，agent 可能正是靠它做出我们意料之外的连接——模型的训练就是在大量"似乎无关"的信号里学会 pattern 的。

第 3 点的根因是我最近才想清楚的，叫它 **intentionality bubble**：过度 filter 会高效地深化现有目标，但系统性地切断 tangential discovery。以前自己直接写代码时，会偶然读到一段 tangential 的 doc、发现一个新 lib——这条学习路径在全量 delegation 给 agent 之后就被切断了。

所以 pattern 4 的本质不是"信息完整度"的 balance，而是 **目标性 vs 探索性** 的 balance。一种比较好的实现机制是 **discovery → enrichment loop**：先 search 发现信号，再针对性深挖。具体每一步怎么裁，是 judgment call，case by case。

---

## Anti-pattern

- **Vibe-coded skill**：一句话造 skill，没 eval，感觉能跑就上线
- **Raw MCP 堆栈**：什么 MCP 都 register，还没开口 25% context 已经没了
- **Runtime web fetch 当 context 源**：每次跑 agent 都现抓，慢、贵、脆
- **Stateful skill 做 script 该做的事**：让 LLM 承担本来 deterministic 逻辑能搞定的流程

看到自己有任何一条，先停下来修。

