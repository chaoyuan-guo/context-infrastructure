from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


class FileCache:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def _key_to_path(self, namespace: str, payload: dict[str, Any]) -> Path:
        encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
        digest = hashlib.sha256(encoded).hexdigest()
        return self.root / namespace / f"{digest}.json"

    def get(self, namespace: str, payload: dict[str, Any]) -> Any | None:
        path = self._key_to_path(namespace, payload)
        if not path.exists():
            return None
        return json.loads(path.read_text(encoding="utf-8"))

    def set(self, namespace: str, payload: dict[str, Any], value: Any) -> Any:
        path = self._key_to_path(namespace, payload)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
        return value
