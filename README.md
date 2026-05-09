# Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank

## Project Overview

This project is a professional portfolio case study focused on the financial analysis and simplified financial modeling of **Millennium bcp / Banco Comercial Português**, a Portuguese listed bank.

The objective is to demonstrate practical skills in banking analysis, financial modeling, valuation logic, public-source data validation and investment research writing.

This project is designed for educational, GitHub, CV and LinkedIn portfolio purposes.

---

## Why Millennium bcp?

Millennium bcp was selected because it is a Portuguese listed bank with publicly available financial information, including annual reports, investor presentations and market disclosures.

The bank is suitable for this case study because it allows analysis of:

- Banking profitability
- Net interest income
- Fees and commissions
- Operating efficiency
- Asset quality
- Capital ratios
- Loans and customer deposits
- Banking valuation multiples
- Scenario and sensitivity analysis

As a listed bank, Millennium bcp is more appropriate for an equity research and financial modeling case study than non-listed banks with limited public market data.

---

## Project Objectives

The main objectives of this project are to:

- Build a simplified bank financial model using public information
- Analyse historical financial performance
- Review key banking ratios
- Create a 3-year forecast with clear assumptions
- Perform a basic valuation using banking-relevant multiples
- Test scenarios and sensitivities
- Document source validation and data quality checks
- Produce a professional investment-style memo
- Demonstrate applied financial modeling skills for finance, banking analytics and AI finance evaluation roles

---

## Skills Demonstrated

This project is intended to demonstrate practical skills in:

- Financial modeling
- Banking analysis
- Financial statement analysis
- Equity research basics
- Valuation multiples
- Scenario analysis
- Sensitivity analysis
- Source validation
- Financial data quality
- Public-source data validation
- Investment memo writing
- Professional communication
- GitHub portfolio presentation

---

## Project Structure

    financial-modeling-case-study-bcp/
    │
    ├── README.md
    ├── RUN_PROJECT.md
    ├── PROJECT_STATUS.md
    ├── CHANGELOG.md
    ├── ROADMAP.md
    ├── sources.md
    ├── company_overview.md
    ├── assumptions.md
    ├── ratio_analysis.md
    ├── valuation_summary.md
    ├── investment_memo.md
    ├── disclaimer.md
    ├── requirements.txt
    │
    ├── model/
    │   ├── create_banking_model_template.py
    │   ├── create_sensitivity_analysis_template.py
    │   ├── model_structure.md
    │   ├── sensitivity_analysis_structure.md
    │   └── formula_reference.md
    │
    ├── data/
    │   ├── historical_financials.csv
    │   ├── banking_ratios.csv
    │   ├── source_mapping.csv
    │   ├── source_links.csv
    │   ├── extraction_tracker.csv
    │   ├── forecast_template.csv
    │   ├── scenario_assumptions.csv
    │   ├── market_data_template.csv
    │   ├── peer_comparison_template.csv
    │   ├── data_dictionary.md
    │   ├── data_quality_report.md
    │   ├── data_validation_rules.md
    │   └── validation_checks.py
    │
    └── notes/
        ├── data_extraction_plan.md
        └── model_review_checklist.md

---

## Main Project Files

| File | Purpose |
|---|---|
| `README.md` | Main project overview and repository guide |
| `RUN_PROJECT.md` | Instructions to run the project locally |
| `PROJECT_STATUS.md` | Current project status, completed work and pending phases |
| `CHANGELOG.md` | Project change history and planned updates |
| `ROADMAP.md` | Planned development roadmap and future project phases |
| `sources.md` | Public sources used in the project |
| `company_overview.md` | Business overview of Millennium bcp |
| `assumptions.md` | Forecast assumptions and modeling logic |
| `ratio_analysis.md` | Analysis of key banking ratios |
| `valuation_summary.md` | Educational valuation overview using banking multiples |
| `investment_memo.md` | Professional investment-style memo |
| `disclaimer.md` | GDPR, public-source and no-investment-advice disclaimer |
| `requirements.txt` | Python dependencies used in the project |
| `model/create_banking_model_template.py` | Python script to generate the banking model Excel template |
| `model/create_sensitivity_analysis_template.py` | Python script to generate the sensitivity analysis Excel template |
| `model/model_structure.md` | Documentation of the banking model structure |
| `model/sensitivity_analysis_structure.md` | Documentation of the sensitivity analysis structure |
| `model/formula_reference.md` | Reference document for the main formulas used in the model |
| `data/historical_financials.csv` | Historical financial data template based on public sources |
| `data/banking_ratios.csv` | Key banking ratios used in the analysis |
| `data/source_mapping.csv` | Source mapping and validation notes |
| `data/source_links.csv` | Official source links used for data extraction |
| `data/extraction_tracker.csv` | Tracker for data extraction from annual reports |
| `data/forecast_template.csv` | Forecast structure for the financial model |
| `data/scenario_assumptions.csv` | Conservative, base and optimistic scenario assumptions |
| `data/market_data_template.csv` | Market data template for valuation inputs |
| `data/peer_comparison_template.csv` | Peer comparison template for listed European banks |
| `data/data_dictionary.md` | Definitions of key data fields, metrics and ratios |
| `data/data_quality_report.md` | Data quality review report |
| `data/data_validation_rules.md` | Data validation rules for the project |
| `data/validation_checks.py` | Python script for basic data quality checks |
| `notes/data_extraction_plan.md` | Step-by-step data extraction plan |
| `notes/model_review_checklist.md` | Human-in-the-loop review checklist |

---

## Excel Model Generation

For local setup and execution instructions, see:

    RUN_PROJECT.md

The Excel model files are generated using Python scripts located in the `model/` folder.

To generate the banking model template:

    python model/create_banking_model_template.py

To generate the sensitivity analysis template:

    python model/create_sensitivity_analysis_template.py

These scripts create the following Excel files:

    model/banking_model.xlsx
    model/sensitivity_analysis.xlsx

The generated Excel files are templates for educational analysis and should be completed using only public information.

---

## Methodology

The case study follows a simplified financial research process:

1. Collect public financial information from annual reports, investor presentations and market disclosures.
2. Map key financial statement items relevant to banking analysis.
3. Build a historical financial dataset.
4. Calculate and review key banking ratios.
5. Define explicit forecast assumptions.
6. Build a simplified 3-year forecast.
7. Analyse base, conservative and optimistic scenarios.
8. Perform valuation using simple banking-relevant multiples.
9. Review sensitivities to key assumptions.
10. Document limitations, source reliability and data validation checks.

This project does not aim to replicate a full professional sell-side equity research model. It is a structured educational case study designed to demonstrate practical analytical capability.

---

## Key Analysis Areas

The project focuses on the following areas:

### Profitability

- Net interest income
- Fees and commissions
- Operating income
- Operating costs
- Net income
- Return on equity
- Return on assets

### Efficiency

- Cost-to-income ratio
- Operating cost trends
- Revenue mix

### Asset Quality

- Impairments and provisions
- Non-performing loan ratio
- Cost of risk, where available

### Balance Sheet

- Loans to customers
- Customer deposits
- Total assets
- Equity
- Loan-to-deposit ratio

### Capital

- CET1 ratio
- Capital adequacy
- Equity base evolution

### Valuation

- Price-to-book
- Price-to-earnings
- Dividend yield, if applicable
- Scenario-based valuation logic
- Sensitivity to ROE, cost of equity and growth assumptions

---

## Data Sources

This project uses only publicly available information, including:

- Annual reports
- Consolidated financial statements
- Investor presentations
- Market disclosures
- Public investor relations materials
- Public market data
- Euronext information
- Other reputable public financial sources

A detailed list of sources is provided in `sources.md`.

Official source links used for the data extraction process are documented in `data/source_links.csv`.

No full reports are copied into this repository. The project only references public sources and uses selected financial data for educational analysis.

---

## Data Validation Approach

Because this project is also intended to demonstrate financial data quality awareness, the model includes a basic source validation approach.

The validation process includes:

- Mapping each key figure to a public source
- Checking consistency between reported figures and calculated ratios
- Reviewing units, currencies and reporting periods
- Identifying missing data or unavailable ratios
- Separating reported figures from own calculations
- Documenting assumptions used in forecasts
- Avoiding unsupported conclusions

The project includes a Python validation script:

    python data/validation_checks.py

This makes the project relevant not only for financial research roles, but also for financial data quality, data validation and AI finance evaluation work.

---

## Human-in-the-Loop Review

The project includes a human-in-the-loop review approach to reduce analytical errors, source inconsistencies and unsupported conclusions.

The review process focuses on:

- Source traceability
- Unit consistency
- Period consistency
- Formula accuracy
- Ratio consistency
- Scenario logic
- Bias review
- Neutral investment language
- No use of personal, confidential or internal information

The review checklist is documented in `notes/model_review_checklist.md`.

---

## Project Status

The project is currently in the structure, documentation and data preparation phase.

Most financial data fields are intentionally marked as `Pending`.

The next major phase is to extract historical financial figures from official public sources and enter them into the relevant data files.

For a detailed status overview, see:

    PROJECT_STATUS.md

---

## Roadmap

The project will be developed in phases:

1. Repository structure and documentation
2. Historical financial data extraction
3. Data validation and quality review
4. Excel model generation and population
5. Forecast and scenario analysis
6. Valuation and sensitivity analysis
7. Investment memo completion
8. Final review and portfolio publication

For the full roadmap, see:

    ROADMAP.md

---

## Changelog

Project changes and planned updates are documented in:

    CHANGELOG.md

---

## Relevance for Target Roles

This project is designed to support applications for roles such as:

- Financial Research Analyst
- Investment Research Analyst
- AI Finance Evaluator
- AI Product Tester – Finance
- Banking Analyst
- Banking Analytics Analyst
- Financial Data Analyst
- Financial Data Quality Analyst
- Data Validation Analyst
- Reporting Analyst – Banking
- Wealth Management / Private Banking Support

The project demonstrates the ability to combine real banking experience with financial analysis, structured modeling, data validation and professional written communication.

---

## Limitations

This project has important limitations:

- It is a simplified educational model.
- It does not represent a full institutional equity research model.
- Forecasts are based on simplified assumptions.
- Valuation outputs are illustrative and not investment recommendations.
- Public data availability may limit the depth of the analysis.
- Market prices and valuation multiples may change over time.
- The project does not include confidential, internal or non-public information.

---

## Disclaimer

This project is for educational and portfolio purposes only and does not constitute investment advice.

This project uses only publicly available information from annual reports, investor presentations, market disclosures and other public sources. No client data, employee data, internal banking information or confidential information is used.

The analysis, assumptions, scenarios and valuation outputs are illustrative and should not be interpreted as a recommendation to buy, sell or hold any financial instrument.

This project is independent from my current and previous employers and does not reflect the views, data, systems, clients, processes or internal information of any financial institution.

---

## Author

**Ricardo Serôdio**

Banking professional with experience in wealth management, investment advisory, retail banking operations, credit, AML/CFT, KYC/CDD, MiFID II, financial products and client relationship management.

Portfolio project by Ricardo Serôdio.

Related project:

- [Portugal Term Deposit Comparator](https://github.com/ricardoserodio/portugal-term-deposit-comparator)
- [Online App](https://pt-deposit-comparator.streamlit.app)
