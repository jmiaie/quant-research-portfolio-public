# Quantitative Finance Research Portfolio

Systematic Research • Financial Modeling • Risk Analytics • Python Engineering

Applied quantitative-finance research portfolio focused on systematic trading, market regime modeling, portfolio risk, derivatives, financial machine learning, and AI-assisted research workflows. This repository is a curated hub for flagship projects, research standards, validation methodology, and selected public-safe research artifacts built with a production-oriented Python mindset.

This repository is intended for review by hiring managers and collaborators who want to see how I structure research, reason about risk, and build reproducible analysis code. It is deliberately designed to demonstrate research quality **without** exposing proprietary trading rules, live integrations, credentials, or production execution details.

## Public-safe / IP boundary

This repository intentionally includes:

- reusable research utilities and research scaffolding
- synthetic data generation and openly specified examples
- risk, portfolio, and regime-analysis building blocks
- validation standards, contributor guidance, tests, and a CI workflow

> **CI status:** a CI workflow is included in this repository. GitHub Actions is currently
> **disabled on this repository pending owner activation**, so no CI run has executed here.
> Every verification claim on this hub was produced by local runs of the commands in
> [portfolio/VERIFYING.md](portfolio/VERIFYING.md) at the SHAs shown there.

This repository intentionally excludes:

- proprietary signal definitions and production thresholds
- broker credentials, API keys, or private datasets
- live trading or order-routing integrations
- production execution playbooks or operational secrets

## Flagship Projects

| Project | Research Domain | Core Methods | Engineering | Status | Repository |
| --- | --- | --- | --- | --- | --- |
| Financial Dynamics Model | Market regime modeling and forecasting | Bayesian inference, financial time-series feature engineering, Markov transitions, calibration, forecasting | Production-oriented Python architecture, benchmarking, visualization, backtesting | Final 2025 holdout characterization | [Portfolio page](portfolio/financial-dynamics-model.md) · [GitHub](https://github.com/jmiaie/financial-dynamics-model) |
| Statistical Arbitrage Engine | Statistical arbitrage and execution research | Pair screening, Engle-Granger cointegration, ADF testing, hedge-ratio estimation, spread modeling, z-score signals, half-life estimation | Event-driven backtesting, simulated execution, paper-trading architecture on `main` | 2025 walk-forward evaluation — no qualifying pairs / no trades | [Portfolio page](portfolio/statistical-arbitrage-engine.md) · [GitHub](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public) |
| Options Volatility Risk Lab | Derivatives, volatility, and portfolio risk research | Black-Scholes-Merton, implied volatility, Greeks, Monte Carlo pricing, hedging, portfolio Greeks, stress testing, VaR/ES | Implemented Python analytics modules (dashboard deferred) | Historical risk evaluation | [Portfolio page](portfolio/options-volatility-risk-lab.md) · [GitHub](https://github.com/jmiaie/options-volatility-risk-lab) |
| ML Sentiment Augmented Price Predictor | Financial ML methodology harness | Point-in-time sentiment alignment, no-leakage features, expanding-window walk-forward, temporal ablations, synthetic methodology runner | Lean validation package with CI and deterministic synthetic artifacts | Historical filing-text evaluation + methodology harness | [Portfolio page](portfolio/ml-sentiment-augmented-price-predictor.md) · [GitHub](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor) |
| Quant Research Scaffold | Public-safe reusable research code | Synthetic data generation, feature engineering, lagged backtesting, inverse-volatility portfolio construction, volatility-regime classification | Lightweight Python package, automated tests, CI, reproducible examples | `Available in this repo` | [`src/quant_research/`](src/quant_research/) · [`examples/synthetic_regime_momentum.py`](examples/synthetic_regime_momentum.py) |

Numerical results referenced by linked repositories should be treated as project-reported until independently reproduced through this portfolio's standardized validation framework. Hub status labels name each project's **evaluation classification**: what was evaluated and how. They do **not** assert empirical out-of-sample trading performance. Passing a project's publication-pack verifier establishes artifact integrity and reproducibility at the cited commit; it does not by itself establish predictive or economic value.

Publication index: [research/publications.md](research/publications.md) — one entry per flagship, with its canonical head, research question, evaluation classification, primary and null findings, principal limitation, and reproduction entrypoint.

## Research Capabilities

- Statistical arbitrage
- Time-series analysis
- Market regime modeling
- Portfolio analytics
- Risk modeling
- Derivatives modeling
- Monte Carlo methods
- Financial machine learning
- AI-assisted financial research
- Backtesting
- Transaction-cost analysis
- Data pipelines
- Quantitative visualization
- Quantitative software engineering

## Research Standards

Portfolio projects are expected to progressively conform to professional quantitative-research standards, including:

- reproducibility
- explicit train/validation/test separation
- no look-ahead bias
- survivorship-bias awareness
- transaction costs
- slippage and realistic execution assumptions
- walk-forward testing
- benchmark comparison
- parameter sensitivity analysis
- statistical uncertainty estimation
- failure-case analysis
- model-risk documentation

See the detailed methodology under [research/methodology](research/methodology/).

## Repository structure

```text
.
├── .github/workflows/ci.yml    # included; Actions currently disabled on this repository
├── docs/
├── examples/
│   └── synthetic_regime_momentum.py
├── portfolio/
├── research/
│   └── methodology/
├── src/quant_research/
│   ├── backtesting.py
│   ├── data.py
│   ├── examples.py
│   ├── features.py
│   ├── portfolio.py
│   └── regimes.py
├── tests/
├── CONTRIBUTING.md
├── pyproject.toml
└── requirements-dev.txt
```

## Supported environment

- Python 3.11 or 3.12
- Lightweight runtime dependencies for the scaffold package: `numpy`, `pandas`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the end-to-end example

```bash
python examples/synthetic_regime_momentum.py
```

The example uses deterministic synthetic price series, computes momentum features, classifies a volatility regime, applies inverse-volatility portfolio scaling, and runs a simple lagged backtest. It is safe to run locally and does not require credentials or external data.

## Quality checks

```bash
python -m ruff check .
python -m mypy src
python -m pytest
```

## Reproducibility expectations

- Examples should run from a fresh checkout after the setup steps above.
- Tests should stay deterministic and avoid network calls.
- Generated notebook outputs, large datasets, and local artifacts should not be committed.
- New public examples should document their data assumptions and research limitations.
- Each flagship project ships a publication pack that a reviewer can reproduce and check from a fresh clone: see [portfolio/VERIFYING.md](portfolio/VERIFYING.md).

## Technology

Python, NumPy, pandas, Pytest, Ruff, mypy, GitHub Actions, Markdown, and reproducible research workflows. Additional linked projects may use broader scientific Python and market-data tooling where documented in their own repositories.

## Research Roadmap

- **Phase 1 — Reproduce and validate existing research:** standardize replication, benchmarking, and evidence quality across current flagship projects.
- **Phase 2 — Upgrade execution and statistical rigor:** improve walk-forward testing, transaction-cost realism, attribution, and uncertainty analysis.
- **Phase 3 — Expand into derivatives, portfolio risk, optimization, and financial ML:** build self-contained new research modules with reusable analytics and reporting standards.

## About

**Jeff Milam, MBA**  
Quantitative Finance | AI Engineering | Technical Transformation

GitHub: https://github.com/jmiaie
