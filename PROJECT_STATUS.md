# Project Status – Financial Modeling Case Study: Millennium bcp

## Current Project Phase

**Phase 2 – Public Data Extraction, Validation and Initial Banking Analytics**

The project has completed the initial **2024A–2025A public data cycle**.

This means the project now includes:

- reviewed 2025A public data;
- reviewed 2024A public/reexpressed comparative data;
- structured financial data;
- structured banking ratios;
- source mapping;
- extraction tracking;
- validation checks;
- initial 2024A–2025A analytical commentary;
- updated financial data quality documentation.

The project is now ready to move into the next historical extraction phase:

```text
2023A and 2022A official annual report extraction
```

---

## Project Objective

This project is a professional portfolio case study focused on Millennium bcp / Banco Comercial Português as a listed Portuguese bank.

The objective is to demonstrate a practical workflow combining:

- financial statement analysis;
- banking ratio analysis;
- public financial data extraction;
- financial data quality;
- source validation;
- SQL-ready structured datasets;
- Power BI dashboard preparation;
- financial modeling preparation;
- human-in-the-loop analytical review.

The project uses only public information and is intended for educational, analytical and professional portfolio purposes.

It does not provide investment advice, financial advice, valuation advice, a price target or any buy/sell/hold recommendation.

---

## Current Timeline

| Period | Status | Notes |
|---|---:|---|
| 2022A | Pending | To be extracted from official public annual report |
| 2023A | Pending | To be extracted from official public annual report |
| 2024A | Completed for initial scope | Official/reexpressed comparative public data extracted and validated |
| 2025A | Completed for initial scope | Official public data extracted and validated |
| 2026E | Pending | Forecast period, not yet activated |
| 2027E | Pending | Forecast period, not yet activated |

---

## Completed Work

### Project Structure

The project structure has been created and organised for:

- data files;
- reports;
- SQL files;
- Power BI documentation;
- model templates;
- methodology documentation;
- source tracking;
- validation checks.

Completed structure includes:

```text
data/
reports/
sql/
powerbi/
model/
notes/
```

---

## Completed Documentation

The following documentation files have been created or updated:

| File | Status |
|---|---:|
| `README.md` | Completed |
| `RUN_PROJECT.md` | Completed |
| `PROJECT_STATUS.md` | Active |
| `CHANGELOG.md` | Active |
| `ROADMAP.md` | Completed |
| `disclaimer.md` | Completed |
| `methodology.md` | Completed |
| `sources.md` | Completed |
| `company_overview.md` | Completed |
| `assumptions.md` | Completed |
| `ratio_analysis.md` | Completed |
| `valuation_summary.md` | Completed |
| `investment_memo.md` | Completed |
| `reports/banking_analytics_report.md` | Updated |
| `reports/data_quality_report.md` | Updated |

---

## Completed Data Files

The following data files are active:

| File | Status | Notes |
|---|---:|---|
| `data/financial_data.csv` | Active | Contains reviewed 2024A and 2025A core financial data |
| `data/banking_ratios.csv` | Active | Contains reviewed 2024A and 2025A banking ratios |
| `data/source_mapping.csv` | Active | Contains reviewed 2024A and 2025A source mapping entries |
| `data/extraction_tracker.csv` | Active | Tracks extraction progress and source validation |
| `data/forecast_assumptions.csv` | Template | Forecast assumptions not yet activated |
| `data/scenario_analysis.csv` | Template | Scenario outputs not yet activated |
| `data/market_data_template.csv` | Template | Market data not yet activated |
| `data/peer_comparison_template.csv` | Template | Peer comparison not yet activated |
| `data/validation_checks.py` | Active | Validation script currently running |

---

## Completed 2025A Extraction

The initial 2025A public data extraction has been completed.

Reviewed 2025A areas include:

- net interest income;
- operating income;
- operating costs;
- impairments and provisions;
- net income;
- customer loans;
- customer funds / customer deposits;
- total assets;
- equity;
- ROE;
- ROA;
- net interest margin;
- cost-to-income ratio;
- cost-to-income ratio excluding specific items;
- cost of risk;
- NPE ratio;
- NPE coverage ratio;
- restructured loans ratio;
- loan-to-deposit ratio;
- loan-to-balance-sheet-customer-resources ratio;
- LCR;
- NSFR;
- CET1 phased-in ratio;
- CET1 fully implemented ratio;
- total capital fully implemented ratio;
- EPS;
- book value per share.

---

## Completed 2024A Extraction

The initial 2024A public/reexpressed comparative data extraction has been completed.

Reviewed 2024A areas include:

- net interest income;
- operating income;
- operating costs;
- operating costs excluding specific items;
- net credit impairments;
- other impairments and provisions;
- net income;
- customer loans;
- customer funds;
- balance sheet customer resources;
- deposits and other customer resources;
- total assets;
- equity;
- ROE;
- ROA;
- net interest margin;
- cost-to-income ratio;
- cost-to-income ratio excluding specific items;
- cost of risk;
- NPE ratio;
- NPE coverage ratio;
- restructured loans ratio;
- loan-to-deposit ratio;
- loan-to-balance-sheet-customer-resources ratio;
- LCR;
- NSFR;
- CET1 phased-in ratio;
- CET1 fully implemented ratio;
- total capital fully implemented ratio;
- EPS;
- book value per share.

---

## Completed 2024A–2025A Data Cycle

The project has completed the first structured historical comparison cycle.

| Component | Status |
|---|---:|
| 2025A financial data | Completed |
| 2024A financial data | Completed |
| 2025A banking ratios | Completed |
| 2024A banking ratios | Completed |
| 2025A source mapping | Completed |
| 2024A source mapping | Completed |
| 2025A extraction tracker | Completed |
| 2024A extraction tracker | Completed |
| 2024A–2025A banking analytics commentary | Completed |
| 2024A–2025A data quality documentation | Completed |

This creates the following workflow:

```text
official public source
→ extracted data
→ structured CSV
→ validation status
→ source mapping
→ analytical commentary
→ data quality review
→ GitHub portfolio documentation
```

---

## Current Validation Status

The validation script is active:

```text
data/validation_checks.py
```

The current expected validation output is:

```text
2 validation issue(s) found:

1. market_data_template.csv: column 'category' has 17 missing values
2. peer_comparison_template.csv: column 'business_type' has 10 missing values
```

These warnings are acceptable at this stage because both files are templates for future phases.

They do not affect the reviewed 2024A–2025A data cycle.

---

## Known Data Quality Notes

### Customer Deposits vs Customer Funds

The main semantic review item is the distinction between:

- customer deposits;
- customer funds;
- deposits and other customer resources;
- balance sheet customer resources.

Some dataset labels use “Customer deposits” for consistency, while the official source may refer to broader customer funds or customer resources.

These entries are flagged as requiring review where necessary.

### Reexpressed 2024A Figures

Some 2024A values are treated as official/reexpressed comparative figures from the 2025 public source.

These figures should be cross-checked against the 2024 annual report where appropriate before final use in a full investment-style memo.

### Reported vs Calculated Values

The project separates reported figures from calculated values.

Valuation multiples such as P/E, P/B and dividend yield remain pending until a specific market data date is selected.

---

## Reports Updated

### Banking Analytics Report

`reports/banking_analytics_report.md` has been updated with:

- 2025A findings;
- 2024A–2025A comparison;
- profitability analysis;
- efficiency analysis;
- asset quality analysis;
- liquidity and funding analysis;
- capital analysis;
- per-share indicators;
- SQL analytics angle;
- Power BI dashboard angle;
- human-in-the-loop review notes.

### Data Quality Report

`reports/data_quality_report.md` has been updated with:

- 2024A–2025A data quality cycle status;
- completed extraction status;
- validation controls;
- source mapping controls;
- semantic review items;
- SQL readiness;
- Power BI readiness;
- data quality risk register;
- recommended validation enhancements;
- portfolio positioning.

---

## SQL Status

The SQL layer has been created.

Completed files:

| File | Status |
|---|---:|
| `sql/schema.sql` | Completed |
| `sql/queries.sql` | Completed |
| `sql/README.md` | Completed |

The SQL layer supports:

- reviewed vs pending analysis;
- period comparison;
- banking ratio analysis;
- source validation checks;
- data quality queries;
- Power BI extract preparation.

SQL execution is not yet active against a database. The structure is ready for future loading into SQLite, PostgreSQL or another analytical environment.

---

## Power BI Status

The Power BI documentation layer has been created.

Completed files:

| File | Status |
|---|---:|
| `powerbi/README.md` | Completed |
| `powerbi/dashboard_structure.md` | Completed |

The Power BI dashboard is planned to include:

- Executive Summary;
- Profitability;
- Efficiency;
- Asset Quality;
- Liquidity and Funding;
- Capital;
- Forecast and Scenario Analysis;
- Data Quality Dashboard.

No `.pbix` file has been created yet.

---

## Forecast and Valuation Status

Forecasting and valuation are not yet active.

Pending areas include:

- 2026E forecast assumptions;
- 2027E forecast assumptions;
- scenario outputs;
- sensitivity analysis;
- selected share price date;
- market capitalisation;
- P/E;
- P/B;
- dividend yield;
- payout ratio;
- peer comparison.

Forecasts and valuation multiples should only be activated after:

1. completing 2022A and 2023A historical extraction;
2. validating metric definitions;
3. selecting a market data date;
4. documenting assumptions;
5. separating historical data from estimates.

---

## Current GitHub Progress

Recent completed Git milestones include:

- adding the banking analytics, SQL and Power BI project structure;
- adding 2025A public banking data;
- adding 2024A official financial data;
- adding 2024A official banking ratios;
- adding 2024A official source mapping entries;
- updating banking analytics commentary;
- updating data quality documentation.

The repository is being built through small, traceable commits.

---

## Current Project Strength

The project currently demonstrates:

- public financial data extraction;
- banking ratio interpretation;
- financial data quality controls;
- source mapping;
- validation scripting;
- human-in-the-loop review;
- SQL readiness;
- Power BI readiness;
- Git/GitHub workflow;
- professional documentation;
- portfolio-oriented financial research.

This is now stronger than a simple financial model because it shows a complete workflow from data extraction to validation and analysis.

---

## Remaining Gaps

The main remaining gaps are:

| Area | Status |
|---|---:|
| 2023A extraction | Pending |
| 2022A extraction | Pending |
| market data | Pending |
| peer comparison | Pending |
| valuation multiples | Pending |
| forecast model | Pending |
| scenario analysis | Pending |
| Power BI implementation | Pending |
| SQL database execution | Pending |

---

## Immediate Next Step

The recommended next step is:

```text
Extract and validate 2023A official public data.
```

This should include:

1. identifying the correct official 2023 annual report source;
2. extracting core financial metrics;
3. updating `data/financial_data.csv`;
4. updating `data/banking_ratios.csv`;
5. updating `data/source_mapping.csv`;
6. updating `data/extraction_tracker.csv`;
7. running `data/validation_checks.py`;
8. committing the changes to GitHub.

After 2023A is completed, the same process should be repeated for 2022A.

---

## Recommended Next Phase

### Phase 3 – Historical Data Completion

Objective:

```text
Complete 2023A and 2022A extraction from official public annual reports.
```

Expected output:

- complete 2022A–2025A historical dataset;
- stronger trend analysis;
- more credible forecast assumptions;
- better Power BI dashboard readiness;
- stronger financial research portfolio value.

---

## Professional Positioning Value

At the current stage, this project is already useful for demonstrating capability in:

- Financial Research;
- Banking Analytics;
- Financial Data Quality;
- Data Validation;
- Reporting Analyst roles;
- Investment Research Support;
- Wealth Management Support;
- AI Finance Evaluation;
- AI Product Testing in Finance;
- SQL-based financial analysis;
- Power BI dashboard planning.

The strongest current narrative is:

```text
Built a public-data banking analytics case study on Millennium bcp, including structured financial data extraction, banking ratio analysis, source mapping, data quality validation, SQL-ready datasets, Power BI dashboard planning and human-in-the-loop analytical review.
```

---

## Current Status Summary

| Area | Status |
|---|---:|
| Project setup | Completed |
| README | Completed |
| Methodology | Completed |
| SQL structure | Completed |
| Power BI structure | Completed |
| 2025A extraction | Completed |
| 2024A extraction | Completed |
| 2024A–2025A comparison | Completed |
| Source mapping | Completed for 2024A and 2025A |
| Data quality report | Completed for 2024A and 2025A cycle |
| Banking analytics report | Completed for 2024A and 2025A cycle |
| Validation script | Active |
| 2023A extraction | Pending |
| 2022A extraction | Pending |
| Forecasting | Pending |
| Valuation | Pending |
| Peer comparison | Pending |
| Power BI build | Pending |

---

## Disclaimer

This project is for educational, analytical and professional portfolio purposes only.

It uses only publicly available information.

It does not use confidential information, internal banking data, client data or proprietary information.

It does not provide investment advice, financial advice, valuation advice, a price target or a buy/sell/hold recommendation.

All figures should be independently verified before any professional, academic or investment-related use.

The analysis is descriptive, illustrative and subject to further validation.