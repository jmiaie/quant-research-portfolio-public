# Research Site Roadmap

[Back to roadmap index](README.md) · [Main README](../README.md) · Requirements: [docs/PRD.md](../docs/PRD.md)

This extends [research-roadmap.md](research-roadmap.md); it does not replace it. That roadmap's
Phase 1 ("reproduce and validate existing research") is the foundation for everything here: the
site only publishes what the four reproducibility bundles already verify. Item 2 below
("positive result") is a Phase 3 item of that roadmap ("expand into derivatives").

## Now (0–30 days)

| Deliverable | Exit criterion | Depends on |
| --- | --- | --- |
| MkDocs site scaffold: `mkdocs.yml`, `website/` home, four study pages, verification page | `python -m mkdocs build --strict` passes locally and in CI. **Done in this PR.** | – |
| Study pages pin the reviewed commit from `research/publications.md` | `tests/test_research_site.py` passes. **Done.** | – |
| Pages workflow that builds on PRs and deploys only on manual dispatch | `.github/workflows/pages.yml` build job green. **Done.** | – |
| Honest "claims verified" badge (manual, links to verification page) | Badge text says "manually, at pinned commits". **Done.** | – |
| Conventional `sharpe_ratio` with `rf`; `cagr_volatility_ratio` for the old quantity | Hand-computed tests pass. **Done.** | – |
| Owner enables Pages and picks a licence | Pages source = GitHub Actions; `LICENSE` committed | Owner |
| First deploy | Manual `workflow_dispatch` with `deploy=true` from `main` succeeds | Pages enabled |

## Next (30–60 days)

| Deliverable | Exit criterion | Depends on |
| --- | --- | --- |
| Vendor figures at pinned SHAs (`scripts/sync_site_assets.py`) with sha256 checks against each bundle's declared hashes | Figures embedded on study pages; build fails on hash mismatch | Now |
| Scheduled verifier workflow: one job per satellite, at its pinned SHA, with that study's install step | Writes `website/status/verification.json` (study, SHA, date, exit code, stdout) | Now |
| Badge and verification page read that JSON | Badge shows date and pass/fail per study; a failure is shown as a failure | Verifier workflow |
| Verifier output rendered on each study page | Captured stdout matches expected text in `portfolio/VERIFYING.md` | Verifier workflow |
| `options-risk` packaging clean-up (LICENSE file, URLs, classifiers, trim study drivers from wheel) | `python -m build` + `twine check` pass; clean-venv install runs the test suite | Owner approval, in satellite repo |

## Later (60–90 days)

| Deliverable | Exit criterion | Depends on |
| --- | --- | --- |
| Publish `options-risk` 0.1.0 via TestPyPI then PyPI (Trusted Publishing, tag-triggered) | `pip install options-risk==0.1.0` works in a clean venv | Next packaging item; PyPI name available; owner approval |
| Positive result: implied-vol surface from real option chains, pre-specified question, fifth reproducibility bundle | Offline verifier passes from a fresh clone; site page added | Licensed chain data source (owner decision) |
| Optionally move shared metrics to `quant_research.metrics` and have satellites import it | Satellites' tests pass against the shared module | Owner decision (PRD open question 3) |
| Per-paper PDF (Quarto) only if typeset maths is needed | Decision recorded | Reader feedback |
