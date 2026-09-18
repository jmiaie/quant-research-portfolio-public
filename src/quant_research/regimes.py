from __future__ import annotations

import numpy as np
import pandas as pd


def rolling_realized_volatility(
    returns: pd.Series,
    window: int = 21,
    annualization: int = 252,
) -> pd.Series:
    """Estimate trailing realized volatility for a univariate return stream."""
    if window < 2:
        raise ValueError("window must be at least 2")
    return returns.rolling(window=window).std(ddof=0) * np.sqrt(annualization)


def classify_volatility_regime(
    returns: pd.Series,
    window: int = 21,
    threshold_quantile: float = 0.75,
) -> pd.Series:
    """Label observations as calm or stressed using an expanding realized-vol threshold."""
    if not 0.0 < threshold_quantile < 1.0:
        raise ValueError("threshold_quantile must be between 0 and 1")

    realized_vol = rolling_realized_volatility(returns.fillna(0.0), window=window)
    threshold = realized_vol.expanding(min_periods=window).quantile(threshold_quantile)
    labels = np.where(realized_vol > threshold, "stressed", "calm")
    return pd.Series(labels, index=returns.index, name="regime")
