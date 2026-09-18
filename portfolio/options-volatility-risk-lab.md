# Options Volatility Risk Lab

[Back to main README](../README.md)

## Research Question

How can a self-contained derivatives and portfolio-risk research system support pricing, volatility analysis, hedging simulation, and portfolio stress testing in a reproducible Python workflow?

## Economic Motivation

Options and portfolio-risk analytics require disciplined modeling of convexity, volatility, tail risk, and exposure aggregation. A dedicated research lab provides a foundation for derivatives evaluation and risk-aware portfolio decision support.

## Quantitative Methodology

Implemented research modules include:

- Black-Scholes-Merton European pricing
- Analytic Greeks with independent finite-difference cross-checks
- Implied-volatility solver with no-arbitrage bounds checking
- Volatility smile / term-structure / surface interpolation
- Risk-neutral GBM Monte Carlo pricing (with SE/CI reporting)
- Discrete delta-hedging simulation (financing, transaction costs, rebalance frequency)
- Portfolio position representation with Greek aggregation
- Full-revaluation stress testing and spot-vol convexity grids
- Greek-based P&L attribution vs. full revaluation
- Historical / Delta-Normal / Monte Carlo VaR and Expected Shortfall
- VaR backtesting diagnostics (Kupiec, Christoffersen, conditional coverage)

## Data

All market data used in tests, examples, and committed results is **synthetic** (seeded fixtures). No live market feeds, brokerage integrations, or invented historical performance numbers are claimed. An optional real-data path may exist as an unused extra; CI does not exercise network calls.

## Validation

Financial invariants are covered by the source repository's automated test suite (pricing parity/bounds, analytic-vs-FD Greeks, IV round-trips, Monte Carlo convergence, portfolio accounting, hedging self-financing identities, VaR/ES closed-form toys, stress/attribution residuals). Example scripts write seeded JSON artifacts under stated assumptions. The publication pack under `publication/options-risk-study/` adds a verifier that regenerates the committed tables and figure byte-identically and re-checks every cited hash — see [Verifying a Pack](VERIFYING.md).

## Risk & Limitations

- Vanilla European options only — no exotics or American exercise.
- Models assume documented idealizations (e.g., constant vol / lognormal diffusion for BSM; linearized exposure for Delta-Normal VaR).
- Synthetic fixtures validate engineering and financial invariants; they are not market evidence.
- Interactive dashboard / lightweight viz layer remains **deferred**.
- Numerical outputs are reproducible from a fresh clone at the recorded tip ([Verifying a Pack](VERIFYING.md)); passing the pack's checks is an artifact-integrity result, not a performance claim.

## Engineering Architecture

Implemented Python package (`options_risk`) with reusable analytics modules, seeded examples, research reports, model-risk documentation, and CI. Dashboard prototyping is deferred pending further validation priorities.

## Current Status

`Available` — implemented research lab (analytics modules and publication pack on `main`); dashboard deferred.

## Planned Improvements

- Optional interactive dashboard for exposure and risk monitoring
- Broader instrument / exercise-style coverage where justified
- Expanded benchmarking and sensitivity templates aligned to hub methodology standards

## Repository

- Portfolio summary: this page
- Verification: [Verifying a Pack](VERIFYING.md)
- Source repository: https://github.com/jmiaie/options-volatility-risk-lab
