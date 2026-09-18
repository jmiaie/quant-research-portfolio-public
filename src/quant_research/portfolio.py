from __future__ import annotations

import numpy as np
import pandas as pd


def inverse_volatility_weights(asset_returns: pd.DataFrame, lookback: int = 21) -> pd.DataFrame:
    """Create inverse-volatility cross-sectional weights from trailing realized volatility."""
    if lookback < 2:
        raise ValueError("lookback must be at least 2")
    realized_vol = asset_returns.rolling(lookback).std(ddof=0).clip(lower=1e-6)
    inverse_vol = 1.0 / realized_vol
    weight_sums = inverse_vol.sum(axis=1).replace(0.0, np.nan)
    return inverse_vol.div(weight_sums, axis=0).fillna(0.0)


def annualized_return(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Convert a return series into a compounded annualized return estimate."""
    if returns.empty:
        return 0.0
    compounded_growth = float((1.0 + returns).prod())
    years = len(returns) / periods_per_year
    if years == 0:
        return 0.0
    return compounded_growth ** (1.0 / years) - 1.0


def annualized_volatility(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Estimate annualized volatility from periodic returns."""
    if returns.empty:
        return 0.0
    return float(returns.std(ddof=0) * np.sqrt(periods_per_year))


def sharpe_ratio(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Estimate a zero-rate Sharpe ratio for a simple research return stream."""
    volatility = annualized_volatility(returns, periods_per_year=periods_per_year)
    if volatility == 0:
        return 0.0
    return annualized_return(returns, periods_per_year=periods_per_year) / volatility


def max_drawdown(returns: pd.Series) -> float:
    """Return the worst drawdown in a cumulative return series."""
    if returns.empty:
        return 0.0
    nav = (1.0 + returns).cumprod()
    drawdown = nav / nav.cummax() - 1.0
    return float(drawdown.min())


def performance_summary(returns: pd.Series, periods_per_year: int = 252) -> dict[str, float]:
    """Summarize core risk and performance diagnostics for a research example."""
    return {
        "annualized_return": annualized_return(returns, periods_per_year=periods_per_year),
        "annualized_volatility": annualized_volatility(returns, periods_per_year=periods_per_year),
        "sharpe_ratio": sharpe_ratio(returns, periods_per_year=periods_per_year),
        "max_drawdown": max_drawdown(returns),
    }
