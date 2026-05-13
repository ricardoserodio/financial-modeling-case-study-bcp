# Banking Analytics Report

This report summarises the planned banking analytics analysis for the **Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank** project.

The project uses only publicly available information and is designed for educational, portfolio and professional development purposes.

It does not constitute investment advice.

---

## 1. Report Purpose

The purpose of this report is to transform structured financial data into a clear banking analytics narrative.

The report is designed to explain:

- how the bank performed historically;
- which KPIs are most relevant;
- how profitability evolved;
- how efficiency evolved;
- how asset quality evolved;
- how capital and liquidity indicators evolved;
- how forecast assumptions affect future scenarios;
- which data quality limitations should be considered.

This report should be read together with the project datasets, SQL layer, Power BI dashboard structure and source validation files.

---

## 2. Scope of Analysis

The main model period is:

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

The report clearly separates:

- historical actual data;
- calculated ratios;
- forecast assumptions;
- scenario outputs.

---

## 3. Executive Summary

This section will summarise the most important findings once the dataset is completed.

Planned focus areas:

- profitability trend;
- net interest income trend;
- fees and commissions trend;
- cost-to-income evolution;
- ROE and ROA evolution;
- asset quality indicators;
- CET1 ratio and capital position;
- customer loans and customer deposits;
- forecast and scenario highlights;
- data quality status.

Current status:

    Pending data extraction and validation

Example neutral wording:

    Based on the completed public-source dataset, this section will summarise the main banking analytics trends observed across profitability, efficiency, asset quality and capital indicators. Any interpretation will be limited to publicly available data and should be read together with the data quality review.

---

## 4. Profitability Analysis

### Metrics Reviewed

This section will analyse:

- net income;
- net interest income;
- fees and commissions;
- operating income;
- ROE;
- ROA.

### Why These Metrics Matter

Profitability is central in banking analysis because it shows whether the bank is able to generate earnings from its balance sheet, customer franchise and operating model.

Net interest income is especially important for banks because it reflects the difference between income generated from interest-earning assets and the cost of funding.

Fees and commissions are also important because they show non-interest income generation and revenue diversification.

ROE measures profitability relative to shareholder equity.

ROA measures profitability relative to total assets.

### Analytical Questions

- Did net income improve or deteriorate across the analysed period?
- Was profitability driven mainly by net interest income, fees or other operating income?
- Did ROE improve?
- Was ROA consistent with the net income trend?
- Were profitability improvements supported by recurring income?

### Commentary Placeholder

    Profitability commentary will be completed after historical data extraction and validation.

---

## 5. Efficiency Analysis

### Metrics Reviewed

This section will analyse:

- operating income;
- operating costs;
- cost-to-income ratio;
- operating cost growth;
- operating income growth.

### Why These Metrics Matter

Efficiency is important because banks operate with large cost bases, including branches, staff, technology, compliance, risk management and operational infrastructure.

The cost-to-income ratio shows how much cost is required to generate income.

A lower cost-to-income ratio usually indicates better operating efficiency, but interpretation should consider context such as inflation, restructuring costs, investment in technology, business growth and one-off items.

### Analytical Questions

- Did operating costs increase or decrease?
- Did income grow faster than costs?
- Did the cost-to-income ratio improve?
- Were efficiency gains consistent or temporary?
- Were there any one-off effects that may distort interpretation?

### Commentary Placeholder

    Efficiency commentary will be completed after historical data extraction and validation.

---

## 6. Asset Quality Analysis

### Metrics Reviewed

This section will analyse:

- NPL ratio;
- NPE ratio, where available;
- cost of risk;
- impairments and provisions;
- coverage ratio, where available;
- customer loans.

### Why These Metrics Matter

Asset quality is one of the most important areas of banking analysis.

Banks lend money and therefore face credit risk.

If borrowers experience financial difficulty, non-performing loans and impairments may increase, affecting profitability and capital.

NPL ratio helps assess the proportion of problematic loans.

Cost of risk shows the cost of credit losses relative to the loan book.

Impairments and provisions indicate expected or recognised credit losses.

### Analytical Questions

- Did the NPL ratio improve or deteriorate?
- Did cost of risk increase or decrease?
- Were impairments aligned with the loan book evolution?
- Was loan growth accompanied by stable asset quality?
- Were asset quality trends consistent across periods?

### Commentary Placeholder

    Asset quality commentary will be completed after historical data extraction and validation.

---

## 7. Capital and Liquidity Analysis

### Metrics Reviewed

This section will analyse:

- CET1 ratio;
- total capital ratio, where available;
- customer loans;
- customer deposits;
- loan-to-deposit ratio;
- equity;
- total assets.

### Why These Metrics Matter

Capital is critical in banking because it represents the bank's ability to absorb losses and meet regulatory requirements.

CET1 is a key measure of high-quality regulatory capital.

Customer deposits are important because they represent a stable funding source.

The loan-to-deposit ratio helps assess the relationship between lending activity and customer funding.

### Analytical Questions

- Was the CET1 ratio stable across the analysed period?
- Did customer loans increase or decrease?
- Did customer deposits increase or decrease?
- Was lending growth supported by deposit growth?
- Did the loan-to-deposit ratio remain within a reasonable range?
- Was the capital position resilient based on public data?

### Commentary Placeholder

    Capital and liquidity commentary will be completed after historical data extraction and validation.

---

## 8. Forecast and Scenario Analysis

### Forecast Period

The forecast period is:

    2026E | 2027E

### Scenario Structure

The project may include the following scenarios:

| Scenario | Description |
|---|---|
| Base | Central educational case |
| Downside | More prudent case with weaker profitability or higher risk |
| Upside | More optimistic case, if justified by assumptions |

### Metrics Reviewed

This section may include forecast analysis of:

- net income;
- net interest income;
- fees and commissions;
- operating costs;
- cost-to-income ratio;
- ROE;
- ROA;
- cost of risk;
- CET1 ratio;
- customer loans;
- customer deposits.

### Interpretation Principles

Forecast commentary should be cautious and clearly labelled as illustrative.

The forecast should not be presented as a prediction.

Scenario outputs should be used to understand sensitivity to assumptions, not to make investment recommendations.

### Commentary Placeholder

    Forecast and scenario commentary will be completed after forecast assumptions are defined and reviewed.

---

## 9. SQL Analytics Summary

The SQL layer supports this report by allowing structured queries over the project datasets.

SQL can help answer questions such as:

- how did profitability metrics evolve by period?
- how did banking ratios change over time?
- which data points are still pending validation?
- which values are actual and which are forecasts?
- which items have missing values?
- which KPIs should feed the Power BI dashboard?

This supports a repeatable analytical workflow rather than relying only on manual spreadsheet review.

---

## 10. Power BI Reporting Summary

The Power BI dashboard is planned as an executive-style banking analytics report.

Planned dashboard pages:

1. Executive Summary
2. Profitability
3. Efficiency
4. Asset Quality
5. Capital & Liquidity
6. Forecast & Scenarios
7. Data Quality

The dashboard should transform financial data into clear, visual and interpretable insights.

It should be suitable for a professional portfolio and understandable by both finance and non-technical stakeholders.

---

## 11. Financial Data Quality Summary

The project includes a data quality layer because public financial analysis depends on reliable and traceable data.

Data quality checks include:

- source validation;
- missing values;
- required fields;
- period consistency;
- unit consistency;
- duplicate records;
- reported vs calculated classification;
- actual vs forecast classification;
- unusual value detection;
- source coverage;
- human review status.

The analysis should not be finalised until the main data points have been reviewed.

---

## 12. Human-in-the-Loop Review

Before publishing final conclusions, the analysis should be reviewed manually.

The review should check:

- source traceability;
- unit consistency;
- formula accuracy;
- ratio interpretation;
- forecast assumptions;
- scenario logic;
- neutral language;
- data quality limitations;
- absence of investment advice;
- absence of personal, confidential or internal information.

This is especially important if AI-assisted drafting or analysis support is used during the project.

---

## 13. Professional Interpretation Guidelines

The report should use cautious and professional language.

Avoid:

- buy;
- sell;
- hold;
- target price;
- guaranteed return;
- undervalued;
- overvalued;
- investment opportunity;
- price prediction.

Preferred wording:

- historical trend;
- public-data analysis;
- simplified forecast;
- illustrative scenario;
- data quality limitation;
- further validation required;
- based on available public information;
- should be interpreted with caution.

---

## 14. Current Report Status

Current status:

    Draft structure created

Pending work:

- extract historical financial data;
- validate source mapping;
- complete financial datasets;
- calculate banking ratios;
- define forecast assumptions;
- complete scenario analysis;
- create SQL outputs;
- build Power BI dashboard;
- complete final commentary.

---

## 15. Disclaimer

This report is part of an educational portfolio project.

It uses only publicly available information.

It does not include personal data, client data, internal banking information or confidential information.

It does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.

All analysis, forecasts and scenarios are illustrative and should be interpreted with caution.