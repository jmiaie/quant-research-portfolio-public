# Research Standards

[Back to main README](../../README.md)

Every portfolio project should document a falsifiable economic hypothesis, data lineage, validation design, and implementation limits before results are promoted as credible evidence.

## Required Questions for Every Quantitative Strategy

1. What is the economic hypothesis?
2. What data is used?
3. What is the universe?
4. How is data cleaned?
5. What information was actually available at decision time?
6. What is the training/formation period?
7. What is the validation period?
8. What is the true out-of-sample period?
9. What are the trading rules?
10. What transaction costs are assumed?
11. What execution assumptions are used?
12. How sensitive are results to parameters?
13. What benchmark is appropriate?
14. What risk factors explain returns?
15. What are the principal failure modes?
16. Is the result statistically and economically significant?

## Minimum Evidence Expectations

- Reproducible environment and documented dependencies
- Explicit separation between exploratory work and final evaluation
- Benchmark comparisons that are appropriate for the strategy or model class
- Statistical uncertainty estimates for key claims where feasible
- Clear discussion of model risk, operational risk, and failure scenarios
