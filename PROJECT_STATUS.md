# Project Status

This document summarises the current status of the **Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank** project.

The project is now structured as a hybrid portfolio project combining:

- Financial Modeling;
- Banking Analytics;
- SQL;
- Power BI;
- Financial Data Quality;
- Source Validation;
- Executive Reporting.

The project is designed for educational, portfolio and professional development purposes only.

It does not constitute investment advice.

---

## Current Project Phase

The project is currently in:

    Phase 2 – Initial Public Data Extraction and Validation

The repository structure, documentation, SQL layer, Power BI planning layer, reports folder and data quality framework have been created.

The first real public-data extraction for 2025A has also been completed.

---

## Completed Work

The following components have been created or updated:

- professional README;
- project disclaimer;
- methodology documentation;
- public source documentation;
- company overview;
- forecast assumptions documentation;
- banking ratio analysis structure;
- valuation summary structure;
- investment memo template;
- data validation rules;
- data dictionary;
- source mapping template;
- source links file;
- historical financials template;
- banking ratios dataset;
- financial data dataset;
- forecast assumptions template;
- scenario analysis template;
- market data template;
- peer comparison template;
- data extraction tracker;
- Python validation checks script;
- banking model Excel template generator;
- sensitivity analysis Excel template generator;
- formula reference documentation;
- local project run instructions;
- project status documentation;
- changelog;
- roadmap;
- SQL schema;
- SQL analytical queries;
- SQL layer documentation;
- Power BI dashboard documentation;
- Power BI dashboard structure;
- banking analytics report;
- financial data quality report;
- human-in-the-loop model review checklist.

---

## Initial 2025A Extraction Status

The initial 2025A public-data extraction has been completed.

The 2025A data has been added to:

- `data/financial_data.csv`;
- `data/banking_ratios.csv`;
- `data/extraction_tracker.csv`;
- `data/source_mapping.csv`.

The initial extraction includes:

- profitability metrics;
- efficiency metrics;
- asset quality metrics;
- balance sheet metrics;
- capital ratios;
- liquidity ratios;
- selected per-share indicators.

Current validation status:

    Reviewed

The data has been added from public sources and reviewed at an initial level.

Before final publication, the 2025A data should still be cross-checked against:

- official annual report;
- official investor presentation;
- official key indicators pages;
- source mapping file;
- extraction tracker file.

---

## Current Data Status

The project currently includes:

| Area | Status |
|---|---|
| Repository structure | Completed |
| Documentation framework | Completed |
| SQL layer | Initial structure completed |
| Power BI layer | Initial structure completed |
| Reports layer | Initial structure completed |
| Data quality framework | Initial structure completed |
| 2025A public data extraction | Completed |
| 2025A banking ratios | Completed |
| 2025A source mapping | Completed |
| 2025A extraction tracker | Completed |
| 2025A banking analytics commentary | Completed |
| 2025A data quality commentary | Completed |
| 2024A extraction | Pending |
| 2023A extraction | Pending |
| 2022A extraction | Pending |
| Forecast assumptions | Pending |
| Scenario analysis | Pending |
| Market data | Pending |
| Peer comparison | Pending |
| Power BI dashboard build | Pending |

---

## Validation Status

The Python validation script has been executed using:

    python data/validation_checks.py

The script completed successfully.

The current warnings relate to template files that are not yet fully populated:

- `data/market_data_template.csv`;
- `data/peer_comparison_template.csv`.

These warnings are acceptable at the current stage because market data and peer comparison belong to later project phases.

No blocking validation issue was identified for the initial 2025A banking analytics dataset.

---

## Completed Reports

The following reporting files have been updated with the initial 2025A work:

| File | Status |
|---|---|
| `reports/banking_analytics_report.md` | Initial 2025A commentary added |
| `reports/data_quality_report.md` | Initial 2025A validation status added |

The project now includes both:

- analytical commentary;
- data quality commentary.

This strengthens the project as a banking analytics and financial data quality portfolio case study.

---

## Pending Work

The following tasks are still pending:

- extract 2024A financial data from official public sources;
- extract 2023A financial data from official public sources;
- extract 2022A financial data from official public sources;
- complete historical trend analysis for 2022A–2025A;
- cross-check 2025A values against the official annual report;
- confirm source references and pages or sections;
- review labels such as customer deposits versus customer funds;
- complete `data/historical_financials.csv`;
- complete multi-year `data/financial_data.csv`;
- complete multi-year `data/banking_ratios.csv`;
- complete multi-year `data/source_mapping.csv`;
- complete multi-year `data/extraction_tracker.csv`;
- select a valuation date for market data;
- complete `data/market_data_template.csv`;
- review and refine peer group selection;
- complete `data/peer_comparison_template.csv`;
- run validation checks after each major data update;
- generate the Excel model templates;
- populate the Excel model;
- define forecast assumptions for 2026E and 2027E;
- complete scenario analysis;
- build Power BI dashboard;
- write final investment memo;
- perform final human-in-the-loop review before publication.

---

## Planned Project Phases

### Phase 1 – Repository Structure and Documentation

Status:

    Completed

Objective:

Create a clean, professional and auditable project structure.

Main outputs completed:

- README;
- disclaimer;
- methodology;
- source documentation;
- data templates;
- validation rules;
- model documentation;
- SQL structure;
- Power BI structure;
- reports structure;
- local run instructions;
- project status;
- changelog;
- roadmap.

---

### Phase 2 – Initial Public Data Extraction

Status:

    In progress

Objective:

Extract historical financial data from official public sources.

Current progress:

- 2025A initial extraction completed;
- 2024A pending;
- 2023A pending;
- 2022A pending.

Main outputs:

- completed `data/financial_data.csv`;
- completed `data/banking_ratios.csv`;
- completed `data/source_mapping.csv`;
- completed `data/extraction_tracker.csv`.

---

### Phase 3 – Historical Trend Analysis

Status:

    Pending

Objective:

Move from a single-year 2025A snapshot to a proper multi-year trend analysis.

Main outputs:

- 2022A–2025A profitability trend;
- 2022A–2025A efficiency trend;
- 2022A–2025A asset quality trend;
- 2022A–2025A capital trend;
- updated banking analytics report;
- updated Power BI dashboard inputs.

---

### Phase 4 – Data Validation and Quality Review

Status:

    In progress

Objective:

Validate financial data quality before using it in final analysis.

Current progress:

- initial validation script executed;
- 2025A data reviewed;
- market data and peer comparison warnings identified as non-blocking template issues.

Main outputs:

- validation script output;
- reviewed source mapping;
- unit consistency checks;
- period consistency checks;
- reported vs calculated figure review;
- updated data quality report.

---

### Phase 5 – SQL Analytics Layer

Status:

    Initial structure completed

Objective:

Structure public financial data into SQL tables and queries.

Main outputs completed:

- `sql/schema.sql`;
- `sql/queries.sql`;
- `sql/README.md`.

Pending work:

- load or replicate completed datasets into SQL tables;
- test analytical queries;
- use SQL outputs for Power BI preparation.

---

### Phase 6 – Power BI Dashboard

Status:

    Planned

Objective:

Create an executive-style banking analytics dashboard.

Planned dashboard pages:

- Executive Summary;
- Profitability;
- Efficiency;
- Asset Quality;
- Capital & Liquidity;
- Forecast & Scenarios;
- Data Quality.

Main outputs:

- Power BI report file;
- dashboard screenshots, if appropriate;
- dashboard documentation;
- updated Power BI README.

---

### Phase 7 – Excel Model Generation and Population

Status:

    Pending

Objective:

Generate and populate the Excel banking model and sensitivity analysis files.

Main outputs:

- `model/banking_model.xlsx`;
- `model/sensitivity_analysis.xlsx`.

---

### Phase 8 – Forecast and Scenario Analysis

Status:

    Pending

Objective:

Build simplified forecast scenarios for 2026E and 2027E based on public information and documented assumptions.

Main outputs:

- base scenario;
- downside scenario;
- upside scenario, if justified;
- scenario comparison;
- sensitivity tables.

---

### Phase 9 – Valuation and Investment Memo

Status:

    Pending

Objective:

Prepare an educational valuation summary and professional investment-style memo.

Main outputs:

- valuation summary;
- investment memo;
- final project review.

---

### Phase 10 – Final Review and Portfolio Publication

Status:

    Pending

Objective:

Perform final quality review before presenting the project publicly.

Main tasks:

- review all documentation;
- check all source references;
- run validation script;
- review Excel model outputs;
- review SQL queries;
- review Power BI dashboard;
- review report language;
- confirm no personal data is included;
- confirm no confidential information is included;
- confirm no investment recommendation is made;
- update project status;
- update changelog.

---

## Quality Control Principles

The project follows these quality control principles:

- use only public information;
- map each key figure to a source;
- separate reported figures from calculated figures;
- separate historical actuals from forecasts;
- document all assumptions;
- date all market data;
- avoid unsupported conclusions;
- avoid investment advice language;
- apply human review before publishing conclusions.

---

## Important Restrictions

This project must not include:

- personal data;
- client data;
- employee data;
- internal banking information;
- confidential documents;
- screenshots from internal systems;
- non-public information;
- investment recommendations.

---

## Next Immediate Step

The next immediate step is to continue historical data extraction.

Recommended next period:

    2024A

Recommended files to update:

- `data/extraction_tracker.csv`;
- `data/financial_data.csv`;
- `data/banking_ratios.csv`;
- `data/source_mapping.csv`.

Recommended workflow:

1. Extract 2024A data from official public sources.
2. Add values to the extraction tracker.
3. Update the main financial dataset.
4. Update banking ratios.
5. Update source mapping.
6. Run validation checks.
7. Update reports.
8. Commit the changes.

---

## Disclaimer

This project is for educational and portfolio purposes only.

It does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.

All analysis is based only on publicly available information.