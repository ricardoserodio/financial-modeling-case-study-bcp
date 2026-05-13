# Financial Data Quality Report – Millennium bcp Case Study

## Purpose of This Report

This report documents the financial data quality process used in the **Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank** project.

The objective is to demonstrate a structured approach to:

- financial data validation;
- source mapping;
- public source traceability;
- banking metric consistency;
- reported vs calculated value separation;
- validation status tracking;
- human-in-the-loop review;
- SQL and Power BI readiness.

This report is part of a professional portfolio project focused on banking analytics, financial modeling, financial data quality and public-data research.

It does not provide investment advice, financial advice, a valuation recommendation or a buy/sell/hold recommendation.

---

## Data Quality Philosophy

Financial analysis is only as reliable as the quality of the underlying data.

For this reason, the project treats data quality as a core analytical layer rather than an afterthought.

The main principles are:

1. Every material metric should be traceable to a public source.
2. Reported figures should be separated from calculated figures.
3. Actual historical data should be separated from forecast data.
4. Values requiring interpretation should be flagged.
5. Semantic issues should be documented.
6. Manual review should be part of the analytical workflow.
7. No confidential, internal or client data should be used.
8. Public-source validation should be explicit and reproducible.
9. Source documents should be documented before analytical conclusions are made.
10. Forecasts, scenarios and valuation multiples should remain clearly separated from historical reported data.

---

## Why Data Quality Matters in Banking Analysis

Banking analysis depends heavily on accurate definitions, consistent metric treatment and reliable source traceability.

A small inconsistency in the treatment of a banking metric can materially affect interpretation.

Examples include:

- customer deposits vs customer funds;
- customer loans vs net customer loans;
- NPE ratio vs NPL ratio;
- phased-in capital ratios vs fully implemented capital ratios;
- reported ratios vs internally calculated ratios;
- reexpressed comparative figures vs original annual report figures;
- point-in-time market data vs full-year financial performance.

For this reason, this project treats financial data quality as a professional control layer.

The goal is not only to collect data, but to understand whether each figure is:

- properly sourced;
- correctly labelled;
- consistently classified;
- traceable;
- reviewed;
- ready for analytics;
- appropriate for reporting.

---

## Project Data Files Reviewed

The current data quality review covers the following files:

| File | Purpose | Current Status |
|---|---|---:|
| `data/financial_data.csv` | Core financial statement and balance sheet metrics | Active |
| `data/banking_ratios.csv` | Banking ratios and per-share indicators | Active |
| `data/source_mapping.csv` | Source traceability and validation mapping | Active |
| `data/extraction_tracker.csv` | Extraction progress and review tracking | Active |
| `data/forecast_assumptions.csv` | Forecast assumption template | Template |
| `data/scenario_analysis.csv` | Scenario output template | Template |
| `data/market_data_template.csv` | Market data template for valuation | Template |
| `data/peer_comparison_template.csv` | Peer comparison template | Template |
| `data/validation_checks.py` | Data validation script | Active |

---

## Period Coverage

The project currently uses the following period convention:

| Period | Meaning | Current Status |
|---|---|---:|
| 2022A | Historical actual | Pending extraction |
| 2023A | Historical actual | Pending extraction |
| 2024A | Historical actual / reexpressed comparative figures | Reviewed for initial scope |
| 2025A | Historical actual | Reviewed for initial scope |
| 2026E | Forecast estimate | Pending |
| 2027E | Forecast estimate | Pending |

The current reviewed data quality scope focuses on **2024A and 2025A**.

2022A and 2023A remain pending until they are extracted and validated from official public annual reports.

---

## Current Extraction Status

### 2025A

The 2025A extraction has been completed for the initial scope.

Reviewed 2025A areas include:

- profitability metrics;
- operating income and costs;
- asset quality indicators;
- balance sheet metrics;
- liquidity ratios;
- capital ratios;
- per-share indicators;
- source mapping.

### 2024A

The 2024A extraction has been completed for the initial scope using official/reexpressed comparative figures from public Millennium bcp sources.

Reviewed 2024A areas include:

- profitability metrics;
- operating income and costs;
- operating costs excluding specific items;
- credit impairments;
- other impairments and provisions;
- net income;
- customer loans;
- customer funds;
- balance sheet customer resources;
- deposits and other customer resources;
- total assets;
- equity;
- banking ratios;
- liquidity indicators;
- capital ratios;
- per-share indicators;
- source mapping.

### 2023A and 2022A

The 2023A and 2022A periods remain pending.

These periods should only be marked as reviewed after extraction from official public annual reports and after source mapping has been completed.

Until then, the project should avoid treating 2023A and 2022A as validated historical data.

---

## Completed 2024A–2025A Data Quality Cycle

The initial 2024A–2025A data quality cycle is now complete across the main project files.

| File | 2024A Status | 2025A Status | Notes |
|---|---:|---:|---|
| `data/extraction_tracker.csv` | Completed | Completed | Tracks extraction progress and source validation |
| `data/financial_data.csv` | Completed | Completed | Contains core financial statement and balance sheet data |
| `data/banking_ratios.csv` | Completed | Completed | Contains reviewed banking ratios and per-share indicators |
| `data/source_mapping.csv` | Completed | Completed | Links each metric to public source documentation |

This creates a complete initial workflow:

```text
official public source
→ extracted metric
→ structured CSV
→ validation status
→ source mapping
→ analytical report
→ human review notes
```

This workflow is important because it demonstrates that the project is not just a manual financial model, but a controlled banking analytics process.

---

## Validation Status Categories

The project uses the following validation status categories:

| Status | Meaning |
|---|---|
| Reviewed | Value has been extracted from a public source and reviewed for the current project scope |
| Needs Review | Value is available but requires semantic, definitional or analytical review |
| Pending | Value has not yet been extracted or validated |
| Estimated | Value relates to forecast or scenario assumptions |
| Calculated | Value is derived from other data points and requires formula validation |

These categories help separate values that are ready for analysis from values that still require review.

---

## Source Mapping Controls

The source mapping process tracks:

- metric name;
- category;
- period;
- value;
- unit;
- source document;
- source type;
- source section or page;
- whether the value is reported or calculated;
- calculation method where applicable;
- validation status;
- review notes.

This allows each material value to be traced back to a public source.

The current source mapping layer includes reviewed entries for 2024A and 2025A.

Source mapping also supports future SQL and Power BI analysis because validation status, source type and period coverage can be queried directly.

---

## Reported vs Calculated Values

A key data quality control is the distinction between:

| Type | Meaning |
|---|---|
| Reported | Figure is directly reported by the company or public source |
| Calculated | Figure is derived using a formula |
| Estimated | Figure is based on forecast assumptions |
| Pending | Figure is not yet validated |

This distinction is important because reported values and calculated values carry different validation risks.

For example:

- net income may be directly reported;
- ROE may be reported or calculated depending on the source;
- P/E and P/B require a selected market data date;
- forecast figures require explicit assumptions;
- valuation multiples require both financial data and market data;
- scenario outputs require documented assumptions and clear model logic.

The project should not mix reported data, calculated ratios and forecast estimates without clear labelling.

---

## Key Semantic Review Item

### Customer Deposits vs Customer Funds

The main semantic issue currently flagged is the distinction between:

- customer deposits;
- deposits and other customer resources;
- balance sheet customer resources;
- customer funds.

Some source values refer to **customer funds** or **customer resources**, not strictly customer deposits.

For dataset consistency, the project currently keeps a “Customer deposits” metric in some files, but relevant entries are flagged as **Needs Review** where the source definition may differ from the metric label.

This is important because incorrect classification could affect liquidity ratio interpretation, especially loan-to-deposit and related funding ratios.

This is a good example of human-in-the-loop review because the issue is not simply technical. It requires understanding banking terminology and the way the bank reports customer resources.

---

## Metric Definition Controls

The project should maintain clear definitions for the main banking metric categories.

### Profitability

Relevant metrics include:

- net income;
- ROE;
- ROA;
- net interest margin;
- EPS;
- book value per share.

Data quality risk:

- profitability ratios may be reported or calculated differently depending on denominator definitions;
- average equity and average assets may not be available in simplified datasets;
- EPS may be adjusted or unadjusted depending on the source.

### Efficiency

Relevant metrics include:

- operating income;
- operating costs;
- cost-to-income ratio;
- cost-to-income ratio excluding specific items.

Data quality risk:

- specific items may not be treated consistently across periods;
- cost-to-income may be reported by the bank or calculated internally;
- inflation, restructuring and one-off effects may distort comparisons.

### Asset Quality

Relevant metrics include:

- cost of risk;
- NPE ratio;
- NPE coverage ratio;
- restructured loans ratio;
- impairments and provisions.

Data quality risk:

- NPE and NPL terminology may differ;
- impairment definitions may vary by source;
- coverage ratios may depend on the treatment of collateral or provisions.

### Liquidity and Funding

Relevant metrics include:

- loan-to-deposit ratio;
- loan-to-balance-sheet-customer-resources ratio;
- LCR;
- NSFR;
- customer funds;
- deposits and other customer resources.

Data quality risk:

- deposits, customer resources and customer funds are not always identical;
- regulatory liquidity metrics should not be compared casually with commercial funding ratios;
- denominator definitions affect interpretation.

### Capital

Relevant metrics include:

- CET1 phased-in ratio;
- CET1 fully implemented ratio;
- total capital fully implemented ratio;
- equity.

Data quality risk:

- phased-in and fully implemented ratios must not be mixed;
- capital ratios depend on risk-weighted assets;
- capital movements may reflect distributions, regulatory adjustments and business growth.

---

## Current Validation Script Result

The project validation script currently identifies two known issues:

```text
1. market_data_template.csv: column 'category' has missing values
2. peer_comparison_template.csv: column 'business_type' has missing values
```

These warnings are acceptable at this stage because both files are templates for future project phases.

They do not affect the reviewed 2024A–2025A financial data cycle.

---

## Known Template-Stage Warnings

| File | Warning | Current Treatment |
|---|---|---|
| `market_data_template.csv` | Missing category values | Acceptable because valuation market data has not yet been activated |
| `peer_comparison_template.csv` | Missing business_type values | Acceptable because peer comparison has not yet been activated |

These warnings should be resolved when the project enters the valuation and peer comparison phase.

---

## Data Quality Checks Currently Applied

The current validation approach includes checks for:

- missing values in active data files;
- invalid validation status values;
- unexpected periods;
- source mapping completeness;
- basic CSV column consistency;
- template-stage missing fields;
- reviewed vs pending status;
- semantic review flags.

Future versions may include additional checks for:

- duplicate metric-period combinations;
- inconsistent units;
- unusual year-on-year movements;
- calculated ratio reconciliation;
- market data date validation;
- peer comparison consistency;
- forecast assumption completeness.

---

## 2024A–2025A Data Quality Observations

### Positive Observations

The reviewed 2024A–2025A cycle demonstrates:

- consistent period labelling;
- clear separation between actual and forecast periods;
- documented source mapping;
- reviewed validation status for core metrics;
- human review flags for semantic issues;
- clean Git-tracked workflow;
- successful validation script execution;
- analytical commentary linked to structured data;
- an initial bridge between financial modeling and data quality;
- a structure that can support SQL and Power BI outputs.

### Items Requiring Continued Review

The following areas require continued human review:

- customer deposits vs customer funds classification;
- NPE vs NPL terminology;
- ratio definition consistency;
- phased-in vs fully implemented capital ratios;
- annual report cross-checks for 2022A and 2023A;
- treatment of reexpressed 2024A comparative figures;
- future valuation date selection;
- peer group definition;
- dividend data treatment;
- calculation of valuation multiples;
- scenario assumption documentation.

---

## Human-in-the-Loop Review

Human-in-the-loop review is necessary because financial data quality is not only technical.

Some checks require professional judgment, especially when:

- terminology differs between sources;
- line items are reclassified;
- ratios are reported under different definitions;
- comparative figures are reexpressed;
- a metric label may not fully match the source definition;
- market data is date-sensitive;
- analytical conclusions could be overinterpreted.

This project intentionally avoids fully automated financial conclusions.

The role of the analyst is to review, challenge and document assumptions before using the data in reports, dashboards or valuation work.

In the context of AI finance or AI-assisted financial analysis, this is particularly relevant because an automated system could easily overinterpret incomplete, inconsistent or semantically ambiguous data.

---

## SQL Readiness

The structured files are suitable for SQL-based analysis.

Potential SQL data quality checks include:

- count reviewed vs pending metrics by period;
- identify missing values in active periods;
- list metrics flagged as Needs Review;
- compare 2024A and 2025A values;
- identify metrics without source documents;
- separate reported from calculated values;
- prepare Power BI extract tables;
- identify metrics available for trend analysis;
- identify periods with incomplete source coverage;
- identify categories with the highest number of pending values.

This supports the project’s positioning as both a financial modeling case study and a banking analytics project.

Example SQL-style analytical questions:

- Which financial metrics are reviewed for both 2024A and 2025A?
- Which metrics improved between 2024A and 2025A?
- Which metrics still require semantic review?
- Which source documents support each reviewed metric?
- Which categories are ready for Power BI reporting?
- Which data files still contain template-stage warnings?

---

## Power BI Readiness

The data quality layer can support a Power BI dashboard page showing:

- number of reviewed metrics;
- number of pending metrics;
- number of metrics requiring review;
- source coverage by period;
- validation status by file;
- reviewed data by category;
- template warnings;
- data quality checklist status.

Suggested visuals include:

- KPI cards;
- validation status bar charts;
- period coverage matrix;
- source coverage table;
- conditional formatting for Reviewed, Pending and Needs Review;
- data quality notes table;
- trend readiness indicators;
- data completeness matrix.

Power BI should clearly distinguish between:

- reviewed actual data;
- pending actual data;
- forecast data;
- template data;
- values requiring semantic review;
- calculated valuation metrics.

---

---

---

## Completed 2022A?2025A Data Quality Cycle

The project now includes a reviewed four-year historical data cycle covering **2022A, 2023A, 2024A and 2025A**.

This expands the case study from an initial three-year trend analysis into a broader banking analytics and financial data quality workflow.

The reviewed 2022A?2025A cycle includes:

- financial statement and balance sheet data;
- banking ratios;
- source mapping;
- extraction tracker updates;
- validation status tracking;
- data dictionary definitions;
- banking analytics commentary;
- human-in-the-loop review notes.

### Completed Files

| File | 2022A | 2023A | 2024A | 2025A | Notes |
|---|---:|---:|---:|---:|---|
| `data/financial_data.csv` | Completed | Completed | Completed | Completed | Core financial statement and balance sheet data |
| `data/banking_ratios.csv` | Completed | Completed | Completed | Completed | Main banking ratios and per-share indicators |
| `data/source_mapping.csv` | Completed | Completed | Completed | Completed | Source mapping and traceability |
| `data/extraction_tracker.csv` | Completed | Completed | Completed | Completed | Extraction status and review notes |
| `data/data_dictionary.md` | Updated | Updated | Updated | Updated | Metric definitions and interpretation notes |
| `reports/banking_analytics_report.md` | Updated | Updated | Updated | Updated | Analytical commentary updated |

### Current Data Quality Position

The 2022A, 2023A, 2024A and 2025A periods are now suitable for initial historical trend analysis.

This allows the project to analyse:

- profitability recovery after 2022A;
- net interest income development;
- operating efficiency;
- asset quality improvement;
- customer loans and customer resources evolution;
- liquidity and funding profile;
- capital strength;
- per-share indicators;
- data quality and source traceability.

### Items Requiring Continued Review

The following items remain visible as human-in-the-loop review points:

| Item | Status | Reason |
|---|---:|---|
| 2022A impairments and provisions | Needs Review | The value combines credit impairment and other impairments/provisions and should be reviewed against later-year definitions. |
| Customer deposits vs customer funds | Needs Review | Banking disclosures may use similar terms with different scopes. |
| Book value per share 2022A | Pending | Not yet added due to source consistency requirement. |
| Valuation ratios | Pending | Market data date has not yet been selected and documented. |
| Peer comparison | Pending | Peer group and comparison methodology are not yet defined. |
| Reexpressed comparative figures | Review Required | Later reports may reexpress prior-year figures for comparability. |
| Reported vs calculated ratios | Review Required | Calculated ratios may not fully match the bank's published methodology. |

### Validation Status

The validation script currently reports only template-stage warnings related to files that are not yet active for the core 2022A?2025A analysis:

1. `market_data_template.csv`: missing `category` values.
2. `peer_comparison_template.csv`: missing `business_type` values.

These warnings are acceptable at this stage because market data and peer comparison remain future phases.

### Data Quality Interpretation

The project now demonstrates a more complete public-source financial data workflow:

| Step | Status |
|---|---:|
| Public source identification | Completed |
| 2022A financial data extraction | Completed |
| 2022A banking ratios extraction | Completed |
| 2023A?2025A historical data cycle | Completed |
| Source mapping | Completed for 2022A?2025A |
| Extraction tracking | Completed for 2022A?2025A |
| Validation script execution | Active |
| Data dictionary definitions | Updated |
| Banking analytics reporting | Updated to 2022A?2025A |
| Human-in-the-loop review | Active |
| Market data | Pending |
| Peer comparison | Pending |
| Valuation | Pending |
| Forecast assumptions | Pending |
| Power BI dashboard build | Pending |

### Power BI Readiness

The project is now closer to Power BI readiness because the core historical dataset covers four annual periods.

The most suitable first Power BI visuals are:

| Dashboard Area | Suggested Visuals |
|---|---|
| Executive Overview | Net income, operating income, net interest income, total assets |
| Profitability | ROE, ROA, net interest margin, EPS |
| Efficiency | Cost-to-income ratio and adjusted cost-to-income ratio |
| Asset Quality | Cost of risk, NPE ratio, NPE coverage ratio, restructured loans ratio |
| Liquidity and Funding | Customer loans, customer funds, loan-to-deposit ratio, LCR, NSFR |
| Capital | CET1 phased-in, CET1 fully implemented, total capital fully implemented |
| Data Quality | Reviewed vs Needs Review vs Pending items |

### Human-in-the-Loop Control

The project should not treat the dataset as automatically final.

Before final reporting, the following manual checks remain important:

- confirm source terminology for customer deposits, customer funds and customer resources;
- confirm whether 2022A impairments and provisions are directly comparable with later-year figures;
- confirm whether any prior-year figures are reexpressed in later disclosures;
- confirm whether ratios are reported or calculated;
- confirm valuation date before adding market multiples;
- confirm peer group methodology before adding peer comparison.

This reinforces the project as a financial data quality and banking analytics case study, not only a financial modelling exercise.


## Completed 2023A?2025A Data Quality Cycle

The project now includes a reviewed 2023A?2025A historical data cycle across the main analytical files.

This represents an important improvement because the case study now moves from a two-year comparison to a three-year historical trend.

The reviewed 2023A?2025A cycle includes:

- financial statement and balance sheet data;
- banking ratios;
- source mapping;
- extraction tracker updates;
- validation status tracking;
- human-in-the-loop review notes;
- banking analytics commentary.

### Completed Files

| File | 2023A | 2024A | 2025A | Notes |
|---|---:|---:|---:|---|
| `data/financial_data.csv` | Completed | Completed | Completed | Core financial statement and balance sheet data |
| `data/banking_ratios.csv` | Completed | Completed | Completed | Banking ratios and per-share indicators |
| `data/source_mapping.csv` | Completed | Completed | Completed | Source mapping and traceability |
| `data/extraction_tracker.csv` | Completed | Completed | Completed | Extraction status and review notes |
| `reports/banking_analytics_report.md` | Completed | Completed | Completed | Analytical commentary updated |

### Current Data Quality Position

The 2023A, 2024A and 2025A periods are now suitable for initial historical trend analysis.

The following areas remain subject to continued review:

- customer deposits vs customer funds terminology;
- reexpressed comparative figures;
- reported vs calculated ratio definitions;
- NPE vs NPL terminology;
- phased-in vs fully implemented capital ratios;
- market data date selection;
- valuation multiples;
- peer comparison assumptions.

### Important Note on 2023A and 2024A

Some 2023A and 2024A figures are based on official public reexpressed comparative figures.

This should remain clearly documented because reexpressed figures may differ from originally published figures due to changes in reporting presentation, methodology or comparability adjustments.

This is not a weakness of the project. It is a realistic financial data quality issue and should remain visible in the documentation.

### Validation Status

The validation script currently reports only template-stage warnings related to files that are not yet active for the core 2023A?2025A analysis:

1. `market_data_template.csv`: missing `category` values.
2. `peer_comparison_template.csv`: missing `business_type` values.

These warnings are acceptable at this stage because market data and peer comparison are future phases.

### Data Quality Interpretation

The project now demonstrates a complete initial workflow:

| Step | Status |
|---|---:|
| Public source identification | Completed |
| Data extraction | Completed for 2023A?2025A |
| CSV structuring | Completed |
| Banking ratio dataset | Completed for 2023A?2025A |
| Source mapping | Completed |
| Extraction tracking | Completed |
| Validation script execution | Active |
| Analytical reporting | Updated |
| Human-in-the-loop review | Active |
| 2022A extraction | Pending |
| Market data | Pending |
| Peer comparison | Pending |
| Valuation | Pending |

This strengthens the project for Financial Data Quality, Banking Analytics, Reporting Analyst, Financial Research and AI Finance Evaluation positioning.


## Current Data Quality Status Summary

| Area | Status |
|---|---:|
| 2025A financial data | Completed |
| 2024A financial data | Completed |
| 2025A banking ratios | Completed |
| 2024A banking ratios | Completed |
| 2025A source mapping | Completed |
| 2024A source mapping | Completed |
| 2025A extraction tracker | Completed |
| 2024A extraction tracker | Completed |
| Validation script | Active |
| Known validation warnings | Template-stage only |
| 2023A extraction | Pending |
| 2022A extraction | Pending |
| Market data | Pending |
| Peer comparison | Pending |
| Forecast assumptions | Pending |
| Valuation multiples | Pending |

---

## Data Quality Risk Register

| Risk | Description | Mitigation |
|---|---|---|
| Source misclassification | A value may be assigned to an incorrect metric label | Use source mapping and review notes |
| Semantic inconsistency | Customer funds, deposits and resources may be confused | Flag as Needs Review |
| Ratio definition mismatch | Ratios may differ depending on reported or calculated basis | Track reported/calculated status |
| Reexpressed figures | 2024A figures may be comparative/reexpressed figures from 2025 source | Document notes clearly |
| Missing historical data | 2022A and 2023A are not yet complete | Keep Pending until validated |
| Overinterpretation | Single-year movement may be treated as a trend | Require multi-year review |
| Valuation date sensitivity | Market multiples depend on selected share price date | Delay valuation until date is documented |
| Template warnings | Future template files contain blanks | Keep warnings documented until activation |
| Forecast assumption risk | Forecasts may be interpreted as predictions | Label all forecasts as illustrative |
| Peer comparison risk | Inappropriate peer group may distort interpretation | Define peer criteria before comparison |

---

## Data Quality Control Checklist

| Control | Current Status |
|---|---:|
| Public source used | Completed for 2024A and 2025A initial scope |
| Source mapping created | Completed for 2024A and 2025A initial scope |
| Validation status assigned | Completed |
| Reported vs calculated distinction | Active |
| Forecast vs actual separation | Active |
| Semantic review flags | Active |
| Git version control used | Active |
| Validation script executed | Active |
| Known warnings documented | Active |
| Human-in-the-loop review notes included | Active |
| SQL readiness considered | Active |
| Power BI readiness considered | Active |
| 2022A and 2023A annual reports validated | Pending |
| Market data date selected | Pending |
| Valuation multiples calculated | Pending |

---

## Recommended Validation Enhancements

Future improvements to `data/validation_checks.py` may include:

1. Duplicate metric-period checks.
2. Unit consistency checks.
3. Validation status allowed-value checks.
4. Missing source document checks for reviewed values.
5. Missing source section checks for reviewed values.
6. Unexpected period checks.
7. Reported vs calculated consistency checks.
8. Ratio sanity checks.
9. Year-on-year movement flags.
10. Forecast assumption completeness checks.
11. Market data date checks.
12. Peer group completeness checks.

These enhancements would make the project stronger for financial data quality and data validation roles.

---

## Next Data Quality Priorities

Recommended next steps:

1. Extract 2023A official financial data.
2. Extract 2022A official financial data.
3. Add 2023A and 2022A banking ratios.
4. Expand source mapping for 2023A and 2022A.
5. Cross-check 2024A reexpressed values with the 2024 annual report where appropriate.
6. Resolve customer deposits vs customer funds terminology.
7. Add duplicate metric-period validation.
8. Add unit consistency validation.
9. Add calculated ratio reconciliation.
10. Prepare a Power BI data quality dashboard.
11. Activate market data only after choosing a specific valuation date.
12. Activate peer comparison only after defining a clear peer group.

---

## Professional Relevance

This data quality report demonstrates skills relevant to:

- Financial Data Quality Analyst;
- Data Validation Analyst;
- Banking Analytics;
- Reporting Analyst;
- Financial Research;
- Investment Research Support;
- AI Finance Evaluation;
- AI Product Testing in Finance;
- Risk and Controls;
- SQL-based financial analysis;
- Power BI reporting.

The project demonstrates the ability to:

- structure financial data;
- validate public-source information;
- document data lineage;
- track review status;
- identify semantic data issues;
- prepare datasets for analytics;
- apply professional judgment to financial information;
- avoid unsupported conclusions.

This is particularly relevant for roles that require a bridge between finance, data quality, reporting and responsible AI-assisted analysis.

---

## Portfolio Positioning

This report supports the broader portfolio narrative:

```text
Banking experience
+ financial data quality
+ public-source validation
+ banking analytics
+ SQL readiness
+ Power BI readiness
+ human-in-the-loop review
```

The report can be referenced in CV or LinkedIn as evidence of practical work in:

- financial data validation;
- source mapping;
- banking metric interpretation;
- data quality controls;
- structured analytics workflows;
- public-data financial research.

---

## Disclaimer

This report is for educational, analytical and professional portfolio purposes only.

It uses only publicly available information and manually structured project datasets.

It does not use confidential information, internal banking data, client data or proprietary information.

It does not provide investment advice, financial advice, valuation advice, a price target or a buy/sell/hold recommendation.

All figures should be independently verified before any professional, academic or investment-related use.

The analysis is descriptive, illustrative and subject to further validation.