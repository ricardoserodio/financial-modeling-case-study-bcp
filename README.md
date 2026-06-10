# Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank

## Project Overview

This case study addresses a practical banking analytics problem: transforming dispersed public financial disclosures into structured, traceable datasets and reusable analytical outputs for historical performance review, banking ratio analysis, scenario modelling and data quality control.

**Status:** Portfolio case study under final validation.

Using Millennium bcp as the case study reference, the project combines public-source financial statement analysis, banking-specific ratios, illustrative forecast scenarios, source validation and review controls. The work is implemented across Python, SQL and Power BI, with supporting documentation in English and Portuguese.

The delivered outputs include structured datasets, forecast and scenario files, analytical reports, a Power BI dashboard, SQL queries, validation documentation and an educational valuation framework. Together, they demonstrate skills in banking analytics, financial data quality, financial modelling, business intelligence, finance operations and analytical communication.

An AI-assisted, human-reviewed workflow is used as a supporting governance and quality-control element. Financial figures, assumptions, interpretations and outputs remain subject to human validation.

Forecasts are illustrative, scenario-based analytical estimates and are not official projections. This project is for educational, analytical and portfolio purposes only.

---

## Key Deliverables

| Deliverable | File / Location | Purpose | Status |
|---|---|---|---|
| Executive report – English | [reports/financial_modeling_report_en.md](reports/financial_modeling_report_en.md) | Summarises the financial analysis, forecast methodology, scenarios and data quality workflow | Under final validation |
| Executive report – Portuguese | [reports/financial_modeling_report_pt.md](reports/financial_modeling_report_pt.md) | Portuguese version of the analytical report | Under final validation |
| Analytical case study memo | [investment_memo.md](investment_memo.md) | Presents the analytical structure, key areas reviewed and educational valuation framework | Under final validation |
| Valuation framework | [valuation_summary.md](valuation_summary.md) | Documents an educational banking valuation framework without completed market valuation outputs | Framework complete; future extensions optional |
| Forecast methodology | [docs/forecast_methodology.md](docs/forecast_methodology.md) | Documents forecast logic, assumptions, scenario design and limitations | Available for review |
| Dataset publication scope | [docs/dataset_publication_scope.md](docs/dataset_publication_scope.md) | Distinguishes core analytical datasets from templates and optional extensions | Available for review |
| Publication audit | [docs/final_publication_audit.md](docs/final_publication_audit.md) | Tracks final validation and public-positioning controls | In progress |
| Power BI documentation | [powerbi/README.md](powerbi/README.md) | Describes dashboard structure, data model and reporting workflow | Dashboard available; final validation in progress |
| SQL analytics documentation | [sql/README.md](sql/README.md) | Explains the SQL schema, analytical queries and data quality checks | Available |

---

## Professional Positioning

This case study supports a professional portfolio narrative focused on:

- Banking analytics
- Financial data quality
- Financial modeling
- Business intelligence
- SQL-based analytical workflows
- Power BI reporting
- Responsible AI-assisted finance workflows
- Human-in-the-loop review and validation

The project is intended to be recruiter-friendly and relevant for roles in:

- Banking Analytics
- Financial Data Quality
- Financial Research
- Risk Operations
- Credit / Banking Operations
- Business Intelligence
- Finance Transformation
- AI-assisted finance workflows

---

## Project Scope

The project covers historical data and forecast outputs across the following periods:

`2022A | 2023A | 2024A | 2025A | 2026E | 2027E | 2028E`

Historical periods are based on structured public-source data.

Forecast periods are scenario-based educational estimates and are marked as requiring human review.

---

## Main Components

### 1. Historical Financial Dataset

The historical financial dataset includes selected banking financial statement metrics such as:

- Net interest income
- Operating income
- Operating costs
- Impairments and provisions
- Net income
- Customer loans
- Customer deposits
- Total assets
- Equity

Main file:

`data/financial_data.csv`

---

### 2. Banking Ratio Dataset

The banking ratio dataset includes selected ratios across profitability, efficiency, asset quality, liquidity, capital, per share and valuation categories.

Examples include:

- ROE
- ROA
- Net interest margin
- Cost-to-income ratio
- Cost of risk
- NPE ratio
- Loan-to-deposit ratio
- LCR
- NSFR
- CET1 ratios
- EPS
- Book value per share
- Valuation ratios where available

Main file:

`data/banking_ratios.csv`

---

### 3. Power BI Dashboard

The project includes Power BI dashboard files designed as portfolio-grade business intelligence deliverables.

Power BI files:

- `powerbi/millennium_bcp_banking_dashboard_v1_clean.pbix`
- `powerbi/millennium_bcp_banking_dashboard_v2.pbix`

The first version covers the historical banking dataset with pages such as:

- Executive Overview
- Liquidity & Funding
- Asset Quality
- Profitability
- Efficiency
- Capital
- Data Quality

The v2 dashboard adds a dedicated Forecast & Scenarios page, including:

- Forecast Net Income by Scenario
- ROE by Scenario
- Cost-to-Income by Scenario
- Cost of Risk by Scenario
- CET1 Ratio by Scenario
- Scenario slicer
- Period slicer
- Forecast disclaimer

The v2 dashboard also includes simple model dimension tables:

- DimScenario
- DimPeriod

These dimensions support scenario and period filtering across forecast visuals.

Supporting Power BI documentation:

- `powerbi/powerbi_v2_improvement_plan.md`
- `powerbi/dax_measures_v2.md`
- `powerbi/dashboard_v2_notes.md`

The dashboard is intended as a portfolio-grade business intelligence deliverable and not as an investment recommendation tool.

---

### 4. Forecast Assumptions

The forecast assumptions are structured across three scenarios:

- Base
- Optimistic
- Conservative

Main file:

`data/forecast_assumptions.csv`

Forecast assumptions include:

- Net interest income growth
- Other operating income growth
- Operating costs growth
- Cost of risk
- Customer loans growth
- Customer deposits growth
- CET1 ratio assumption

All assumptions are educational estimates and are marked as requiring review.

---

### 5. Forecast Financials

The forecast financials are generated from 2025A actuals and scenario-based assumptions.

Main files:

- `scripts/build_forecast_financials.py`
- `data/forecast_financials.csv`

The forecast model estimates:

- Net interest income
- Other operating income
- Operating income
- Operating costs
- Pre-provision operating profit
- Impairments and provisions
- Net income
- Customer loans
- Customer deposits
- Total assets
- Equity
- CET1 ratio assumption

---

### 6. Forecast Ratios

Forecast ratios are generated from forecast financials and scenario assumptions.

Main files:

- `scripts/build_forecast_ratios.py`
- `data/forecast_ratios.csv`

Forecast ratios include:

- ROE
- ROA
- Cost-to-income ratio
- Loan-to-deposit ratio
- Cost of risk
- CET1 ratio assumption

For 2025A, reported ratios from the banking ratio dataset are used where available.

For 2026E–2028E, ratios are calculated from forecast outputs or taken directly from forecast assumptions.

---

### 7. Scenario Analysis

The scenario analysis compares Base, Optimistic and Conservative cases across key financial and ratio metrics.

Main files:

- `scripts/build_scenario_analysis.py`
- `data/scenario_analysis.csv`

The scenario analysis includes:

- Scenario value
- Base case value
- Variance vs Base
- Variance vs Base percentage
- Scenario logic
- Main driver
- Risk level
- Interpretation
- Validation status

---

### 8. SQL Analytics Layer

The SQL layer demonstrates how the project datasets can be queried in an analytical workflow.

SQL files:

- `sql/create_tables.sql`
- `sql/banking_ratio_queries.sql`
- `sql/data_quality_queries.sql`
- `sql/forecast_queries.sql`
- `sql/README.md`

The SQL layer covers:

- Table creation
- Historical banking ratio queries
- Data quality review queries
- Forecast review queries
- Scenario analysis queries
- Human review outputs

---

### 9. Data Quality and Source Review

The project includes a data quality workflow covering:

- Validation status
- Source mapping
- Extraction tracking
- Missing values
- Pending items
- Reviewed vs To Review classification

Main files:

- `data/source_mapping.csv`
- `data/extraction_tracker.csv`
- `data/validation_checks.py`
- `docs/project_review_checklist.md`
- `docs/banking_ratio_glossary.md`

Validation can be run with:

`python data/validation_checks.py`

Known template warnings may exist for placeholder files and should be reviewed in context.

---

## Methodology Documentation

The forecast methodology is documented in:

`docs/forecast_methodology.md`

The methodology explains:

- Forecast scope
- Base year treatment
- Revenue forecast logic
- Cost forecast logic
- Risk cost forecast logic
- Balance sheet forecast logic
- Net income bridge
- Ratio forecast logic
- Scenario analysis
- Limitations
- Final review requirements

---

## Executive Reports

The project includes two executive-style Markdown reports:

- `reports/financial_modeling_report_en.md`
- `reports/financial_modeling_report_pt.md`

The reports include:

- Cover / front matter
- Executive summary
- Project objective
- Scope of analysis
- Historical financial analysis
- Banking ratio analysis
- Banking ratio glossary summary
- Forecast methodology
- Scenario analysis
- Power BI dashboard summary
- SQL analytics workflow
- Data quality and human review notes
- Limitations and disclaimer

The reports are designed as recruiter-facing analytical deliverables under final validation and complement the README, Power BI dashboard, SQL workflow and data quality documentation.

## Project Structure

```text
financial-modeling-case-study-bcp/
│
├── data/
│   ├── financial_data.csv
│   ├── banking_ratios.csv
│   ├── source_mapping.csv
│   ├── extraction_tracker.csv
│   ├── forecast_assumptions.csv
│   ├── forecast_financials.csv
│   ├── forecast_ratios.csv
│   ├── scenario_analysis.csv
│   └── validation_checks.py
│
├── docs/
│   ├── forecast_methodology.md
│   └── project_review_checklist.md
│
├── powerbi/
│   └── millennium_bcp_banking_dashboard_v1_clean.pbix
│
├── scripts/
│   ├── build_forecast_financials.py
│   ├── build_forecast_ratios.py
│   └── build_scenario_analysis.py
│
├── sql/
│   ├── create_tables.sql
│   ├── banking_ratio_queries.sql
│   ├── data_quality_queries.sql
│   ├── forecast_queries.sql
│   └── README.md
│
└── README.md
```

---

## How to Run the Forecast Workflow

### 1. Validate existing data

`python data/validation_checks.py`

### 2. Build forecast financials

`python scripts/build_forecast_financials.py`

### 3. Build forecast ratios

`python scripts/build_forecast_ratios.py`

### 4. Build scenario analysis

`python scripts/build_scenario_analysis.py`

### 5. Re-run validation

`python data/validation_checks.py`

---

## AI-Assisted, Human-Reviewed Workflow

This project follows an AI-assisted, human-reviewed workflow.

AI tools may be used to support:

- Documentation structure
- Analytical framing
- Code generation
- Consistency checks
- Data quality review
- Drafting of methodology notes

However, all financial figures, assumptions, interpretations and final outputs require human review by the author before publication.

Forecast outputs are marked as:

`To Review`

Historical reviewed figures are marked as:

`Reviewed`

---

## Limitations

This project has several limitations:

- It is based only on publicly available information.
- It is a simplified educational model.
- It does not replicate internal bank forecasting methodology.
- It does not model all regulatory capital movements.
- It does not model risk-weighted assets in detail.
- It does not model full dividend, buyback or OCI impacts.
- It does not provide valuation advice.
- It does not provide investment recommendations.
- It should not be interpreted as an official forecast.

---

## Disclaimer

This project is for educational, analytical and portfolio purposes only.

It does not constitute:

- Financial advice
- Investment advice
- Valuation advice
- Credit advice
- Legal advice
- A recommendation to buy, sell or hold any financial instrument

All forecast figures are scenario-based estimates and should be interpreted as analytical modelling outputs, not as official projections.

The author is not affiliated with Millennium bcp for the purpose of this project. The project uses public information only.

---

## Suggested CV Description

Built a financial modeling case study on a listed Portuguese bank, including financial statement analysis, banking ratio analysis, forecast assumptions, valuation-aware scenario analysis, Power BI dashboarding, SQL analytical queries and source validation using only publicly available information.

---

## Suggested LinkedIn / Portfolio Description

Public-source banking analytics case study combining financial modeling, Power BI, SQL, scenario analysis and an AI-assisted, human-reviewed data quality workflow.

---

## Author

Ricardo Serôdio

Professional portfolio:

`https://ricardoserodio.com`

GitHub:

`https://github.com/ricardoserodio`

## Dataset Publication Scope

The core analytical datasets included in the final validation scope are defined in:

`docs/dataset_publication_scope.md`

Some template, reference and legacy files are intentionally retained for transparency, modelling structure and future extension. These files should not be interpreted as final analytical outputs unless explicitly marked as core datasets.

The core forecast horizon is:

- 2026E
- 2027E
- 2028E

Forecast outputs are illustrative, scenario-based and require human review before any professional use. They are not official projections, investment recommendations or price targets.

