from __future__ import annotations

import pandas as pd

from quant_research.regimes import classify_volatility_regime


def test_classify_volatility_regime_marks_higher_vol_periods() -> None:
    returns = pd.Series([0.001] * 10 + [0.03, -0.03] * 10)

    regimes = classify_volatility_regime(returns, window=5, threshold_quantile=0.6)

    assert set(regimes.unique()) <= {"calm", "stressed"}
    assert (regimes.iloc[10:] == "stressed").any()
