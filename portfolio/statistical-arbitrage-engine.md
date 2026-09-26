# Statistical Arbitrage Engine

[Back to main README](../README.md)

## Research Question

Can an event-driven statistical-arbitrage research stack produce more credible spread-trading evaluation by combining rigorous pair selection, signal construction, and execution-aware backtesting?

## Economic Motivation

Relative-value strategies depend on temporary dislocations, mean reversion, and execution quality. A robust research platform should test whether apparent alpha persists after realistic costs, timing constraints, and market frictions.

## Quantitative Methodology

- Pair screening with Benjamini-Hochberg / FDR control
- Engle-Granger cointegration
- ADF stationarity testing (secondary diagnostic)
- Static OLS and sequential Kalman hedge-ratio estimation (explicit `estimation_mode` labels)
- Spread modeling
- Trailing-only z-score signals (current observation excluded from its own mean/std)
- Half-life estimation
- Chronological formation/test separation and walk-forward helpers
- Event-driven backtesting with same-timestamp pair-signal discipline
- Marked-to-market portfolio ledger (cash, exposure, NAV)
- Stylized cost-aware simulated execution (partial fills / VWAP)

## Data

Market-data sourcing, pair universe definition, and historical sampling choices are documented in the reproducibility bundle (`publication/stat-arb-study/`), which maps each reported figure to its source artifact. Public universe examples remain convenience/survivorship-exposed.

## Evaluation Status

- **Evaluation classification: FINAL 2025 WALK-FORWARD EVALUATION** — deliberately *not* described as an "untouched holdout". Earlier design iterations overlapped this period, so the stronger label would be an overclaim.
- **2025 result:** three pure-2025 windows, each with **55 candidate tests, 0 FDR survivors, and 0 trades** — a complete **null** trading outcome.
- **No fabricated metrics:** no Sharpe, drawdown, or turnover figure exists for the 2025 evaluation, and none is claimed.
- The absence of qualifying pairs is reported **neutrally**: multiple-testing control declined to certify any pair, which is the screen working as designed. It is **not** presented as foresight or as a strategy correctly "sitting out" an unfavorable period.
- Re-discovering pairs within each formation window is part of the declared design, **not** hyperparameter reselection.
- Every reference elsewhere on this page to paper/live-trading extensions is **architecture-only**.

## Validation

The research-engine invariant checks are on `main` and covered by the repository's test suite:

1. Same-timestamp pair signals
2. Marked-to-market NAV
3. Decision-time pair research (`as_of_frame` / formation-only cutoffs)
4. Static-vs-sequential-Kalman distinction
5. Correct analytics (NAV-based net return; qualified gross cost add-back)

These checks verify research-engine timing, accounting, and estimation invariants on synthetic/unit fixtures. They do **not** assert empirical out-of-sample trading performance. The out-of-sample study is on `main` under `publication/stat-arb-study/`, with pure-standard-library verifiers that re-check declared artifact hashes, generated files, and map citations — see [Reproducing the Results](VERIFYING.md).

## Risk & Limitations

- Pair selection may be vulnerable to data snooping / convenience-universe bias.
- Execution remains a stylized scenario engine, not empirical microstructure reconstruction.
- Gross return via cost add-back is a **qualified proxy**, not pathwise pre-cost equity.
- Capacity, borrow, and ADV constraints can materially change results.
- Reported performance metrics are traceable to committed artifacts through the bundle's claim-to-evidence table and cross-check; passing those checks is an artifact-integrity result, not a performance claim ([Reproducing the Results](VERIFYING.md)).

## Engineering Architecture

Event-driven research infrastructure with simulated execution, portfolio ledger accounting, Alpaca market-data integration hooks, and an architecture designed to support paper/live-trading extensions without exposing proprietary production details in this hub. That capability is **architecture-only**: it is not a claim of deployment, and no live or paper-traded result is reported.

## Current Status

Final 2025 walk-forward evaluation — no qualifying pairs and no trades, reported as a null outcome. The research-engine invariant checks and the out-of-sample study are on `main`; no empirical out-of-sample performance is claimed.

## Planned Improvements

- Dynamic capacity / ADV and deeper borrow-cost modeling
- Fama-French and factor attribution
- Bootstrap / block-bootstrap confidence intervals
- Regime-conditioned result reporting
- Turnover and strategy capacity analysis beyond current stylized costs

## Repository

- Portfolio summary: this page
- Verification: [Reproducing the Results](VERIFYING.md)
- Source repository: https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public
