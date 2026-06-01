# Tests-First Receipts

Date: 2026-05-31

This project was introduced as a new formal project late in the 2026-05-31 work session, so git history for `formal_projects/podinsight_mvp/` does not honestly capture the chronology of the in-session bugfix iterations. For the acceptance criterion **"tests-first where behavior changes"**, the verifier-facing proof is therefore the OpenCode session trace below plus the current regression receipts.

This document does **not** claim that every greenfield scaffold file in the initial project creation was written under TDD. It claims that the behavior-changing fixes called out below were executed with regression-first intent before the corresponding implementation tightening.

## Session receipts

Primary session: `ses_1840f8957ffefVlK4XCRJjI47r`

| Time (UTC) | Session message | Evidence of tests-first step | Related files / verification |
|---|---|---|---|
| 2026-05-31T05:17:45Z | `msg_e7c777976001qWPUg0qjzGDV49` | "This step is still tests-first: add one transport-level regression and one CLI-level regression that prove auth failures surface from the live path..." | Live-boundary honesty coverage in `tests/test_openai_client.py` and `tests/test_cli.py`; verified later by the `27 passed` session receipt and current repo-visible suite receipts. |
| 2026-05-31T05:33:28Z | `msg_e7c85de290016HgVr21ELJ8jaq` | "tests-first again: tighten deterministic demo card quality so weak claims..." | Weak-claim tightening reflected in `tests/test_validate.py`, `tests/test_cli.py`, and the current offline packet receipts. |
| 2026-05-31T07:50:53Z | `msg_e7d03aea6001IbG7c7Age3ZmEA` | "...with a RED regression first in `tests/test_model_clients.py`..." | Evidence-integrity fix reflected in `tests/test_model_clients.py`, `src/podinsight_mvp/model_clients.py`, and the post-fix `61 passed` / `0 errors` receipts. |
| 2026-05-31T08:52:09Z | `msg_e7d3bc4bf001CYErc3fi4GYTdC` | "The reviewer blocker fix held locally: targeted tests are green, the full suite is now `61 passed`, and typecheck is still `0 errors`." | Final post-fix verification aligned with `docs/podinsight_query_flow_refresh_20260531_pytest.log` and `docs/podinsight_query_flow_refresh_20260531_basedpyright.log`. |

## How to inspect

The cited receipts are inspectable via OpenCode session tooling, for example:

- `session_search(query="RED regression", session_id="ses_1840f8957ffefVlK4XCRJjI47r")`
- `session_search(query="tests-first again", session_id="ses_1840f8957ffefVlK4XCRJjI47r")`
- `session_search(query="transport-level regression", session_id="ses_1840f8957ffefVlK4XCRJjI47r")`
- `session_search(query="61 passed", session_id="ses_1840f8957ffefVlK4XCRJjI47r")`

These receipts are the honest chronology source for the behavior-changing fixes because the formal project path was added to the repository index after the session work had already converged.
