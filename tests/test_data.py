from __future__ import annotations

import pandas as pd
import pytest

from quant_research.data import generate_synthetic_prices, prices_to_returns, validate_price_frame


def test_generate_synthetic_prices_is_positive_and_ordered() -> None:
    prices = generate_synthetic_prices(periods=10, seed=1)

    assert list(prices.columns) == ["trend", "defensive"]
    assert len(prices) == 10
    assert prices.index.is_monotonic_increasing
    assert (prices > 0.0).all().all()


def test_prices_to_returns_matches_simple_percent_change() -> None:
    dates = pd.bdate_range("2024-01-01", periods=3)
    prices = pd.DataFrame({"asset": [100.0, 110.0, 121.0]}, index=dates)

    returns = prices_to_returns(prices)

    assert returns["asset"].tolist() == pytest.approx([0.1, 0.1])


def test_validate_price_frame_rejects_unsorted_index() -> None:
    dates = pd.to_datetime(["2024-01-02", "2024-01-01"])
    prices = pd.DataFrame({"asset": [100.0, 101.0]}, index=dates)

    with pytest.raises(ValueError, match="sorted"):
        validate_price_frame(prices)
