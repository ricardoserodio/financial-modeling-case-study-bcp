# SQL Layer

This folder contains the SQL layer for the **Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank** project.

The purpose of this layer is to demonstrate how public banking data can be structured, queried and transformed into analytical insights.

This project is for educational and portfolio purposes only.

It does not constitute investment advice.

---

## Purpose of the SQL Layer

The SQL layer supports the banking analytics and financial data quality parts of the project.

It helps transform public financial information into structured tables that can be queried for:

- profitability trends;
- efficiency analysis;
- asset quality analysis;
- capital analysis;
- actual vs forecast comparison;
- scenario analysis;
- source validation;
- missing data checks;
- Power BI dashboard preparation.

The objective is not to create a complex production database.

The objective is to demonstrate clear financial data structuring and analytical querying.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `schema.sql` | Defines the database tables used in the project |
| `queries.sql` | Contains example analytical SQL queries for banking analytics and data quality |

---

## Planned Tables

The SQL schema includes the following tables:

| Table | Purpose |
|---|---|
| `financial_statements` | Stores historical and forecast financial statement data |
| `banking_ratios` | Stores key banking ratios by period |
| `source_mapping` | Maps each data point to its public source |
| `data_quality_checks` | Stores data quality review results |
| `forecast_assumptions` | Stores assumptions used in forecasts |
| `scenario_analysis` | Stores base, downside and upside scenario outputs |
| `market_data` | Stores market data used for valuation |
| `peer_comparison` | Stores peer comparison metrics |

---

## Main Model Periods

The main periods used in the project are:

    2022A | 2023A | 2024A | 2025A | 2026E | 2027E

Where:

| Period | Meaning |
|---|---|
| `2022A` | Published historical data |
| `2023A` | Published historical data |
| `2024A` | Published historical data |
| `2025A` | Published historical data |
| `2026E` | Forecast / estimate |
| `2027E` | Forecast / estimate |

The SQL layer must clearly separate historical actual data from forecast estimates.

---

## Why SQL Matters in This Project

SQL is useful because it allows financial data to be structured and analysed in a repeatable way.

Instead of manually reviewing CSV files one by one, SQL can answer analytical questions such as:

- How did net income evolve over time?
- How did the cost-to-income ratio change?
- Which ratios are still pending validation?
- Which fields have missing values?
- Which values are actual historical figures?
- Which values are forecast estimates?
- What data should be used in the Power BI dashboard?

This demonstrates practical data analysis skills relevant to banking analytics, reporting, financial data quality and business operations roles.

---

## Example Analytical Questions

The SQL queries are designed to support questions such as:

### Profitability

- How did net income evolve between 2022A and 2025A?
- How did net interest income contribute to operating income?
- How did ROE and ROA evolve?

### Efficiency

- Did the cost-to-income ratio improve or deteriorate?
- Are operating costs growing faster than income?

### Asset Quality

- How did the NPL ratio evolve?
- How did cost of risk change over time?
- Are impairments increasing or decreasing?

### Capital

- How did the CET1 ratio evolve?
- Is the capital position stable across periods?

### Forecast and Scenarios

- How do 2026E and 2027E compare with historical actuals?
- What changes under the downside scenario?
- Which assumptions drive the forecast?

### Data Quality

- Which values are missing?
- Which data points are still pending validation?
- Which metrics are reported and which are calculated?
- Are source references complete?

---

## Relationship With Power BI

The SQL layer supports the Power BI dashboard.

SQL queries can be used to prepare datasets for dashboard pages such as:

- Executive Summary;
- Profitability;
- Efficiency;
- Asset Quality;
- Capital & Liquidity;
- Forecast & Scenarios;
- Data Quality.

For example:

A SQL query that extracts ROE, ROA and net income by year can feed the Profitability page.

A SQL query that groups validation status can feed the Data Quality page.

A SQL query that separates actual and forecast periods can feed the Forecast & Scenarios page.

---

## Relationship With Financial Data Quality

The SQL layer is also useful for data quality control.

It helps identify:

- missing values;
- pending validation items;
- incomplete source references;
- inconsistent period labels;
- actual vs forecast classification;
- reported vs calculated figures;
- unusual or incomplete data points.

This supports the project's financial data quality and source validation objectives.

---

## Suggested Workflow

The suggested SQL workflow is:

1. Extract data from public sources.
2. Save structured data in CSV files.
3. Map each value to its public source.
4. Load or replicate the data into SQL tables.
5. Run analytical queries.
6. Run data quality queries.
7. Use query outputs to support Power BI visuals.
8. Document key findings in the reports folder.

---

## Professional Relevance

This SQL layer supports the project’s relevance for roles such as:

- Banking Analyst;
- Banking Analytics Analyst;
- Financial Data Analyst;
- Financial Data Quality Analyst;
- Data Validation Analyst;
- Reporting Analyst – Banking;
- Business Operations Analyst;
- Program Operations Analyst;
- Financial Operations Analyst;
- Fintech / Product Operations Analyst.

It demonstrates the ability to structure financial data, query it, validate it and prepare it for reporting.

---

## Disclaimer

This SQL layer is part of an educational portfolio project.

It uses only publicly available information.

It does not contain personal data, client data, internal banking information or confidential information.

The analysis does not constitute investment advice or a recommendation to buy, sell or hold any financial instrument.