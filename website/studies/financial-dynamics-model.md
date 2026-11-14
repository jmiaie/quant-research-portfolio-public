# Financial Dynamics Model

<div class="study-meta"><span class="pill">Descriptive, then tested</span><span>SPY primary, four ETFs for robustness · 2025 holdout · reviewed commit <code>86a843f</code></span></div>

**Evaluation:** final 2025 holdout evaluation — a descriptive regime and risk characterization.

## Question

Do Bayesian regime labels, built from fixed theory-based centroids over five market features,
separate subsequent risk characteristics (forward-return dispersion, realized and downside
volatility, tail risk, drawdown, persistence) on SPY?

## Result

--8<-- "fdm-interval.html"

- Risk characteristics differ **descriptively** across regimes. The difference is **not
  statistically significant**: for QQQ's 2025 `RISK_OFF` cell (n = 29), the paper's 90%
  moving-block and stationary bootstrap intervals for the 1-day forward return both include zero.
- **Follow-up test (2026-11-14).** As a forecaster of next-day variance, the regime labels are worse
  than a simple quartile of trailing 20-day volatility (pooled five-ETF QLIKE difference +0.173,
  p = 0.012) and only slightly better than no labels. The comparison was pre-specified; the data had
  been inspected before, so it is not a holdout result. [Report](https://github.com/jmiaie/financial-dynamics-model/blob/main/research/vol_benchmark/REPORT.md).
- No predictive edge, directional accuracy or trading alpha is claimed.
- 174 sparse-cell bootstrap rows have an effective block size below the requested 20, so those
  intervals are degenerate or near-degenerate rather than evidence of stability.

## Corrections since publication

- The earlier wording that risk "differs measurably across regimes" was never tested against a simple
  volatility baseline. The follow-up test above has now run that comparison, and the baseline won.

## Read the paper

- [Technical paper](https://github.com/jmiaie/financial-dynamics-model/blob/86a843f82c8ffa1545ceea7261b22afc12e29ffa/publication/historical-regime-study/TECHNICAL-PAPER.md) (pinned to `86a843f`)
- [Case study](https://github.com/jmiaie/financial-dynamics-model/blob/86a843f82c8ffa1545ceea7261b22afc12e29ffa/publication/historical-regime-study/CASE-STUDY.md) ·
  [Claim register](https://github.com/jmiaie/financial-dynamics-model/blob/86a843f82c8ffa1545ceea7261b22afc12e29ffa/publication/historical-regime-study/CLAIM-REGISTER.md) ·
  [Data provenance](https://github.com/jmiaie/financial-dynamics-model/blob/86a843f82c8ffa1545ceea7261b22afc12e29ffa/publication/historical-regime-study/SOURCE-GATE.md)
- Figures: [`figures/` at the pinned commit](https://github.com/jmiaie/financial-dynamics-model/tree/86a843f82c8ffa1545ceea7261b22afc12e29ffa/publication/historical-regime-study/figures) (embedding them on this site is a roadmap item)

## Verify

```bash
git clone https://github.com/jmiaie/financial-dynamics-model.git
cd financial-dynamics-model && git checkout 86a843f82c8ffa1545ceea7261b22afc12e29ffa
python3 -m venv .venv
.venv/bin/pip install -r publication/historical-regime-study/requirements.txt PyYAML
.venv/bin/python publication/historical-regime-study/scripts/verify_pack.py
```

Expected: `RESULT: all 5 check(s) passed`, exit code 0.
