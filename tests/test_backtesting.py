from __future__ import annotations

import pandas as pd
import pytest

from quant_research.backtesting import lagged_positions, normalize_signals, run_backtest


def test_normalize_signals_scales_to_unit_gross_exposure() -> None:
    signals = pd.DataFrame({"a": [1.0], "b": [-1.0]})

    normalized = normalize_signals(signals)

    assert normalized.abs().sum(axis=1).iloc[0] == pytest.approx(1.0)
    assert normalized.iloc[0].tolist() == pytest.approx([0.5, -0.5])


def test_lagged_positions_prevent_lookahead_bias() -> None:
    index = pd.bdate_range("2024-01-01", periods=3)
    signals = pd.DataFrame({"a": [1.0, 0.0, 1.0]}, index=index)

    positions = lagged_positions(signals)

    assert positions["a"].tolist() == pytest.approx([0.0, 1.0, 0.0])


def test_run_backtest_compounds_using_lagged_positions() -> None:
    index = pd.bdate_range("2024-01-01", periods=3)
    returns = pd.DataFrame({"a": [0.10, 0.10, -0.05]}, index=index)
    signals = pd.DataFrame({"a": [1.0, 1.0, 1.0]}, index=index)

    backtest = run_backtest(returns, signals)

    assert backtest["portfolio_returns"].tolist() == pytest.approx([0.0, 0.10, -0.05])
    assert backtest["nav"].iloc[-1] == pytest.approx(1.045)
