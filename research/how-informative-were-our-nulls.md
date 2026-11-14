# How Informative Were Our Nulls?

[Back to main README](../README.md) · [Publication index](publications.md)

Three of the four studies ended in a null or a failure to demonstrate. A null only tells you
something if the test could have found an effect had one been there. After publication, each of
those three studies was followed by a power study that asks exactly that: how large would an effect
have needed to be for this design to detect it 80% of the time?

Each power study froze its protocol in a commit before the full run, used the study's own
production test code, and changed no published artifact.

## Summary

| Study | Published result | Could have detected (80% power) | Could not have detected | Report |
| --- | --- | --- | --- | --- |
| Statistical Arbitrage Engine | 0 of 55 pair tests passed in each of 3 windows in 2025 | A cointegrated pair whose spread half-life is about 5 trading days | Half-lives of 20 days or more, the usual range for ETF pairs (4% detection at 20 days, 1% or less beyond) | [Report](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public/blob/main/research/power/REPORT.md) |
| Options Volatility Risk Lab | Coverage tests did not reject the 95% VaR at n = 95, 12 and 12 forecasts | A true breach rate about 6.5 times the 5% target at n = 12; about 2.6 times at n = 95 | A VaR that is wrong by a factor of two (flagged 11% of the time at n = 12, 48% at n = 95) | [Report](https://github.com/jmiaie/options-volatility-risk-lab/blob/main/research/power/REPORT.md) |
| ML Sentiment Study | Adding filing text did not lower log loss (n = 197) | An improvement of at least 0.0112 nats per event, 1.6% of the baseline log loss | Smaller improvements; the realised interval excludes gains above about 0.7% of baseline | [Report](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor/blob/main/research/power/REPORT.md) |

The Financial Dynamics Model study is descriptive and made no pass/fail test, so it has no power
study. Its open question was different: whether its regime labels separate forward risk better than
a simple trailing-volatility bucket. A pre-specified follow-up test has now run that comparison for
next-day variance. The volatility bucket is better (pooled five-ETF QLIKE difference +0.173,
p = 0.012); the labels are only slightly better than no labels ([report](https://github.com/jmiaie/financial-dynamics-model/blob/main/research/vol_benchmark/REPORT.md)).
That test could only detect a large gap (its minimum detectable effect was 91% of the volatility
bucket's own gain), and the gap it found is large.

## What each result means

### Statistical Arbitrage Engine

The screen runs 55 Engle-Granger tests per window and applies Benjamini-Hochberg control at
q = 0.05. With one true pair among 55, a pair has to reach roughly p ≤ 0.0009 to pass. In
simulation the screen found a planted pair 98% of the time at a 5-day half-life, 51% at 10 days,
4% at 20 days and 1% or less at 40 days and beyond.

So the 2025 result rules out a within-group ETF pair with week-scale mean reversion in a given
window. It says almost nothing about slower mean reversion: "0 survivors" is the expected outcome
whether or not such pairs exist. The three 2025 windows share 441 of their 504 formation days, so
they are not three independent trials.

The same study found that the validation Sharpe fields are null by construction in holdout mode,
so the published Static-OLS versus Kalman comparison could not have been evidenced from the 2025
windows.

### Options Volatility Risk Lab

The published backtest makes one forecast per monthly roll. With 12 forecasts, the Kupiec test
rejects only if 3 or more breach, and it can never flag an over-conservative VaR, because zero
breaches is not rejectable below 38 forecasts. The Christoffersen clustering test has at most 14%
power at n = 12, so the published p = 1.000 values carry no information about clustering.

Detecting a doubled breach rate with 80% power takes about 224 forecasts. A daily backtest over
2015–2025 (about 2,500 forecasts) would detect a breach rate about 1.26 times the target.

### ML Sentiment Study

The design had 80% power only for log-loss improvements of at least 0.0112 nats per event. In
plainer terms, that is roughly what a calibrated forecast with an AUC near 0.58 would deliver. It
did not find one. Detecting a 1% improvement would take about 515 events under the same design, and
0.5% would take about 2,060.

Two further findings limit the comparison. The market-only model had no skill either: its 2025 log
loss equals the majority baseline's to 0.00002 nats. And the published percentile block bootstrap
(19 blocks) rejects a true null about 7.8% of the time instead of 5%.

## What a more informative version would need

| Study | Next test | What it changes |
| --- | --- | --- |
| Statistical Arbitrage Engine | A larger universe including delisted ETFs, corrected position sizing, and positive controls such as SPY/IVV and GLD/IAU | The current design cannot answer its own question at realistic half-lives |
| Options Volatility Risk Lab | A daily VaR/ES backtest with a volatility risk factor and an expected-shortfall test | Detectable mis-calibration falls from about 6.5 times to about 1.3 times |
| ML Sentiment Study | A larger event set (on the order of 100,000 events) with a positive control | The detectable effect falls from 1.6% of baseline to well under 0.1% |
| Financial Dynamics Model | Done for next-day variance (2026-11-14). Still open: the same comparison on untouched data, and for drawdown or tail risk | The current result uses previously inspected data and one loss function |

Apart from the financial-dynamics comparison, none of these has been run. They are listed so a reader can see what the published results do and
do not establish.
