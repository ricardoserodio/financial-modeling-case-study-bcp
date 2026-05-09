# Data Quality Report

This report documents the data quality review for the **Millennium bcp / Banco Comercial Português** financial modeling case study.

The objective is to ensure that all financial figures used in the model are traceable, consistent, publicly sourced and suitable for an educational portfolio project.

This project uses only publicly available information and does not include personal data, internal banking information or confidential information.

---

## 1. Report Purpose

The purpose of this report is to summarise the quality of the data used in the financial model.

The review focuses on:

- source traceability;
- period consistency;
- unit consistency;
- reported vs calculated figures;
- ratio validation;
- forecast assumption documentation;
- market data validation;
- missing values;
- human review status.

---

## 2. Data Files Reviewed

| File | Purpose | Status |
|---|---|---|
| `data/source_mapping.csv` | Maps each figure to a public source | Pending |
| `data/historical_financials.csv` | Stores historical financial data | Pending |
| `data/banking_ratios.csv` | Stores reported and calculated banking ratios | Pending |
| `data/forecast_template.csv` | Stores forecast structure | Pending |
| `data/scenario_assumptions.csv` | Stores scenario assumptions | Pending |
| `data/market_data_template.csv` | Stores market data inputs | Pending |
| `data/peer_comparison_template.csv` | Stores peer comparison data | Pending |

---

## 3. Source Traceability Review

Each key figure should be mapped to a public source.

| Area | Source Requirement | Review Status |
|---|---|---|
| Income statement data | Official annual reports or earnings presentations | Pending |
| Balance sheet data | Official annual reports | Pending |
| Capital ratios | Official annual reports or regulatory disclosures | Pending |
| Asset quality ratios | Official annual reports or earnings presentations | Pending |
| Market data | Euronext or public market data provider | Pending |
| Peer comparison data | Public reports or public market data | Pending |

Review questions:

- Is the source public?
- Is the source official or reliable?
- Is the period clearly identified?
- Is the figure reported or calculated?
- Is the source documented in `source_mapping.csv`?

---

## 4. Period Consistency Review

The model uses the following periods:

| Period | Type | Status |
|---|---|---|
| 2022A | Actual | Pending |
| 2023A | Actual | Pending |
| 2024A | Actual | Pending |
| 2025A | Actual | Pending |
| 2026E | Estimate | Pending |
| 2027E | Estimate | Pending |
| 2028E | Estimate | Pending |

Review checks:

- Full-year data should be used for actual years.
- Quarterly or 9M data should not be mixed with annual figures.
- Forecast years should be clearly marked as estimates.
- Historical and forecast periods should be visually separated in the model.

---

## 5. Unit Consistency Review

Preferred model units:

| Data Type | Preferred Unit | Status |
|---|---|---|
| Income statement items | EUR million | Pending |
| Balance sheet items | EUR million | Pending |
| Capital figures | EUR million | Pending |
| Share price | EUR | Pending |
| Per-share data | EUR | Pending |
| Ratios | % | Pending |
| Multiples | x | Pending |

Review checks:

- Confirm whether source documents report in EUR, EUR thousand or EUR million.
- Convert values consistently before entering them into the model.
- Avoid mixing percentages and decimals.
- Avoid mixing accounting data and market data without date/source clarity.

---

## 6. Reported vs Calculated Figures

The model should clearly distinguish reported figures from calculated figures.

| Figure Type | Examples | Status |
|---|---|---|
| Reported figures | Net income, total assets, customer deposits, CET1 ratio | Pending |
| Calculated figures | ROA, loan-to-deposit, P/B, P/E, dividend yield | Pending |
| Estimated figures | 2026E, 2027E and 2028E forecast values | Pending |

Review checks:

- Reported figures should be traceable to public sources.
- Calculated figures should include formulas.
- Estimated figures should be linked to assumptions.
- Any difference between reported and calculated ratios should be explained.

---

## 7. Ratio Validation Review

Key ratios to validate:

| Ratio | Validation Method | Status |
|---|---|---|
| ROE | Reported figure or net income / average equity | Pending |
| ROA | Net income / average total assets | Pending |
| Cost-to-income | Operating costs / operating income | Pending |
| Net interest margin | Reported figure where available | Pending |
| Cost of risk | Reported figure where available | Pending |
| NPL / NPE ratio | Official reported figure | Pending |
| Loan-to-deposit ratio | Loans to customers / customer deposits | Pending |
| CET1 ratio | Official reported regulatory figure | Pending |
| P/B | Market capitalisation / equity | Pending |
| P/E | Market capitalisation / net income | Pending |
| Dividend yield | Dividend per share / share price | Pending |

---

## 8. Missing Data Review

Missing values should be reviewed before finalising the model.

| Data Area | Missing Data Risk | Status |
|---|---|---|
| Historical financials | Some line items may use different terminology across reports | Pending |
| Ratios | Some ratios may be reported differently across years | Pending |
| Market data | Market data depends on selected valuation date | Pending |
| Peer comparison | Peer data may not be fully comparable | Pending |
| Forecast assumptions | Assumptions must be completed manually | Pending |

Missing data should be classified as:

| Status | Meaning |
|---|---|
| Pending | Not yet reviewed |
| Not Available | Not found in public sources |
| Needs Review | Requires additional checking |
| Calculated | Derived from public data |
| Validated | Reviewed and accepted |

---

## 9. Forecast Assumption Review

Forecast assumptions should be documented in `assumptions.md` and structured in `data/scenario_assumptions.csv`.

Review checks:

- Are assumptions explicit?
- Are conservative, base and optimistic scenarios separated?
- Are assumptions linked to historical trends or public information?
- Are assumptions realistic and not overly optimistic?
- Are forecast figures clearly marked as estimates?
- Are outputs presented as scenarios rather than predictions?

---

## 10. Market Data Review

Market data must be dated and sourced.

| Item | Date Required | Source Required | Status |
|---|---|---|---|
| Share price | Yes | Yes | Pending |
| Market capitalisation | Yes | Yes | Pending |
| Number of shares | Yes | Yes | Pending |
| P/B | Yes | Yes | Pending |
| P/E | Yes | Yes | Pending |
| Dividend yield | Yes | Yes | Pending |

Review checks:

- Use the same date for share price and market capitalisation.
- Do not mix market data from different dates without explanation.
- Use market data only for illustrative valuation purposes.
- Avoid presenting market data as permanent or predictive.

---

## 11. Bias and Human Review

The project includes a human-in-the-loop review approach.

Main bias risks:

| Bias Type | Risk | Mitigation |
|---|---|---|
| Data bias | Using only favourable data | Use multi-year historical data |
| Selection bias | Choosing favourable peers | Explain peer selection |
| Assumption bias | Overly optimistic forecasts | Use multiple scenarios |
| Confirmation bias | Forcing a preferred conclusion | Let the data drive the memo |
| Valuation bias | Choosing convenient multiples | Use sensitivity analysis |
| Source bias | Relying on weak sources | Prioritise official sources |
| AI output bias | Accepting generated content without review | Apply human review checklist |

The human review checklist is documented in `notes/model_review_checklist.md`.

---

## 12. Validation Script

The project includes a Python validation script:

`data/validation_checks.py`

The script checks:

- required columns;
- missing values in key fields;
- expected period columns;
- validation status values;
- basic file structure consistency.

Expected command:

`python data/validation_checks.py`

---

## 13. Current Data Quality Status

| Area | Status | Notes |
|---|---|---|
| Source mapping | Pending | Template created; values to be extracted |
| Historical financials | Pending | Template created; values to be extracted |
| Banking ratios | Pending | Template created; values to be extracted or calculated |
| Forecast assumptions | Pending | Template created; assumptions to be completed |
| Market data | Pending | Template created; valuation date to be selected |
| Peer comparison | Pending | Template created; peers to be reviewed |
| Human review | Pending | Checklist created |

---

## 14. Final Review Checklist

Before finalising the model, confirm:

- all key figures are mapped to public sources;
- all units are consistent;
- all periods are correct;
- actual data and forecast data are separated;
- reported and calculated figures are labelled;
- formulas are documented;
- missing data is explained;
- market data is dated;
- assumptions are documented;
- no personal data is included;
- no internal banking data is included;
- no confidential information is included;
- no investment recommendation language is used.

---

## Disclaimer

This data quality report is part of an educational financial modeling case study.

It uses only publicly available information and does not include personal data, internal banking information or confidential information.

The project does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.
