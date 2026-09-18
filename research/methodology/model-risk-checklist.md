# Model Risk Checklist

[Back to main README](../../README.md)

Use this checklist before promoting research outputs as portfolio evidence.

## Data Risk

- Are data sources documented and reproducible?
- Are missing values, outliers, splits, and corporate actions handled appropriately?
- Is timestamp alignment consistent with decision-time information?

## Model Risk

- Is the economic hypothesis explicit and testable?
- Are parameters stable across reasonable ranges?
- Are benchmark models strong enough to challenge the result?

## Implementation Risk

- Are calculations covered by targeted tests or independent checks?
- Can the environment be recreated cleanly?
- Are units, conventions, and numerical assumptions documented?

## Execution Risk

- Are transaction costs, spread, slippage, and latency modeled where relevant?
- Are borrow, liquidity, and capacity constraints addressed?
- Does the strategy depend on unrealistic fill assumptions?

## Market-Regime Risk

- Does the approach rely on a narrow historical regime?
- How does performance change across volatility, trend, or crisis states?
- Are structural breaks or regime shifts explicitly considered?

## Operational Risk

- Are external data/API dependencies identified?
- Are monitoring, failure handling, and reproducibility controls defined?
- Are known limitations documented for reviewers and future maintainers?
