import os
import subprocess
import sys


def test_streamlit_entry_imports_from_project_root(project_root) -> None:
    env = os.environ.copy()
    result = subprocess.run(
        [sys.executable, "streamlit_app.py"],
        cwd=project_root,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
