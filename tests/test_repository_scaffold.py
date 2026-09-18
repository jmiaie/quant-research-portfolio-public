from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "README.md",
    "pyproject.toml",
    "requirements-dev.txt",
    "portfolio/financial-dynamics-model.md",
    "portfolio/statistical-arbitrage-engine.md",
    "portfolio/options-volatility-risk-lab.md",
    "research/methodology/research-standards.md",
    "research/methodology/backtesting-standards.md",
    "research/methodology/validation-framework.md",
    "research/methodology/model-risk-checklist.md",
    ".github/workflows/ci.yml",
]


REQUIRED_README_SECTIONS = [
    "# Quantitative Finance Research Portfolio",
    "## Flagship Projects",
    "## Research Capabilities",
    "## Research Standards",
    "## Technology",
    "## Research Roadmap",
    "## About",
    "project-reported until independently reproduced",
]


def test_required_files_exist() -> None:
    for relative_path in REQUIRED_FILES:
        assert (REPO_ROOT / relative_path).is_file(), relative_path


def test_root_readme_contains_key_sections() -> None:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    for section in REQUIRED_README_SECTIONS:
        assert section in readme, section
