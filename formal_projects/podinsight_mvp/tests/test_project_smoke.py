from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_project_scaffold_exists() -> None:
    expected = [
        PROJECT_ROOT / "AGENTS.md",
        PROJECT_ROOT / "README.md",
        PROJECT_ROOT / "pyproject.toml",
        PROJECT_ROOT / ".env.example",
        PROJECT_ROOT / "data" / "demo_episode_ids.json",
        PROJECT_ROOT / "data" / "topic_aliases.json",
    ]
    missing = [str(path.relative_to(PROJECT_ROOT)) for path in expected if not path.exists()]
    assert not missing, f"missing scaffold files: {missing}"
