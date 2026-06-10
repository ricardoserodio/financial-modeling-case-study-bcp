# Dataset Publication Scope

This document defines which datasets are part of the publication-ready analytical scope and which files are retained as templates, references or legacy planning material.

## 1. Core Publication Datasets

The following files are considered part of the main analytical case study:

| File | Purpose | Publication status |
|---|---|---|
| `data/financial_data.csv` | Structured historical financial data and selected forecast lines | Core dataset |
| `data/banking_ratios.csv` | Historical banking ratios and valuation-related ratio placeholders | Core dataset |
| `data/forecast_assumptions.csv` | Scenario assumptions for 2026E–2028E | Core forecast input |
| `data/forecast_financials.csv` | Scenario-based financial forecast outputs for 2026E–2028E | Core forecast output |
| `data/forecast_ratios.csv` | Scenario-based banking ratio forecast outputs for 2026E–2028E | Core forecast output |
| `data/scenario_analysis.csv` | Scenario variance analysis across Base, Optimistic and Conservative cases | Core scenario output |
| `data/source_mapping.csv` | Mapping between data items, periods, sources and validation status | Core data quality file |
| `data/extraction_tracker.csv` | Extraction and review tracking for source-based data collection | Core data quality file |
| `data/source_links.csv` | Public source inventory | Core reference file |

## 2. Template / Reference / Legacy Files

The following files are retained for transparency, modelling structure or future extension. They should not be interpreted as final publication-ready datasets unless explicitly updated.

| File | Purpose | Status |
|---|---|---|
| `data/historical_financials.csv` | Initial historical-data template | Template / legacy reference |
| `data/forecast_template.csv` | Original forecast model template | Template / reference |
| `data/scenario_assumptions.csv` | Original scenario assumptions template | Template / reference |
| `data/market_data_template.csv` | Market data template for valuation extension | Template / future extension |
| `data/peer_comparison_template.csv` | Peer comparison template for future benchmarking | Template / future extension |

## 3. Forecast Horizon

The project intentionally retains a three-year illustrative forecast horizon:

- 2026E
- 2027E
- 2028E

These outputs are scenario-based and educational. They are not official projections, investment recommendations or price targets.

## 4. Forecast Validation Status

Forecast assumptions and forecast outputs may remain marked as `To Review`.

This is intentional because forecast outputs require human review before any professional use. The purpose of the project is to demonstrate analytical workflow, scenario modelling, data quality controls and Power BI reporting — not to provide investment advice.

## 5. Valuation and Market Data

Market data, peer comparison and valuation multiples are treated as optional/future extensions unless explicitly finalised in the main report.

Any valuation language must remain:

- illustrative;
- educational;
- non-advisory;
- not a buy/sell/hold recommendation;
- not a target price.

## 6. Recruiter Interpretation

For recruiter or portfolio review, the recommended focus should be:

1. `README.md`
2. Executive reports in `reports/`
3. Power BI dashboard v3
4. Core datasets listed in Section 1
5. SQL outputs in `outputs/sql_analysis/`
6. Data quality and validation documentation

