from __future__ import annotations

from quant_research.examples import run_regime_momentum_example


def test_end_to_end_example_runs_and_returns_summary() -> None:
    result = run_regime_momentum_example(periods=80, seed=3)

    assert set(result.summary) == {
        "annualized_return",
        "annualized_volatility",
        "sharpe_ratio",
        "max_drawdown",
    }
    assert len(result.tail) == 5
    assert sum(result.regime_counts.values()) == 79
