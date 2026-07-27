## Changelog

### 2026-07-27

- Removed the unused session sources and their adapters, CLI flags, state cursors, tests, and documentation. The local tool now supports OpenCode, Claude Code, and Codex only.

### 2026-07-25

- Extended the backward-compatible Markdown frontmatter contract with optional `turn_models`, aligned one-to-one with rendered dialogue sections and using `null` for unknown attribution.
- Preserved native OpenCode turn models, assigned Claude user turns from their next assistant response, and tracked Codex turn-context models including delayed context events.
- Added synthetic renderer and adapter coverage without introducing real transcript data into the public repository.

### 2026-07-15

- Added Codex rollout export from active and archived JSONL sessions, using `session_index.jsonl` for titles and the existing unified Markdown contract.
- Codex keeps only explicit user and agent narrative events; developer instructions, reasoning, tool traffic, token accounting, and world-state records are excluded.
- Added per-session incremental state so active rollouts update one stable Markdown file. Source mtimes avoid reparsing unchanged historical rollouts.
- State writes now use an atomic same-directory replacement, preventing a large Codex state map from being truncated if a process stops mid-write.
- Moved the default output root outside the public repository to `~/.local/share/ai-session-export/` and added gitignore defenses for every generated source directory and state file.
- Added synthetic parser, filtering, incremental-update, and all-source integration coverage.

## Lessons Learned

- **Session-level model inventories cannot recover turn attribution.** Downstream analytics need an index-aligned `turn_models` contract; `models_used` remains descriptive metadata only.
- **Codex records the same conversation through multiple event channels.** `response_item` mirrors narrative and tool traffic, while `event_msg` provides clean `user_message` and `agent_message` events. Reading both duplicates the transcript; the adapter treats `event_msg` as canonical.
- **Codex rollouts are mutable session files.** A global timestamp cursor creates duplicate `_2.md` files when an active session grows. Per-session output identity is required for incremental correctness.
