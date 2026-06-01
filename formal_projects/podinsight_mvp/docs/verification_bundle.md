# PodInsight MVP Verification Bundle

Date: 2026-05-31

This document is the current verifier-facing proof bundle for the PodInsight interview-demo MVP.

## Historical snapshot note

The workspace root still contains three PodInsight snapshots:

- `podinsight_snapshot.md`
- `podinsight_snapshot_clean_session.md`
- `podinsight_snapshot_fixed.md`

They are preserved as debugging history only. They do not describe the current verified state.

- `podinsight_snapshot.md` captures the earlier `ModuleNotFoundError` before `streamlit_app.py` bootstrapped `src/`.
- `podinsight_snapshot_clean_session.md` and `podinsight_snapshot_fixed.md` capture the earlier template-heavy demo output before grounded claim/evidence/boundary/action fixes.

Current verification for this project is the combination of this file plus the receipts stored under `formal_projects/podinsight_mvp/docs/`.

## Current status summary

- Default offline demo path is the primary verified mode.
- Authenticated live wiring has been exercised successfully against the configured OpenAI-compatible DeepSeek/Qwen endpoints, but that live artifact set is archived separately from the primary interview-demo packet.
- The project is local-only and intentionally does not include deployment, auth, background workers, or a database.

## Requirement-to-evidence matrix

| Requirement | Implementation / artifact | Test / verification | Current receipt |
|---|---|---|---|
| Formal project under `formal_projects/` | `formal_projects/podinsight_mvp/` | directory + project `AGENTS.md` | repo state |
| Tests-first where behavior changes | `docs/tests_first_receipts.md` | session receipts + matching regression files and current suite receipts | `docs/tests_first_receipts.md` |
| Use transcript data from `contexts/podcast_read` | `src/podinsight_mvp/ingest.py`, `data/demo_episode_ids.json` | `tests/test_ingest.py`, `tests/test_catalog.py` | `docs/podinsight_query_flow_refresh_20260531_pytest.log` |
| Demo-oriented MVP over 6-8 AI/agent episodes | `data/demo_episode_ids.json`, `data/derived/episodes.json` | `tests/test_catalog.py` | `docs/podinsight_query_flow_refresh_20260531.png` |
| Theme aggregation + simple query | `data/derived/themes.json`, `src/podinsight_mvp/query.py`, `streamlit_app.py` | `tests/test_query.py`, browser smoke | `docs/podinsight_query_flow_refresh_20260531.png`, `docs/podinsight_query_flow_refresh_20260531_console.txt`, `docs/podinsight_query_flow_refresh_20260531_snapshot_clean.md` |
| Schema with `claim/evidence/boundary/optional action` | `src/podinsight_mvp/types.py`, `data/derived/cards.json` | `tests/test_types.py`, `tests/test_validate.py` | `docs/podinsight_query_flow_refresh_20260531.png` |
| Three-view extraction with lightweight validation | `scripts/run_pipeline.py`, `src/podinsight_mvp/extract.py`, `src/podinsight_mvp/validate.py` | `tests/test_cli.py`, `tests/test_extract.py`, `tests/test_validate.py` | `docs/podinsight_query_flow_refresh_20260531_pytest.log`, `docs/demo_pipeline.log` |
| Relations via embeddings + light classifier | `src/podinsight_mvp/relations.py`, `data/derived/relations.json` | `tests/test_relations.py`, `tests/test_cli.py` | `docs/podinsight_query_flow_refresh_20260531_pytest.log`, `docs/demo_pipeline.log` |
| Streamlit UI | `streamlit_app.py` | `tests/test_streamlit_import.py`, browser smoke on port `8506` | `docs/podinsight_query_flow_refresh_20260531.png`, `docs/podinsight_query_flow_refresh_20260531_streamlit_8506.log`, `docs/podinsight_query_flow_refresh_20260531_console.txt` |
| OpenAI SDK wrapper with cache | `src/podinsight_mvp/openai_client.py`, `src/podinsight_mvp/cache.py` | `tests/test_openai_client.py`, `tests/test_cli.py::test_build_runtime_clients_returns_live_stack` | `docs/podinsight_query_flow_refresh_20260531_pytest.log`, `docs/podinsight_query_flow_refresh_20260531_basedpyright.log` |
| Reproducible verifier install for pytest + typecheck | `pyproject.toml` | `.venv/bin/python -m pip install -e .[dev]` | `docs/dev_install.log` |
| Heavy model `deepseek-v4-pro` | `.env.example`, `src/podinsight_mvp/settings.py` | `tests/test_cli.py::test_build_runtime_clients_returns_live_stack` | `docs/podinsight_query_flow_refresh_20260531_pytest.log` |
| Light model `deepseek-v4-flash` | `.env.example`, `src/podinsight_mvp/settings.py` | `tests/test_cli.py::test_build_runtime_clients_returns_live_stack` | `docs/podinsight_query_flow_refresh_20260531_pytest.log` |
| Embedding model `Qwen3-Embedding-0.6B` | `.env.example`, `src/podinsight_mvp/settings.py` | `tests/test_cli.py::test_build_runtime_clients_returns_live_stack` | `docs/podinsight_query_flow_refresh_20260531_pytest.log` |
| Deterministic offline demo when key is empty | `scripts/run_pipeline.py::_should_use_live_clients` | `tests/test_cli.py::test_run_pipeline_cli_writes_output` | `docs/demo_pipeline.log` |
| Honest live-mode boundary and authenticated runtime proof | `scripts/run_pipeline.py`, `src/podinsight_mvp/openai_client.py`, `data/derived/live_auth_20260531/` | authenticated live run + archived snapshot | `docs/live_runtime_models.log`, `docs/live_pipeline.log` |

## Completed verification receipts

### Test and quality gates

- Verifier install: `.venv/bin/python -m pip install -e .[dev]` installs both `pytest` and `basedpyright` from `pyproject.toml` (`docs/dev_install.log`)
- Full suite: `.venv/bin/python -m pytest` → `61 passed` (`docs/podinsight_query_flow_refresh_20260531_pytest.log`)
- Type check: `.venv/bin/basedpyright` → `0 errors`, `297 warnings`; the remaining warnings span both source files and tests, mostly around reportUnknown/reportAny coverage plus a smaller set of unused-code findings, but the current verifier-facing run has no typecheck errors (`docs/podinsight_query_flow_refresh_20260531_basedpyright.log`)
- Tests-first chronology for behavior-changing fixes is captured explicitly in `docs/tests_first_receipts.md`, which cites the 2026-05-31 session receipts for the live-boundary, weak-claim, and evidence-integrity regressions rather than claiming nonexistent git-history ordering for this new formal-project path
- Regression guard for old fake-demo metadata: `tests/test_cli.py` now fails if cards reuse the earlier fixed boundary/action templates
- Regression guard for weak claims: `tests/test_validate.py` and `tests/test_cli.py` now fail if fragmentary, question-style, or low-signal claims survive into shipped cards
- Regression guard for implausible relations: `tests/test_cli.py` now fails if the demo relation classifier or rebuilt artifacts reintroduce the previously implausible `support/conflict/prerequisite` edges
- Regression guard for live-boundary honesty: `tests/test_cli.py` and `tests/test_openai_client.py` now fail if live-mode transport errors are swallowed or silently degraded to demo behavior
- Regression guard for authenticated live payload normalization: `tests/test_model_clients.py` now fails if object-shaped views or string evidence from the live provider collapse into zero cards
- Regression guard for fabricated live anchors: `tests/test_model_clients.py` now fails if a fully populated provider evidence dict bypasses transcript re-anchoring

### Current offline demo artifact state

- Rebuilt with the default offline path using `PODINSIGHT_CHAT_API_KEY=""` (`docs/demo_pipeline.log`)
- Output directory: `formal_projects/podinsight_mvp/data/derived/`
- The refreshed Streamlit/browser smoke below reused that same current `data/derived/` artifact set rather than rebuilding again; the browser snapshot and direct artifact counts agree on Episodes `8`, Cards `24`, Relations `7`, Themes `5`
- Current counts from the rendered app: Episodes `8`, Cards `24`, Relations `7`, Themes `5`
- The current cards artifact no longer contains the earlier fixed template strings:
  - `This works when the team can scope the task and still verify the output against real work.`
  - `This matters when cost, reliability, or replacement risk directly shapes adoption decisions.`
  - `This holds when the operator can turn goals into explicit prompts, tools, or workflow steps.`
  - `Benchmark the workflow on one bounded task before scaling it.`
  - `Track cost and operational risk before scaling usage.`
  - `Write the workflow down before delegating it to an agent.`
- The current cards artifact also no longer contains the weak shipped claims Oracle rejected, including `在大量的被 AI agent 替换掉。`, `它是基于 MCP 还是 API 还是一些别的东西。`, `这样的一个 prompt 其实丢给豆包也好。`, `思考这个问题的价值在于思考模型下一步能进化到什么程度。`, `我们用 20 个问题一起搞懂 AI Agent。`, `我们前几年聊了很多你的 AI Talker，你的 Prompt 工程师，或者是 Agent 的创业。`, `前两天写了个朋友圈，我就说美国有很多这种 AI 创业让人感觉是中产创业。`, `抽象出来的一个 AI 的思维链或者 AI 的 Prompt。`, and `包括我们产品的一些具体问题。`
- The current relations artifact is intentionally smaller and more conservative than the earlier `31`-edge demo output. It should be read as lightweight exploratory local-demo linking, not as production-grade semantic relation truth.

### Streamlit browser smoke

- Command: `.venv/bin/python -m streamlit run streamlit_app.py --server.headless true --server.port 8506`
- Server receipt: `docs/podinsight_query_flow_refresh_20260531_streamlit_8506.log`
- Screenshot: `docs/podinsight_query_flow_refresh_20260531.png`
- Browser console receipt: `docs/podinsight_query_flow_refresh_20260531_console.txt`
- Browser state snapshot: `docs/podinsight_query_flow_refresh_20260531_snapshot_clean.md`
- Verified UI facts:
  - the page title is `PodInsight MVP`
  - the overview metrics render with the current counts
  - the evidence-backed query accepts a typed non-default question: `What do these episodes suggest about Claude Code for developers?`
  - the rendered answer switches to the `AI coding tools are framed as real leverage...` branch for that question
  - the supporting cards update to Claude Code-grounded claims instead of the default preview ordering, including the `sub-agent` and `3D 模型自己去部署` cards
- the refreshed browser snapshot reflects the current tightened `8 / 24 / 7 / 5` artifact state

### Authenticated live-path proof

- Authenticated run used the configured endpoints and models: `deepseek-v4-pro`, `deepseek-v4-flash`, `Qwen3-Embedding-0.6B`
- Runtime receipt: `docs/live_runtime_models.log`
- Pipeline receipt: `docs/live_pipeline.log` → `{"card_count": 21, "mode": "live"}`
- Archived live artifact snapshot: `data/derived/live_auth_20260531/`
- Archived live counts: Episodes `8`, Cards `21`, Relations `10`, Themes `55`
- Interpretation: the real DeepSeek/Qwen extraction, embedding, relation, and answer stack now runs end-to-end with authenticated credentials. That live artifact set is archived separately because the primary interview-demo packet and browser receipts are still anchored to the tighter offline `8 / 24 / 7 / 5` dataset.

### Historical live-boundary fallback receipt

- The earlier dummy-key receipt remains preserved at `docs/live_dummy_401.log`
- Interpretation: when credentials are invalid, the code still enters the real live path and fails remotely instead of silently degrading to demo mode

## What this bundle claims

This bundle claims the current project is locally implemented and locally verifiable as an interview-demo MVP with a conservative offline demo packet, a real authenticated live-path proof, a reproducible verifier install for pytest/typecheck, and explicit session-backed tests-first receipts for the behavior-changing fixes.

This bundle does not claim that the archived live artifact set is the primary interview-demo packet or that it has received the same browser/manual-QA treatment as the restored offline `8 / 24 / 7 / 5` demo dataset.
