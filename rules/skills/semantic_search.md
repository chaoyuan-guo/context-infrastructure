# 语义搜索技能（本地配置）

通用实现位于 [`../../tools/semantic_search/`](../../tools/semantic_search/)，同步自
[`grapeot/semantic-search-skill`](https://github.com/grapeot/semantic-search-skill)。完整 CLI
契约见 [`skill_semantic_search.md`](../../tools/semantic_search/skills/skill_semantic_search.md)。
当前同步基线为 `master@6f5d8e6c1dbeadc83dd918c42cd7e4b4009eae91`。

本文件只保存当前 workspace 的路径和 embedding 配置，不修改通用实现。

## 何时使用

- 需要按含义检索历史观点、日志、调研材料或 Agent 会话，而关键词可能不一致。
- 构建 `rules/axioms/` 下的公理，或回答涉及用户价值观、方法论和思想演变的问题。
- 从大量 Markdown、文本、CSV 或转录文件中提取主题相关片段。

实体名、项目名、日期和 session id 等精确信息先用 `rg`；模糊记忆和概念关联再用语义搜索。

## 本地默认配置

- Endpoint：`http://10.0.34.60:8034/v1`
- Model：`Qwen3-Embedding-0.6B`
- Cache：workspace 根目录 `.knowledge_cache_v2/`
- CLI：`tools/semantic_search/.venv/bin/semantic-search`

该 endpoint 不校验 API key，但 OpenAI SDK 要求环境变量非空，因此本地命令使用
`OPENAI_API_KEY=unused`。待搜索文件和 cache 都留在本机；用于生成 embedding 的文本会发送到
上述 endpoint。

## 安装

在 `tools/semantic_search/` 中执行：

```bash
uv python install 3.12
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -e '.[dev]'
```

## 查询

每次按当前搜索范围重新生成 file list，不复用旧列表：

```bash
mkdir -p tmp
rg --files contexts -g '*.md' > tmp/search_files.txt

OPENAI_API_KEY=unused tools/semantic_search/.venv/bin/semantic-search \
  --base-url http://10.0.34.60:8034/v1 \
  --model Qwen3-Embedding-0.6B \
  query \
  --file-list tmp/search_files.txt \
  --query "<自然语言查询>" \
  --top-k 10 \
  --cache-dir .knowledge_cache_v2
```

`query` 默认增量刷新新增或变更的文件。只读已有 cache 时添加 `--no-refresh`。

## 维护

```bash
OPENAI_API_KEY=unused tools/semantic_search/.venv/bin/semantic-search \
  --model Qwen3-Embedding-0.6B stats --cache-dir .knowledge_cache_v2
OPENAI_API_KEY=unused tools/semantic_search/.venv/bin/semantic-search \
  --model Qwen3-Embedding-0.6B doctor --cache-dir .knowledge_cache_v2
```

旧版 `.knowledge_cache/` 使用 `chunks.pkl`，不符合新版迁移器支持的 v1 格式，不能运行
`migrate-v1`。确认新版完成所需语料的 rebuild 后，再单独清理旧 cache。
