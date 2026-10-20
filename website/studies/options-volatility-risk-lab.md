# Options Volatility Risk Lab

**Evaluation:** historical evaluation of a **hypothetical** option book on real SPY, DGS3MO and
VIXCLS paths, 2015–2025. No historical option quotes are reconstructed.

## Question

How do Historical-Simulation, Delta-Normal and Monte Carlo VaR/ES, and discrete delta hedging,
behave on real risk-factor paths?

## Result

- VaR/ES method comparison with Kupiec/Christoffersen coverage diagnostics on **one forecast per
  monthly roll**: n = 95 (2015–2023 development), n = 12 (2024 validation), n = 12 (2025).
- Sample sizes are far below the ~250-observation rule of thumb for reasonable test power. At
  n = 12, "fail to reject" is weak evidence that coverage is correct.
- **Withdrawn:** an earlier order-of-magnitude divergence between methods was largely a
  volatility-units defect.
- No options-tape P&L and no live or deployed trading result is claimed.

## Read the paper

- [Technical paper](https://github.com/jmiaie/options-volatility-risk-lab/blob/0b6417639157fb3cf9744da8f751a77c973d4640/publication/options-risk-study/TECHNICAL-PAPER.md) (pinned to `0b64176`)
- [Case study](https://github.com/jmiaie/options-volatility-risk-lab/blob/0b6417639157fb3cf9744da8f751a77c973d4640/publication/options-risk-study/CASE-STUDY.md) ·
  [Result-to-source map](https://github.com/jmiaie/options-volatility-risk-lab/blob/0b6417639157fb3cf9744da8f751a77c973d4640/publication/options-risk-study/RESULT-SOURCE-MAP.md)
- Figures: [`figures/` at the pinned commit](https://github.com/jmiaie/options-volatility-risk-lab/tree/0b6417639157fb3cf9744da8f751a77c973d4640/publication/options-risk-study/figures) (embedding them on this site is a roadmap item)

## Verify

```bash
git clone https://github.com/jmiaie/options-volatility-risk-lab.git
cd options-volatility-risk-lab && git checkout 0b6417639157fb3cf9744da8f751a77c973d4640
python3 -m venv .venv
.venv/bin/pip install -e ".[dev,viz]"
.venv/bin/python publication/options-risk-study/scripts/verify_pack.py
```

Expected: `All publication-pack verification checks passed.`, exit code 0.
