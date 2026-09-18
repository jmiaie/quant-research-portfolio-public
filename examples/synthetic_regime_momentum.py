from quant_research.examples import run_regime_momentum_example

if __name__ == "__main__":
    result = run_regime_momentum_example()

    print("Synthetic regime-aware momentum example")
    print("\nSummary metrics")
    for key, value in result.summary.items():
        print(f"- {key}: {value:.4f}")

    print("\nRegime counts")
    for key, value in result.regime_counts.items():
        print(f"- {key}: {value}")

    print("\nLast 5 backtest rows")
    print(result.tail.to_string())
