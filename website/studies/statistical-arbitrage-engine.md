# Statistical Arbitrage Engine

<div class="study-meta"><span class="pill">Null result</span><span>2025 walk-forward · reviewed commit <code>6ae04ed</code></span></div>

**Evaluation:** final 2025 walk-forward evaluation — deliberately not called an untouched holdout.

## Question

Does a pre-specified Engle-Granger cointegration screen with Benjamini-Hochberg FDR control find
tradable pairs, evaluated with an event-driven, cost-aware backtest?

## Result

<figure class="viz">
<figcaption><span class="viz-title">The screen let nothing through in 2025</span><span class="viz-subtitle">Three walk-forward windows, 55 candidate pair tests each</span></figcaption>
<div class="window-row">
<div class="window"><span class="window-name">2025 window 1</span><span class="window-flow">55 tests → 0 passed</span><span class="window-sub">no trade</span></div>
<div class="window"><span class="window-name">2025 window 2</span><span class="window-flow">55 tests → 0 passed</span><span class="window-sub">no trade</span></div>
<div class="window"><span class="window-name">2025 window 3</span><span class="window-flow">55 tests → 0 passed</span><span class="window-sub">no trade</span></div>
</div>
<p class="meter-label"><span>All 32 windows in the study</span><span>4 selected a pair, all before 2025</span></p>
<div class="meter" role="img" aria-label="4 of 32 windows selected a pair"><span class="meter-on" style="flex: 4"></span><span class="meter-off" style="flex: 28"></span></div>
<p class="viz-note">Across all windows the screen ran 1,724 candidate tests. A screen that rejects everything in a period produces no return, Sharpe ratio or drawdown for that period, and none is estimated.</p>
</figure>

- **Null.** Three pure-2025 windows, 55 candidate tests each: 0 FDR survivors, 0 trades.
- Across all four walk-forward buckets (32 windows, 1,724 candidate tests) the screen selected
  a pair in only four windows, all before 2025.
- No 2025 return, Sharpe, drawdown or turnover exists, and none is estimated.

**What this test could detect.** In simulation the screen finds a truly cointegrated pair 98% of the
time at a 5-day spread half-life and 4% of the time at 20 days. See
[What the tests could detect](../power.md).

## Corrections since publication

- The position-sizing code does not trade the tested spread, and the backtest charges no exit cost at
  the end of a window.
- Four development windows that traded have out-of-sample results the write-up did not report.
- The Benjamini-Hochberg step-up rule was corrected after publication. Old and corrected rules agree
  on whether any pair is selected, so the 2025 zero-survivor result is unchanged.
- Details: [`docs/known-defects-and-unreported-results.md`](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public/blob/main/docs/known-defects-and-unreported-results.md) and
  [`docs/post-publication-bh-correction.md`](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public/blob/main/docs/post-publication-bh-correction.md).

## Read the paper

- [Technical paper](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public/blob/6ae04edd339f39b163b5420c0892c12c668c540c/publication/stat-arb-study/TECHNICAL-PAPER.md) (pinned to `6ae04ed`)
- [Case study](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public/blob/6ae04edd339f39b163b5420c0892c12c668c540c/publication/stat-arb-study/CASE-STUDY.md) ·
  [Claims and limits](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public/blob/6ae04edd339f39b163b5420c0892c12c668c540c/publication/stat-arb-study/CLAIMS-AND-LIMITS.md) ·
  [Result-to-source map](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public/blob/6ae04edd339f39b163b5420c0892c12c668c540c/publication/stat-arb-study/RESULT-SOURCE-MAP.md)
- Figures: [`figures/` at the pinned commit](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public/tree/6ae04edd339f39b163b5420c0892c12c668c540c/publication/stat-arb-study/figures) (embedding them on this site is a roadmap item)

## Verify

```bash
git clone https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public.git
cd Advanced_Algorithmic_Trading_Simulator_public && git checkout 6ae04edd339f39b163b5420c0892c12c668c540c
python3 publication/stat-arb-study/scripts/publication_pack.py check
python3 publication/stat-arb-study/scripts/claim_crosscheck.py
```

Expected: `publication-pack check OK: 13 artifact hashes, 4 generated files, 11 map citations verified`
and `claim cross-check OK: 101 independent assertions passed`. Standard library only.
