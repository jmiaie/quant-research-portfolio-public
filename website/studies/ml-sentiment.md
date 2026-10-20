# ML Sentiment Study

**Evaluation:** previously inspected historical evaluation (2025 block, n = 197, twelve issuers)
— not an untouched holdout.

## Question

Does point-in-time Loughran-McDonald filing-text sentiment add predictive information beyond
market-only features for short-horizon returns, tested without leakage?

## Result

- **Failure to demonstrate.** Δ log loss (combined − market-only) = +0.0041, block-bootstrap 95%
  interval [−0.0049, +0.0108], which includes zero. Balanced-accuracy delta −0.027.
- This is not a claim that filing text is useless, and not a claim that the effect is exactly zero:
  n = 197 is too small to rule out a small effect.

## Read the paper

- [Technical paper](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor/blob/036c3d33c34afb6a6d9f1846dee18f3fbcc17727/publication/sentiment-study/TECHNICAL-PAPER.md) (pinned to `036c3d3`)
- [Case study](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor/blob/036c3d33c34afb6a6d9f1846dee18f3fbcc17727/publication/sentiment-study/CASE-STUDY.md) ·
  [Claim register](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor/blob/036c3d33c34afb6a6d9f1846dee18f3fbcc17727/publication/sentiment-study/CLAIM-REGISTER.md) ·
  [Data provenance](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor/blob/036c3d33c34afb6a6d9f1846dee18f3fbcc17727/publication/sentiment-study/SOURCE-GATE.md)
- Figures: [`figures/` at the pinned commit](https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor/tree/036c3d33c34afb6a6d9f1846dee18f3fbcc17727/publication/sentiment-study/figures) (embedding them on this site is a roadmap item)

## Verify

```bash
git clone https://github.com/jmiaie/ML_Sentiment_Augmented_Price_Predictor.git
cd ML_Sentiment_Augmented_Price_Predictor && git checkout 036c3d33c34afb6a6d9f1846dee18f3fbcc17727
python3 publication/sentiment-study/scripts/publication_pack.py check
python3 publication/sentiment-study/scripts/claim_crosscheck.py
```

Expected: `check OK: 18 declared artifact hashes verified, 4 generated files byte-identical, 22 map citations verified`
and `claim cross-check OK: 178 independent assertions passed`. Standard library only.
