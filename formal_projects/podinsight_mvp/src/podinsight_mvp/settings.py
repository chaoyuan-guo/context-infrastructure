from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class ModelEndpointConfig:
    base_url: str
    api_key: str
    model: str


@dataclass(frozen=True)
class AppSettings:
    chat_base_url: str
    chat_api_key: str
    heavy_model: str
    light_model: str
    embedding_base_url: str
    embedding_model: str
    cache_dir: Path


def load_settings(project_root: Path) -> AppSettings:
    return AppSettings(
        chat_base_url=os.getenv("PODINSIGHT_CHAT_BASE_URL", "http://10.0.34.62:9200/v1"),
        chat_api_key=os.getenv("PODINSIGHT_CHAT_API_KEY", ""),
        heavy_model=os.getenv("PODINSIGHT_HEAVY_MODEL", "deepseek-v4-pro"),
        light_model=os.getenv("PODINSIGHT_LIGHT_MODEL", "deepseek-v4-flash"),
        embedding_base_url=os.getenv("PODINSIGHT_EMBEDDING_BASE_URL", "http://10.0.34.60:8034/v1"),
        embedding_model=os.getenv("PODINSIGHT_EMBEDDING_MODEL", "Qwen3-Embedding-0.6B"),
        cache_dir=project_root / os.getenv("PODINSIGHT_CACHE_DIR", "data/cache"),
    )
