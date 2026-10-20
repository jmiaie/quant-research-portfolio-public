# How verification works

Each study ships a reproducibility bundle under `publication/` in its own repository. Its
verifier is **offline and deterministic**: no network, no credentials, no re-fitting. It
**fails closed**, so a drifted artifact fails with a named reason instead of passing silently.

| Study | Pinned commit | Verifier |
| --- | --- | --- |
| Financial Dynamics Model | `86a843f` | `publication/historical-regime-study/scripts/verify_pack.py` |
| Statistical Arbitrage Engine | `6ae04ed` | `publication/stat-arb-study/scripts/publication_pack.py check` + `claim_crosscheck.py` |
| Options Volatility Risk Lab | `0b64176` | `publication/options-risk-study/scripts/verify_pack.py` |
| ML Sentiment Study | `036c3d3` | `publication/sentiment-study/scripts/publication_pack.py check` + `claim_crosscheck.py` |

Full commands, install steps and expected output for each study:
[Reproducing the Results](https://github.com/jmiaie/quant-research-portfolio-public/blob/main/portfolio/VERIFYING.md).

## Current badge status

The "claims verified" badge on the home page is **manual**: the commands above were run from a
fresh clone of each pinned commit, as recorded in the hub's `portfolio/VERIFYING.md`. This site
does not yet re-run the verifiers. Until it does, treat the badge as a dated record, not a live
status.

## Scope

A pass establishes artifact integrity at the pinned commit. It does not establish out-of-sample
performance and is no substitute for reading each paper's methodology and limitations.
