from __future__ import annotations

import numpy as np
import pandas as pd

from quant_research.data import validate_price_frame


def rolling_momentum(prices: pd.DataFrame, lookback: int = 21) -> pd.DataFrame:
    """Return trailing simple price momentum over the given lookback window."""
    if lookback < 1:
        raise ValueError("lookback must be at least 1")
    validated = validate_price_frame(prices)
    return validated.pct_change(periods=lookback)


def rolling_zscore(series: pd.Series, window: int = 21) -> pd.Series:
    """Compute a rolling z-score for a univariate research signal."""
    if window < 2:
        raise ValueError("window must be at least 2")
    mean = series.rolling(window=window).mean()
    std = series.rolling(window=window).std(ddof=0).replace(0.0, np.nan)
    zscore = (series - mean) / std
    return zscore.fillna(0.0)
