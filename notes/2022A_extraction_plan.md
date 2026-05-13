# 2022A Extraction Plan ? Millennium bcp Case Study

## Purpose

This note defines the planned extraction workflow for the 2022A historical period.

The objective is to extend the current 2023A?2025A reviewed historical cycle to a four-year cycle:

| Period | Status |
|---|---:|
| 2022A | Pending extraction |
| 2023A | Completed |
| 2024A | Completed |
| 2025A | Completed |

## Official Source Priority

The 2022A extraction should use only official public sources from Millennium bcp / Banco Comercial Portugu?s.

Recommended source priority:

1. FY2022 Results Press Release.
2. FY2022 Financial Statements.
3. FY2022 Results Presentation.
4. FY2022 Fact Sheet.
5. Integrated Report / Annual Report, if needed for cross-checking.

## Data Items to Extract

### Financial Statement and Balance Sheet Data

| Metric | Status |
|---|---:|
| Net interest income | Pending |
| Operating income | Pending |
| Operating costs | Pending |
| Impairments and provisions | Pending |
| Net income | Pending |
| Customer loans | Pending |
| Customer deposits / customer funds | Pending |
| Total assets | Pending |
| Equity | Pending |

### Banking Ratios

| Ratio | Status |
|---|---:|
| ROE | Pending |
| ROA | Pending |
| Net interest margin | Pending |
| Cost-to-income ratio | Pending |
| Cost-to-income ratio excluding specific items | Pending |
| Cost of risk | Pending |
| NPE ratio | Pending |
| NPE coverage ratio | Pending |
| Restructured loans ratio | Pending |
| Loan-to-deposit ratio | Pending |
| Loan-to-balance-sheet-customer-resources ratio | Pending |
| LCR | Pending |
| NSFR | Pending |
| CET1 phased-in ratio | Pending |
| CET1 fully implemented ratio | Pending |
| Total capital fully implemented ratio | Pending |
| EPS | Pending |
| Book value per share | Pending |

## Data Quality Notes

The 2022A extraction must continue the same data quality principles used for 2023A?2025A:

- use official public sources only;
- document the source document and section/page;
- distinguish reported figures from calculated figures;
- flag customer deposits vs customer funds terminology;
- flag reexpressed comparative figures where applicable;
- avoid investment advice or valuation conclusions;
- keep human-in-the-loop review notes visible.

## Files to Update

The 2022A extraction should update:

| File | Action |
|---|---|
| `data/financial_data.csv` | Add 2022A financial data |
| `data/banking_ratios.csv` | Add 2022A banking ratios |
| `data/source_mapping.csv` | Add 2022A source mapping |
| `data/extraction_tracker.csv` | Add/update 2022A extraction status |
| `reports/banking_analytics_report.md` | Expand trend analysis to 2022A?2025A |
| `reports/data_quality_report.md` | Expand data quality review to 2022A?2025A |
| `PROJECT_STATUS.md` | Update once 2022A cycle is completed |
| `CHANGELOG.md` | Register 2022A update |
| `ROADMAP.md` | Mark 2022A as completed when done |

## Planned Workflow

1. Identify official FY2022 source documents.
2. Extract core financial data.
3. Extract banking ratios.
4. Update `financial_data.csv`.
5. Update `banking_ratios.csv`.
6. Update `source_mapping.csv`.
7. Update `extraction_tracker.csv`.
8. Run validation checks.
9. Update reports.
10. Commit each logical step separately.

## Current Status

2022A extraction has not started yet.

This file is a preparation note before adding 2022A data to the structured datasets.
