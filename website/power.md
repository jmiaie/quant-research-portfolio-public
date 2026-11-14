# What the tests could detect

Three of the four studies ended in a null. A null only tells you something if the test could have
found an effect had one been there. After publication, each of those studies was followed by a
power study asking how large an effect would have needed to be for the design to catch it 80% of
the time. Each one froze its protocol before the full run and used the study's own test code.

<div class="stat-row">
<div class="stat"><span class="stat-value">5 days</span><span class="stat-label">slowest spread half-life the stat-arb screen reliably detects</span></div>
<div class="stat"><span class="stat-value">6.5×</span><span class="stat-label">how wrong a VaR breach rate must be to be caught with 12 forecasts</span></div>
<div class="stat"><span class="stat-value">1.6%</span><span class="stat-label">smallest log-loss gain the sentiment test could detect</span></div>
</div>

## Statistical Arbitrage Engine

--8<-- "statarb-power.html"

The 2025 result rules out a within-group ETF pair with week-scale mean reversion in a given window.
It says almost nothing about slower mean reversion: zero survivors is the expected outcome whether
or not such pairs exist. [Power report](https://github.com/jmiaie/Advanced_Algorithmic_Trading_Simulator_public/blob/main/research/power/REPORT.md).

## Options Volatility Risk Lab

--8<-- "options-power.html"

With 12 forecasts the coverage test rejects only if 3 or more breach, and it can never flag an
over-conservative VaR. A daily backtest over 2015–2025 (about 2,500 forecasts) would detect a breach
rate about 1.26 times the target. [Power report](https://github.com/jmiaie/options-volatility-risk-lab/blob/main/research/power/REPORT.md).

## ML Sentiment Study

<div class="stat-row">
<div class="stat"><span class="stat-value">197</span><span class="stat-label">events in the published test: detects a 1.6% gain</span></div>
<div class="stat"><span class="stat-value">515</span><span class="stat-label">events needed to detect a 1% gain</span></div>
<div class="stat"><span class="stat-value">2,060</span><span class="stat-label">events needed to detect a 0.5% gain</span></div>
</div>

Gains are improvements in log loss as a share of the baseline. The comparison model had no skill
either: the market-only model's 2025 log loss equals the majority baseline's to 0.00002 nats.
[Power report](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor/blob/main/research/power/REPORT.md).

## Financial Dynamics Model

This study is descriptive and made no pass/fail test, so it has no power study. Its open question
is whether its regime labels separate forward risk better than a simple trailing-volatility bucket.
That comparison has not been run.

The longer write-up, including what a more informative version of each study would need, is in the
[hub repository](https://github.com/jmiaie/quant-research-portfolio-public/blob/main/research/how-informative-were-our-nulls.md).
