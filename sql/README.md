# SQL Layer

## Purpose

This folder contains SQL scripts for the Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank project.

The SQL layer demonstrates how structured banking datasets can be loaded into a local SQLite database and queried in an analytical workflow.

This is a portfolio and educational component. It is not intended to represent an official bank database, production data model or investment recommendation tool.

## Files

| File | Purpose |
|---|---|
| `create_tables.sql` | Defines analytical tables mirroring the project CSV datasets. |
| `banking_ratio_queries.sql` | Provides example queries for historical banking ratio analysis. |
| `data_quality_queries.sql` | Provides validation, missing value and source traceability queries. |
| `forecast_queries.sql` | Provides forecast, scenario and analytical review queries. |

## Related Python Scripts

| Script | Purpose |
|---|---|
| `scripts/load_sqlite_database.py` | Loads the structured CSV datasets into a local SQLite database. |
| `scripts/run_sql_analysis.py` | Executes analytical SQL queries against the SQLite database and exports CSV outputs. |

## Local SQLite Workflow

The SQL workflow uses a local SQLite database:

`data/bcp_case_study.sqlite`

This database is generated locally and is excluded from GitHub through `.gitignore`.

To create or refresh the local SQLite database, run:

`python scripts/load_sqlite_database.py`

This loads the following CSV datasets into SQL tables:

- `financial_data.csv`
- `banking_ratios.csv`
- `source_mapping.csv`
- `extraction_tracker.csv`
- `forecast_assumptions.csv`
- `forecast_financials.csv`
- `forecast_ratios.csv`
- `scenario_analysis.csv`

## Running SQL Analysis

To execute analytical SQL queries and export review outputs, run:

`python scripts/run_sql_analysis.py`

The script generates CSV outputs in:

`outputs/sql_analysis/`

Example outputs include:

- `table_row_counts.csv`
- `banking_ratios_2025_snapshot.csv`
- `forecast_net_income_by_scenario.csv`
- `forecast_roe_by_scenario.csv`
- `scenario_net_income_variance.csv`
- `forecast_outputs_requiring_review.csv`

These outputs demonstrate that SQL queries were executed against structured banking datasets.

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
- Human review workflow

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

## Professional Relevance

This SQL layer demonstrates the ability to:

- Load structured financial datasets into a relational database
- Query banking ratios and forecast outputs
- Review data quality through SQL
- Export analytical outputs for review
- Build a reproducible finance analytics workflow

Suggested CV wording:

`Loaded structured banking datasets into SQLite and executed SQL analytics queries for banking ratio analysis, forecast review and data quality checks.`

## AI-Assisted, Human-Reviewed Workflow

This project follows an AI-assisted, human-reviewed workflow.

AI tools may support documentation, code generation, consistency checks and analytical framing. However, all financial figures, assumptions, interpretations and final outputs require human review before publication.

## Disclaimer

This SQL layer is for educational and portfolio purposes only.

It does not constitute financial advice, investment advice, valuation advice, credit advice, legal advice or a recommendation to buy, sell or hold any financial instrument.

Forecast outputs are scenario-based estimates and should not be interpreted as official projections.
