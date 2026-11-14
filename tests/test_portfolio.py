from __future__ import annotations

import math

import pandas as pd
import pytest

from quant_research.portfolio import (
    cagr_volatility_ratio,
    inverse_volatility_weights,
    max_drawdown,
    performance_summary,
    sharpe_ratio,
)


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


# Hand-computed reference values for the corrected Sharpe ratio.
#
# returns = [0.03, 0.01, 0.03, 0.01], periods_per_year = 4
#   mean = 0.02; deviations = +/-0.01; sample var = 4 * 1e-4 / 3; sample std = 0.01 * 2 / sqrt(3)
#   Sharpe(rf=0)    = 0.02 * 4 / (0.02 / sqrt(3) * 2)        = 2 * sqrt(3) ~= 3.4641
#   Sharpe(rf=4%)   = per-period rf 0.01, excess mean 0.01   = sqrt(3)     ~= 1.7321
#   CAGR / vol      = (1.03**2 * 1.01**2 - 1) / (0.01 * 2)   = 0.08222409 / 0.02 = 4.1112045
QUARTERLY = pd.Series([0.03, 0.01, 0.03, 0.01])


def test_sharpe_ratio_matches_hand_computed_value_zero_rf() -> None:
    assert sharpe_ratio(QUARTERLY, periods_per_year=4) == pytest.approx(2 * math.sqrt(3))


def test_sharpe_ratio_subtracts_annual_risk_free_rate() -> None:
    assert sharpe_ratio(QUARTERLY, periods_per_year=4, rf=0.04) == pytest.approx(math.sqrt(3))


def test_sharpe_ratio_daily_hand_computed() -> None:
    # returns = [0.01, -0.02, 0.03]: mean = 2/300, sample std = sqrt(57)/300
    # Sharpe = (2 / sqrt(57)) * sqrt(252) = 2 * sqrt(252 / 57) ~= 4.20526
    returns = pd.Series([0.01, -0.02, 0.03])
    assert sharpe_ratio(returns) == pytest.approx(2 * math.sqrt(252 / 57))
    assert sharpe_ratio(returns) == pytest.approx(4.20526, abs=1e-5)


def test_sharpe_ratio_is_not_cagr_over_vol() -> None:
    assert cagr_volatility_ratio(QUARTERLY, periods_per_year=4) == pytest.approx(4.1112045)
    assert sharpe_ratio(QUARTERLY, periods_per_year=4) != pytest.approx(
        cagr_volatility_ratio(QUARTERLY, periods_per_year=4)
    )


def test_sharpe_ratio_degenerate_inputs_return_zero() -> None:
    assert sharpe_ratio(pd.Series([], dtype=float)) == 0.0
    assert sharpe_ratio(pd.Series([0.01])) == 0.0
    assert sharpe_ratio(pd.Series([0.01, 0.01, 0.01])) == 0.0
    with pytest.raises(ValueError):
        sharpe_ratio(QUARTERLY, periods_per_year=0)


def test_performance_summary_uses_conventional_sharpe() -> None:
    summary = performance_summary(QUARTERLY, periods_per_year=4)
    assert summary["sharpe_ratio"] == pytest.approx(2 * math.sqrt(3))
