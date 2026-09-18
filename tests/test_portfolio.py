from __future__ import annotations

import pandas as pd
import pytest

from quant_research.portfolio import inverse_volatility_weights, max_drawdown, performance_summary


def test_inverse_volatility_weights_favor_lower_vol_asset() -> None:
    index = pd.bdate_range("2024-01-01", periods=4)
    returns = pd.DataFrame(
        {
            "stable": [0.01, 0.01, 0.01, 0.01],
            "risky": [0.04, -0.04, 0.04, -0.04],
        },
        index=index,
    )

    weights = inverse_volatility_weights(returns, lookback=2)
    final_weights = weights.iloc[-1]

    assert final_weights.sum() == pytest.approx(1.0)
    assert final_weights["stable"] > final_weights["risky"]


def test_performance_summary_contains_expected_metrics() -> None:
    returns = pd.Series([0.01, -0.02, 0.03])

    summary = performance_summary(returns)

    assert set(summary) == {
        "annualized_return",
        "annualized_volatility",
        "sharpe_ratio",
        "max_drawdown",
    }
    assert max_drawdown(returns) <= 0.0
