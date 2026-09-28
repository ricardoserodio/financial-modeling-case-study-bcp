> Historical working note retained for provenance. The current H1 2026 release is described in the root README, reports and docs/forecast_methodology.md. Status labels below describe an earlier revision.

# Metric migration — 28 September 2026

The CSV data, forecast scripts, scenario extraction and SQL now distinguish net credit impairments, other impairments and provisions, total impairments, deposits and other customer resources, and total customer funds. Source-mapped changes remain `Needs Review`; this is not author sign-off. Existing PBIX, database files, exported PDFs and screenshots are not refreshed by this change.

## Historical definitions and source vintage

All financial amounts below are EUR million. Each press-release locator is PDF page 2, Summary of indicators. The tables were extracted and visually inspected.

| Period | Net credit impairments | Other impairments/provisions | Calculated total | Deposits and other customer resources | Total customer funds | Source vintage |
|---|---:|---:|---:|---:|---:|---|
| 2022A | 300.6 | 755.6 | 1056.2 | 75907 | 92808 | [FY2022](https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/ResultadosTrimestrais/2022/Resultados-Millenniumbcp-FY22-27022023.pdf), as reported |
| 2023A | 240.0 | 859.8 | 1099.8 | 77928 | 95328 | [FY2024](https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/ResultadosTrimestrais/2024/Resultados_Millenniumbcp_FY24_final_26022025.pdf), comparative |
| 2024A | 183.3 | 674.2 | 857.5 | 84042 | 102938 | [FY2025](https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/ApresentacaoResultados/2025/Resultados_Millenniumbcp_FY25_f_25022026.pdf), restated comparative |
| 2025A | 199.5 | 625.9 | 825.4 | 89749 | 111782 | FY2025, as reported |

`Impairments and provisions` now consistently means the **calculated sum of the two disclosed impairment components**. It excludes modification results, taxes and minority interests; it is not all deductions from operating profit. The separate credit component is the forecast risk driver. The total and its components overlap: never sum every metric into a grand total.

The ambiguous `Customer deposits` key becomes `Deposits and other customer resources` everywhere in the active forecast pipeline. The disclosed total customer funds are preserved in a separate historical metric. This denominator matches the source's loan-to-deposit indicator; it is broader than pure deposits and excludes off-balance-sheet customer funds.

The migration retains the established per-year source vintage, rather than importing selected FY2025 restatements into 2023. Cross-year growth is therefore not a uniform-vintage or organic-growth measure. The previously reconciled net commissions remain 771.9 / 771.7 / 812.7 / 847.4.

## 2023 ratio reconciliation

The 2023 column in FY2024 page 2 reports ROE 15.3%; ROA 1.0%; net interest margin 3.36%; cost-to-income 30.8%; cost-to-income excluding specific items 31.6%; cost of risk 42 bps; NPE 3.4%; coverage 81.8%; restructured loans 3.0%; loan-to-deposit 70.9%; loans/balance-sheet resources 69.7%; LCR 276%; NSFR 167%; CET1 phased-in 15.5%; CET1 fully implemented 15.4%; total capital 19.9%. These replace conflicting values or confirm matching values, with one corresponding source-mapping and extraction record per updated key.

Book value per share 2023 becomes **EUR 0.417**, reported in [Annual Report 2024](https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/RelatorioContas/2024/RABCP2024Vol1PT.pdf), printed page 25 / PDF page 26. This is a reported value, not reconstructed from the simplified equity field. The formula field now points to the reported definition and treasury-share note.

EPS 2023 was subsequently reconciled to **EUR 0.054 of reported basic EPS**, using consolidated note 18, printed page 244 / PDF page 245 of Annual Report 2024. The bank subtracts EUR 37.000 million of AT1 interest from EUR 856.050 million attributable net income, obtaining EUR 819.050 million over 15,113,989,952 weighted-average shares. Basic and diluted EPS are equal in the source. The earlier 0.056 and simplified formula were corrected. Source mapping and extraction now contain one matching record. `Needs Review` preserves pending author review; other years retain their prior values.

## Forecast behavior

The three scenarios and all numeric assumptions remain unchanged. Growth previously labelled `Customer deposits growth` is explicitly applied to deposits and other customer resources. The corrected 2025 denominator is 89749 rather than total funds of 111782. The base-year proxy is 61240 / 89749 × 100 = 68.235%, consistent with the reported rounded 68.2%, rather than 54.785% from the wrong denominator.

The forecast risk line is now `Net credit impairments`. Net income still uses the existing residual conversion bridge:

`conversion = 1018.6 / (3815.2 - 1415.1 - 199.5)`

`forecast net income = (forecast operating income - forecast operating costs - forecast net credit impairments) × conversion`

The conversion implicitly absorbs non-credit impairments/provisions, modification results, tax and minorities. They are not forecast separately, and the historical total of 825.4 must not be subtracted again. This migration preserves the existing net-income scenarios and does not add a new assumption about legal-risk provisions or taxation.

Forecast cost of risk uses closing net customer loans as an educational proxy; it does not reproduce the reported average/gross exposure basis. Forecast ROE/ROA similarly use closing balances. Reported historical ratios remain separately sourced.

Copied 2025 financial and ratio values inherit their input review status. Derived historical bridge lines are `Needs Review`, and forecast rows remain `To Review`. Duplicate source keys now raise an error instead of silently selecting the first row.

## Power BI handoff

1. Preserve a copy of the existing PBIX. Refresh only after the Python/SQL checks and human source review.
2. Replace historical and forecast filters/slicers on `Customer deposits` with `Deposits and other customer resources`. Update labels to the full definition. Keep `Total customer funds` separate.
3. Replace **forecast** filters on `Impairments and provisions` with `Net credit impairments`. Historical total, credit and other components are separate series; do not aggregate them together.
4. Refresh all eight CSV tables together; the output headers are unchanged. The SQLite database and six SQL CSV exports were rebuilt after EPS reconciliation; existing PBIX/PDF outputs are still unrefreshed.
5. Compare 2025 deposits/resources 89749, credit impairments 199.5, total impairments 825.4, reported L/D 68.2%, and 2023 BVPS 0.417 against the source/SQL. Check the Base 2026 L/D is approximately 68.235%, with no denominator-induced cliff from 2025.
6. Verify the review page exposes unresolved statuses and the source status for the reconciled EPS. Save/export only after visual inspection. Update stale explanatory text and screenshots.

The old `sql/queries.sql`, alternate schema documents and `historical_financials.csv` remain legacy and outside the active pipeline; they must not be used as validation evidence. A reproducible source/forecast regression check is in `scripts/test_metric_migration.py`.
