# ML Sentiment Augmented Price Predictor

[Back to main README](../README.md)

## Research Question

Does point-in-time sentiment add incremental predictive information beyond market-only features for short-horizon asset returns — and can that question be tested without leakage?

## Economic Motivation

Sentiment features are easy to misuse: publication latency, session boundaries, and feature construction can leak future information into training labels. A credible methodology harness should enforce decision-time availability before any claim about incremental predictive value.

## Quantitative Methodology

This page describes a **methodology harness**, not a historical-alpha study:

- Point-in-time sentiment event schema (publication, ingestion, availability, timezone, model version, confidence, `effective_trading_timestamp`)
- Deterministic US regular-hours session alignment (before-open, intraday, after-close, weekend/holiday mapping)
- Leakage-safe trailing market and sentiment feature generation
- Decision-time-safe labels (primary next-session direction; documented secondary horizon)
- Expanding-window walk-forward validation with horizon-driven embargo/gap handling
- Ablations on identical out-of-sample periods: majority baseline, market-only, sentiment-only, and combined logistic regression
- Classification metrics, log loss, Brier score, and calibration-table data
- Deterministic synthetic methodology validation runner and artifacts

## Data

Current public workflows use deterministic **synthetic** methodology validation. Historical results remain pending a reproducible point-in-time dataset. No paid APIs, credentials, network downloads, or GPU requirements are required for CI.

## Validation

Source-repository tests cover calendar alignment, features, modeling, and validation helpers. The synthetic runner writes an artifact explicitly labeled as synthetic methodology validation and must not be read as historical evidence. The publication pack under `publication/sentiment-study/` adds standard-library verifiers that re-check declared artifact hashes, byte-identical regeneration, and map citations — see [Verifying a Pack](VERIFYING.md).

## Risk & Limitations

- **No historical sentiment alpha is claimed.**
- Synthetic ablation outputs validate methodology plumbing only.
- Real point-in-time sentiment corpora, economic-performance headlines (e.g., Sharpe), and richer model families are out of scope until reproducible evidence exists.
- Session rules assume a documented US regular-hours calendar; other venues require explicit remapping.

## Engineering Architecture

Lean Python package (`quant_sentiment`) with CI, truthful README positioning, research notes on model risk / leakage controls, and a reproducible synthetic validation entrypoint.

## Current Status

`Methodology harness` — point-in-time / no-leakage / ablation framework on `main`; no historical alpha claims.

## Planned Improvements

- Reproducible point-in-time historical dataset integration (when available)
- Extended model families only with matching leakage and ablation controls
- Stronger calibration and uncertainty reporting under hub methodology standards

## Repository

- Portfolio summary: this page
- Verification: [Verifying a Pack](VERIFYING.md)
- Source repository: https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor
