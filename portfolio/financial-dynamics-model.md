# Financial Dynamics Model

[Back to main README](../README.md)

## Research Question

Can Bayesian and system-dynamics-inspired modeling improve market regime classification, risk conditioning, and forward-looking scenario analysis for financial time series?

## Economic Motivation

Market behavior is non-stationary, path-dependent, and regime-sensitive. A credible regime model can support allocation, hedging, and risk-aware strategy design when it identifies changes in market structure earlier than static models.

## Quantitative Methodology

- Financial time-series feature engineering
- Bayesian inference
- Markov transitions
- Regime classification
- Calibration and forecasting
- Benchmark comparison and backtesting

## Data

Time-series inputs, feature definitions, and sampling decisions are documented in the source repository's publication pack (`SOURCE-GATE.md`), which records the inputs, transformations, and sampling choices behind the committed results.

## Evaluation Status

- **Evaluation classification: FINAL 2025 HOLDOUT EVALUATION.** The holdout audit is **CLEAR**.
- **What the study is:** a descriptive **regime and risk characterization** — how risk characteristics differ across identified market regimes.
- **What it is not:** no statistically validated predictive edge is claimed, and no directional-accuracy or trading-alpha figure is asserted.
- Robustness work (cross-asset QQQ / IWM / TLT / GLD, and the SPY-v2 line) is labeled **post-primary**: it supports the primary characterization and is not an independent confirmation of predictive skill.
- **Sparse-cell limitation:** cells whose regime occurrence count falls below 20 are reported under a `min(20, n)` rule. A **174-row sparse-cell bootstrap disclosure table** (the `sparse_cell.*` rows of `tables/source_map.json`) records every affected interval, and the technical paper states that the effective block equals `n` in those rows, so those intervals are degenerate or near-degenerate rather than evidence of stability. The pack's wider result-source map contains 469 rows in total.
- **No prospective or live-market claim is made.**

## Validation

Repository outputs are reproducible from a fresh clone: the publication pack ships a verifier that re-derives every cited figure, table, and hash from the committed artifacts. See [Verifying a Pack](VERIFYING.md).

## Risk & Limitations

- Regime definitions may be specification-sensitive.
- Forecast quality can degrade under structural breaks.
- Calibration choices may materially affect transition behavior.
- Numerical results are reproducible from a fresh clone at the recorded tip ([Verifying a Pack](VERIFYING.md)); passing the pack's checks is an artifact-integrity result, not a performance claim.

## Engineering Architecture

Production-oriented Python research architecture with modular analytics, calibration workflows, visualization, and benchmarking support. The publication pack under `publication/` adds a technical paper, a claim register, a source gate, and a 174-row sparse-cell bootstrap disclosure table (the wider result-source map it draws on contains 469 rows).

## Current Status

Final 2025 holdout characterization — a descriptive regime and risk study. The publication pack (technical paper, claim register, source gate, result tables) is on `main` with a passing verifier; no predictive-edge or trading-alpha claim is made, and validation standardization continues.

## Planned Improvements

- Standardize benchmark comparisons and out-of-sample reporting
- Add parameter sensitivity and uncertainty reporting
- Document failure modes and model-risk controls

## Repository

- Portfolio summary: this page
- Verification: [Verifying a Pack](VERIFYING.md)
- Source repository: https://github.com/jmiaie/financial-dynamics-model
