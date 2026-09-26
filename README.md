# Quantitative Finance Research Portfolio

Systematic Research • Financial Modeling • Risk Analytics • Python Engineering

Independent quantitative-finance research across market regimes, statistical arbitrage, derivatives risk, and financial machine learning. Each project is a separate repository with its own tests, a pre-specified historical study, and an offline check that reproduces every reported number from committed artifacts.

## Headline findings

| Project | What was tested | Result |
| --- | --- | --- |
| Financial Dynamics Model | Do Bayesian regime labels separate forward risk on a 2025 holdout? | Risk characteristics differ measurably across regimes (descriptive); no predictive edge claimed. |
| Statistical Arbitrage Engine | Does a cointegration + FDR-controlled pair screen find tradable pairs in 2025? | **Null:** 3 walk-forward windows × 55 tests, 0 FDR survivors, 0 trades. Multiple-testing control declined to certify any pair. |
| Options Volatility Risk Lab | How do VaR/ES methods and discrete delta hedging behave on real 2015–2025 SPY paths? | Kupiec/Christoffersen-backtested comparison on a hypothetical book; an earlier method-divergence finding was traced to a volatility-units bug and withdrawn. |
| Sentiment study | Does filing-text sentiment add information beyond market-only features? | **Failure to demonstrate:** Δ log loss +0.0041, 95% CI [−0.0049, +0.0108], n = 197 — too small to rule out a small effect. |

Null and negative results are reported as found. Full write-ups, evidence links, and reproduction commands: [research/publications.md](research/publications.md).

## Flagship Projects

| Project | Research Domain | Core Methods | Engineering | Status | Repository |
| --- | --- | --- | --- | --- | --- |
| Financial Dynamics Model | Market regime modeling and forecasting | Bayesian inference, financial time-series feature engineering, Markov transitions, calibration, forecasting | Typed, tested Python package; benchmarking, visualization, backtesting | Final 2025 holdout characterization | [Portfolio page](portfolio/financial-dynamics-model.md) · [GitHub](https://github.com/jmiaie/financial-dynamics-model) |
| Statistical Arbitrage Engine | Statistical arbitrage and execution research | Pair screening, Engle-Granger cointegration, ADF testing, hedge-ratio estimation, spread modeling, z-score signals, half-life estimation | Event-driven backtesting, simulated execution, paper-trading architecture on `main` | 2025 walk-forward evaluation — no qualifying pairs / no trades | [Portfolio page](portfolio/statistical-arbitrage-engine.md) · [GitHub](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public) |
| Options Volatility Risk Lab | Derivatives, volatility, and portfolio risk research | Black-Scholes-Merton, implied volatility, Greeks, Monte Carlo pricing, hedging, portfolio Greeks, stress testing, VaR/ES | Implemented Python analytics modules (dashboard deferred) | Historical risk evaluation | [Portfolio page](portfolio/options-volatility-risk-lab.md) · [GitHub](https://github.com/jmiaie/options-volatility-risk-lab) |
| ML Sentiment Augmented Price Predictor | Financial ML / filing-text evaluation | Point-in-time sentiment alignment, no-leakage features, expanding-window walk-forward, temporal ablations, synthetic methodology runner | Lean validation package with CI and deterministic synthetic artifacts | Historical filing-text evaluation + methodology harness | [Portfolio page](portfolio/ml-sentiment-augmented-price-predictor.md) · [GitHub](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor) |

Figures are project-reported until independently reproduced (see [Reproducing the Results](portfolio/VERIFYING.md)). Status labels describe what was evaluated and how; none asserts live or out-of-sample trading performance. Passing a project's reproducibility check establishes that its artifacts are consistent at the cited commit, not that the strategy has predictive or economic value.

Supporting code in this repository: [`src/quant_research/`](src/quant_research/) — a small tested package (synthetic data, features, lagged backtest, inverse-volatility sizing, volatility regimes) with a runnable [example](examples/synthetic_regime_momentum.py).

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
├── .github/workflows/ci.yml
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

Run locally (GitHub Actions is not enabled on this repository):

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
- Each flagship project ships a reproducibility bundle that a reviewer can check from a fresh clone: see [portfolio/VERIFYING.md](portfolio/VERIFYING.md).

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
