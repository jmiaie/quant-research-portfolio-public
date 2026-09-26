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

The repository uses both deterministic synthetic fixtures and a documented historical risk-factor dataset. **Synthetic fixtures** are used for unit tests and methodology validation. The accepted historical study uses historical **SPY, DGS3MO, and VIXCLS** risk-factor data to evaluate a hypothetical nonlinear option portfolio on historical underlying, risk-free-rate, and volatility-index paths. It does not reconstruct historical option quotes and does not claim historical options-tape P&L, and it is not a live or deployed options-trading result. No live market feeds or brokerage integrations are used, and no invented performance numbers are claimed.

## Evaluation Status

- **Evaluation classification: HISTORICAL EVALUATION.**
- **Two evidence layers, distinct in kind.** Deterministic **synthetic fixtures** are used for unit tests and methodology validation. The accepted historical study evaluates a **hypothetical** nonlinear option portfolio on historical underlying, risk-free-rate, and volatility-index paths (SPY, DGS3MO, VIXCLS risk-factor data).
- It does **not** reconstruct historical option quotes and does **not** claim historical options-tape P&L. The option portfolio is hypothetical, and this is **not** a live or deployed options-trading result.
- **Volatility treatment (corrected):** BSM option pricing receives *annualized* volatility; the one-day Delta-Normal and Monte Carlo VaR/ES legs receive *daily factor* volatility; Historical Simulation does not depend on that volatility input.
- **Withdrawn:** the previously reported order-of-magnitude divergence between risk methods was largely a **volatility-units defect**. That explanation is withdrawn and is not restated as a finding.
- Nonlinear / convexity interpretation is **consistent-with** language, not a proven causal decomposition.
- Corrected results and limitations live in the reproducibility bundle (`publication/options-risk-study/`).

## Validation

Financial invariants are covered by the source repository's automated test suite (pricing parity/bounds, analytic-vs-FD Greeks, IV round-trips, Monte Carlo convergence, portfolio accounting, hedging self-financing identities, VaR/ES closed-form toys, stress/attribution residuals). Example scripts write seeded JSON artifacts under stated assumptions. The reproducibility bundle under `publication/options-risk-study/` adds a verifier that regenerates the committed tables and figure byte-identically and re-checks every cited hash — see [Reproducing the Results](VERIFYING.md).

## Risk & Limitations

- Vanilla European options only — no exotics or American exercise.
- Models assume documented idealizations (e.g., constant vol / lognormal diffusion for BSM; linearized exposure for Delta-Normal VaR).
- Synthetic fixtures validate engineering and financial invariants; they are not market evidence. The added historical evidence is a *historical evaluation* of a hypothetical portfolio, and is not options-tape P&L.
- Interactive dashboard / lightweight viz layer remains **deferred**.
- Numerical outputs are reproducible from a fresh clone at the recorded tip ([Reproducing the Results](VERIFYING.md)); passing the bundle's checks is an artifact-integrity result, not a performance claim.

## Engineering Architecture

Implemented Python package (`options_risk`) with reusable analytics modules, seeded examples, research reports, model-risk documentation, and CI. Dashboard prototyping is deferred.

## Current Status

Historical risk evaluation — implemented research lab with an accepted historical study and its reproducibility bundle on `main`. The option portfolio is hypothetical; no options-tape P&L and no live-deployment implication. Dashboard deferred.

## Planned Improvements

- Optional interactive dashboard for exposure and risk monitoring
- Broader instrument / exercise-style coverage where justified
- Expanded benchmarking and sensitivity templates aligned to hub methodology standards

## Repository

- Portfolio summary: this page
- Verification: [Reproducing the Results](VERIFYING.md)
- Source repository: https://github.com/jmiaie/options-volatility-risk-lab
