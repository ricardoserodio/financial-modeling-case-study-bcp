# Methodology

This document explains the methodology used in the **Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank** project.

The project combines financial modeling, banking analytics, SQL-based data structuring, Power BI dashboarding and financial data quality validation using only publicly available information.

This project is for educational and portfolio purposes only.

It does not constitute investment advice.

---

## 1. Project Purpose

The purpose of this project is to transform public financial information from Millennium bcp / Banco Comercial Português into a structured banking analytics and financial modeling case study.

The project is designed to demonstrate the ability to:

- read and interpret public banking reports;
- extract relevant financial data;
- structure financial information into datasets;
- validate public financial data;
- calculate and interpret banking KPIs;
- create simplified forecasts;
- build scenario analysis;
- prepare SQL queries for analytical reporting;
- design a Power BI executive dashboard;
- communicate insights in a prudent and professional way.

---

## 2. Strategic Project Scope

This project has five main layers:

1. Financial Modeling
2. Banking Analytics
3. SQL Data Layer
4. Power BI Dashboard
5. Financial Data Quality

The goal is not only to build a simplified bank model, but also to show how public financial data can be structured, validated, queried, visualised and explained.

---

## 3. Time Period Covered

The main model period is:

    2022A | 2023A | 2024A | 2025A | 2026E | 2027E

Where:

| Period | Meaning |
|---|---|
| 2022A | Published historical data |
| 2023A | Published historical data |
| 2024A | Published historical data |
| 2025A | Published historical data |
| 2026E | Forecast / estimate |
| 2027E | Forecast / estimate |

The project distinguishes clearly between:

- actual published historical figures;
- own calculations based on published figures;
- forecast assumptions;
- scenario outputs.

---

## 4. Source Selection

The project uses only public sources.

Preferred source hierarchy:

1. Millennium bcp annual reports
2. Millennium bcp investor presentations
3. Millennium bcp official investor relations materials
4. Euronext market data
5. CMVM public disclosures
6. Banco de Portugal public information
7. ECB and EBA public materials
8. Other reputable public financial sources, when needed

Official annual reports and investor presentations are preferred over secondary sources.

Secondary sources should only be used for market context or cross-checking when appropriate.

---

## 5. Data Extraction Process

The data extraction process follows these steps:

1. Open the relevant public source document.
2. Identify the financial metric or ratio.
3. Record the reporting period.
4. Record the value.
5. Record the unit, for example EUR million.
6. Record the source document.
7. Record the page, table or section where the figure appears.
8. Classify the figure as reported, calculated or estimated.
9. Enter the figure into the relevant CSV file.
10. Update the source mapping and extraction tracker.
11. Review the figure for consistency before using it in analysis.

The extraction tracker should be used before finalising the main datasets.

---

## 6. Main Financial Data Categories

The project focuses on banking metrics across the following categories:

### Profitability

- net interest income;
- fees and commissions;
- operating income;
- operating costs;
- impairments and provisions;
- net income;
- ROE;
- ROA.

### Efficiency

- cost-to-income ratio;
- operating cost growth;
- operating income growth.

### Asset Quality

- NPL ratio;
- NPE ratio, where applicable;
- cost of risk;
- impairments and provisions;
- coverage ratio, where available.

### Balance Sheet

- customer loans;
- customer deposits;
- total assets;
- equity;
- loan-to-deposit ratio.

### Capital

- CET1 ratio;
- total capital ratio;
- leverage ratio, where available;
- risk-weighted assets, where available.

### Market and Valuation

- share price;
- market capitalisation;
- number of shares;
- book value per share;
- earnings per share;
- price-to-book;
- price-to-earnings;
- dividend yield, if applicable.

---

## 7. Banking Analytics Approach

The banking analytics layer converts financial data into business insights.

The analysis should answer practical questions such as:

- Is profitability improving?
- Is net income growth sustainable?
- Is the bank more efficient over time?
- Are costs growing faster than income?
- Is asset quality improving or deteriorating?
- Is the capital position stable?
- Is loan growth supported by deposits?
- Which KPIs should appear in an executive dashboard?
- Which trends require further explanation?

The goal is to produce interpretation, not just calculations.

Commentary should remain neutral, factual and prudent.

---

## 8. Financial Modeling Approach

The financial model is simplified and educational.

The model should include:

- historical financial performance;
- key banking ratios;
- 2026E forecast;
- 2027E forecast;
- base scenario;
- prudent or downside scenario;
- optimistic or upside scenario, if appropriate;
- clear assumptions;
- sensitivity analysis.

Forecasts should be based on reasonable and documented assumptions.

The model should avoid excessive precision and should not present forecasts as predictions.

---

## 9. Forecast Assumption Principles

Forecast assumptions should be:

- simple;
- transparent;
- linked to historical trends;
- clearly documented;
- conservative where uncertainty is high;
- separated from historical actual data;
- reviewed before being used in conclusions.

Examples of forecast assumptions include:

- net interest income growth;
- fees and commissions growth;
- operating cost growth;
- cost-to-income ratio;
- cost of risk;
- loan growth;
- deposit growth;
- CET1 ratio assumption;
- ROE assumption.

Each assumption should explain the logic behind the estimate.

---

## 10. Scenario Analysis Approach

The scenario analysis should compare different possible outcomes.

Suggested scenarios:

| Scenario | Purpose |
|---|---|
| Base | Central educational case |
| Downside | More prudent case with weaker profitability or higher risk |
| Upside | More optimistic case with stronger performance |

Scenario analysis should not be used as an investment recommendation.

It is used to understand sensitivity to key assumptions.

---

## 11. SQL Methodology

The SQL layer structures the project data into analytical tables.

Planned tables include:

- financial_statements;
- banking_ratios;
- source_mapping;
- data_quality_checks;
- forecast_assumptions;
- scenario_analysis.

The SQL layer should support:

- historical trend queries;
- KPI extraction;
- year-on-year comparisons;
- actual vs forecast comparisons;
- source validation checks;
- data quality checks;
- Power BI data preparation.

The SQL layer is intentionally simple.

The objective is to demonstrate clear data structuring and analytical querying, not database engineering complexity.

---

## 12. Power BI Methodology

The Power BI dashboard should present the analysis in an executive and recruiter-friendly format.

Planned dashboard pages:

1. Executive Summary
2. Profitability
3. Efficiency
4. Asset Quality
5. Capital & Liquidity
6. Forecast & Scenarios
7. Data Quality

The dashboard should include:

- KPI cards;
- trend charts;
- ratio evolution;
- scenario comparison;
- data quality indicators;
- short explanatory comments;
- clear titles and labels.

The Power BI report should be designed as if it were being presented to non-technical stakeholders.

---

## 13. Financial Data Quality Methodology

The project includes a financial data quality layer to validate the reliability of the dataset.

Validation checks include:

- missing values;
- required fields;
- duplicate records;
- period consistency;
- unit consistency;
- source availability;
- source type classification;
- historical vs forecast classification;
- reported vs calculated classification;
- unusual value detection;
- basic KPI reconciliation;
- validation status review.

The validation process should be documented in the data quality report.

---

## 14. Human-in-the-Loop Review

Human review is required before publishing analysis or conclusions.

The human-in-the-loop review should check:

- whether figures are sourced correctly;
- whether formulas are reasonable;
- whether assumptions are documented;
- whether scenario outputs make sense;
- whether commentary is neutral;
- whether conclusions avoid investment advice;
- whether no confidential or personal information is included.

This review is especially important because the project may use AI-assisted drafting or analysis support.

---

## 15. Writing and Interpretation Principles

All commentary should be:

- factual;
- neutral;
- professional;
- cautious;
- source-based;
- clear for non-technical readers;
- free from investment recommendation language.

The project should avoid phrases such as:

- buy;
- sell;
- hold;
- target price;
- undervalued;
- overvalued;
- guaranteed upside;
- expected return.

Preferred language includes:

- illustrative scenario;
- public-data analysis;
- educational estimate;
- simplified assumption;
- historical trend;
- potential sensitivity;
- data quality limitation;
- further review required.

---

## 16. Limitations

This project has important limitations:

- it is educational and simplified;
- it is based only on public information;
- it does not include internal bank data;
- it does not include client or personal data;
- forecasts are illustrative;
- valuation outputs are not recommendations;
- public reporting formats may change over time;
- some metrics may not be directly comparable across sources;
- Power BI visuals are intended for portfolio demonstration.

---

## 17. Professional Relevance

This methodology supports the project’s relevance for roles such as:

- Financial Research Analyst;
- Banking Analyst;
- Banking Analytics Analyst;
- Financial Data Analyst;
- Financial Data Quality Analyst;
- Data Validation Analyst;
- Reporting Analyst – Banking;
- Investment Support;
- Wealth Management Support;
- Business Operations;
- Program Operations;
- Risk Operations;
- Financial Operations;
- Fintech / Product Operations.

The project demonstrates the ability to combine banking knowledge, data structuring, reporting, validation and analytical communication.

---

## 18. Disclaimer

This project is for educational and portfolio purposes only.

It does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.

All analysis is based only on publicly available information.

No personal data, client data, internal banking information or confidential information is used.