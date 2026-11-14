---
title: Home
hide:
  - toc
---

<div class="hero">
<p class="hero-eyebrow">Micap AI · Quantitative research</p>
<h1>Quant research you can check for yourself</h1>
<p class="hero-lede">Four pre-specified studies across market regimes, statistical arbitrage, derivatives risk and financial machine learning. Each ships a technical paper and an offline verifier that re-derives every cited number from committed files. Null and negative results are reported as found.</p>
<div class="hero-actions">
<a class="md-button md-button--primary" href="#studies">See the studies</a>
<a class="md-button" href="verification/">How verification works</a>
</div>
</div>

<div class="stat-row">
<div class="stat"><span class="stat-value">4</span><span class="stat-label">studies, each with a paper and a verifier</span></div>
<div class="stat"><span class="stat-value">1,724</span><span class="stat-label">candidate pair tests screened in the stat-arb study</span></div>
<div class="stat"><span class="stat-value">11 yrs</span><span class="stat-label">of real SPY paths in the options study, 2015–2025</span></div>
<div class="stat"><span class="stat-value">0</span><span class="stat-label">claims of a trading edge</span></div>
</div>

## Studies

<div class="card-grid">
<a class="study-card" href="studies/financial-dynamics-model/">
<span class="pill">Descriptive</span>
<span class="card-title">Financial Dynamics Model</span>
<span class="card-question">Do Bayesian regime labels separate forward risk on a 2025 holdout?</span>
<span class="card-figure"><span class="card-number">n = 29</span><span class="card-caption">risk-off days in 2025; both bootstrap intervals include zero</span></span>
<span class="card-more">Read the study →</span>
</a>
<a class="study-card" href="studies/statistical-arbitrage-engine/">
<span class="pill">Null result</span>
<span class="card-title">Statistical Arbitrage Engine</span>
<span class="card-question">Does a cointegration screen with false-discovery control find tradable pairs in 2025?</span>
<span class="card-figure"><span class="card-number">0 of 165</span><span class="card-caption">pair tests passed the 2025 screen, so no trade was opened</span></span>
<span class="card-more">Read the study →</span>
</a>
<a class="study-card" href="studies/options-volatility-risk-lab/">
<span class="pill">Method comparison</span>
<span class="card-title">Options Volatility Risk Lab</span>
<span class="card-question">How do three VaR methods behave on real SPY paths for a hypothetical option book?</span>
<span class="card-figure"><span class="card-number">35×</span><span class="card-caption">how far a units bug had overstated Monte Carlo VaR before it was found and withdrawn</span></span>
<span class="card-more">Read the study →</span>
</a>
<a class="study-card" href="studies/ml-sentiment/">
<span class="pill">Not demonstrated</span>
<span class="card-title">ML Sentiment Study</span>
<span class="card-question">Does filing-text sentiment add information beyond market-only features?</span>
<span class="card-figure"><span class="card-number">+0.0041</span><span class="card-caption">change in log loss; the 95% interval spans zero (n = 197)</span></span>
<span class="card-more">Read the study →</span>
</a>
</div>

These are independent research projects. None represents live trading or deployed capital.

## How a claim gets checked

<div class="pipeline" role="list">
<div class="step" role="listitem"><strong>Committed files</strong>Results, tables and figures are committed with their hashes at a pinned commit.</div>
<div class="step" role="listitem"><strong>Offline verifier</strong>One command per study. No network, no credentials, no re-fitting.</div>
<div class="step" role="listitem"><strong>Four checks</strong>Hashes match, tables regenerate, figures pass the rendering check, every cited claim resolves.</div>
<div class="step" role="listitem"><strong>Pass or named failure</strong>If any file has drifted, the verifier fails and says which one.</div>
</div>

[Claims verified: manually, at pinned commits](verification.md){ .md-button title="Each study's offline verifier was run from a fresh clone of the pinned commit. Automated re-verification is planned." }

!!! note "What verified means"
    The study's committed files are internally consistent at the pinned commit. It does **not** mean
    the strategy or model has predictive or economic value. Today the badge reflects a manual run
    recorded in [How verification works](verification.md); an automated, dated badge is planned.

## Corrections

A review on 2026-11-14 found statements in all four studies that needed correcting. The frozen
files and their hashes are unchanged. Each study page lists its corrections, and the full list is
in the [publication index](https://github.com/jmiaie/quant-research-portfolio-public/blob/main/research/publications.md#corrections-and-known-limitations-2026-11-14).

## How this was built

Research questions, study designs and acceptance criteria are set by Micap AI. Implementation,
testing and review are carried out with AI coding and review agents, with separate author, reviewer
and verifier roles and fail-closed checks.

**Disclaimer.** Research and educational material only. Nothing on this site is investment advice,
a recommendation to trade, or a trading signal service; every number is a model output under stated
assumptions.

Source: [jmiaie/quant-research-portfolio-public](https://github.com/jmiaie/quant-research-portfolio-public).
