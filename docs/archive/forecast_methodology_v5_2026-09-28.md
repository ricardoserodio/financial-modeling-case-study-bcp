# Previous v5 methodology - superseded for scenarios

Current model: ../../revisions/2026-09-29/METHODOLOGY.md

# Forecast methodology - H1 2026 update

Information cut-off: 28 September 2026. Latest operating disclosure: H1 2026, published 29 July 2026.

2025A remains the last full-year historical reference. 2026E is **reported H1 2026 + estimated H2 2026** for income-statement flows. Balance-sheet stocks start at June 2026 and are projected to December; they are never added to June stocks. Growth rates in the 2026E assumption column mean H2/H1 growth for income and costs, or June/December growth for stocks. 2027E and 2028E use annual growth rates.

Eight drivers across three scenarios and three years give 72 explicit parameters. They are author-selected sensitivities, not issuer guidance, fitted probabilities or backtested forecasts. The Base scenario keeps H2 net interest income flat against H1, then grows it 2% and 3% in 2027/28; other assumptions are in `data/forecast_assumptions.csv`.

- Other operating income = operating income - net interest income. This includes more than commissions.
- Operating income = net interest income + other operating income.
- Pre-provision operating profit = operating income - operating costs.
- H2 credit impairment charge = projected December net loans × annualised cost-of-risk assumption / 10,000 × 0.5. Later annual charges omit the half-year factor.
- Profit conversion factor = 565.8 / (1950.3 - 720.2 - 104.4) = 0.5026205916.
- Estimated net income = (operating income - costs - credit impairments) × conversion factor. The residual factor absorbs other impairments, modification results, taxes and minorities; these are not subtracted again.
- Forecast assets grow at the average of loan and deposit growth rates.
- Closing equity = prior closing equity + forecast-period net income × retention rate. For 2026 only H2 forecast net income is retained because June equity already incorporates H1. Retention is a sensitivity (Base 10%, Optimistic 20%, Conservative 0%), not a dividend or buyback prediction. OCI and other equity movements are not modelled.
- Forecast ROE/ROA use closing total equity/assets, unlike the issuer's reported ratios based on averages and adjustments. Historical-to-forecast ROE/ROA are not directly comparable.
- Loan-to-deposit uses net loans / deposits and other customer resources. It excludes off-balance-sheet customer funds from the denominator.
- CET1 is a direct scenario assumption. No RWA or regulatory capital model is claimed.

Calculations retain full precision internally, then publish financial values to 0.1 EUR million and ratios to 0.001. Ratios use published rounded forecast financials. `scripts/validate_publication.py` independently recomputes 162 forecast cells with Decimal arithmetic and checks 126 scenario comparisons.
