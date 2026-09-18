from __future__ import annotations

import numpy as np
import pandas as pd


def validate_price_frame(prices: pd.DataFrame) -> pd.DataFrame:
    """Validate that a price frame is suitable for simple research examples."""
    if prices.empty:
        raise ValueError("prices must not be empty")
    if not isinstance(prices.index, pd.DatetimeIndex):
        raise TypeError("prices index must be a pandas DatetimeIndex")
    if not prices.index.is_monotonic_increasing:
        raise ValueError("prices index must be sorted in increasing order")
    if prices.isnull().any().any():
        raise ValueError("prices must not contain missing values")
    if (prices <= 0).any().any():
        raise ValueError("prices must be strictly positive")
    return prices.astype(float)


def prices_to_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Convert validated price levels into simple returns."""
    validated = validate_price_frame(prices)
    returns = validated.pct_change().dropna(how="all")
    return returns.fillna(0.0)


def generate_synthetic_prices(
    periods: int = 260,
    seed: int = 7,
    start: str = "2020-01-01",
) -> pd.DataFrame:
    """Generate deterministic synthetic price paths with a mid-sample volatility regime shift."""
    if periods < 2:
        raise ValueError("periods must be at least 2")

    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(start=start, periods=periods)
    drifts = np.array([0.0004, 0.0002])
    low_vol = np.array([0.008, 0.006])
    high_vol = np.array([0.02, 0.015])
    regime_split = periods // 2
    vols = np.vstack(
        [
            np.tile(low_vol, (regime_split, 1)),
            np.tile(high_vol, (periods - regime_split, 1)),
        ]
    )
    shocks = rng.normal(loc=drifts, scale=vols)
    prices = 100.0 * np.exp(np.cumsum(shocks, axis=0))
    return pd.DataFrame(prices, index=dates, columns=["trend", "defensive"])
