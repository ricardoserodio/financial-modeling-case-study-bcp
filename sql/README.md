# SQL Layer

## Purpose

This folder contains SQL scripts for the Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank project.

The SQL layer is designed to demonstrate how structured banking data, ratio analysis, data quality checks, forecast assumptions and scenario analysis outputs can be queried in an analytical workflow.

This is a portfolio and educational component. It is not intended to represent an official bank database, production data model or investment recommendation tool.

## Files

| File | Purpose |
|---|---|
| `create_tables.sql` | Defines analytical tables mirroring the project CSV datasets. |
| `banking_ratio_queries.sql` | Provides example queries for historical banking ratio analysis. |
| `data_quality_queries.sql` | Provides validation, missing value and source traceability queries. |
| `forecast_queries.sql` | Provides forecast, scenario and sensitivity-style analytical queries. |

## Covered Datasets

The SQL schema covers the following project datasets:

- `financial_data.csv`
- `banking_ratios.csv`
- `source_mapping.csv`
- `extraction_tracker.csv`
- `forecast_assumptions.csv`
- `forecast_financials.csv`
- `forecast_ratios.csv`
- `scenario_analysis.csv`

## Analytical Areas

The SQL layer supports analysis of:

- Historical financial statement metrics
- Banking ratios
- Profitability
- Efficiency
- Asset quality
- Liquidity
- Capital
- Source mapping
- Extraction tracking
- Forecast assumptions
- Forecast financials
- Forecast ratios
- Scenario analysis
- Data quality review

## Data Quality Workflow

The SQL files include queries to identify:

- Items not marked as `Reviewed`
- Missing values
- Pending source mappings
- Pending extraction tracker items
- Forecast outputs requiring human review

This supports the project narrative of a controlled, human-reviewed financial data workflow.

## Forecast Workflow

The forecast SQL queries are designed to review:

- Base, Optimistic and Conservative scenarios
- Forecast income statement lines
- Forecast balance sheet items
- Forecast ratios
- Scenario variance versus the Base case
- Risk level and scenario interpretation

Forecast outputs are marked as `To Review` until manually reviewed.

## AI-Assisted, Human-Reviewed Workflow

This project follows an AI-assisted, human-reviewed workflow.

AI tools may support documentation, code generation, consistency checks and analytical framing. However, all financial figures, assumptions, interpretations and final outputs require human review before publication.

## Disclaimer

This SQL layer is for educational and portfolio purposes only.

It does not constitute financial advice, investment advice, valuation advice, credit advice, legal advice or a recommendation to buy, sell or hold any financial instrument.

Forecast outputs are scenario-based estimates and should not be interpreted as official projections.
