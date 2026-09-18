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

Market-data sourcing, pair universe definition, and historical sampling choices are documented in the publication pack (`publication/stat-arb-study/`), which maps each reported figure to its source artifact. Public universe examples remain convenience/survivorship-exposed.

## Validation

Release gates are on `main` (squash merge of PR #6 @ `e23f33beee752e5d00d736571ac70aba12afd7d0`; pre-merge head `01907515f38bbe36782c0e74a2fbdc7f6f6dd573`), covered by `tests/test_directive3_gates.py`:

1. Same-timestamp pair signals
2. Marked-to-market NAV
3. Decision-time pair research (`as_of_frame` / formation-only cutoffs)
4. Static-vs-sequential-Kalman distinction
5. Correct analytics (NAV-based net return; qualified gross cost add-back)

These gates verify research-engine timing, accounting, and estimation invariants on synthetic/unit fixtures. They do **not** assert empirical out-of-sample trading performance. The out-of-sample experiment pack is on `main` under `publication/stat-arb-study/`, with pure-standard-library verifiers that re-check declared artifact hashes, generated files, and map citations — see [Verifying a Pack](VERIFYING.md).

## Risk & Limitations

- Pair selection may be vulnerable to data snooping / convenience-universe bias.
- Execution remains a stylized scenario engine, not empirical microstructure reconstruction.
- Gross return via cost add-back is a **qualified proxy**, not pathwise pre-cost equity.
- Capacity, borrow, and ADV constraints can materially change results.
- Reported performance metrics are traceable to committed artifacts through the pack's claim register and cross-check; passing those checks is an artifact-integrity result, not a performance claim ([Verifying a Pack](VERIFYING.md)).

## Engineering Architecture

Event-driven research infrastructure with simulated execution, portfolio ledger accounting, Alpaca market-data integration hooks, and an architecture designed to support paper/live-trading extensions without exposing proprietary production details in this hub.

## Current Status

`Available` (research engine) — D3 release gates and the out-of-sample experiment pack are on `main`; no empirical OOS performance claims.

## Planned Improvements

- Dynamic capacity / ADV and deeper borrow-cost modeling
- Fama-French and factor attribution
- Bootstrap / block-bootstrap confidence intervals
- Regime-conditioned result reporting
- Turnover and strategy capacity analysis beyond current stylized costs

## Repository

- Portfolio summary: this page
- Verification: [Verifying a Pack](VERIFYING.md)
- Source repository: https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public
