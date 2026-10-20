# PRD: Public Research Site and Shared Metrics Module

[Back to main README](../README.md) · Roadmap: [research-site roadmap](../roadmap/research-site-roadmap.md)

Status: draft for owner review. Every statement about current behaviour below refers to code or
documents in this repository or in the four satellite repositories at the commits cited in
[research/publications.md](../research/publications.md). Items marked **ASSUMPTION** are not
backed by the code and need the owner to confirm them.

## 1. Problem

The four flagship studies are reproducible and honest, but hard to evaluate quickly:

- The evidence is spread across four repositories. A reviewer has to open each repository's
  `publication/<study>/` directory, find `TECHNICAL-PAPER.md`, and work out which commit was
  reviewed. The hub's [publications index](../research/publications.md) and
  [VERIFYING.md](../portfolio/VERIFYING.md) help, but they are long Markdown pages on GitHub.
- Figures are only viewable as files in each satellite's `publication/<study>/figures/`.
- "Verified" status is recorded in prose (VERIFYING.md: "every command below was executed
  against a fresh clone of the SHA shown"), with no date and no machine-readable status.
- All four headline results are null, negative or descriptive. That is the correct reading of
  the evidence, but there is no positive, constructive result alongside them.
- The hub's own `quant_research.portfolio.sharpe_ratio` returned CAGR / annualized volatility,
  which is not a Sharpe ratio. Fixed in this change (see §9). None of the four satellites has its
  own Sharpe/drawdown helper today (searched `src/` for `def sharpe`, `def max_drawdown`,
  `def annualized_vol`), so there is no shared, tested definition to cite.

## 2. Target users

| User | What they need | Evidence that they exist |
| --- | --- | --- |
| Quant hiring manager / interviewer | Judge research judgement and engineering quality in about ten minutes | Stated audience for this work (owner brief). **ASSUMPTION:** no traffic or recruiter data exists. |
| Research collaborator / reviewer | Check a specific number against its source and re-run the verifier | [docs/reviewer-guide.md](reviewer-guide.md) is written for this reader. |
| Python user of `options_risk` | `pip install` the pricing / IV / VaR toolkit without cloning | **ASSUMPTION:** no external users today; the package is not on PyPI. |

## 3. Jobs to be done

1. "When I have a candidate's portfolio open, I want one page that says what each study asked,
   what it found and how sure it is, so I can decide whether to read deeper."
2. "When a number looks interesting, I want to reach the paper section and the committed
   artifact behind it in two clicks."
3. "When I'm told the claims are verified, I want to know when, at which commit, and by what
   command."
4. "When I need BSM pricing, implied vol or VaR backtests, I want to install a tested package."

## 4. Goals and non-goals

**Goals**

- G1. One public site on GitHub Pages: home page, one page per study, a verification page.
- G2. Each study page links the technical paper pinned to the reviewed commit, states the
  headline result with its uncertainty, and gives the verifier command and expected output.
- G3. A "claims verified" badge whose meaning is stated on the page and which is never shown as
  automated until it is.
- G4. A shared, tested metrics module (Sharpe, volatility, drawdown) with conventional definitions.
- G5. A plan to publish `options_risk` to PyPI.
- G6. A plan for one constructive result: an implied-volatility surface built from real option
  chains.

**Non-goals**

- Not a trading product, signal service or performance track record.
- No re-running of studies or re-fitting of models on the site; the site renders committed
  artifacts only.
- No changes to satellite repositories in this change.
- No new performance claims. The site restates what the papers say, with the same caveats.
- No analytics, cookies or contact forms in v1.

## 5. Tool choice: MkDocs (Material) rather than Quarto

Chosen: **MkDocs 1.6.1 + mkdocs-material 9.5.39**, pinned in
[requirements-site.txt](../requirements-site.txt).

- **Content is already Markdown.** The papers, case studies and claim registers are `.md`.
  Quarto's main strength is executing code cells (`.qmd`/notebooks) at render time. That is the
  opposite of what this site needs: the verifiers' contract is "no re-running"; the site should
  render committed artifacts, not recompute them.
- **Installs from PyPI alone.** `pip install -r requirements-site.txt` is enough, so the same
  Python toolchain used for tests builds the site, locally and in CI. Quarto is a separate
  binary (the `quarto-cli` PyPI wheel wraps a platform download), and PDF output would add a
  LaTeX toolchain.
- **Strict link checking.** `mkdocs build --strict` fails on broken internal links, which suits
  a site whose value is that its links resolve.
- **Trade-off accepted:** no native PDF or LaTeX-quality equations. If a paper needs typeset maths
  or a PDF, revisit Quarto for that paper only (see Open questions).

Verified locally: `python -m mkdocs build --strict` builds the scaffold with no warnings.

## 6. User stories and acceptance criteria

**US1 – Study overview (hiring manager).** As a hiring manager, I want the home page to show
each study's question and result in one table.
- AC: The home page lists all four studies, each with the question and a result that uses the
  same wording as the README headline table (descriptive / null / failure to demonstrate).
- AC: Each row links to that study's page. *(Scaffold: done.)*

**US2 – Paper at the reviewed commit (reviewer).** As a reviewer, I want the study page to link
the technical paper at the exact reviewed commit.
- AC: The link's commit SHA equals the one in `research/publications.md`. Enforced by
  `tests/test_research_site.py::test_study_pages_link_paper_at_reviewed_commit`. *(Done.)*

**US3 – Honest badge (both).** As a reader, I want the badge to say what was verified, when and
how.
- AC (v1, done): the badge reads "Claims verified: manually, at pinned commits" and links to a
  page that says it reflects a manual run, not a live status.
- AC (Next): a scheduled workflow runs each satellite's verifier at its pinned SHA, writes a
  dated JSON status file, and the badge text comes from that file. A failing verifier shows as
  failing, never as passing.

**US4 – Figures in place (both).** As a reader, I want to see each study's figures on its page.
- AC: Figures are copied from the satellite at the pinned SHA, with a sha256 check against the
  bundle's declared hashes; the build fails on mismatch. *(Next; v1 links the `figures/`
  directory.)*

**US5 – Verifier output (reviewer).** As a reviewer, I want to see the verifier's actual output.
- AC: Each study page shows the captured stdout of the last verifier run, its date, and the
  commit. *(Next; v1 shows expected output copied from VERIFYING.md.)*

**US6 – Correct metrics (developer).** As a developer, I want `sharpe_ratio` to be the
conventional definition.
- AC: `sharpe_ratio(r, periods_per_year, rf=0.0)` returns
  `mean(r - rf/p) * p / (std(r - rf/p) * sqrt(p))` with sample std; tests check hand-computed
  values; the old CAGR / vol quantity is available as `cagr_volatility_ratio`. *(Done.)*

**US7 – `pip install options-risk` (package user).** See §8.

**US8 – A positive result (hiring manager).** See §8.

## 7. Requirements

**Functional**

- F1. Pages: home, four study pages, verification page (scaffold in `website/`).
- F2. Study page sections: evaluation label, question, result with uncertainty, links (paper,
  case study, claim register or source map, figures), verify commands, expected output.
- F3. Navigation and config in `mkdocs.yml`; site sources in `website/` so `docs/` (this PRD,
  internal guides) is not published.
- F4. `.github/workflows/pages.yml` builds with `--strict` on PRs and pushes touching the site;
  deploys only on manual dispatch with `deploy=true`, from `main`.
- F5. Shared metrics: `quant_research.portfolio` provides `sharpe_ratio`,
  `cagr_volatility_ratio`, `annualized_return`, `annualized_volatility`, `max_drawdown`,
  `performance_summary`. A later step may rename this to `quant_research.metrics` and have the
  satellites import it (Open question 3).

**Non-functional**

- N1. No network at build time beyond `pip install`. No third-party scripts, fonts or images
  loaded at view time (`theme.font: false` disables Material's default Google Fonts).
- N2. Reproducible: pinned site dependencies; build output (`_site/`) ignored by git.
- N3. Accessible: Material's light and dark palettes; every figure gets alt text when embedded.
- N4. Claims parity: no sentence on the site may be stronger than the corresponding paper. Each
  study page cites the paper section it summarises (Next).
- N5. Package CI stays independent: `ci.yml` does not install site dependencies.

## 8. Planned work beyond the scaffold

### 8.1 Publish `options_risk` to PyPI

Grounding: `options-volatility-risk-lab/pyproject.toml` declares `name = "options-risk"`,
`version = "0.1.0"`, `license = { text = "MIT" }`, setuptools `src/` layout, extras `viz`,
`data` (yfinance), `dev`. There is no `LICENSE` file in that repository and no release workflow.

Plan (owner approval needed before any upload):

1. Add a `LICENSE` file matching the declared MIT licence; add `project.urls`, `keywords`, a
   `License ::` classifier and a `Typing :: Typed` classifier with a `py.typed` marker if missing.
2. Decide what ships: `historical_risk_study.py` and `historical_risk_study_v2.py` are study
   drivers, not library API. Either exclude them from the wheel or move them under `scripts/`.
3. Check the name `options-risk` is free on PyPI (not checked here; no network calls were made).
4. Build with `python -m build`, check with `twine check`, install the wheel in a clean venv and
   run the test suite against it.
5. Publish to TestPyPI first, then PyPI, via a tag-triggered workflow using PyPI Trusted
   Publishing (no API token stored in the repository).
6. Exit criterion: `pip install options-risk==0.1.0` in a clean venv, then
   `python -c "import options_risk"` and the package's tests pass.

### 8.2 One positive result: an implied-vol surface from real option chains

Grounding: `options_risk.data.chain` defines a chain schema and `clean_chain`, and states that
real-data loaders are out of CI. `options_risk.volatility.surface` provides
`build_surface_from_chain` and `check_surface_sanity`, and its docstring says no
calendar-spread or butterfly-arbitrage enforcement is implemented. All existing tests use
`synthetic_chain` fixtures.

Plan:

- Question (pre-specify before looking at data): "From end-of-day SPY option chains on a fixed
  set of dates, does the cleaned, solved IV surface show the expected skew and term structure, and
  how many quotes fail cleaning, IV solving or sanity checks?" This is a measurement result, not
  a trading claim.
- Data: **ASSUMPTION / owner decision.** A licensable source of historical chains is needed.
  yfinance gives current snapshots only and its terms restrict redistribution; Cboe DataShop or
  OptionMetrics are licensed. Committed artifacts must respect the licence (possibly derived
  surfaces only, not raw quotes).
- Method: freeze snapshots with sha256 hashes, run `clean_chain` → `build_surface_from_chain` →
  `check_surface_sanity`; add static-arbitrage checks (calendar and butterfly) as reported
  diagnostics; report counts of dropped quotes by reason.
- Deliverable: a fifth reproducibility bundle with the same structure (paper, source map,
  offline verifier) and a site page.
- Exit criterion: the verifier passes from a fresh clone; the paper states what the surface does
  and does not show.

## 9. Fixes shipped with this PRD

- `sharpe_ratio` is now the arithmetic annualized Sharpe ratio with an `rf` argument (annual,
  default 0) and sample standard deviation. The previous quantity is `cagr_volatility_ratio`.
  Tests use hand-computed values. **Effect on published numbers:** no README or results page
  printed a value from this function. The example script's printed Sharpe changes from 0.4776 to
  0.5127 (synthetic data, seed 7); that output is not recorded anywhere in the repository.
- README: CI statement now matches `.github/workflows/ci.yml`; the Financial Dynamics Model row
  says the regime differences are descriptive and not statistically significant; the Options
  Volatility Risk Lab row states the coverage-test sample sizes (95 / 12 / 12) and their low power.
  The same FDM wording was corrected in `research/publications.md`.

## 10. Success metrics

No baseline exists for any of these; targets are for the owner to set.

- Build health: `mkdocs build --strict` passes on every PR touching the site (binary).
- Claims parity: 4 of 4 study pages pin the reviewed commit (enforced by test).
- Verification freshness (Next): days since last automated verifier pass, per study.
- **ASSUMPTION:** reach (page views, referrals from CVs) needs analytics, which is a non-goal
  for v1. Qualitative signal: reviewer or interviewer feedback that cites the site.
- Package (after 8.1): a clean-venv install-and-test job passes for each release.

## 11. Positioning

An evidence-first portfolio: four studies that report null and descriptive results honestly,
each with a fail-closed verifier, plus (once 8.2 lands) one constructive measurement result.
The pitch to a hiring manager is research judgement and reproducibility, not returns. No pricing
applies; everything is public.

## 12. Risks

| Risk | Mitigation |
| --- | --- |
| Site wording drifts from the papers and overstates results | Pin commits; parity test; restate the papers' own caveats; review on every paper update |
| A "verified" badge reads as a performance claim | Badge text and verification page say "artifact integrity, not performance" |
| Automated verifiers need installs (FDM needs PyYAML, options lab needs matplotlib) | Per-study install steps from VERIFYING.md; run each in its own job |
| Hotlinked or vendored figures go stale | Copy at pinned SHA with sha256 checks (US4) |
| Option-chain data licence forbids redistribution | Commit derived surfaces and hashes only; owner decides the source |
| Publishing `options-risk` exposes study-specific modules as API | Trim the wheel before 0.1.0 (§8.1 step 2) |
| No licence on this hub repository | Owner decision (below) |

## 13. Open questions for the owner

1. **Licence for this hub repository** (none today). MIT would match the satellites that declare
   one (`financial-dynamics-model` has a LICENSE file; `options-risk` declares MIT in
   `pyproject.toml`). Not chosen here.
2. Custom domain, or the default `jmiaie.github.io/quant-research-portfolio-public/`?
3. Should the satellites import the hub's metrics module, or should it stay a hub-only reference
   implementation?
4. Which option-chain data source, and what may be committed?
5. Enable Pages with "GitHub Actions" as the source (repository setting, not changed here).
