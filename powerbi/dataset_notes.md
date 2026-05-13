# Power BI Dataset Notes ? Millennium bcp Case Study

## Purpose

This document explains how the project datasets should be used in Power BI.

The goal is to connect the Power BI dashboard to the structured CSV files already created in the project, allowing the dashboard to refresh as the underlying data is updated.

The Power BI layer should support:

- banking analytics;
- financial trend analysis;
- ratio analysis;
- data quality review;
- source validation visibility;
- human-in-the-loop review.

---

## Main CSV Files

### `data/financial_data.csv`

This file contains the main financial statement and balance sheet metrics.

Recommended Power BI use:

| Field | Use |
|---|---|
| `bank_name` | Entity filter |
| `period` | Year/period axis |
| `metric` | Financial metric selector |
| `category` | Metric grouping |
| `value` | Main numeric value |
| `unit` | Unit label |
| `validation_status` | Data quality status |
| `reported_or_calculated` | Reported vs calculated flag |
| `source_document` | Source traceability |
| `notes` | Review context |

Recommended visuals:

- net income trend;
- net interest income trend;
- operating income trend;
- operating costs trend;
- total assets trend;
- customer loans trend;
- customer deposits/customer funds trend;
- equity trend.

---

### `data/banking_ratios.csv`

This file contains the main banking ratios across 2022A?2025A.

The current format is wide, with one column per period:

| Column | Meaning |
|---|---|
| `ratio` | Ratio name |
| `category` | Ratio grouping |
| `formula` | Ratio formula or definition |
| `2022A` | 2022 actual value |
| `2023A` | 2023 actual value |
| `2024A` | 2024 actual value |
| `2025A` | 2025 actual value |
| `unit` | %, bps, EUR or x |
| `source_status` | Review status |
| `notes` | Additional context |

Recommended Power BI transformation:

The file should be unpivoted in Power Query so that the period columns become rows.

Target shape:

| ratio | category | formula | period | value | unit | source_status | notes |
|---|---|---|---|---:|---|---|---|

Recommended visuals:

- ROE trend;
- ROA trend;
- net interest margin trend;
- cost-to-income trend;
- cost of risk trend;
- NPE ratio trend;
- NPE coverage ratio trend;
- LCR trend;
- NSFR trend;
- CET1 ratio trend.

---

### `data/source_mapping.csv`

This file documents source traceability for each extracted item.

Recommended Power BI use:

| Field | Use |
|---|---|
| `item` | Metric or ratio name |
| `category` | Analytical grouping |
| `period` | Year/period |
| `value` | Extracted value |
| `unit` | Unit |
| `source_document` | Official document used |
| `source_type` | Source type |
| `source_section_or_page` | Section/page reference |
| `reported_or_calculated` | Reported vs calculated flag |
| `calculation_method` | Calculation explanation |
| `validation_status` | Data quality status |
| `notes` | Review notes |

Recommended visuals:

- source coverage table;
- reviewed vs needs review count;
- reported vs calculated split;
- source document coverage;
- pending/review items table.

---

### `data/extraction_tracker.csv`

This file documents the extraction workflow.

Recommended Power BI use:

| Field | Use |
|---|---|
| `data_item` | Extracted item |
| `category` | Analytical grouping |
| `period` | Year/period |
| `source_document` | Source document |
| `page_or_section` | Location in source |
| `value_extracted` | Extracted value |
| `unit` | Unit |
| `entered_in_file` | Target CSV file |
| `validation_status` | Review status |
| `review_notes` | Review comments |

Recommended visuals:

- extraction status by period;
- extraction status by category;
- reviewed vs needs review;
- entered-in-file coverage;
- review notes table.

---

## Suggested Power BI Tables

Recommended imported tables:

| Power BI Table Name | Source CSV |
|---|---|
| `FinancialData` | `data/financial_data.csv` |
| `BankingRatios` | `data/banking_ratios.csv` |
| `SourceMapping` | `data/source_mapping.csv` |
| `ExtractionTracker` | `data/extraction_tracker.csv` |

Optional future tables:

| Power BI Table Name | Source CSV |
|---|---|
| `MarketData` | `data/market_data_template.csv` |
| `PeerComparison` | `data/peer_comparison_template.csv` |
| `ForecastAssumptions` | `data/forecast_assumptions.csv` |
| `ScenarioAnalysis` | `data/scenario_analysis.csv` |

---

## Recommended Data Model

For the first dashboard version, keep the model simple.

Recommended approach:

- load each CSV as a separate table;
- transform `BankingRatios` from wide to long format;
- use `period` consistently across tables;
- avoid complex relationships in the first version;
- use simple slicers for period, category and validation status.

Potential common fields:

| Field | Tables |
|---|---|
| `period` | FinancialData, BankingRatios, SourceMapping, ExtractionTracker |
| `category` | All core tables |
| `validation_status` | FinancialData, SourceMapping, ExtractionTracker |
| `source_status` | BankingRatios |

For the MVP dashboard, relationships are optional. Many visuals can be built directly from each table.

---

## Power Query Notes

Recommended transformations:

### FinancialData

- Confirm `value` is decimal number.
- Confirm `period` is text.
- Confirm `metric` is text.
- Keep `notes` as text.
- Do not remove `validation_status`.

### BankingRatios

- Keep `ratio`, `category`, `formula`, `unit`, `source_status` and `notes`.
- Unpivot period columns: `2022A`, `2023A`, `2024A`, `2025A`.
- Rename unpivoted columns:
  - `Attribute` ? `period`
  - `Value` ? `value`
- Confirm `value` is decimal number.

### SourceMapping

- Confirm `value` is decimal number.
- Keep source and validation fields.
- Use this table mainly for traceability and data quality visuals.

### ExtractionTracker

- Confirm `value_extracted` is decimal number.
- Keep review notes.
- Use this table mainly for audit trail visuals.

---

## Data Quality Controls Before Refresh

Before refreshing the Power BI dashboard, run:

`python data/validation_checks.py`

Expected current output:

- `market_data_template.csv`: missing `category` values.
- `peer_comparison_template.csv`: missing `business_type` values.

These are acceptable template-stage warnings.

No critical issue should block the dashboard refresh if only these two warnings appear.

---

## Human-in-the-Loop Review Items

The following items should remain visible in the dashboard or supporting documentation:

| Item | Reason |
|---|---|
| Customer deposits vs customer funds | Terminology may differ across disclosures. |
| 2022A impairments and provisions | Calculated from multiple impairment/provision components. |
| 2022A book value per share | Still pending. |
| Reexpressed comparative figures | Prior-year figures may be reexpressed in later reports. |
| Reported vs calculated values | Calculated values may differ from bank methodology. |
| Capital ratio basis | Phased-in and fully implemented ratios must not be mixed. |
| Valuation ratios | Pending until market data and valuation date are documented. |

---

## Dashboard MVP Scope

The first Power BI dashboard should include:

1. Executive Overview.
2. Profitability.
3. Efficiency.
4. Asset Quality.
5. Liquidity & Funding.
6. Capital.
7. Data Quality.

The first version should focus on clarity, not complexity.

---

## Refresh Workflow

Recommended workflow:

1. Update CSV files.
2. Run validation checks.
3. Commit and push changes to GitHub.
4. Open Power BI Desktop.
5. Click Refresh.
6. Review visuals.
7. Check data quality page.
8. Export screenshots only after dashboard review.

---

## Disclaimer

The Power BI dashboard is part of an educational and professional portfolio case study.

It uses only public information manually structured into CSV files.

It does not provide investment advice, financial advice, valuation advice, a price target or a buy/sell/hold recommendation.

All figures should be independently verified before professional, academic or investment-related use.
