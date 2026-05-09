# Roadmap

This document outlines the planned development roadmap for the **Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank** project.

The project is designed for educational, portfolio and professional development purposes only.

It does not constitute investment advice.

---

## Roadmap Overview

The project will be developed in phases:

1. Repository structure and documentation
2. Historical financial data extraction
3. Data validation and quality review
4. Excel model generation and population
5. Forecast and scenario analysis
6. Valuation and sensitivity analysis
7. Investment memo completion
8. Final review and portfolio publication

---

## Phase 1 – Repository Structure and Documentation

Status:

    In progress

Objective:

Create a clean, auditable and professional project structure.

Main tasks:

- Create professional README
- Add disclaimer
- Document public sources
- Create company overview
- Create assumptions documentation
- Create ratio analysis documentation
- Create valuation summary structure
- Create investment memo template
- Create data dictionary
- Create data validation rules
- Create data quality report
- Create source links file
- Create extraction tracker
- Create local run instructions
- Create project status file
- Create changelog
- Create roadmap

Expected output:

    Professional GitHub repository structure ready for data extraction

---

## Phase 2 – Historical Financial Data Extraction

Status:

    Pending

Objective:

Extract historical financial data from official public sources.

Target periods:

- 2022A
- 2023A
- 2024A
- 2025A

Main tasks:

- Review official annual reports
- Extract income statement figures
- Extract balance sheet figures
- Extract capital ratios
- Extract asset quality ratios
- Extract profitability ratios
- Record source document and page or section
- Update `data/extraction_tracker.csv`
- Update `data/historical_financials.csv`
- Update `data/banking_ratios.csv`
- Update `data/source_mapping.csv`

Expected output:

    Structured historical financial dataset with source traceability

---

## Phase 3 – Data Validation and Quality Review

Status:

    Pending

Objective:

Validate the financial data before using it in the model.

Main tasks:

- Run `data/validation_checks.py`
- Review missing values
- Review source mapping
- Check unit consistency
- Check period consistency
- Check reported vs calculated figures
- Review formula consistency
- Update `data/data_quality_report.md`
- Mark reviewed items as `Reviewed` or `Validated`

Expected output:

    Validated dataset ready for modeling

---

## Phase 4 – Excel Model Generation and Population

Status:

    Pending

Objective:

Generate and populate the Excel model templates.

Main tasks:

- Run banking model generator
- Run sensitivity analysis generator
- Populate historical financials
- Populate banking ratios
- Link assumptions to forecast outputs
- Add checks and review formulas
- Save model outputs

Expected output:

    Completed educational banking model and sensitivity analysis workbook

---

## Phase 5 – Forecast and Scenario Analysis

Status:

    Pending

Objective:

Create simplified forecast scenarios based on public information and documented assumptions.

Main tasks:

- Define conservative scenario
- Define base scenario
- Define optimistic scenario
- Forecast income statement items
- Forecast balance sheet items
- Forecast profitability ratios
- Forecast efficiency ratios
- Forecast capital assumptions
- Review forecast reasonableness

Expected output:

    Scenario-based forecast model for 2026E–2028E

---

## Phase 6 – Valuation and Sensitivity Analysis

Status:

    Pending

Objective:

Build an educational valuation summary using banking-relevant multiples and sensitivity analysis.

Main tasks:

- Select valuation date
- Collect market data
- Complete market data template
- Review peer group
- Complete peer comparison template
- Calculate P/B multiple
- Calculate P/E multiple
- Calculate dividend yield, if applicable
- Build sensitivity tables
- Review output ranges

Expected output:

    Educational valuation framework with sensitivity analysis

---

## Phase 7 – Investment Memo Completion

Status:

    Pending

Objective:

Prepare a professional investment-style memo based on the completed model.

Main tasks:

- Summarise business overview
- Summarise historical performance
- Summarise profitability trends
- Summarise asset quality
- Summarise capital position
- Summarise valuation output
- Summarise key risks
- Include data quality limitations
- Avoid investment advice language

Expected output:

    Professional investment-style memo suitable for portfolio presentation

---

## Phase 8 – Final Review and Portfolio Publication

Status:

    Pending

Objective:

Perform final quality review before presenting the project publicly.

Main tasks:

- Review all documentation
- Check all source references
- Run validation script
- Review Excel model outputs
- Review investment memo language
- Confirm no personal data is included
- Confirm no confidential information is included
- Confirm no investment recommendation is made
- Update project status
- Update changelog

Expected output:

    Final portfolio-ready project

---

## Future Enhancements

Potential future improvements:

- Add automated tests for CSV file structure
- Add GitHub Actions workflow for validation checks
- Add visual charts for key ratios
- Add a Streamlit dashboard for educational model review
- Add peer comparison visualisation
- Add scenario dashboard
- Add data quality scorecard
- Add AI-assisted research memo review checklist

These enhancements should remain educational and should not turn the project into an investment recommendation tool.

---

## Guiding Principles

The project should always follow these principles:

- use only public information;
- avoid personal data;
- avoid internal or confidential information;
- document sources clearly;
- separate reported and calculated figures;
- explain assumptions;
- validate data before analysis;
- use neutral language;
- avoid investment recommendations;
- keep the project suitable for professional portfolio presentation.

---

## Disclaimer

This roadmap is part of an educational financial modeling case study.

The project does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.

All analysis must be based only on publicly available information.
