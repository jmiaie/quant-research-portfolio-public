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
    "research/publications.md",
    "docs/reviewer-guide.md",
    ".github/workflows/ci.yml",
]


REQUIRED_README_SECTIONS = [
    "# Quantitative Finance Research Portfolio",
    "## Headline findings",
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


def test_publications_index_lists_four_flagships() -> None:
    text = (REPO_ROOT / "research/publications.md").read_text(encoding="utf-8")
    for name in (
        "Financial Dynamics Model",
        "Statistical Arbitrage Engine",
        "Options Volatility Risk Lab",
        "ML Sentiment Augmented Price Predictor",
    ):
        assert name in text, name


def test_readme_ci_statement_matches_workflow() -> None:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert (REPO_ROOT / ".github/workflows/ci.yml").is_file()
    # Actions is disabled for this repo; the README must not claim CI runs.
    assert "currently disabled" in readme
    assert ".github/workflows/ci.yml" in readme


def test_readme_does_not_overstate_headline_findings() -> None:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    # FDM: bootstrap intervals include zero, so the difference is descriptive only.
    assert "differ measurably" not in readme
    assert "not statistically significant" in readme
    # Options lab: coverage tests on 12 monthly forecasts must state the sample size.
    assert "n = 12" in readme
    assert "low power" in readme
