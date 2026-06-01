# AGENTS.md - podinsight_mvp

This project is a local interview-demo MVP for PodInsight.

## Scope

- Build a file-based pipeline over `contexts/podcast_read`
- Extract opinion cards from 6-8 curated AI/agent episodes
- Build lightweight relations and a simple evidence-backed query flow
- Present the result in Streamlit for interview demos

## Constraints

- Keep the project local-only
- No auth, database, background workers, or deployment work
- Derived artifacts live under `data/derived/`
- Cache model responses under `data/cache/`
- Prefer deterministic tests with stubbed model clients

## Runbook

- Install with `uv pip install -e .[dev]` or equivalent
- Run tests with `pytest`
- Run the pipeline with `python scripts/run_pipeline.py`
- Run the demo with `streamlit run streamlit_app.py`

## Data contracts

- Source catalog: `contexts/podcast_read/prep_index.json`
- Source transcript: `contexts/podcast_read/<episode_id>/Transcript.md`
- Source QC: `contexts/podcast_read/<episode_id>/QC.report.json`
