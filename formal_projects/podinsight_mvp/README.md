# PodInsight MVP

PodInsight MVP is a local interview-demo project that turns a small curated set of podcast transcripts into structured opinion cards, lightweight relation edges, and a Streamlit demo for theme browsing and evidence-backed querying.

## What this MVP includes

- curated 6-8 episode demo set from `contexts/podcast_read`
- card schema with `claim`, `evidence`, `boundary`, optional `action`, and metadata
- three extraction views: `judgment`, `controversy`, `practice`
- relation discovery via embeddings recall plus light-model classification, surfaced conservatively as lightweight exploratory links in the local demo
- Streamlit UI for topic aggregation and simple question answering
- local cache for model responses and embeddings

## What this MVP does not include

- production deployment
- user accounts
- background jobs
- database persistence
- full topic evolution automation

## Planned layout

- `src/podinsight_mvp/` application code
- `data/` curated ids, topic aliases, derived artifacts, caches
- `scripts/` runnable entry points
- `tests/` offline tests and fixtures

## Running locally

`python scripts/run_pipeline.py` uses the configured DeepSeek/Qwen-style endpoints when `PODINSIGHT_CHAT_API_KEY` is set to a real value. When that key is empty or left as `replace-me`, the script falls back to deterministic demo clients so offline tests and smoke runs stay reproducible.

## Current verification receipts

The current verifier-facing QA bundle lives under `docs/verification_bundle.md`.

That bundle links the current verifier-facing receipts for:

- full test pass
- typecheck status
- dev-install receipt for reproducible `pytest` and `basedpyright` setup
- tests-first session receipts for behavior-changing fixes
- current Streamlit screenshot and server log
- clean browser console receipt
- authenticated live runtime and pipeline receipts plus the archived live artifact snapshot

The workspace-root files `podinsight_snapshot*.md` are historical debugging snapshots only. They do not describe the current verified state.
