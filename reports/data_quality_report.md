# Financial Data Quality Report

This report documents the financial data quality approach used in the **Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank** project.

The project uses only publicly available information and is designed for educational, portfolio and professional development purposes.

It does not constitute investment advice.

---

## 1. Report Purpose

The purpose of this report is to document the quality, completeness, reliability and validation status of the financial data used in the project.

The report supports the project's financial data quality layer by reviewing:

- source validation;
- missing values;
- required fields;
- period consistency;
- unit consistency;
- duplicate records;
- reported vs calculated classification;
- actual vs forecast classification;
- public-source traceability;
- unusual value detection;
- basic reconciliation checks;
- human-in-the-loop review status.

This report should be updated as the dataset is completed and validated.

---

## 2. Why Data Quality Matters

Financial analysis depends on reliable data.

In banking analytics, small data issues can lead to incorrect conclusions about profitability, capital, asset quality or efficiency.

For example:

- a value in EUR may be confused with EUR million;
- a reported figure may be mixed with a calculated figure;
- an annual value may be compared with an interim value;
- a forecast may be incorrectly presented as historical actual data;
- a ratio may be calculated using inconsistent denominators;
- a source may be missing or incomplete.

For this reason, data quality is treated as a core part of the project, not as an afterthought.

---

## 3. Data Sources Reviewed

The project uses only public sources.

Preferred source hierarchy:

1. Millennium bcp annual reports
2. Millennium bcp investor presentations
3. Millennium bcp official investor relations materials
4. Euronext market data
5. CMVM public disclosures
6. Banco de Portugal public information
7. ECB and EBA public materials
8. Other reputable public financial sources, when needed

Official company reports and investor materials are preferred for historical financial data.

Market data should always include the market data date because prices and valuation multiples change over time.

---

## 4. Main Data Files Reviewed

The data quality review covers the following files:

| File | Purpose |
|---|---|
| `data/financial_data.csv` | Main structured financial dataset |
| `data/historical_financials.csv` | Historical financial data |
| `data/banking_ratios.csv` | Banking ratio dataset |
| `data/source_mapping.csv` | Source traceability and validation status |
| `data/extraction_tracker.csv` | Extraction tracking from public reports |
| `data/forecast_assumptions.csv` | Forecast assumptions |
| `data/scenario_analysis.csv` | Scenario outputs |
| `data/market_data_template.csv` | Market data inputs |
| `data/peer_comparison_template.csv` | Peer comparison inputs |

---

## 5. Period Convention Review

The project uses the following main periods:

    2022A | 2023A | 2024A | 2025A | 2026E | 2027E

Where:

| Period | Meaning | Data Type |
|---|---|---|
| `2022A` | Published historical data | Actual |
| `2023A` | Published historical data | Actual |
| `2024A` | Published historical data | Actual |
| `2025A` | Published historical data | Actual |
| `2026E` | Forecast / estimate | Forecast |
| `2027E` | Forecast / estimate | Forecast |

Validation requirement:

    Historical actual data and forecast estimates must never be mixed without clear labelling.

---

## 6. Required Field Checks

Each dataset should include required fields that make the data understandable and traceable.

Recommended required fields include:

- metric or data item;
- category;
- period;
- value;
- unit;
- source document;
- source type;
- reported or calculated classification;
- actual or forecast classification;
- validation status;
- notes.

If a required field is missing, the item should be classified as:

    Needs Review

or:

    Pending

---

## 7. Source Validation Checks

Each key figure should be mapped to a public source.

Source validation checks include:

- source document is identified;
- source type is identified;
- source section, table or page is recorded where possible;
- value can be traced back to the public document;
- source date or reporting period is clear;
- source is appropriate for the metric;
- secondary sources are not used when official sources are available.

Suggested validation statuses:

| Status | Meaning |
|---|---|
| `Pending` | Data still needs review |
| `Reviewed` | Data has been manually reviewed |
| `Validated` | Data has been traced to a public source |
| `Needs Review` | Data has an issue or requires manual checking |
| `Not Available` | Data is not available from public sources |
| `Calculated` | Data is calculated from other validated figures |

---

## 8. Missing Values Review

Missing values should be reviewed before analysis.

Potential causes of missing values:

- the metric is not reported;
- the source has not been reviewed yet;
- the metric is not applicable;
- the value needs to be calculated;
- the dataset is still in preparation.

Missing values are acceptable during the data preparation phase, but they should be clearly identified before analysis or dashboarding.

Recommended action:

    Missing values should not be silently ignored.

---

## 9. Unit Consistency Review

Banking data may be reported in different units.

Examples:

- EUR;
- EUR million;
- EUR billion;
- percentage;
- basis points;
- number of shares;
- ratio.

Validation checks:

- confirm the unit for each value;
- avoid mixing EUR and EUR million;
- avoid mixing percentage and decimal format;
- document whether ratios are shown as percentages;
- confirm market data units separately.

Example issue:

    1,000 EUR million is not the same as 1,000 EUR.

This type of error can materially distort analysis.

---

## 10. Reported vs Calculated Figures

The project should distinguish between:

| Classification | Meaning |
|---|---|
| `Reported` | Figure is directly disclosed in a public source |
| `Calculated` | Figure is calculated from other figures |
| `Estimated` | Figure is based on a forecast or assumption |

Examples:

- Net income may be reported.
- ROE may be reported or calculated.
- Price-to-book may be calculated using market data and book value.
- 2026E net income is an estimate.

This distinction is important for transparency and professional credibility.

---

## 11. Actual vs Forecast Classification

The project must clearly distinguish actual historical data from forecast estimates.

Actual periods:

    2022A | 2023A | 2024A | 2025A

Forecast periods:

    2026E | 2027E

Validation rule:

    Forecast values should never be presented as published historical results.

Forecast values should include documented assumptions and scenario classification.

---

## 12. Duplicate Checks

Duplicate records can distort analysis and dashboard outputs.

Duplicate checks should review whether the same metric appears multiple times for the same:

- bank;
- period;
- metric;
- category;
- scenario;
- source.

If duplicates are intentional, they should be explained in the notes field.

If duplicates are accidental, they should be corrected before analysis.

---

## 13. Unusual Value Checks

Unusual values should be flagged for review.

Examples of unusual values:

- negative values where not expected;
- very large year-on-year changes;
- ratios outside reasonable banking ranges;
- missing units;
- percentages entered as whole numbers when decimals were expected;
- market data without a date;
- forecast values that differ materially from historical trends without explanation.

Unusual values are not automatically wrong, but they require review and explanation.

---

## 14. Basic Reconciliation Checks

Simple reconciliation checks help identify potential errors.

Examples:

- operating income should be consistent with its components;
- cost-to-income should be consistent with operating costs and operating income;
- ROE should be consistent with net income and equity;
- ROA should be consistent with net income and total assets;
- loan-to-deposit ratio should be consistent with customer loans and customer deposits;
- price-to-book should be consistent with market capitalisation and book value;
- price-to-earnings should be consistent with market capitalisation and net income.

These checks are simplified and educational, but they help improve analytical reliability.

---

## 15. SQL Data Quality Checks

The SQL layer can support data quality review by identifying:

- missing values;
- pending validation items;
- incomplete source references;
- duplicate records;
- actual vs forecast classification;
- reported vs calculated classification;
- validation status counts.

Example analytical use:

    Count how many data points are Validated, Pending or Needs Review.

This type of query can feed the Power BI Data Quality page.

---

## 16. Power BI Data Quality Page

The Power BI dashboard should include a dedicated Data Quality page.

Suggested visuals:

- validation status count;
- missing values count;
- source coverage table;
- reported vs calculated classification;
- actual vs forecast classification;
- data quality scorecard;
- items requiring review table.

This helps show that the project values both analysis and data reliability.

---

## 17. Human-in-the-Loop Review

Human review is required before publishing analytical conclusions.

The review should check:

- source traceability;
- values copied correctly;
- units are correct;
- ratios are correctly interpreted;
- assumptions are documented;
- forecasts are clearly labelled;
- scenario outputs are reasonable;
- commentary avoids investment advice;
- no personal, internal or confidential information is included.

This is especially important if AI-assisted drafting or analysis support is used.

---

## 18. Current Data Quality Status

Current status:

    Initial 2025A data extraction completed
    Initial source mapping completed
    Initial extraction tracker updated
    Initial banking ratios updated
    Python validation check executed
    Historical trend completion pending
    Market data pending
    Peer comparison pending
    Forecast assumptions pending
    Scenario analysis pending

Most values for 2022A, 2023A and 2024A remain marked as:

    Pending

until official public-source extraction and review are completed.

### Initial 2025A Data Quality Status

The project now includes an initial 2025A public-data extraction for Millennium bcp.

The 2025A data has been added to the following files:

- `data/financial_data.csv`;
- `data/banking_ratios.csv`;
- `data/extraction_tracker.csv`;
- `data/source_mapping.csv`.

The initial 2025A extraction covers:

- profitability metrics;
- efficiency metrics;
- asset quality metrics;
- balance sheet metrics;
- capital ratios;
- liquidity ratios;
- selected per-share indicators.

The current validation status for the initial 2025A data is:

    Reviewed

This means that the values have been added from public sources and checked at a first review level.

Before final publication, the data should still be cross-checked against:

- the official annual report;
- official investor presentations;
- official key indicators pages;
- source mapping records;
- extraction tracker records.

The current Python validation check has been executed. The validation script completed successfully and identified only template-related issues in files that are not yet fully populated:

- `data/market_data_template.csv`;
- `data/peer_comparison_template.csv`.

These issues are acceptable at the current stage because market data and peer comparison are planned for a later phase.

The key 2025A files used for the initial banking analytics analysis did not generate blocking validation issues.

Current interpretation:

    Initial 2025A data structure is usable for preliminary analysis.
    Final conclusions should wait until 2022A, 2023A and 2024A are extracted and validated.
    Market data and peer comparison remain pending.
    Forecast assumptions remain pending.

---

## 19. Initial 2025A Validation Summary

The initial 2025A data extraction includes the following types of values:

| Area | Status |
|---|---|
| Profitability metrics | Reviewed |
| Efficiency metrics | Reviewed |
| Asset quality metrics | Reviewed |
| Balance sheet metrics | Reviewed |
| Capital ratios | Reviewed |
| Liquidity ratios | Reviewed |
| Per-share indicators | Reviewed |
| Market data | Pending |
| Peer comparison | Pending |
| Forecast assumptions | Pending |
| Scenario outputs | Pending |

The 2025A values are currently suitable for preliminary banking analytics commentary, but not yet for final investment-style conclusions.

The main reason is that a single year does not provide enough historical context.

The next data quality priority is to complete the historical series for:

    2022A | 2023A | 2024A

Once these periods are completed, the project can move from a 2025A snapshot to a proper historical trend analysis.

---

## 20. Current Validation Script Result

The validation script has been executed using:

    python data/validation_checks.py

The script completed successfully.

The current warnings relate to templates that are not yet fully populated:

- `data/market_data_template.csv`;
- `data/peer_comparison_template.csv`.

These warnings do not block the current project phase because those files belong to later stages of the roadmap.

Current interpretation:

    No blocking validation issue was identified for the initial 2025A banking analytics dataset.

Further validation will be required after adding 2022A, 2023A and 2024A data.

---

## 21. Data Quality Checklist

Before finalising the project, check:

- all key metrics have a source;
- all values have a unit;
- all periods are correctly labelled;
- actual and forecast data are separated;
- reported and calculated figures are classified;
- missing values are explained;
- unusual values are reviewed;
- ratios are formula-checked;
- assumptions are documented;
- SQL queries run correctly;
- Power BI visuals use the correct fields;
- commentary is neutral and factual;
- no investment recommendation is included.

---

## 22. Next Data Quality Priorities

The next data quality priorities are:

1. Complete 2024A extraction.
2. Complete 2023A extraction.
3. Complete 2022A extraction.
4. Cross-check 2025A values against the annual report.
5. Confirm source references and pages or sections.
6. Review labels such as customer deposits versus customer funds.
7. Validate reported versus calculated ratio classifications.
8. Select a market data date for valuation ratios.
9. Complete market data inputs.
10. Complete peer comparison inputs.
11. Re-run validation checks after each major update.

The most important next step is to move from a single-year 2025A snapshot to a multi-year historical dataset.

---

## 23. Professional Relevance

This data quality report supports the project’s relevance for roles such as:

- Financial Data Quality Analyst;
- Data Validation Analyst;
- Financial Data Analyst;
- Reporting Analyst – Banking;
- Banking Analytics Analyst;
- AI Finance Evaluator;
- Risk Operations Analyst;
- Financial Operations Analyst;
- Business Operations Analyst;
- Program Operations Analyst.

It demonstrates the ability to treat financial analysis as a controlled, documented and auditable workflow.

---

## 24. Disclaimer

This report is part of an educational portfolio project.

It uses only publicly available information.

It does not contain personal data, client data, employee data, internal banking information or confidential information.

It does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.

All analysis, forecasts, scenarios and data quality checks are illustrative and should be interpreted with caution.