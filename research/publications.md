# Publication Index

[Back to main README](../README.md)

These are independent quantitative-research projects. They do not represent
institutional quantitative employment, hedge-fund deployment, live production
alpha, or real-capital strategy deployment. Passing a publication-pack verifier
establishes artifact integrity and reproducibility at the cited commit; it does
not independently establish predictive or economic value.

Each flagship below ships a **publication pack**: a technical paper, a case study, a
claim register, a source gate, a result-source map, and an **offline verifier** that
re-derives every cited figure, table, and hash from the committed artifacts. Dependencies are
**repository-specific, not uniform**: two packs verify with the standard library alone, two
require a documented install step (see [Verifying a Pack](../portfolio/VERIFYING.md)). The packs are
on each repository's `main` branch. Directive #10 program sign-off remains pending; nothing
here is a sign-off.

**How to verify any pack.** Clone the repository, check out the canonical head listed below,
then run that project's reproduction entrypoint (offline — no network, no credentials; the
install step is repository-specific and given in the Verifying a Pack entry for that project). A passing run reproduces the committed tables and figures byte-identically and
re-checks every cited artifact hash. See [Verifying a Pack](../portfolio/VERIFYING.md) for the general
procedure. A pass establishes *artifact integrity at that commit* — not performance.

---

## 1. Financial Dynamics Model

- **Repository:** [`jmiaie/financial-dynamics-model`](https://github.com/jmiaie/financial-dynamics-model)
- **Canonical `main` head at time of writing** (verify the current value with `git ls-remote`): `2b0a919e4500dabda3c0b6430494361a50d36e4f`
- **Technical paper:** `publication/historical-regime-study/TECHNICAL-PAPER.md`
- **Case study:** `publication/historical-regime-study/CASE-STUDY.md`
- **Claim register:** `publication/historical-regime-study/CLAIM-REGISTER.md`
- **Source gate:** `publication/historical-regime-study/SOURCE-GATE.md`
- **Research question:** Can Bayesian and system-dynamics-inspired modeling improve market regime classification, risk conditioning, and forward-looking scenario analysis for financial time series?
- **Evaluation classification:** **FINAL 2025 HOLDOUT EVALUATION** (holdout audit **CLEAR**) — a descriptive *regime and risk characterization*.
- **Primary finding:** Risk characteristics differ measurably across the identified market regimes, characterized descriptively with every reported figure mapped to a committed artifact (a 469-row result-source map).
- **Primary null / negative finding:** **No statistically validated predictive edge** is claimed, and no directional-accuracy or trading-alpha figure is asserted.
- **Principal limitation:** Cells whose regime occurrence count falls below 20 are reported under a `min(20, n)` rule — 174 sparse-cell bootstrap rows carry an effective block size below the requested 20, so those intervals are degenerate or near-degenerate rather than evidence of stability.
- **Reproduction entrypoint:** `python publication/historical-regime-study/scripts/verify_pack.py`

## 2. Statistical Arbitrage Engine

- **Repository:** [`jmiaie/Advanced_Algorithmic_Trading_Simulator_public`](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public)
- **Canonical `main` head at time of writing** (verify the current value with `git ls-remote`): `372d5571ca72913ed0c69c53337473ffe63f8c94`
- **Technical paper:** `publication/stat-arb-study/TECHNICAL-PAPER.md`
- **Case study:** `publication/stat-arb-study/CASE-STUDY.md`
- **Claim register:** `publication/stat-arb-study/CLAIM-REGISTER.md`
- **Source gate:** `publication/stat-arb-study/SOURCE-GATE.md`
- **Research question:** Can an event-driven statistical-arbitrage research stack produce more credible spread-trading evaluation by combining rigorous pair selection, signal construction, and execution-aware backtesting?
- **Evaluation classification:** **FINAL 2025 WALK-FORWARD EVALUATION** — deliberately *not* described as an untouched holdout.
- **Primary finding:** Across four walk-forward buckets (32 windows, 1,724 candidate pair tests) the pre-specified Engle-Granger plus Benjamini-Hochberg FDR screen selected a pair in only four windows, all before 2024.
- **Primary null / negative finding:** In 2025 the screen produced **zero qualifying pairs**, so the portfolio held **no position** — three pure-2025 windows, 55 candidate tests each, zero FDR survivors, zero trades. No return, Sharpe, drawdown, or turnover quantity exists for 2025, and none is estimated or implied.
- **Principal limitation:** Pair selection is exposed to data-snooping and convenience-universe bias, and execution is a stylized scenario engine rather than a reconstruction of market microstructure.
- **Reproduction entrypoint:** `python3 publication/stat-arb-study/scripts/publication_pack.py check` · `… hashcheck` · `python3 publication/stat-arb-study/scripts/claim_crosscheck.py`

## 3. Options Volatility Risk Lab

- **Repository:** [`jmiaie/options-volatility-risk-lab`](https://github.com/jmiaie/options-volatility-risk-lab)
- **Canonical `main` head at time of writing** (verify the current value with `git ls-remote`): `8d7f761d6ece8276b529c8ebfaa1cfc32dd74b91`
- **Technical paper:** `publication/options-risk-study/TECHNICAL-PAPER.md`
- **Case study:** `publication/options-risk-study/CASE-STUDY.md`
- **Claim register:** `publication/options-risk-study/CLAIM-REGISTER.md`
- **Source gate:** `publication/options-risk-study/SOURCE-GATE.md`
- **Research question:** How can a self-contained derivatives and portfolio-risk research system support pricing, volatility analysis, hedging simulation, and portfolio stress testing in a reproducible Python workflow?
- **Evaluation classification:** **HISTORICAL EVALUATION** — a hypothetical nonlinear option portfolio on historical risk-factor paths.
- **Primary finding:** Two hypothetical standardized constructs were evaluated on real historical SPY, DGS3MO, and VIXCLS paths from 2015–2025: discrete delta-hedging of a short ATM 30-session call replayed against actual SPY closes, and a standardized long-equity/short-call/long-put book risk-managed with three independent VaR/ES methodologies at two confidence levels, backtested with Kupiec/Christoffersen coverage diagnostics.
- **Primary null / negative finding:** The previously reported order-of-magnitude divergence between risk methodologies was largely a **volatility-units defect**; that explanation is withdrawn. No historical options-tape P&L is implied, and no live or deployed options-trading result is claimed.
- **Principal limitation:** The portfolio is hypothetical and evaluated on historical underlying, risk-free-rate, and volatility-index paths — no historical option quotes are reconstructed. Vanilla European instruments only, with documented model idealizations.
- **Reproduction entrypoint:** `python publication/options-risk-study/scripts/verify_pack.py`

## 4. ML Sentiment Augmented Price Predictor

- **Repository:** [`jmiaie/ML_Sentiment_Augmented_Price_Predictor`](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor)
- **Canonical `main` head at time of writing** (verify the current value with `git ls-remote`): `77a2390c460f2c609e5a39c36feed7da56a794e3`
- **Technical paper:** `publication/sentiment-study/TECHNICAL-PAPER.md`
- **Case study:** `publication/sentiment-study/CASE-STUDY.md`
- **Claim register:** `publication/sentiment-study/CLAIM-REGISTER.md`
- **Source gate:** `publication/sentiment-study/SOURCE-GATE.md`
- **Research question:** Does point-in-time sentiment add incremental predictive information beyond market-only features for short-horizon asset returns — and can that question be tested without leakage?
- **Evaluation classification:** **PREVIOUSLY INSPECTED / HISTORICAL EVALUATION** (2025 block, n = 197, twelve issuers) — not an untouched holdout.
- **Primary finding:** A leakage-controlled comparison was run on a documented twelve-issuer SEC filing corpus (2,349 filing events) against corresponding market data, comparing majority-baseline, market-only, sentiment-only, and combined specifications on identical out-of-sample periods.
- **Primary null / negative finding:** Loughran-McDonald filing-text features **failed to demonstrate incremental predictive value** beyond market-only features under the pre-specified log-loss comparison: Δ log loss (m3 − m1) `+0.0040902`, block-bootstrap 95% interval `[-0.0048506, +0.0108001]` (**includes zero**); balanced-accuracy delta `-0.0274725275`. This is a failure to demonstrate — **not** a claim that filing text is universally useless or harmful, and **not** a claim that the effect is exactly zero.
- **Principal limitation:** A single evaluation year with 197 rows across twelve issuers yields wide intervals, and the 2025 block is a previously inspected historical evaluation rather than a fresh holdout.
- **Reproduction entrypoint:** `python3 publication/sentiment-study/scripts/publication_pack.py check` · `… hashcheck` · `python3 publication/sentiment-study/scripts/claim_crosscheck.py`

---

## Program state

| Stream | State |
| --- | --- |
| D9 | COMPLETE / ACCEPTED |
| D10 | TECHNICALLY INTEGRATED / FORMAL SIGN-OFF PENDING |
| D11 | PARTIALLY STARTED THROUGH THE PUBLIC HUB / NOT FORMALLY ACTIVATED |
| D12 | DRAFTED / BLOCKED BY D11 HIRING EVIDENCE |
| D13 | DRAFTED / NOT YET JUSTIFIED |

No authoritative `DIRECTIVE #10 PUBLICATION PACK SIGN-OFF: YES` has been issued. A D9 program sign-off is not a D10 program sign-off.
