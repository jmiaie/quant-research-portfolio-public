# Backtesting Standards

[Back to main README](../../README.md)

Backtests in this portfolio should be treated as decision-support evidence, not proof of deployable alpha, unless they survive realistic implementation and validation checks.

## Bias and Overfitting Controls

- Eliminate look-ahead bias in feature construction, signal generation, and benchmark alignment.
- Address survivorship bias in security universes and constituent histories.
- Document and reduce selection bias introduced by ex post universe filtering.
- Track data snooping risk created by repeated idea iteration.
- Monitor overfitting through holdout discipline and sensitivity analysis.
- Control for multiple testing when many instruments, signals, or parameter sets are examined.

## Execution and Market Realism

- Include transaction costs.
- Model bid/ask spread and slippage.
- Include borrow costs where relevant.
- Consider market impact for size-sensitive strategies.
- Evaluate liquidity and capacity constraints.
- Account for latency and signal delay where execution timing matters.

## Evaluation Design

- Use walk-forward evaluation when strategy parameters are updated over time.
- Use temporal cross-validation where appropriate for predictive models.
- Separate formation, validation, and true out-of-sample periods.
- Compare against suitable benchmarks and naive alternatives.
- Report sensitivity to parameter choices, holding periods, and cost assumptions.
