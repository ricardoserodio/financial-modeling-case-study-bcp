# Power BI Dashboard v2 Notes

## Purpose

This document summarises the Power BI dashboard v2 improvements for the Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank project.

## Dashboard v2 Improvements

The v2 dashboard adds a dedicated Forecast & Scenarios page.

This page includes:

- Forecast Net Income by Scenario
- ROE by Scenario
- Cost-to-Income by Scenario
- Cost of Risk by Scenario
- CET1 Ratio by Scenario
- Scenario slicer
- Period slicer
- Forecast disclaimer

## Data Model Improvements

The dashboard v2 includes simple dimension tables to improve filtering:

- DimScenario
- DimPeriod

These dimensions are used to control slicers and filter forecast-related visuals across multiple tables.

## Forecast Tables Used

The Forecast & Scenarios page uses:

- forecast_financials
- forecast_ratios
- scenario_analysis
- DimScenario
- DimPeriod

## Disclaimer

Forecast figures are educational scenario-based estimates.

They are not official projections, investment advice or financial recommendations.

## Review Status

The Power BI dashboard v2 is a functional portfolio dashboard draft.

Before final publication, it should be reviewed for:

- Visual consistency
- KPI formatting
- Slicer behaviour
- Forecast labelling
- Disclaimer visibility
- Alignment with README and final report language
