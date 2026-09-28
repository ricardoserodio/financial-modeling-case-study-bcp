# Millennium bcp - document revision of 29 September 2026

Information cut-off: 28 September 2026. No later reporting period has been added.
This is the current scenario package. The root-level historical pipeline and
PBIX v5 preserve the prior model; their scenario outputs are superseded by this package.

## Reproduce

Run `python reproduce_model.py` with Python 3.10 or later. Only the Python
standard library is required. Input snapshots are under inputs/data; outputs
and source records are under data; checks.json records the arithmetic checks.
The 40-page combined PDF is the publication attachment, not these working files.

## Model

Six operating drivers x three scenarios x three years = 54 assumptions.
2026 combines actual H1 flows with forecast H2 flows; stocks run June to December.
2027 and 2028 apply annual growth. Net interest income, other operating income,
costs, net customer loans and deposit resources follow the specified drivers.
H2 credit impairments = projected closing net loans x annual risk bp / 10,000 x 0.5.
The half-year factor is omitted in later annual charges. Net loans are a proxy,
not the issuer's exact gross amortised-cost denominator.

Reference estimated profit = (operating income - costs - credit impairments) x 0.48.
48% is an illustrative value within the observed historical conversion range;
it is neither a fitted estimate nor a tax rate. Sensitivities use 46%, 48%, 50%,
and 565.8 / (1950.3 - 720.2 - 104.4). H1 actual profit is never rescaled.
Other impairments, modification results, taxes and minorities remain bundled.
The scenario design is not probabilistic and has not been predictively backtested.

Base risk of 40 bp is a cautious reference near adjusted FY2024 39 bp (FY2025
release, PDF p3 note 4), rather than extrapolation of latest 32 bp. The 45 bp
in 2028 is a chosen additional stress. Revenue and volume drivers remain
illustrative author choices, not issuer guidance.

Capital policy is evaluated separately. Retention of 0%, 10% and 20% applies
to each operating scenario; June 2026 book equity is EUR 9,562m and only H2
profit is eligible in 2026. OCI, buybacks, AT1 distributions and other equity
movements are excluded. This is an isolated sensitivity, not a capital forecast.
No CET1, ROE or ROA is projected. Regulatory capital, RWA and issuer-adjusted
average denominators are not reconstructed.

## Evidence and checks

The core historical register still has 182 records: 176 source-verified values
and six recalculated impairment totals. The supplementary register contains
19 records, some overlapping the core register, for the earnings bridge,
NPE coverage decomposition and adjusted risk reference. Do not sum both counts
as unique new observations. Each supplementary record has an issuer URL and page.

81 financial output cells are independently recomputed using compounded inputs.
36 conversion outcomes are cross-checked by linear conversion identities.
27 retention outcomes are cross-checked by cumulative retained-profit identities.
The earnings bridge reconciles to 565.8 from 502.3; coverage calculations round
to reported 90.9% and 97.2%. These are source/arithmetic checks, not an audit.

## Document changes

- Complete earnings bridge and NPE numerator/denominator decomposition.
- 48% illustrative conversion reference and explicit conversion sensitivities.
- Operating and capital-policy assumptions separated.
- Direct CET1 paths and incomparable projected ROE/ROA removed.
- Nine original historical Power BI pages retained; old forecast page excluded.
- Revised scenario charts are generated in the report, not a refreshed PBIX export.
- English appendix and consistent author spelling: Ricardo Serôdio.
- Historical data cut-off retained; revision date explicitly updated.
