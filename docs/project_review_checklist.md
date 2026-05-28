# Project Review Checklist

## Purpose

This checklist supports the final review of the Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank project before publication.

The purpose is to ensure that the project is accurate, transparent, well-documented, recruiter-friendly and clearly positioned as an educational portfolio case study.

## 1. Historical Data Review

- [ ] Confirm that all historical financial figures are sourced from public information.
- [ ] Confirm that 2022A, 2023A, 2024A and 2025A figures are correctly structured.
- [ ] Confirm that validation statuses are accurate.
- [ ] Review all items marked as `Pending`.
- [ ] Confirm that source documents are clearly referenced.
- [ ] Confirm that no confidential, internal or private banking information is used.

## 2. Banking Ratio Review

- [ ] Confirm that reported 2025A ratios are used where available.
- [ ] Confirm that banking ratio categories are consistent.
- [ ] Review profitability ratios.
- [ ] Review efficiency ratios.
- [ ] Review asset quality ratios.
- [ ] Review liquidity ratios.
- [ ] Review capital ratios.
- [ ] Review valuation ratios marked as pending.
- [ ] Confirm that simplified calculated ratios are not presented as official reported ratios.

## 3. Forecast Assumptions Review

- [ ] Review Base scenario assumptions.
- [ ] Review Optimistic scenario assumptions.
- [ ] Review Conservative scenario assumptions.
- [ ] Confirm that all forecast assumptions are clearly marked as educational estimates.
- [ ] Confirm that assumptions are not presented as official projections.
- [ ] Confirm that `Other operating income` is used appropriately where `Fees and commissions` is pending.
- [ ] Confirm that all assumptions have rationale and source/basis notes.

## 4. Forecast Financials Review

- [ ] Review forecast net interest income.
- [ ] Review forecast other operating income.
- [ ] Review forecast operating income.
- [ ] Review forecast operating costs.
- [ ] Review pre-provision operating profit.
- [ ] Review impairments and provisions.
- [ ] Review net income.
- [ ] Review customer loans.
- [ ] Review customer deposits.
- [ ] Review total assets.
- [ ] Review equity.
- [ ] Confirm that all forecast values are marked as `To Review`.

## 5. Forecast Ratios Review

- [ ] Confirm that 2025A ratios use reported values from `banking_ratios.csv`.
- [ ] Review forecast ROE.
- [ ] Review forecast ROA.
- [ ] Review forecast cost-to-income ratio.
- [ ] Review forecast loan-to-deposit ratio.
- [ ] Review forecast cost of risk.
- [ ] Review CET1 ratio assumptions.
- [ ] Confirm that forecast ratios are not presented as official bank guidance.
- [ ] Confirm that the loan-to-deposit ratio methodology is clearly explained.

## 6. Scenario Analysis Review

- [ ] Review Base case scenario outputs.
- [ ] Review Optimistic case scenario outputs.
- [ ] Review Conservative case scenario outputs.
- [ ] Review variance vs Base calculations.
- [ ] Review scenario interpretation text.
- [ ] Review risk level labels.
- [ ] Confirm that scenario analysis is clearly marked as educational and scenario-based.

## 7. Data Quality Review

- [ ] Run `python data/validation_checks.py`.
- [ ] Review all validation warnings.
- [ ] Confirm that expected template warnings are documented.
- [ ] Review missing values.
- [ ] Review pending source mappings.
- [ ] Review extraction tracker status.
- [ ] Confirm that data quality limitations are visible to readers.

## 8. SQL Layer Review

- [ ] Review `sql/create_tables.sql`.
- [ ] Review `sql/banking_ratio_queries.sql`.
- [ ] Review `sql/data_quality_queries.sql`.
- [ ] Review `sql/forecast_queries.sql`.
- [ ] Review `sql/README.md`.
- [ ] Confirm that SQL scripts are aligned with the CSV structure.
- [ ] Confirm that SQL queries are clearly educational and analytical.

## 9. Power BI Review

- [ ] Review Executive Overview page.
- [ ] Review Liquidity & Funding page.
- [ ] Review Asset Quality page.
- [ ] Review Profitability page.
- [ ] Review Efficiency page.
- [ ] Review Capital page.
- [ ] Review Data Quality page.
- [ ] Confirm that visuals are clear and recruiter-friendly.
- [ ] Confirm that any forecast visuals are clearly labelled as estimates if added later.
- [ ] Confirm that no visual implies investment advice or official projections.

## 10. Documentation Review

- [ ] Review `README.md`.
- [ ] Review `docs/forecast_methodology.md`.
- [ ] Review this project review checklist.
- [ ] Confirm that project scope is clear.
- [ ] Confirm that limitations are clearly stated.
- [ ] Confirm that disclaimers are visible.
- [ ] Confirm that the AI-assisted, human-reviewed workflow is explained.

## 11. Public Positioning Review

- [ ] Confirm that the project description is recruiter-friendly.
- [ ] Confirm that the project highlights banking analytics.
- [ ] Confirm that the project highlights financial data quality.
- [ ] Confirm that the project highlights Power BI.
- [ ] Confirm that the project highlights SQL.
- [ ] Confirm that the project highlights financial modelling.
- [ ] Confirm that the project does not overclaim forecasting accuracy.
- [ ] Confirm that the project does not imply investment recommendation.

## 12. GitHub Review

- [ ] Confirm that all relevant files are committed.
- [ ] Confirm that the repository has a clean structure.
- [ ] Confirm that generated files are useful and not excessive.
- [ ] Confirm that no private, confidential or sensitive files are committed.
- [ ] Confirm that `.gitignore` is appropriate.
- [ ] Confirm that commit history is clean enough for a public portfolio project.

## 13. Final Publication Review

Before publishing or promoting the project publicly:

- [ ] Review all forecast assumptions manually.
- [ ] Review all generated forecast outputs manually.
- [ ] Review all Power BI pages manually.
- [ ] Review all SQL files manually.
- [ ] Review all documentation manually.
- [ ] Review README.
- [ ] Review website description.
- [ ] Review LinkedIn post.
- [ ] Review CV bullet.
- [ ] Confirm all disclaimers are present.
- [ ] Confirm that the project is clearly educational and portfolio-based.

## Final Sign-Off

- [ ] Historical data reviewed.
- [ ] Forecast methodology reviewed.
- [ ] Scenario analysis reviewed.
- [ ] SQL layer reviewed.
- [ ] Power BI dashboard reviewed.
- [ ] Documentation reviewed.
- [ ] Public wording reviewed.
- [ ] Final human review completed.

## Disclaimer

This checklist is part of an educational and portfolio-oriented workflow.

The project does not constitute financial advice, investment advice, valuation advice, credit advice, legal advice or a recommendation to buy, sell or hold any financial instrument.

All forecast figures are scenario-based estimates and should be interpreted as analytical modelling outputs, not as official projections.
