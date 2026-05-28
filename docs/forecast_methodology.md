# Forecast Methodology

## Purpose

This document explains the forecast methodology used in the Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank project.

The forecast is designed for educational, portfolio and analytical demonstration purposes only. It is not an official projection, investment advice, financial advice, valuation advice, target price or a recommendation to buy, sell or hold any financial instrument.

## Forecast Scope

The model uses historical actual data for:

- 2022A
- 2023A
- 2024A
- 2025A

The forecast period covers:

- 2026E
- 2027E
- 2028E

The forecast is scenario-based and includes three cases:

- Base
- Optimistic
- Conservative

## Data Sources

The model uses structured project datasets based on publicly available financial information.

Main input files:

- `data/financial_data.csv`
- `data/banking_ratios.csv`
- `data/forecast_assumptions.csv`

Generated forecast outputs:

- `data/forecast_financials.csv`
- `data/forecast_ratios.csv`
- `data/scenario_analysis.csv`

Supporting scripts:

- `scripts/build_forecast_financials.py`
- `scripts/build_forecast_ratios.py`
- `scripts/build_scenario_analysis.py`

## Base Year Treatment

The year 2025A is treated as the forecast base year.

Historical 2025A financial statement values are taken from `data/financial_data.csv`.

Historical 2025A banking ratios are taken from `data/banking_ratios.csv`.

Reported banking ratios may use specific definitions, averages, regulatory bases or management reporting methodologies that are not always fully replicated by simplified calculations.

For this reason, the model uses reported 2025A ratios where available instead of recalculating them from simplified financial statement inputs.

## Revenue Forecast

The model forecasts:

- Net interest income
- Other operating income
- Operating income

Fees and commissions are not forecast directly because the value is currently marked as pending in the dataset.

Instead, the model uses:

`Other operating income = Operating income - Net interest income`

This avoids overstating precision where the underlying line item is not yet fully validated.

## Cost Forecast

Operating costs are forecast using scenario-based growth assumptions.

The model then derives:

`Pre-provision operating profit = Operating income - Operating costs`

## Risk Cost Forecast

Impairments and provisions are estimated using a cost of risk assumption applied to customer loans.

`Impairments and provisions = Customer loans × Cost of risk / 10,000`

Cost of risk is expressed in basis points.

## Balance Sheet Forecast

The model forecasts:

- Customer loans
- Customer deposits
- Total assets
- Equity

Customer loans and customer deposits are grown using scenario-based assumptions.

Total assets are estimated using a simple proxy based on the average of loan growth and deposit growth.

`Total assets growth = Average of customer loans growth and customer deposits growth`

Equity is estimated using a simplified retained earnings bridge:

`Equity = Prior year equity + 50% of estimated net income`

This is a simplified educational approach.

The model does not fully model:

- Dividends
- Share buybacks
- Regulatory deductions
- Other comprehensive income
- Risk-weighted assets
- Full capital generation dynamics

## Net Income Forecast

Net income is estimated using a simplified conversion bridge based on 2025A.

The model calculates a conversion ratio from:

`Net income / (Pre-provision operating profit - Impairments and provisions)`

This ratio is then applied to future estimated profit after impairments.

This is not an official banking forecasting methodology. It is a simplified educational bridge designed to make the model explainable and auditable.

## Ratio Forecast

Forecast ratios include:

- ROE
- ROA
- Cost-to-income ratio
- Loan-to-deposit ratio
- Cost of risk
- CET1 ratio assumption

For 2025A, reported ratios from `banking_ratios.csv` are used.

For 2026E–2028E, ratios are calculated from forecast outputs or taken directly from forecast assumptions.

## Scenario Analysis

The scenario analysis compares Base, Optimistic and Conservative cases across key financial and ratio metrics.

For each metric, the model calculates:

- Scenario value
- Base case value
- Absolute variance vs Base
- Percentage variance vs Base
- Scenario logic
- Main driver
- Risk level
- Interpretation

The output is stored in `data/scenario_analysis.csv`.

## Scenario Logic

### Base Case

The Base case assumes moderate normalisation, controlled cost growth, stable customer funding and broadly stable capital.

### Optimistic Case

The Optimistic case assumes stronger profitability, better non-interest operating income development, controlled risk costs and resilient capital.

### Conservative Case

The Conservative case assumes weaker revenue development, higher cost pressure, higher credit risk costs and some pressure on capital assumptions.

## Validation Status

Forecast outputs are marked as `To Review`.

This means the outputs require human review before being used in any public report, dashboard or portfolio description.

Historical reviewed figures remain marked as `Reviewed`.

## AI-Assisted, Human-Reviewed Workflow

This project follows an AI-assisted, human-reviewed workflow.

AI tools may support documentation structure, analytical framing, consistency checks, code generation and data quality review. However, all financial figures, assumptions, interpretations and final outputs are reviewed by the author.

## Limitations

The forecast has several limitations:

- It is based on simplified assumptions.
- It does not model macroeconomic variables explicitly.
- It does not model interest rate curves directly.
- It does not model risk-weighted assets.
- It does not model dividends, buybacks or full regulatory capital movements.
- It does not fully replicate internal bank forecasting methodology.
- It does not provide valuation advice or investment recommendations.
- It should not be interpreted as an official forecast.

## Methodology Items Requiring Final Review

Before publication, the following items must be reviewed:

- Forecast assumptions
- Scenario values
- Ratio methodology
- Capital assumptions
- Loan-to-deposit ratio methodology
- Cost of risk assumptions
- Equity bridge assumptions
- Source mapping
- Validation status
- Power BI consistency
- Report language
- Disclaimers

## Disclaimer

This project is for educational and portfolio purposes only.

It does not constitute financial advice, investment advice, valuation advice, credit advice, legal advice or a recommendation to buy, sell or hold any financial instrument.

All forecast figures are scenario-based estimates and should be interpreted as analytical modelling outputs, not as official projections.
