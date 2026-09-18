from __future__ import annotations

import pandas as pd
import pytest

from quant_research.features import rolling_momentum, rolling_zscore


def test_rolling_momentum_uses_requested_lookback() -> None:
    dates = pd.bdate_range("2024-01-01", periods=4)
    prices = pd.DataFrame({"asset": [100.0, 105.0, 110.25, 115.7625]}, index=dates)

    momentum = rolling_momentum(prices, lookback=1)

    assert momentum["asset"].iloc[-1] == pytest.approx(0.05)


def test_rolling_zscore_returns_zero_for_flat_series() -> None:
    series = pd.Series([1.0, 1.0, 1.0, 1.0])

    zscore = rolling_zscore(series, window=2)

    assert zscore.tolist() == pytest.approx([0.0, 0.0, 0.0, 0.0])
