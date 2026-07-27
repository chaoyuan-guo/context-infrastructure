# AI Session Search & Archive

## Objective

Find prior AI sessions across a unified Markdown archive without depending on a
single vendor's history UI. Use lexical search for names and identifiers, then
semantic search when the remembered wording is approximate.

This workflow assumes an archive produced by a multi-source exporter such as
the locally installed [AI Session Export](./ai_session_export.md). Keep the
archive private: session titles, transcripts, project paths, and identifiers
may all contain sensitive information.

## Source Routing

A typical archive has one directory per source:

```text
contexts/ai_sessions/
  opencode/
  claude_code/
  codex/
```

- When the user names a source, search only that directory.
- When the source is unknown, search every available source directory.
- Generate client-specific action links only when the result metadata and host
  explicitly support them. Otherwise return an ordinary Markdown file link.

## Retrieval Order

### 1. Lexical search for named entities

Product names, people, projects, titles, dates, and session ids should use
`rg` first. Expand a remembered name into a few plausible variants rather than
assuming the user's wording exactly matches the archived title.

```bash
rg -i -n --glob '*.md' \
  'Claude Teacher|Claude for Teachers|Anthropic for Teachers' \
  contexts/ai_sessions/
```

Glob searches filenames, not file contents. A truncated glob result is not
evidence that no matching session exists.

### 2. Semantic search for approximate memories

Generate the file list from the current source scope at query time. Do not
reuse an old `tmp/*files*.txt`: a semantic-search file list is also a result
allowlist, so an omitted file cannot be returned even if its vectors exist in
the cache.

```bash
FILELIST="$(mktemp)"
trap 'rm -f "$FILELIST"' EXIT
rg --files contexts/ai_sessions/ \
  -g '*.md' \
  -g '!**/*The_following_is_the_Codex_agent_history*' \
  > "$FILELIST"

# Run once after an export; skip during ordinary read-only lookup.
OPENAI_API_KEY=unused tools/semantic_search/.venv/bin/semantic-search \
  --base-url http://10.0.34.60:8034/v1 \
  --model Qwen3-Embedding-0.6B \
  rebuild \
  --file-list "$FILELIST" \
  --cache-dir .knowledge_cache_v2

OPENAI_API_KEY=unused tools/semantic_search/.venv/bin/semantic-search \
  --base-url http://10.0.34.60:8034/v1 \
  --model Qwen3-Embedding-0.6B \
  query \
  --file-list "$FILELIST" \
  --cache-dir .knowledge_cache_v2 \
  --query 'the remembered concept' \
  --top-k 10 \
  --no-refresh
```

Use the installed semantic-search skill's provider and model configuration. After
an export, refresh the new files with `semantic-search rebuild` as a separate
maintenance action. A read-only lookup should use `--no-refresh` rather than
silently rebuilding a large shared cache.

## Freshness Fallback

Check `contexts/ai_sessions/.export_state.json` before reading native stores. If the
target session predates the latest successful source export, search the
archive directly. Only perform a source-specific temporary export when the
session is newer than the archive. Delete temporary exports after lookup.

## Result Contract

- Group chunks by source and session id so one session appears once.
- Show title, date, source, project short name when available, and a verbatim
  excerpt that lets the user verify the match.
- Do not display embedding scores or replace evidence with an AI summary.
- Read action ids from frontmatter; never infer them from filenames or text.
- Do not put credentials, server addresses, local host profiles, absolute
  archive paths, or user queries into action URLs.

## Acceptance Criteria

A session lookup is complete when the search covered the correct source scope,
named-entity variants were tried before semantic fallback, semantic queries
used a fresh scoped file list, duplicate chunks were consolidated, and every
navigation action came from validated archive metadata.
