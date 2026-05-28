# Power BI Dashboard v2 Improvement Plan

## Purpose

This document defines the planned improvements for the Power BI dashboard used in the Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank project.

The goal is to improve the dashboard presentation, add stronger KPI cards, integrate forecast and scenario analysis outputs, and reinforce the data quality / human review narrative.

## Recommended Output File

Recommended Power BI output:

`powerbi/millennium_bcp_banking_dashboard_v2.pbix`

The v1 file should be preserved as the clean first version.

## Dashboard Pages

Recommended final dashboard pages:

1. Executive Overview
2. Profitability
3. Efficiency
4. Asset Quality
5. Liquidity & Funding
6. Capital
7. Forecast & Scenarios
8. Data Quality

## Page 1 – Executive Overview

### Objective

Provide a clean high-level summary of the bank's historical performance and key 2025A indicators.

### Recommended KPI Cards

- Net Income 2025A
- ROE 2025A
- ROA 2025A
- Cost-to-Income Ratio 2025A
- Cost of Risk 2025A
- CET1 Fully Implemented Ratio 2025A
- LCR 2025A
- NSFR 2025A

### Recommended Visuals

- Operating income trend
- Net income trend
- Key ratio snapshot
- Data quality status summary

### Suggested Notes

Add a small footer note:

`Educational portfolio project. Public-source data only. Forecast outputs are scenario-based estimates and not investment advice.`

## Page 2 – Profitability

### Recommended KPIs

- Net Interest Income
- Operating Income
- Net Income
- ROE
- ROA
- Net Interest Margin

### Recommended Visuals

- Net interest income by period
- Operating income by period
- Net income by period
- ROE / ROA trend
- Net interest margin trend

## Page 3 – Efficiency

### Recommended KPIs

- Operating Costs
- Cost-to-Income Ratio
- Cost-to-Income Excluding Specific Items

### Recommended Visuals

- Operating costs by period
- Cost-to-income ratio trend
- Operating income vs operating costs

## Page 4 – Asset Quality

### Recommended KPIs

- Cost of Risk
- NPE Ratio
- NPE Coverage Ratio
- Restructured Loans Ratio
- Impairments and Provisions

### Recommended Visuals

- Cost of risk trend
- NPE ratio trend
- NPE coverage ratio trend
- Impairments and provisions by period

## Page 5 – Liquidity & Funding

### Recommended KPIs

- Customer Loans
- Customer Deposits
- Loan-to-Deposit Ratio
- LCR
- NSFR

### Recommended Visuals

- Customer loans vs customer deposits
- Loan-to-deposit ratio trend
- LCR and NSFR trend

## Page 6 – Capital

### Recommended KPIs

- CET1 Fully Implemented Ratio
- CET1 Phased-In Ratio
- Total Capital Fully Implemented Ratio
- Equity
- Book Value per Share

### Recommended Visuals

- CET1 ratio trend
- Total capital ratio trend
- Equity trend
- Book value per share trend

## Page 7 – Forecast & Scenarios

### Objective

Show scenario-based forecast outputs for 2026E–2028E.

### Input Tables

- `forecast_financials.csv`
- `forecast_ratios.csv`
- `scenario_analysis.csv`

### Recommended Slicers

- Scenario
- Period
- Metric category

### Recommended KPI Cards

- Net Income 2028E by selected scenario
- ROE 2028E by selected scenario
- Cost-to-Income 2028E by selected scenario
- Cost of Risk 2028E by selected scenario
- CET1 Ratio Assumption 2028E by selected scenario

### Recommended Visuals

- Net income by scenario and period
- ROE by scenario and period
- Cost-to-income ratio by scenario and period
- Cost of risk by scenario and period
- CET1 ratio assumption by scenario and period
- Variance vs Base by metric

### Required Disclaimer

Add a visible note:

`Forecast figures are educational scenario-based estimates. They are not official projections, investment advice or financial recommendations.`

## Page 8 – Data Quality

### Objective

Show the controlled data workflow behind the project.

### Recommended KPIs

- Reviewed items
- To Review items
- Pending items
- Source-mapped items
- Forecast outputs requiring review

### Recommended Visuals

- Validation status breakdown
- Source status breakdown
- Reviewed vs To Review by dataset
- Forecast outputs requiring human review

### Suggested Narrative

This page should reinforce:

- Public-source data
- Source mapping
- Validation checks
- Human review
- AI-assisted but human-reviewed workflow

## Visual Design Guidelines

Use a clean banking / institutional style:

- Dark blue / navy as primary colour
- Gold or muted accent colour
- White or light background
- Consistent card layout
- Clear page titles
- Minimal clutter
- Consistent font sizes
- Small explanatory notes where needed

## Final Review Checklist

Before saving the v2 dashboard:

- [ ] Confirm all pages refresh correctly.
- [ ] Confirm historical visuals use actual periods only.
- [ ] Confirm forecast visuals are clearly labelled as estimates.
- [ ] Confirm scenario slicers work.
- [ ] Confirm KPI cards show correct values.
- [ ] Confirm Data Quality page is understandable.
- [ ] Confirm disclaimers are visible.
- [ ] Confirm no visual implies investment recommendation.
- [ ] Save as `millennium_bcp_banking_dashboard_v2.pbix`.

## Disclaimer

This dashboard is for educational and portfolio purposes only.

It does not constitute financial advice, investment advice, valuation advice, credit advice, legal advice or a recommendation to buy, sell or hold any financial instrument.

Forecast outputs are scenario-based estimates and should not be interpreted as official projections.
