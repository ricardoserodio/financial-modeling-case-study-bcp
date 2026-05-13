# Power BI Measures Plan ? Millennium bcp Case Study

## Purpose

This document defines the planned Power BI measures, visuals and dashboard pages for the Millennium bcp banking analytics case study.

The goal is to convert the structured CSV dataset into a clear visual dashboard covering:

- financial performance;
- profitability;
- efficiency;
- asset quality;
- liquidity and funding;
- capital;
- data quality;
- source validation.

The first Power BI version should stay simple, clean and recruiter-friendly.

---

## Dataset Tables

Recommended Power BI table names:

| Table | Source |
|---|---|
| FinancialData | data/financial_data.csv |
| BankingRatios | data/banking_ratios.csv |
| SourceMapping | data/source_mapping.csv |
| ExtractionTracker | data/extraction_tracker.csv |

Important note:

`BankingRatios` should be unpivoted in Power Query so that the period columns become rows.

Target format:

| ratio | category | formula | period | value | unit | source_status | notes |
|---|---|---|---|---:|---|---|---|

---

## Dashboard Page 1 ? Executive Overview

### Purpose

Give a high-level view of the bank's historical performance from 2022A to 2025A.

### Recommended Cards

| Card | Table | Field / Filter |
|---|---|---|
| Latest Net Income | FinancialData | metric = Net income |
| Latest Net Interest Income | FinancialData | metric = Net interest income |
| Latest Operating Income | FinancialData | metric = Operating income |
| Latest Total Assets | FinancialData | metric = Total assets |
| Latest Customer Loans | FinancialData | metric = Customer loans |
| Latest Customer Deposits / Funds | FinancialData | metric = Customer deposits |
| Latest Equity | FinancialData | metric = Equity |

### Recommended Charts

| Visual | Table | Axis | Values | Filter |
|---|---|---|---|---|
| Net income trend | FinancialData | period | value | metric = Net income |
| Net interest income trend | FinancialData | period | value | metric = Net interest income |
| Operating income vs operating costs | FinancialData | period | value | metric = Operating income / Operating costs |
| Customer loans vs customer deposits/funds | FinancialData | period | value | metric = Customer loans / Customer deposits |

### Suggested Interpretation

The Executive Overview should show the improvement from 2022A to 2025A, especially the increase in net income, stronger revenue base and balance sheet development.

---

## Dashboard Page 2 ? Profitability

### Purpose

Analyse profitability and earnings indicators.

### Main Metrics

| Metric | Table | Field |
|---|---|---|
| ROE | BankingRatios | ratio = ROE |
| ROA | BankingRatios | ratio = ROA |
| Net interest margin | BankingRatios | ratio = Net interest margin |
| EPS | BankingRatios | ratio = EPS |
| Net income | FinancialData | metric = Net income |

### Recommended Visuals

| Visual | Axis | Values |
|---|---|---|
| ROE trend | period | value |
| ROA trend | period | value |
| Net interest margin trend | period | value |
| EPS trend | period | value |
| Net income trend | period | value |

### Analytical Notes

- ROE increased significantly after 2022A.
- Net income improved strongly from 2022A to 2025A.
- Net interest margin rose in 2023A and then moderated slightly in 2024A and 2025A.
- Profitability should be interpreted together with capital, asset quality and interest rate environment.

---

## Dashboard Page 3 ? Efficiency

### Purpose

Analyse cost discipline and operating efficiency.

### Main Metrics

| Metric | Table | Field |
|---|---|---|
| Operating income | FinancialData | metric = Operating income |
| Operating costs | FinancialData | metric = Operating costs |
| Cost-to-income ratio | BankingRatios | ratio = Cost-to-income ratio |
| Cost-to-income ratio excluding specific items | BankingRatios | ratio = Cost-to-income ratio excluding specific items |

### Recommended Visuals

| Visual | Axis | Values |
|---|---|---|
| Operating income vs operating costs | period | value |
| Cost-to-income trend | period | value |
| Cost-to-income adjusted trend | period | value |

### Analytical Notes

- Cost-to-income improved sharply in 2023A.
- 2024A and 2025A returned closer to 2022A efficiency levels.
- Adjusted efficiency should be reviewed carefully because specific item definitions may vary across periods.

---

## Dashboard Page 4 ? Asset Quality

### Purpose

Analyse credit quality and impairment-related indicators.

### Main Metrics

| Metric | Table | Field |
|---|---|---|
| Cost of risk | BankingRatios | ratio = Cost of risk |
| NPE ratio | BankingRatios | ratio = NPE ratio |
| NPE coverage ratio | BankingRatios | ratio = NPE coverage ratio |
| Restructured loans ratio | BankingRatios | ratio = Restructured loans ratio |
| Impairments and provisions | FinancialData | metric = Impairments and provisions |

### Recommended Visuals

| Visual | Axis | Values |
|---|---|---|
| NPE ratio trend | period | value |
| NPE coverage ratio trend | period | value |
| Cost of risk trend | period | value |
| Restructured loans ratio trend | period | value |
| Impairments and provisions trend | period | value |

### Analytical Notes

- NPE ratio declined from 2022A to 2025A.
- NPE coverage increased over the same period.
- Cost of risk improved from 2022A to 2024A, with a small increase in 2025A.
- 2022A impairments and provisions remain a review item because the figure combines multiple components.

---

## Dashboard Page 5 ? Liquidity and Funding

### Purpose

Analyse funding structure, customer resources and liquidity resilience.

### Main Metrics

| Metric | Table | Field |
|---|---|---|
| Customer loans | FinancialData | metric = Customer loans |
| Customer deposits / customer funds | FinancialData | metric = Customer deposits |
| Loan-to-deposit ratio | BankingRatios | ratio = Loan-to-deposit ratio |
| Loan-to-balance-sheet-customer-resources ratio | BankingRatios | ratio = Loan-to-balance-sheet-customer-resources ratio |
| LCR | BankingRatios | ratio = LCR |
| NSFR | BankingRatios | ratio = NSFR |

### Recommended Visuals

| Visual | Axis | Values |
|---|---|---|
| Customer loans vs customer deposits/funds | period | value |
| Loan-to-deposit trend | period | value |
| LCR trend | period | value |
| NSFR trend | period | value |

### Analytical Notes

- Loan-to-deposit ratio declined after 2022A.
- LCR and NSFR improved materially from 2022A to 2025A.
- Customer deposits vs customer funds terminology must remain visible as a data quality note.

---

## Dashboard Page 6 ? Capital

### Purpose

Analyse regulatory capital strength.

### Main Metrics

| Metric | Table | Field |
|---|---|---|
| CET1 phased-in ratio | BankingRatios | ratio = CET1 phased-in ratio |
| CET1 fully implemented ratio | BankingRatios | ratio = CET1 fully implemented ratio |
| Total capital fully implemented ratio | BankingRatios | ratio = Total capital fully implemented ratio |
| Equity | FinancialData | metric = Equity |

### Recommended Visuals

| Visual | Axis | Values |
|---|---|---|
| CET1 phased-in trend | period | value |
| CET1 fully implemented trend | period | value |
| Total capital fully implemented trend | period | value |
| Equity trend | period | value |

### Analytical Notes

- CET1 fully implemented improved from 2022A to 2025A.
- Total capital ratio also strengthened over the period.
- Phased-in and fully implemented ratios should not be mixed in the same interpretation without clear labels.

---

## Dashboard Page 7 ? Data Quality

### Purpose

Show transparency around source validation, review status and pending items.

### Recommended Visuals

| Visual | Table | Field |
|---|---|---|
| Validation status count | SourceMapping | validation_status |
| Review status by period | ExtractionTracker | validation_status / period |
| Reported vs calculated split | SourceMapping | reported_or_calculated |
| Source document table | SourceMapping | source_document |
| Pending items table | SourceMapping / BankingRatios | validation_status / source_status |
| Review notes table | ExtractionTracker | review_notes |

### Key Items to Highlight

| Item | Status |
|---|---|
| 2022A impairments and provisions | Needs Review |
| Customer deposits vs customer funds | Needs Review |
| 2022A book value per share | Pending |
| Valuation ratios | Pending |
| Peer comparison | Pending |
| Market data | Pending |

### Analytical Notes

The Data Quality page is important because it shows that the project is not only a dashboard, but also a controlled financial data workflow.

This strengthens the project for banking analytics, financial data quality, reporting and AI finance evaluation positioning.

---

## Suggested Simple Measures

The first Power BI version can use mostly direct fields and filters.

Optional DAX measures can be added later.

### Latest Value

Purpose:

Show the latest available value for a selected metric or ratio.

Conceptual DAX:

Latest Value = value for the latest selected period.

### Period Change

Purpose:

Show the absolute change between periods.

Conceptual DAX:

Period Change = Current Period Value - Previous Period Value.

### Percentage Change

Purpose:

Show relative growth or decline.

Conceptual DAX:

Percentage Change = Period Change / Previous Period Value.

### Reviewed Count

Purpose:

Count items marked as Reviewed.

Conceptual DAX:

Reviewed Count = count rows where validation_status = Reviewed.

### Needs Review Count

Purpose:

Count items marked as Needs Review.

Conceptual DAX:

Needs Review Count = count rows where validation_status = Needs Review.

### Pending Count

Purpose:

Count items marked as Pending.

Conceptual DAX:

Pending Count = count rows where validation_status = Pending.

---

## First Dashboard MVP

The first dashboard should prioritise:

1. simple line charts;
2. clear cards;
3. period slicer;
4. category slicer;
5. data quality table;
6. minimal styling;
7. readable labels;
8. no unnecessary complexity.

The goal is not to create a complex corporate reporting system.

The goal is to show that public financial data was transformed into a structured, validated and visual banking analytics workflow.

---

## Recommended Build Order

1. Load `financial_data.csv`.
2. Load `banking_ratios.csv`.
3. Unpivot `banking_ratios.csv`.
4. Load `source_mapping.csv`.
5. Load `extraction_tracker.csv`.
6. Create Executive Overview page.
7. Create Banking Ratios page.
8. Create Data Quality page.
9. Add additional pages only after the first three pages are clean.
10. Document screenshots after the dashboard is stable.

---

## Refresh Rule

Before refreshing Power BI, run:

`python data/validation_checks.py`

Current acceptable warnings:

- `market_data_template.csv`: missing `category` values.
- `peer_comparison_template.csv`: missing `business_type` values.

If new validation issues appear, fix the dataset before refreshing the dashboard.

---

## Portfolio Positioning

This Power BI dashboard should support the following professional positioning:

- banking analytics;
- financial data quality;
- source validation;
- public financial data analysis;
- reporting analyst skills;
- business intelligence readiness;
- AI-assisted finance workflow with human review.

---

## Disclaimer

The Power BI dashboard is for educational and professional portfolio purposes only.

It does not provide investment advice, financial advice, valuation advice, a price target or a buy/sell/hold recommendation.

All figures should be independently verified before professional, academic or investment-related use.
