import sys
from pathlib import Path

import pytest


SRC_ROOT = Path(__file__).resolve().parents[1] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


@pytest.fixture
def workspace_root() -> Path:
    return Path(__file__).resolve().parents[3]


@pytest.fixture
def project_root() -> Path:
    return Path(__file__).resolve().parents[1]
