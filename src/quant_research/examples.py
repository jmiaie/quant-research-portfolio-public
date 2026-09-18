from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from quant_research.backtesting import run_backtest
from quant_research.data import generate_synthetic_prices, prices_to_returns
from quant_research.features import rolling_momentum
from quant_research.portfolio import inverse_volatility_weights, performance_summary
from quant_research.regimes import classify_volatility_regime


@dataclass(frozen=True)
class ExampleResult:
    summary: dict[str, float]
    tail: pd.DataFrame
    regime_counts: dict[str, int]


def run_regime_momentum_example(periods: int = 260, seed: int = 7) -> ExampleResult:
    """Run a simple end-to-end research example on deterministic synthetic data."""
    prices = generate_synthetic_prices(periods=periods, seed=seed)
    returns = prices_to_returns(prices)
    momentum = rolling_momentum(prices, lookback=21).reindex(returns.index).fillna(0.0)
    regime = classify_volatility_regime(returns.mean(axis=1), window=21)
    risk_budget = inverse_volatility_weights(returns, lookback=21)
    regime_mask = regime.eq("calm").astype(float)
    signals = momentum.gt(0.0).astype(float).mul(risk_budget).mul(regime_mask, axis=0)
    backtest = run_backtest(returns, signals)
    regime_counts = {
        str(key): int(value) for key, value in regime.value_counts().sort_index().items()
    }
    return ExampleResult(
        summary=performance_summary(backtest["portfolio_returns"]),
        tail=backtest.tail(5).round(6),
        regime_counts=regime_counts,
    )
