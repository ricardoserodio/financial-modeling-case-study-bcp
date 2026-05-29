# Financial Modeling Case Study  
## Millennium bcp / Portuguese Listed Bank

**Public-Source Banking Analytics, Forecasting and Data Quality Review**

Prepared by: **Ricardo Serôdio**  
Portfolio: `https://ricardoserodio.com`  
GitHub: `https://github.com/ricardoserodio`  

---

## Report Scope

This report presents a public-source financial modeling and banking analytics case study focused on a Portuguese listed bank, using Millennium bcp as the case study reference.

The project combines financial statement analysis, banking ratio analysis, scenario-based forecast assumptions, Power BI dashboarding, SQL analytical queries, data quality review and an AI-assisted, human-reviewed validation workflow.

---

## Important Disclaimer

This report is for educational, portfolio and professional development purposes only.

It does not constitute financial advice, investment advice, valuation advice, credit advice, legal advice or a recommendation to buy, sell or hold any financial instrument.

All forecast figures are scenario-based estimates and should be interpreted as analytical modelling outputs, not as official projections.

---

## 1. Executive Summary

This report presents a public-source financial modeling and banking analytics case study focused on a Portuguese listed bank, using Millennium bcp as the case study reference.

The objective is to demonstrate a structured analytical workflow combining historical financial data, banking ratio analysis, forecast assumptions, scenario analysis, Power BI reporting, SQL analytical queries and data quality review.

This report is for educational, portfolio and professional development purposes only. It does not constitute financial advice, investment advice, valuation advice, credit advice, legal advice or a recommendation to buy, sell or hold any financial instrument.

## 2. Project Objective

The project aims to demonstrate the ability to:

- Structure public financial data into reusable datasets
- Analyse banking profitability, efficiency, asset quality, liquidity and capital metrics
- Build scenario-based forecast assumptions
- Generate forecast financials and forecast ratios
- Compare Base, Optimistic and Conservative scenarios
- Create Power BI dashboard outputs
- Build a SQL analytical layer
- Apply data quality checks and human review controls

## 3. Scope of Analysis

The project covers the following periods:

- 2022A
- 2023A
- 2024A
- 2025A
- 2026E
- 2027E
- 2028E

Historical periods are based on structured public-source information.

Forecast periods are educational scenario-based estimates and require final human review before professional or public promotional use.

## 4. Data Sources and Structure

The project uses structured CSV datasets based on publicly available information.

Main datasets include:

- `data/financial_data.csv`
- `data/banking_ratios.csv`
- `data/source_mapping.csv`
- `data/extraction_tracker.csv`
- `data/forecast_assumptions.csv`
- `data/forecast_financials.csv`
- `data/forecast_ratios.csv`
- `data/scenario_analysis.csv`

The data structure supports traceability, validation status review and analytical reuse across Python, Power BI and SQL.

## 5. Historical Financial Analysis

The historical financial dataset includes selected banking financial statement metrics, including:

- Net interest income
- Operating income
- Operating costs
- Impairments and provisions
- Net income
- Customer loans
- Customer deposits
- Total assets
- Equity

These metrics provide the foundation for the forecast model and scenario analysis.

## 6. Banking Ratio Analysis

The banking ratio dataset includes profitability, efficiency, asset quality, liquidity and capital indicators.

Key ratio categories include:

- Profitability: ROE, ROA, net interest margin
- Efficiency: cost-to-income ratio
- Asset quality: cost of risk, NPE ratio, NPE coverage ratio
- Liquidity: loan-to-deposit ratio, LCR, NSFR
- Capital: CET1 and total capital ratios
- Per share metrics: EPS and book value per share
- Valuation metrics where available

For 2025A, reported ratios are used where available. This avoids overstating precision where simplified calculations may not fully replicate management reporting, regulatory definitions or average balance methodologies.

### Banking Ratio Glossary – Key Metrics Used

The following table summarises the main banking ratios used in this report. These formulas are simplified analytical formulas and may not fully replicate official bank reporting, regulatory calculations or internal methodologies.

| Ratio | Simplified Formula | Meaning |
|---|---|---|
| ROE | Net Income / Average Equity | Measures profitability relative to the equity base. |
| ROA | Net Income / Average Total Assets | Measures profitability relative to the bank's asset base. |
| Net Interest Margin | Net Interest Income / Average Interest-Earning Assets | Measures the bank's interest spread relative to earning assets. |
| Cost-to-Income Ratio | Operating Costs / Operating Income | Measures operating efficiency. A lower ratio generally indicates better efficiency. |
| Cost of Risk | Loan Impairments / Average Customer Loans | Measures credit impairment charges relative to the loan book. Usually expressed in basis points. |
| NPE Ratio | Non-Performing Exposures / Total Exposures | Measures the proportion of exposures classified as non-performing. |
| Loan-to-Deposit Ratio | Customer Loans / Customer Deposits | Measures the relationship between customer lending and customer deposits. |
| LCR | High Quality Liquid Assets / 30-Day Net Cash Outflows | Measures short-term liquidity resilience under stress. |
| NSFR | Available Stable Funding / Required Stable Funding | Measures the stability of the funding profile over a one-year horizon. |
| CET1 Ratio | CET1 Capital / Risk-Weighted Assets | Measures the bank's highest-quality regulatory capital relative to risk-weighted assets. |
| Total Capital Ratio | Total Own Funds / Risk-Weighted Assets | Measures total regulatory capital relative to risk-weighted assets. |
| EPS | Net Income Attributable to Shareholders / Weighted Average Shares | Measures earnings attributable to each ordinary share. |
| Book Value per Share | Equity Attributable to Shareholders / Shares Outstanding | Measures accounting equity value per share. |
| Price-to-Book | Market Capitalisation / Book Value of Equity | Compares market value with accounting book value. |
| Price-to-Earnings | Share Price / Earnings per Share | Compares share price with earnings per share. |

For a more detailed explanation of each ratio, including interpretation notes and limitations, see:

`docs/banking_ratio_glossary.md`

## 7. Forecast Methodology

The forecast is built from 2025A actuals and scenario-based assumptions.

The forecast covers:

- 2026E
- 2027E
- 2028E

The three scenarios are:

- Base
- Optimistic
- Conservative

Forecast assumptions include:

- Net interest income growth
- Other operating income growth
- Operating costs growth
- Cost of risk
- Customer loans growth
- Customer deposits growth
- CET1 ratio assumption

Forecast outputs are generated using Python scripts and require final human review before professional or public promotional use.

## 8. Base Year Treatment

The year 2025A is treated as the forecast base year.

Historical 2025A financial statement values are taken from `data/financial_data.csv`.

Historical 2025A banking ratios are taken from `data/banking_ratios.csv`.

Reported 2025A ratios are used where available because bank-reported ratios may rely on specific definitions, average balances, regulatory bases or management reporting approaches.

## 9. Revenue Forecast

The model forecasts:

- Net interest income
- Other operating income
- Operating income

Fees and commissions are not forecast directly in the current version because this line item has not yet been fully validated across all historical periods.

Instead, the model uses:

`Other operating income = Operating income - Net interest income`

This approach avoids overstating precision where the underlying line item is not yet fully validated.

## 10. Cost and Risk Forecast

Operating costs are forecast using scenario-based growth assumptions.

The model derives:

`Pre-provision operating profit = Operating income - Operating costs`

Impairments and provisions are estimated using a cost of risk assumption applied to customer loans:

`Impairments and provisions = Customer loans × Cost of risk / 10,000`

Cost of risk is expressed in basis points.

## 11. Balance Sheet Forecast

The model forecasts:

- Customer loans
- Customer deposits
- Total assets
- Equity

Customer loans and customer deposits are grown using scenario-based assumptions.

Total assets are estimated using a simplified proxy based on the average of customer loan growth and customer deposit growth.

Equity is estimated using a simplified retained earnings bridge:

`Equity = Prior year equity + 50% of estimated net income`

This is an educational simplification and does not fully model dividends, buybacks, other comprehensive income, regulatory deductions or risk-weighted assets.

## 12. Forecast Ratios

Forecast ratios include:

- ROE
- ROA
- Cost-to-income ratio
- Loan-to-deposit ratio
- Cost of risk
- CET1 ratio assumption

For 2025A, reported ratios from `banking_ratios.csv` are used.

For 2026E–2028E, ratios are calculated from forecast outputs or taken directly from forecast assumptions.

## 13. Scenario Analysis

The scenario analysis compares Base, Optimistic and Conservative cases across key financial and ratio metrics.

For each metric, the analysis includes:

- Scenario value
- Base case value
- Absolute variance vs Base
- Percentage variance vs Base
- Scenario logic
- Main driver
- Risk level
- Interpretation
- Validation status

This supports a structured view of how assumptions affect profitability, efficiency, asset quality, liquidity and capital indicators.

## 14. Power BI Dashboard

The Power BI dashboard provides a visual layer for the project.

Dashboard pages include:

- Executive Overview
- Liquidity & Funding
- Asset Quality
- Profitability
- Efficiency
- Capital
- Data Quality

The dashboard is designed as a portfolio-grade business intelligence output and should not be interpreted as an investment recommendation tool.

## 15. SQL Analytics Layer

The SQL layer demonstrates how the project datasets can be queried in an analytical workflow.

SQL files include:

- `sql/create_tables.sql`
- `sql/banking_ratio_queries.sql`
- `sql/data_quality_queries.sql`
- `sql/forecast_queries.sql`
- `sql/README.md`

The SQL layer supports:

- Historical ratio review
- Data quality review
- Forecast assumption review
- Forecast output review
- Scenario comparison
- Human review workflow

## 16. Data Quality and Human Review

The project includes a data quality workflow covering:

- Validation status
- Source mapping
- Extraction tracking
- Missing values
- Reviewed vs human-review-required classification
- Forecast output review
- Final publication checklist

Validation can be run with:

`python data/validation_checks.py`

Forecast outputs require final human review before professional or public promotional use.

## 17. AI-Assisted, Human-Reviewed Workflow

This project follows an AI-assisted, human-reviewed workflow.

AI tools may support documentation structure, analytical framing, code generation, consistency checks and data quality review.

However, all financial figures, assumptions, interpretations and final outputs require human review by the author before publication.

## 18. Key Limitations

This project has several limitations:

- It uses only publicly available information.
- It is a simplified educational model.
- It does not replicate internal bank forecasting methodology.
- It does not fully model regulatory capital dynamics.
- It does not model risk-weighted assets in detail.
- It does not model dividends, buybacks or OCI impacts in full.
- It does not provide valuation advice.
- It does not provide investment recommendations.
- It should not be interpreted as an official forecast.

## 19. Professional Relevance

This case study demonstrates practical skills relevant to:

- Banking analytics
- Financial data quality
- Financial modeling
- Power BI reporting
- SQL analytical workflows
- Scenario analysis
- Risk-aware financial interpretation
- Responsible AI-assisted finance workflows

The project is designed to be clear, recruiter-friendly and aligned with roles in financial data quality, banking analytics, financial research, risk operations, business intelligence and finance transformation.

## 20. Disclaimer

This report is for educational, analytical and portfolio purposes only.

It does not constitute financial advice, investment advice, valuation advice, credit advice, legal advice or a recommendation to buy, sell or hold any financial instrument.

All forecast figures are scenario-based estimates and should be interpreted as analytical modelling outputs, not as official projections.

The author is not affiliated with Millennium bcp for the purpose of this project. The project uses public information only.


