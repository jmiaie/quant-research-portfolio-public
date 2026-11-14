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


def sharpe_ratio(
    returns: pd.Series,
    periods_per_year: int = 252,
    rf: float = 0.0,
    ddof: int = 1,
) -> float:
    """Conventional arithmetic annualized Sharpe ratio.

    ``mean(r - rf_p) * periods_per_year / (std(r - rf_p) * sqrt(periods_per_year))``,
    which simplifies to ``mean / std * sqrt(periods_per_year)``.

    ``rf`` is an *annual* risk-free rate (default 0), converted to a per-period rate as
    ``rf / periods_per_year`` so that it matches the arithmetic (non-compounded) mean.
    ``ddof=1`` uses the sample standard deviation, the usual convention.

    Returns 0.0 when the statistic is undefined (fewer than ``ddof + 1`` observations or
    zero dispersion), matching the previous behaviour for degenerate inputs.
    """
    if periods_per_year <= 0:
        raise ValueError("periods_per_year must be positive")
    if len(returns) <= ddof:
        return 0.0
    excess = returns - rf / periods_per_year
    std = float(excess.std(ddof=ddof))
    if std == 0 or np.isnan(std):
        return 0.0
    mean = float(excess.mean())
    return mean * periods_per_year / (std * np.sqrt(periods_per_year))


def cagr_volatility_ratio(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Compounded annual growth rate divided by annualized volatility (no risk-free rate).

    This is what ``sharpe_ratio`` returned before it was corrected. It is *not* a Sharpe
    ratio: the numerator is geometric and no risk-free rate is subtracted. Kept under a
    separate name for callers that want the return-to-risk ratio on a compounded basis.
    """
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
