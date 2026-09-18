"""Reusable building blocks for public-safe quantitative research examples."""

from quant_research.backtesting import lagged_positions, normalize_signals, run_backtest
from quant_research.data import generate_synthetic_prices, prices_to_returns, validate_price_frame
from quant_research.examples import ExampleResult, run_regime_momentum_example
from quant_research.features import rolling_momentum, rolling_zscore
from quant_research.portfolio import (
    annualized_return,
    annualized_volatility,
    inverse_volatility_weights,
    max_drawdown,
    performance_summary,
    sharpe_ratio,
)
from quant_research.regimes import classify_volatility_regime, rolling_realized_volatility

__all__ = [
    "ExampleResult",
    "annualized_return",
    "annualized_volatility",
    "classify_volatility_regime",
    "generate_synthetic_prices",
    "inverse_volatility_weights",
    "lagged_positions",
    "max_drawdown",
    "normalize_signals",
    "performance_summary",
    "prices_to_returns",
    "rolling_momentum",
    "rolling_realized_volatility",
    "rolling_zscore",
    "run_backtest",
    "run_regime_momentum_example",
    "sharpe_ratio",
    "validate_price_frame",
]
