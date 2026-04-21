# RAG 面试速查：IR 领域积累的最佳实践

> 用途：面试时快速调用的参考。把 RAG 教程里的"默认值"还原成 IR 学科里有出处、有 trade-off 的有意识选择。
> 来源文章：`formal_projects/curated_reads/260327_RAG 的每一项核心技术，搜索引擎都做过.md`

每条按四样组织：**结论 / 出处与年份 / 为什么这样选（trade-off）/ 在 RAG 里怎么落地**。后面有"高阶串讲"和"显学术深度的话术"两节，是把分数从 80 拉到 95 的杠杆。

---

## 一、Chunking：passage size 是变量，不是常数

**结论**：chunk size 不应固化为 512 token。最优值跟查询类型强相关，事实性查询适合短 passage，主题性查询适合长 passage。

**出处**：Callan, SIGIR 1994；TREC Passage Track 2003-2004；DPR 2020 沿用 100-word。

**Trade-off**：粒度越细，匹配信号越精确，但上下文越少，主题性判断越弱。Callan 的实验区间 100-150 词，DPR 用 100，RAG 社区在二次传播中把这个变量固化成了 512 token，丢失了"按查询类型调"的灵活性。

**RAG 落地**：
- chunk size 当作可调参数，不是常数。如果只能给一个默认值，参考 TREC 经验取 200-300 token 而非 512。
- 按语义边界（标题、段落、列表）切，优于按固定 token 数切。
- 长文档场景上 hierarchical retrieval：先文档级粗排，再段落级精排。

**面试一句话**：512 token 是 RAG 教程的默认值，不是 IR 的最优值。Callan 1994 年就证明 passage size 是 query-dependent 的。

---

## 二、Dense Embedding：cosine vs dot product 是有意识的选择

**结论**：cosine similarity 默认优于 dot product，因为它消除文档长度对分数的影响。

**出处**：DSSM, 微软 2013（架构跟 2020 年的 DPR 完全一致）。

**Trade-off**：dot product 不归一化，长文档 embedding 范数天然更大，会系统性偏向长文档。cosine 通过归一化消除了这个偏差。一些向量数据库默认用 dot product，在文档长度差异大的语料上会出问题。

**RAG 落地**：
- 语料里混合短 FAQ 和长技术手册时，确认向量库用的是 cosine，或者在 embedding 后做 L2 归一化（归一化后两者数学等价）。
- 知道 dense retrieval 在精确匹配上的根本弱点：专有名词、产品编号、错误代码会被 embedding 模型泛化成语义类别，丢失字面精度。这是 hybrid search 存在的根本理由，不是锦上添花。

**面试一句话**：dot product 偏向长文档；cosine 通过 L2 归一化消除这个偏差。两者在归一化后等价，但默认设置不同会带来系统性偏差。

---

## 三、Vector Search：HNSW 的两个参数要分开调

**结论**：`ef_construction` 和 `ef_search` 是两个独立旋钮。检索质量敏感的场景，把 `ef_search` 调到默认值的 2-3 倍，几乎没成本。

**出处**：HNSW 2016；Facebook FAISS 2019。

**Trade-off**：`ef_construction` 控制索引构建质量（一次性离线成本），`ef_search` 控制每次查询探索的邻居数（在线持续成本）。HNSW 故意把它们解耦，因为成本结构不同。

**RAG 落地**：
- 一次 HNSW 查询几毫秒到几十毫秒，后续 reranker + LLM 是几百毫秒到几秒。检索阶段多花 10ms 换 5% 召回提升，在 LLM 调用面前完全可以忽略。
- 默认值是教程值，不是生产值。生产环境先把 `ef_search` 翻倍试一下。

**面试一句话**：HNSW 的两个参数解耦是有意识的设计，对应离线构建和在线查询两种不同成本结构。在 LLM pipeline 里，检索延迟根本不是瓶颈，应该把 `ef_search` 调高换召回率。

---

## 四、Cascade Ranking：上限由召回决定，不是 reranker

**结论**：两阶段排序的效果上限由第一阶段召回质量决定，不是 reranker 模型。优化优先级是先做好召回，再调 reranker。

**出处**：微软 RankNet 2005，Learning to Rank 这条线。IR 把这个架构叫 cascade ranking。

**Trade-off**：第一阶段用 dual encoder（快但粗），第二阶段用 cross-encoder（慢但准）。如果第一阶段没把相关文档捞上来，第二阶段排序再精确也没用，因为候选池里全是噪声。

**RAG 落地**：
- 别先调 reranker。先确保召回阶段多通道（BM25 + dense，可能再加其他信号），top-k 给得够大。
- ms-marco 系列 reranker 是在 Bing 搜索日志上训的，偏向通用网页查询。法律、医疗、代码这类垂直领域至少做一次 domain-specific 评测，确认通用 reranker 的效果不会塌。

**面试一句话**：reranker 是放大器，不是召回器。第一阶段没捞回来，第二阶段救不回来。RAG 社区常见的优化误区就是反过来。

---

## 五、Hybrid Search 与 RRF：用 rank 做融合，不要用 score

**结论**：BM25 + dense 双通道融合，标准方法是 RRF（Reciprocal Rank Fusion），公式 `1 / (k + rank)`，k 取 60。**用 rank 不用 score**。

**出处**:Cormack, SIGIR 2009，原论文只有 2 页，来源于 meta-search（多搜索引擎结果融合）。

**Trade-off**：BM25 分数范围可能 0-30，cosine similarity 范围 -1 到 1，量纲不可比。直接做 score 加权或归一化都没有统计意义。rank 是通用的，第 1 名就是第 1 名，无论分数多少。一些 RAG 实现试图归一化 BM25 和 cosine 后加权，效果反而不如简单 RRF。

**附带知识点：BM25 自带 saturation function**：词频增长到一定程度收益递减，防止长文档因为词频高就垄断排名。Dense retrieval 没有这个机制，长文档信号会淹没短文档。这是 hybrid 的另一个价值：BM25 通道天然对长度做了补偿。

**RAG 落地**：
- 当前只用 dense 的话，加 BM25 通道做 hybrid 是 ROI 最高的一项改进。
- RRF k 值取 60（原论文默认），40-100 都可以。
- Elasticsearch、Vespa、Weaviate、Milvus 都原生支持 RRF。

**面试一句话**：score 量纲不可比，rank 通用。RRF 简单到只有一行公式，但比所有归一化加权方案都更稳。

---

## 六、Query Rewriting：本质是 Rocchio 的升级版，注意 query drift

**结论**：LLM query rewriting 是 1971 年 Rocchio relevance feedback 的延续，2001 年 RM3 把它演化成 pseudo-relevance feedback。LLM 升级了灵活性，但继承了同一个风险：query drift。

**出处**：Rocchio 1971；Lavrenko & Croft 2001 (RM3)。

**Trade-off**：扩展能补 vocabulary gap，提升召回。但如果第一轮检索结果本身偏，扩展会把 query 越改越偏，引入噪声。

**RAG 落地**：
- 同时用原始 query 和改写 query 做检索，取并集，不要完全替换原始 query。
- 这是 IR 学科明确积累的失败教训，不是 LLM 时代才有的问题。

**面试一句话**：LLM query rewriting 不是新东西，是 Rocchio 1971 + RM3 2001 的升级。要警惕 query drift，对策是原始 query 和改写 query 同时检索取并集。

---

## 七、新一代交叉技术：SPLADE / ColBERT / Agentic Search

这块面试可以作为加分项，证明你不只懂 RAG 教程也懂学术前沿。

**SPLADE**：让 BERT 学会写倒排索引。用 MLM head 对词汇表所有词预测概率，取高概率词做扩展，log-saturation 转权重，输出稀疏向量。同时做了隐式 query expansion 和学习型词权重，**输出兼容倒排索引**，可以直接进 Elasticsearch。它是 neural IR 和传统 IR 的桥。Elasticsearch 的 ELSER 是商业版的 SPLADE，是 BM25 的自然升级路径。

**ColBERT**：late interaction。dual encoder 把整篇文档压成一个向量，丢 token 级信息；cross-encoder 保留 token 交互但太贵。ColBERT 保留每个 token 的向量，匹配时对每个 query token 找最相似的 doc token，取 MaxSim 加总。doc token 向量可预计算，比 cross-encoder 快几个数量级，比 dual encoder 准。

**Agentic Search**：LLM 充当检索规划器，决定搜什么、搜几次、每步用什么方法。多步推理类问题（比如跨年度比较）传统 RAG 处理不好。Perplexity Deep Research、OpenAI deep research 都在这条线上。

---

## 八、高阶串讲：把零散点拧成一条主线

如果面试官问"你怎么优化一个 RAG 系统"，别按上面 7 条平铺直叙。按这条优先级讲，体现你有判断力：

**第一优先级，召回阶段做对**。加 BM25 通道做 hybrid，RRF 融合，k=60 用 rank 不用 score。这一步对应 cascade ranking 的核心 insight：上限由召回决定。

**第二优先级，chunking 当变量调**。语义边界切分，chunk size 200-300 token 而非 512，长文档考虑 hierarchical retrieval。

**第三优先级，相似度选对**。cosine 默认优于 dot product，长度差异大的语料尤其要确认。

**第四优先级，HNSW 参数调高**。`ef_search` 翻倍，几乎不增加成本。

**第五优先级，reranker 评测**。垂直领域不要直接用 ms-marco，做一次 domain-specific 评测。

**第六优先级，query rewriting 加上 fallback**。原始和改写并集检索，防 drift。

**最后**：如果这些都做了还要进一步，转向 SPLADE/ColBERT/Agentic Search 的方向，或者跳出单轮 RAG 范式做迭代式检索。

---

## 九、面试时可以主动抛的几句"显学术深度"的话

按使用场景分类，挑一两句用就够了，多了显得在背书：

谈到 hybrid search 时：**"score 量纲不可比是 RRF 设计的核心动机，这是 Cormack 2009 年从 meta-search 领域带过来的洞见。"**

谈到 reranker 时：**"cascade ranking 的效果上限由第一阶段召回决定，IR 这条经验从 2005 年 RankNet 就已经稳定下来。"**

谈到 chunking 时：**"DPR 2020 用的 100-word passage 跟 TREC 2003 标准几乎一致，512 token 是 RAG 社区在二次传播中固化的，不是 IR 验证过的最优值。"**

谈到 dense retrieval 时：**"DSSM 2013 的双塔架构跟 2020 年 DPR 完全一致，dense retrieval 的算法骨架其实有十年历史。"**

谈到 RAG 整体时：**"RAG 在算法层基本是 IR 的二次发明，真正的贡献是把原本需要 IR 博士搭建的管线压缩到 Python 开发者一天就能跑起来。这是 democratization，不是算法创新。"**

---

## 十、表达策略：先讲坑，再用术语命名

既然实际踩过这些坑，面试时**先讲踩过的坑，再用 IR 的术语和论文给坑命名**。

例：先讲"我们之前 chunk 切死成 512，长文档场景召回总是掉，后来按段落切才好"，再补"这其实是 Callan 1994 就讨论过的 passage size 问题"。

这样既有实战又有理论，比纯背知识点说服力强一个量级。
