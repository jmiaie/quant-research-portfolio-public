from __future__ import annotations

import numpy as np
import pandas as pd


def normalize_signals(signals: pd.DataFrame) -> pd.DataFrame:
    """Scale each row of signals to unit gross exposure when active."""
    gross_exposure = signals.abs().sum(axis=1).replace(0.0, np.nan)
    return signals.div(gross_exposure, axis=0).fillna(0.0)


def lagged_positions(signals: pd.DataFrame) -> pd.DataFrame:
    """Lag signals by one period to avoid look-ahead bias in simple examples."""
    return normalize_signals(signals.shift(1).fillna(0.0))


def run_backtest(asset_returns: pd.DataFrame, signals: pd.DataFrame) -> pd.DataFrame:
    """Run a simple vectorized backtest with lagged, normalized positions."""
    aligned_returns = asset_returns.astype(float)
    aligned_signals = signals.reindex(
        index=aligned_returns.index,
        columns=aligned_returns.columns,
    ).fillna(0.0)
    positions = lagged_positions(aligned_signals)
    portfolio_returns = (positions * aligned_returns).sum(axis=1)
    nav = (1.0 + portfolio_returns).cumprod()
    return pd.DataFrame(
        {
            "portfolio_returns": portfolio_returns,
            "nav": nav,
            "gross_exposure": positions.abs().sum(axis=1),
        },
        index=aligned_returns.index,
    )
