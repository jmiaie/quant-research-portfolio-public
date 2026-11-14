"""Static consistency checks for the MkDocs research-site scaffold.

These do not need MkDocs installed: they parse mkdocs.yml as text and check that
every nav page exists and that each study page links the technical paper at the
same reviewed commit that research/publications.md cites.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = REPO_ROOT / "website"

STUDY_PAGES = {
    "financial-dynamics-model.md": "jmiaie/financial-dynamics-model",
    "statistical-arbitrage-engine.md": "jmiaie/Advanced_Algorithmic_Trading_Simulator_public",
    "options-volatility-risk-lab.md": "jmiaie/options-volatility-risk-lab",
    "ml-sentiment.md": "jmiaie/ML_Sentiment_Augmented_Price_Predictor",
}

PAPER_LINK = re.compile(
    r"https://github\.com/(?P<repo>[\w.-]+/[\w.-]+)/blob/(?P<sha>[0-9a-f]{40})/"
    r"publication/[\w.-]+/TECHNICAL-PAPER\.md"
)


def _nav_pages() -> list[str]:
    text = (REPO_ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    nav = text.split("\nnav:\n", 1)[1].split("\n\n", 1)[0]
    return re.findall(r":\s*([\w./-]+\.md)\s*$", nav, flags=re.MULTILINE)


def _paper_links(text: str) -> dict[str, str]:
    return {m.group("repo"): m.group("sha") for m in PAPER_LINK.finditer(text)}


def test_mkdocs_config_points_at_website_dir() -> None:
    text = (REPO_ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    assert re.search(r"^docs_dir: website$", text, flags=re.MULTILINE)
    assert re.search(r"^site_dir: _site$", text, flags=re.MULTILINE)


def test_every_nav_page_exists_and_every_study_is_in_nav() -> None:
    pages = _nav_pages()
    assert "index.md" in pages
    for page in pages:
        assert (SITE_DIR / page).is_file(), page
    for study in STUDY_PAGES:
        assert f"studies/{study}" in pages, study


def test_study_pages_link_paper_at_reviewed_commit() -> None:
    reviewed = _paper_links((REPO_ROOT / "research/publications.md").read_text(encoding="utf-8"))
    for page, repo in STUDY_PAGES.items():
        links = _paper_links((SITE_DIR / "studies" / page).read_text(encoding="utf-8"))
        assert repo in links, f"{page} does not link the {repo} technical paper"
        assert links[repo] == reviewed[repo], f"{page} pins a different commit than publications.md"


def test_badge_is_not_presented_as_automated() -> None:
    index = (SITE_DIR / "index.md").read_text(encoding="utf-8")
    assert "Claims verified: manually, at pinned commits" in index
    assert "(verification.md)" in index


def test_pages_workflow_never_deploys_automatically() -> None:
    workflow = (REPO_ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    assert "mkdocs build --strict" in workflow
    deploy_if = re.search(r"^  deploy:\n    if: (.+)$", workflow, flags=re.MULTILINE)
    assert deploy_if is not None
    assert "workflow_dispatch" in deploy_if.group(1)
    assert "inputs.deploy" in deploy_if.group(1)
