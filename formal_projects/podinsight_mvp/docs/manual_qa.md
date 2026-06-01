# Manual QA

## Current verification record

- Date: 2026-05-31
- Scope: default offline demo path plus authenticated live-path proof
- Source of truth for current verification: `docs/verification_bundle.md`

## Latest completed run

1. Rebuilt the default offline demo artifacts with the current tightened claim-validation and conservative relation heuristics using `PODINSIGHT_CHAT_API_KEY="" .venv/bin/python scripts/run_pipeline.py` and captured the result in `docs/demo_pipeline.log`.
2. Confirmed `data/derived/` contains `episodes.json`, `cards.json`, `relations.json`, `themes.json`, and `answers_preview.json`.
3. Confirmed the current rebuilt artifact counts are Episodes `8`, Cards `24`, Relations `7`, Themes `5`.
4. Started Streamlit with `.venv/bin/python -m streamlit run streamlit_app.py --server.headless true --server.port 8506`.
5. Verified the landing page shows the current metrics: Episodes `8`, Cards `24`, Relations `7`, Themes `5`.
6. Typed the non-default query `What do these episodes suggest about Claude Code for developers?` into the live textbox.
7. Waited for the rendered answer to switch to the `AI coding tools are framed as real leverage...` branch and confirmed the supporting cards updated to Claude Code-grounded claims including the `sub-agent` and `3D 模型自己去部署` cards.
8. Verified browser console is clean: `docs/podinsight_query_flow_refresh_20260531_console.txt`.
9. Saved the refreshed screenshot, state snapshot, and server log under `docs/podinsight_query_flow_refresh_20260531.png`, `docs/podinsight_query_flow_refresh_20260531_snapshot_clean.md`, and `docs/podinsight_query_flow_refresh_20260531_streamlit_8506.log`.
10. Reinstalled the project from the declared dev extras using `.venv/bin/python -m pip install -e .[dev]` and captured the verifier-facing setup receipt in `docs/dev_install.log`, so both `pytest` and `basedpyright` are reproducible from project config.
11. Re-ran project verification after the live evidence-integrity fix: `61 passed` in `docs/podinsight_query_flow_refresh_20260531_pytest.log`; `basedpyright` reported `0 errors` and `297 warnings` in `docs/podinsight_query_flow_refresh_20260531_basedpyright.log`.
12. Ran the authenticated live pipeline against the configured DeepSeek/Qwen endpoints and captured the successful live receipts in `docs/live_runtime_models.log` and `docs/live_pipeline.log`.
13. Archived the authenticated live artifact set under `data/derived/live_auth_20260531/` and confirmed its counts are Episodes `8`, Cards `21`, Relations `10`, Themes `55`.
14. Restored `data/derived/` to the default offline interview-demo packet after archiving the live snapshot so the main Streamlit demo remains on the curated `8 / 24 / 7 / 5` artifact set.
15. Added `docs/tests_first_receipts.md` to capture the session-backed tests-first chronology for the live-boundary, weak-claim, and evidence-integrity behavior fixes, instead of claiming that chronology from nonexistent git history on this new formal-project path.
16. The current receipt set reflects the tightened post-fix demo state plus a separately archived authenticated live run, rather than the earlier `31 relations` browser run.

## Re-run checklist

1. Install dev extras with `python -m pip install -e .[dev]` or `uv pip install -e .[dev]` and keep the install receipt if you are refreshing verifier-facing logs.
2. Run `python scripts/run_pipeline.py` and confirm `data/derived/` contains `episodes.json`, `cards.json`, `relations.json`, `themes.json`, and `answers_preview.json`.
3. Run `streamlit run streamlit_app.py --server.headless true --server.port 8506`.
4. Open the landing page and confirm episode, card, relation, and theme counts are visible.
5. Expand one theme and confirm cards show claim, evidence, boundary, topics, source views, and action.
6. Open the query section, replace the default text with a non-default question, and confirm the rendered answer plus supporting cards change accordingly.
7. Save the screenshot, console log, and server log into `docs/` before review.
8. For live-path proof, run `python scripts/run_pipeline.py` with real `PODINSIGHT_*` environment variables, save `docs/live_runtime_models.log` and `docs/live_pipeline.log`, and archive the resulting live artifacts outside the default offline `data/derived/` packet before restoring the interview-demo dataset.
9. If you need the tests-first chronology for the behavior-changing fixes, inspect `docs/tests_first_receipts.md` and the cited session/message IDs.
