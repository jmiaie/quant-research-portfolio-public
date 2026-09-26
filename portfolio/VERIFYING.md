# Reproducing the Results

[Back to main README](../README.md) · [Portfolio projects](README.md)

Each flagship project ships a **reproducibility bundle**: a self-contained directory of reports,
tables, figures, claim-to-evidence tables, and source maps, plus a verifier that re-derives every
cited number and hash from the committed artifacts.

The verifiers are **offline and deterministic**: no network, no credentials, no re-running of
the original study, no re-fitting. Each one **fails closed** — if an artifact drifts, the check
fails with a named reason rather than silently passing. Verification does not require trusting
this hub page: every command below was executed against a fresh clone of the SHA shown.

**Dependencies.** Verification requirements are repository-specific: the Statistical Arbitrage
Engine and ML Sentiment bundles verify with the standard library alone, while the Financial
Dynamics Model bundle needs its `requirements.txt` plus `PyYAML`, and the Options Volatility Risk
Lab bundle needs `.[dev,viz]` (matplotlib). 

## Commands

| Project | Repository | Verified at |
|---|---|---|
| Financial Dynamics Model | [`financial-dynamics-model`](https://github.com/jmiaie/financial-dynamics-model) | `2b0a919e4500dabda3c0b6430494361a50d36e4f` |
| Statistical Arbitrage Engine | [`Advanced_Algorithmic_Trading_Simulator_public`](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public) | `372d5571ca72913ed0c69c53337473ffe63f8c94` |
| Options Volatility Risk Lab | [`options-volatility-risk-lab`](https://github.com/jmiaie/options-volatility-risk-lab) | `8d7f761d6ece8276b529c8ebfaa1cfc32dd74b91` |
| ML Sentiment Augmented Price Predictor | [`ML_Sentiment_Augmented_Price_Predictor`](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor) | `77a2390c460f2c609e5a39c36feed7da56a794e3` |

Clone with full history (no `--depth`), check out the commit in the table (`git checkout <sha>`), then run from the repository root.

### Financial Dynamics Model

```bash
git clone https://github.com/jmiaie/financial-dynamics-model.git
cd financial-dynamics-model
uv venv .venv                                    # or: python3 -m venv .venv
uv pip install --python .venv/bin/python \
  -r publication/historical-regime-study/requirements.txt PyYAML
.venv/bin/python publication/historical-regime-study/scripts/verify_pack.py
```

Expected: `RESULT: all 5 check(s) passed` (citations, figures and tables regenerate
byte-identically, declared hashes, and the no-rerun assertion), exit code 0.

`PyYAML` is required by the table check (`scripts/generate_tables.py` reads a YAML config) and
is **not** listed in that `requirements.txt` at this commit — without it the run ends
`FAIL [tables]: generate_tables.py exited non-zero`. The authoritative description of the check
is `SOURCE-GATE.md` § *Reviewer instructions*; `RESULT-SOURCE-MAP.md` § *How to check a number in
TECHNICAL-PAPER.md* gives a manual number → `row_id` → file → `sha256sum` trace.

### Statistical Arbitrage Engine

```bash
git clone https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public.git
cd Advanced_Algorithmic_Trading_Simulator_public
python3 publication/stat-arb-study/scripts/publication_pack.py check
python3 publication/stat-arb-study/scripts/claim_crosscheck.py
```

Expected (both exit code 0):

```
publication-pack check OK: 13 artifact hashes, 4 generated files, 11 map citations verified
claim cross-check OK: 101 independent assertions passed
```

These verifiers are pure standard library — no install step, no virtualenv. That is specific to this project: the Financial Dynamics Model and Options Volatility Risk Lab bundles both require a documented install step, given in their entries above and below.

### Options Volatility Risk Lab

```bash
git clone https://github.com/jmiaie/options-volatility-risk-lab.git
cd options-volatility-risk-lab
uv venv .venv                                    # or: python3 -m venv .venv
uv pip install --python .venv/bin/python -e ".[dev,viz]"
.venv/bin/python publication/options-risk-study/scripts/verify_pack.py
```

Expected: `All publication-pack verification checks passed.`, exit code 0 — including
byte-identical regeneration of the committed tables and figure.

Matplotlib is required (figure regeneration); a bare interpreter reports
`matplotlib is not importable ... the figure could not be regenerated to verify it` and exits 1
— that is the check failing closed, not a broken artifact. Pinned versions live in
`publication/options-risk-study/requirements.txt`.

### ML Sentiment Augmented Price Predictor

```bash
git clone https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor.git
cd ML_Sentiment_Augmented_Price_Predictor
python3 publication/sentiment-study/scripts/publication_pack.py check
python3 publication/sentiment-study/scripts/claim_crosscheck.py
```

Expected (both exit code 0):

```
check OK: 18 declared artifact hashes verified, 4 generated files byte-identical, 22 map citations verified
claim cross-check OK: 178 independent assertions passed
```

These verifiers are pure standard library. The repository's own suite is
`python -m pip install -e ".[dev,data]"` then `ruff check .`, `mypy src tests`, `pytest`.
A shallow clone will break the package build — clone with full history.

## Scope

Passing these checks means the committed artifacts are internally consistent and reproducible
from a fresh clone at the SHA shown: every cited hash, figure, and table regenerates, and every
cited claim resolves to a source. It does **not** assert out-of-sample trading
performance, and it is not a substitute for reviewing the methodology, the stated limitations,
or the data-provenance and claim-to-evidence documents in each bundle.
