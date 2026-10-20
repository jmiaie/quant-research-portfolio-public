# Quantitative Finance Research

[Claims verified: manually, at pinned commits](verification.md){ .md-button title="Each study's offline verifier was run from a fresh clone of the pinned commit. Automated re-verification is a roadmap item." }

Four pre-specified studies across market regimes, statistical arbitrage, derivatives risk and
financial machine learning. Each study lives in its own repository with a technical paper, a
claim-to-evidence map and an **offline verifier** that re-derives every cited number, table,
figure and hash from committed artifacts.

!!! note "What the badge means"
    "Claims verified" means the study's committed artifacts are internally consistent and
    regenerate byte-identically at the pinned commit. It does **not** mean the strategy or model
    has predictive or economic value. Today the badge reflects a manual run recorded in
    [How verification works](verification.md); an automated, dated badge is planned
    (see the hub's research-site roadmap).

## Studies

| Study | Question | Result |
| --- | --- | --- |
| [Financial Dynamics Model](studies/financial-dynamics-model.md) | Do Bayesian regime labels separate forward risk on a 2025 holdout? | Risk characteristics differ descriptively; not statistically significant (bootstrap intervals include zero). No predictive edge claimed. |
| [Statistical Arbitrage Engine](studies/statistical-arbitrage-engine.md) | Does a cointegration + FDR pair screen find tradable pairs in 2025? | **Null:** 3 windows × 55 tests, 0 FDR survivors, 0 trades. |
| [Options Volatility Risk Lab](studies/options-volatility-risk-lab.md) | How do VaR/ES methods behave on real 2015–2025 SPY paths for a hypothetical book? | Method comparison; coverage tests on n = 12 monthly forecasts per year are low-power. An earlier divergence finding was a units bug and is withdrawn. |
| [ML Sentiment Study](studies/ml-sentiment.md) | Does filing-text sentiment add information beyond market-only features? | **Failure to demonstrate:** Δ log loss +0.0041, 95% CI [−0.0049, +0.0108], n = 197. |

Null and negative results are reported as found. These are independent research projects; none
represents live trading, deployed capital or institutional employment.

## Source

The hub repository holds the publication index, methodology standards and this site:
[jmiaie/quant-research-portfolio-public](https://github.com/jmiaie/quant-research-portfolio-public).
