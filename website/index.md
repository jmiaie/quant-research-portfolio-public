# Micap AI Quantitative Research

[Claims verified: manually, at pinned commits](verification.md){ .md-button title="Each study's offline verifier was run from a fresh clone of the pinned commit. Automated re-verification is a roadmap item." }

Four pre-specified studies across market regimes, statistical arbitrage, derivatives risk and
financial machine learning. Each study lives in its own repository with a technical paper, a
claim-to-evidence map and an **offline verifier** that re-derives every cited number, table,
figure and hash from committed artifacts.

!!! note "What the badge means"
    "Claims verified" means the study's committed artifacts are internally consistent at the
    pinned commit: tables regenerate byte-identically, figures pass that study's rendering check, and
    every cited hash matches. It does **not** mean the strategy or model
    has predictive or economic value. Today the badge reflects a manual run recorded in
    [How verification works](verification.md); an automated, dated badge is planned.

## Studies

| Study | Question | Result |
| --- | --- | --- |
| [Financial Dynamics Model](studies/financial-dynamics-model.md) | Do Bayesian regime labels separate forward risk on a 2025 holdout? | Regime-conditional risk is reported descriptively; bootstrap intervals include zero. Whether the labels beat a simple trailing-volatility bucket has not been tested. No predictive edge claimed. |
| [Statistical Arbitrage Engine](studies/statistical-arbitrage-engine.md) | Does a cointegration + FDR pair screen find tradable pairs in 2025? | **Null:** 3 windows × 55 tests, 0 FDR survivors, 0 trades. No candidate met the pre-specified threshold. |
| [Options Volatility Risk Lab](studies/options-volatility-risk-lab.md) | How do VaR/ES methods behave on real 2015–2025 SPY paths for a hypothetical book? | Method comparison; coverage tests on n = 12 monthly forecasts per year are low-power. An earlier divergence finding was a units bug and is withdrawn. |
| [ML Sentiment Study](studies/ml-sentiment.md) | Does filing-text sentiment add information beyond market-only features? | **Failure to demonstrate:** Δ log loss +0.0041, 95% CI [−0.0049, +0.0108], n = 197. |

Null and negative results are reported as found. These are independent research projects; none
represents live trading or deployed capital.

## Corrections

A review on 2026-11-14 found statements in all four studies that needed correcting. The frozen
artifacts and their hashes are unchanged. Each study page lists its corrections, and the full list is
in the [publication index](https://github.com/jmiaie/quant-research-portfolio-public/blob/main/research/publications.md#corrections-and-known-limitations-2026-11-14).

## How this was built

Research questions, study designs and acceptance criteria are set by Micap AI. Implementation,
testing and review are carried out with AI coding and review agents, with separate author, reviewer
and verifier roles and fail-closed checks.

**Disclaimer.** Research and educational material only. Nothing on this site is investment advice,
a recommendation to trade, or a trading signal service; every number is a model output under stated
assumptions.

## Source

The hub repository holds the publication index, methodology standards and this site:
[jmiaie/quant-research-portfolio-public](https://github.com/jmiaie/quant-research-portfolio-public).
