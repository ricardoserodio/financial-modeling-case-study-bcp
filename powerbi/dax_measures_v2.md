# Power BI DAX Measures v2

## Purpose

This document contains suggested DAX measures for the Power BI v2 dashboard of the Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank project.

The measures are intended to support KPI cards, trend visuals, forecast scenario visuals and data quality review pages.

## Important Note

Table names may need to be adjusted depending on the names imported into Power BI.

Recommended table names:

- FinancialData
- BankingRatios
- ForecastFinancials
- ForecastRatios
- ScenarioAnalysis

If Power BI imported the CSV tables with different names, update the table names accordingly.

---

## 1. Historical Financial KPI Measures

### Net Income 2025A

    Net Income 2025A =
    CALCULATE(
        SUM(FinancialData[value]),
        FinancialData[metric] = "Net income",
        FinancialData[period] = "2025A"
    )

### Operating Income 2025A

    Operating Income 2025A =
    CALCULATE(
        SUM(FinancialData[value]),
        FinancialData[metric] = "Operating income",
        FinancialData[period] = "2025A"
    )

### Operating Costs 2025A

    Operating Costs 2025A =
    CALCULATE(
        SUM(FinancialData[value]),
        FinancialData[metric] = "Operating costs",
        FinancialData[period] = "2025A"
    )

### Customer Loans 2025A

    Customer Loans 2025A =
    CALCULATE(
        SUM(FinancialData[value]),
        FinancialData[metric] = "Customer loans",
        FinancialData[period] = "2025A"
    )

### Customer Deposits 2025A

    Customer Deposits 2025A =
    CALCULATE(
        SUM(FinancialData[value]),
        FinancialData[metric] = "Customer deposits",
        FinancialData[period] = "2025A"
    )

### Total Assets 2025A

    Total Assets 2025A =
    CALCULATE(
        SUM(FinancialData[value]),
        FinancialData[metric] = "Total assets",
        FinancialData[period] = "2025A"
    )

### Equity 2025A

    Equity 2025A =
    CALCULATE(
        SUM(FinancialData[value]),
        FinancialData[metric] = "Equity",
        FinancialData[period] = "2025A"
    )

---

## 2. Historical Ratio KPI Measures

### ROE 2025A

    ROE 2025A =
    CALCULATE(
        MAX(BankingRatios[2025A]),
        BankingRatios[ratio] = "ROE"
    )

### ROA 2025A

    ROA 2025A =
    CALCULATE(
        MAX(BankingRatios[2025A]),
        BankingRatios[ratio] = "ROA"
    )

### Cost-to-Income 2025A

    Cost-to-Income 2025A =
    CALCULATE(
        MAX(BankingRatios[2025A]),
        BankingRatios[ratio] = "Cost-to-income ratio"
    )

### Cost of Risk 2025A

    Cost of Risk 2025A =
    CALCULATE(
        MAX(BankingRatios[2025A]),
        BankingRatios[ratio] = "Cost of risk"
    )

### Loan-to-Deposit Ratio 2025A

    Loan-to-Deposit Ratio 2025A =
    CALCULATE(
        MAX(BankingRatios[2025A]),
        BankingRatios[ratio] = "Loan-to-deposit ratio"
    )

### CET1 Fully Implemented 2025A

    CET1 Fully Implemented 2025A =
    CALCULATE(
        MAX(BankingRatios[2025A]),
        BankingRatios[ratio] = "CET1 fully implemented ratio"
    )

### LCR 2025A

    LCR 2025A =
    CALCULATE(
        MAX(BankingRatios[2025A]),
        BankingRatios[ratio] = "LCR"
    )

### NSFR 2025A

    NSFR 2025A =
    CALCULATE(
        MAX(BankingRatios[2025A]),
        BankingRatios[ratio] = "NSFR"
    )

---

## 3. Forecast KPI Measures

### Forecast Net Income

    Forecast Net Income =
    CALCULATE(
        SUM(ForecastFinancials[value]),
        ForecastFinancials[line_item] = "Net income"
    )

### Forecast Operating Income

    Forecast Operating Income =
    CALCULATE(
        SUM(ForecastFinancials[value]),
        ForecastFinancials[line_item] = "Operating income"
    )

### Forecast Operating Costs

    Forecast Operating Costs =
    CALCULATE(
        SUM(ForecastFinancials[value]),
        ForecastFinancials[line_item] = "Operating costs"
    )

### Forecast Customer Loans

    Forecast Customer Loans =
    CALCULATE(
        SUM(ForecastFinancials[value]),
        ForecastFinancials[line_item] = "Customer loans"
    )

### Forecast Customer Deposits

    Forecast Customer Deposits =
    CALCULATE(
        SUM(ForecastFinancials[value]),
        ForecastFinancials[line_item] = "Customer deposits"
    )

### Forecast ROE

    Forecast ROE =
    CALCULATE(
        MAX(ForecastRatios[value]),
        ForecastRatios[ratio] = "ROE"
    )

### Forecast ROA

    Forecast ROA =
    CALCULATE(
        MAX(ForecastRatios[value]),
        ForecastRatios[ratio] = "ROA"
    )

### Forecast Cost-to-Income

    Forecast Cost-to-Income =
    CALCULATE(
        MAX(ForecastRatios[value]),
        ForecastRatios[ratio] = "Cost-to-income ratio"
    )

### Forecast Cost of Risk

    Forecast Cost of Risk =
    CALCULATE(
        MAX(ForecastRatios[value]),
        ForecastRatios[ratio] = "Cost of risk"
    )

### Forecast CET1 Ratio

    Forecast CET1 Ratio =
    CALCULATE(
        MAX(ForecastRatios[value]),
        ForecastRatios[ratio] = "CET1 ratio assumption"
    )

---

## 4. Scenario Analysis Measures

### Scenario Value

    Scenario Value =
    SUM(ScenarioAnalysis[value])

### Base Case Value

    Base Case Value =
    SUM(ScenarioAnalysis[base_case_value])

### Variance vs Base

    Variance vs Base =
    SUM(ScenarioAnalysis[variance_vs_base])

### Variance vs Base %

    Variance vs Base % =
    AVERAGE(ScenarioAnalysis[variance_vs_base_percent])

---

## 5. Data Quality Measures

### Forecast Items To Review

    Forecast Items To Review =
    CALCULATE(
        COUNTROWS(ForecastFinancials),
        ForecastFinancials[validation_status] <> "Reviewed"
    )
    +
    CALCULATE(
        COUNTROWS(ForecastRatios),
        ForecastRatios[validation_status] <> "Reviewed"
    )
    +
    CALCULATE(
        COUNTROWS(ScenarioAnalysis),
        ScenarioAnalysis[validation_status] <> "Reviewed"
    )

### Forecast Financials To Review

    Forecast Financials To Review =
    CALCULATE(
        COUNTROWS(ForecastFinancials),
        ForecastFinancials[validation_status] <> "Reviewed"
    )

### Forecast Ratios To Review

    Forecast Ratios To Review =
    CALCULATE(
        COUNTROWS(ForecastRatios),
        ForecastRatios[validation_status] <> "Reviewed"
    )

### Scenario Analysis To Review

    Scenario Analysis To Review =
    CALCULATE(
        COUNTROWS(ScenarioAnalysis),
        ScenarioAnalysis[validation_status] <> "Reviewed"
    )

### Historical Reviewed Items

    Historical Reviewed Items =
    CALCULATE(
        COUNTROWS(FinancialData),
        FinancialData[validation_status] = "Reviewed"
    )

### Historical Pending Items

    Historical Pending Items =
    CALCULATE(
        COUNTROWS(FinancialData),
        FinancialData[validation_status] <> "Reviewed"
    )

---

## 6. Suggested Formatting

Use the following formatting:

- EUR million metrics: decimal number, 1 decimal place
- Percentage ratios: decimal number with % suffix, unless model format already handles percentage
- Cost of risk: decimal number with bps suffix
- Row counts: whole number

---

## 7. Recommended KPI Cards for Executive Overview

Use these measures:

- Net Income 2025A
- ROE 2025A
- ROA 2025A
- Cost-to-Income 2025A
- Cost of Risk 2025A
- CET1 Fully Implemented 2025A
- LCR 2025A
- NSFR 2025A

---

## 8. Recommended KPI Cards for Forecast & Scenarios

Use these measures with slicers for Scenario and Period:

- Forecast Net Income
- Forecast ROE
- Forecast Cost-to-Income
- Forecast Cost of Risk
- Forecast CET1 Ratio
- Variance vs Base
- Variance vs Base %

---

## 9. Required Power BI Disclaimer Text

Add this text to the Forecast & Scenarios page:

Forecast figures are educational scenario-based estimates. They are not official projections, investment advice or financial recommendations.

Add this text to the Executive Overview page footer:

Educational portfolio project. Public-source data only. Not investment advice.
