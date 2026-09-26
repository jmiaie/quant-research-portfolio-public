# ML Sentiment Augmented Price Predictor

[Back to main README](../README.md)

## Research Question

Does point-in-time sentiment add incremental predictive information beyond market-only features for short-horizon asset returns — and can that question be tested without leakage?

## Economic Motivation

Sentiment features are easy to misuse: publication latency, session boundaries, and feature construction can leak future information into training labels. A credible methodology harness should enforce decision-time availability before any claim about incremental predictive value.

## Quantitative Methodology

This page describes a **methodology harness** *and* an accepted **historical filing-text evaluation** (no historical alpha is claimed):

- Point-in-time sentiment event schema (publication, ingestion, availability, timezone, model version, confidence, `effective_trading_timestamp`)
- Deterministic US regular-hours session alignment (before-open, intraday, after-close, weekend/holiday mapping)
- Leakage-safe trailing market and sentiment feature generation
- Decision-time-safe labels (primary next-session direction; documented secondary horizon)
- Expanding-window walk-forward validation with horizon-driven embargo/gap handling
- Ablations on identical out-of-sample periods: majority baseline, market-only, sentiment-only, and combined logistic regression
- Classification metrics, log loss, Brier score, and calibration-table data
- Deterministic synthetic methodology validation runner and artifacts

## Data

The repository now contains both a deterministic synthetic methodology harness and an accepted historical filing-text evaluation. The study uses a documented twelve-issuer SEC filing corpus and corresponding market data. The 2025 block is a previously inspected / historical evaluation (**n = 197**), not an untouched holdout. No paid APIs, credentials, network downloads, or GPU requirements are required for CI.

## Evaluation Status

- **Evaluation classification: PREVIOUSLY INSPECTED / HISTORICAL EVALUATION** — not an untouched holdout.
- **Two evidence layers.** A deterministic **synthetic methodology harness**, and an accepted **historical filing-text evaluation** over a documented twelve-issuer SEC filing corpus (2,349 filing events) with corresponding market data.
- **2025 primary result (n = 197).** Adding Loughran-McDonald filing-text features did **not** demonstrate incremental predictive value beyond the market-only feature set under the pre-specified log-loss comparison: delta log loss (m3 - m1) `+0.0040902`, block-bootstrap 95% interval `[-0.0048506, +0.0108001]` (**includes zero**); balanced-accuracy delta `-0.0274725275`.
- **Not claimed:** that filing text is universally useless or harmful; that the market-only model is proven predictive; or that the effect is proven exactly zero.
- No historical alpha is claimed. The synthetic harness remains useful as methodology validation, but it is no longer the repository's only evidence layer.

## Validation

Source-repository tests cover calendar alignment, features, modeling, and validation helpers. The synthetic runner writes an artifact explicitly labeled as synthetic methodology validation and must not be read as historical evidence. The reproducibility bundle under `publication/sentiment-study/` adds standard-library verifiers that re-check declared artifact hashes, byte-identical regeneration, and map citations — see [Reproducing the Results](VERIFYING.md).

## Risk & Limitations

- **No historical sentiment alpha is claimed.**
- Adding filing-text features did **not** demonstrate incremental predictive value over market-only features in the pre-specified 2025 comparison, and the confidence interval includes zero. That is a failure to demonstrate, **not** a claim that filing text is harmful or useless, and **not** a claim that the effect is exactly zero.
- Synthetic ablation outputs validate methodology plumbing only; the historical study is the repository's accepted evidence layer.
- Economic-performance headlines (e.g., Sharpe) remain out of scope: none is computed or claimed.
- Session rules assume a documented US regular-hours calendar; other venues require explicit remapping.

## Engineering Architecture

Lean Python package (`quant_sentiment`) with CI, truthful README positioning, research notes on model risk / leakage controls, and a reproducible synthetic validation entrypoint.

## Current Status

Historical filing-text evaluation + methodology harness — point-in-time / no-leakage / ablation framework and an accepted historical filing-text study on `main`; no historical alpha claims.

## Planned Improvements

- Extend the accepted historical filing-text study to further point-in-time corpora where reproducible data exists
- Extended model families only with matching leakage and ablation controls
- Stronger calibration and uncertainty reporting under hub methodology standards

## Repository

- Portfolio summary: this page
- Verification: [Reproducing the Results](VERIFYING.md)
- Source repository: https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor
