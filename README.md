# Millennium bcp - Banking Analytics Case Study

Public financial disclosures transformed into a traceable dataset, Python calculations, SQL analysis and Power BI visuals.

**Current analytical revision: 29 September 2026.** Annual history: 2022-2025. Latest operating period: H1 2026, released 29 July 2026. Information cut-off: 28 September 2026.

## Start here

| Deliverable | Link |
|---|---|
| Complete English case study - 40 pages | [Current PDF](reports/bcp_complete_case_study_en_2026-09-29.pdf) |
| Estudo completo em português - 38 páginas | [PDF atual](reports/bcp_complete_case_study_pt_2026-09-29.pdf) |
| Guia dos 18 rácios em português - revisão atual | [PDF](reports/bcp_analysis_and_ratios_guide_pt_2026-09-29.pdf) |
| Refreshed Power BI v6 | [PBIX](powerbi/millennium_bcp_banking_dashboard_v6_revised.pbix) |
| Native v6 dashboard export - 10 pages | [PDF](reports/millennium_bcp_banking_dashboard_v6_revised.pdf) |
| Power BI setup and verification | [Instructions](powerbi/V6_README.md) · [Checks](powerbi/v6_validation.json) |
| Revised scenario model and input snapshots | [Calculation package](revisions/2026-09-29) |
| Current assumptions, sensitivity and limitations | [Methodology](revisions/2026-09-29/METHODOLOGY.md) |
| Revised scenario outcomes | [CSV](revisions/2026-09-29/data/forecast_financials.csv) |
| Profit-conversion sensitivity | [CSV](revisions/2026-09-29/data/conversion_sensitivity.csv) |
| Separate retention sensitivity | [CSV](revisions/2026-09-29/data/retention_sensitivity.csv) |
| Core historical source register - 182 observations | [CSV](data/source_mapping.csv) |
| Supplementary earnings/coverage source records | [CSV](revisions/2026-09-29/data/supplemental_source_register.csv) |
| Run the current model | [Instructions](RUN_PROJECT.md) |

## What the analysis shows

H1 2026 Group net income was EUR 565.8m. Operating profit before impairments rose EUR 65.7m; lower other impairments and provisions contributed EUR 92.1m, while higher credit impairments, taxes and non-controlling interests offset part of the gains. The complete bridge reconciles the EUR 63.5m net income increase.

From December 2025 to June 2026, NPE stock declined from EUR 1,503m to EUR 1,442m and total credit allowances increased from EUR 1,366m to EUR 1,402m. Both movements contributed to coverage increasing from 90.9% to 97.2%. Sources, scope and rounding are documented in the report.

## What changed in the current model

- Six operating drivers, three scenarios and three years: **54 explicit inputs**.
- A common **48% illustrative profit-conversion reference**, with sensitivities at 46%, 48%, 50% and the prior 50.2621% calibration. These are chosen sensitivities, not statistical forecasts.
- Base net income: **EUR 1,090.6m in 2026E**, **EUR 1,061.1m in 2027E** and **EUR 1,074.6m in 2028E**. Actual H1 2026 is held fixed.
- Retention is separated from operating performance and tested at 0%, 10% and 20%.
- Direct CET1 assumptions and incomparable projected ROE/ROA have been removed. No regulatory-capital forecast is claimed.
- Base credit risk of 40 bp is explicitly justified as a cautious normalisation assumption near adjusted FY2024 39 bp; the projected net-loan denominator remains a disclosed proxy.

81 financial cells are independently recomputed; 36 conversion sensitivities and 27 retention sensitivities are cross-checked. [Current checks](revisions/2026-09-29/checks.json).

## Historical Power BI project and previous edition

The **current Power BI v6 is refreshed** to the revised scenario model. Its 11 CSV sources (852 imported rows across analytical and supporting tables) were compared with the saved, reopened model. Both slicers were tested and all ten native PDF pages were visually reviewed. Use `powerbi/v6-data` for v6 refreshes; see the setup instructions above.

The complete analytical PDFs retain nine original historical/H1 2026 Power BI pages and revised report scenario charts; the separate ten-page v6 export contains the newly refreshed native visuals. The archived v5 PBIX and root-level `data/forecast_*` / `data/scenario_analysis.csv` remain **legacy v5 outputs**, superseded by `revisions/2026-09-29/data` for scenario interpretation.

| Previous-edition resource | Link |
|---|---|
| Power BI v5 - historical report with superseded scenario page | [PBIX](powerbi/millennium_bcp_banking_dashboard_v5_validated.pbix) |
| Original ten-page v5 dashboard export | [PDF](reports/millennium_bcp_banking_dashboard_v5_validated.pdf) |
| Previous English analytical report | [PDF](reports/ricardo_serodio_bcp_banking_analytics_case_study_en.pdf) |
| Relatório português - edição anterior de 28 setembro | [PDF](reports/ricardo_serodio_bcp_banking_analytics_case_study_pt.pdf) |
| Historical validation appendix | [PDF](reports/bcp_validation_appendix_2026-09-28.pdf) |

The historical v5 SQL/model checks remain available in [validation_results.json](docs/validation_results.json) and [v5_validation.json](powerbi/v5_validation.json). They are not evidence of a refreshed current-scenario PBIX.

## Evidence and scope

182 unique historical values comprise 176 source-verified values and six recalculated totals. The supplementary 19-record register includes overlaps and must not be added to 182 as unique observations. Annual history retains documented source vintages; half-year observations use the same H1 2026 release.

Source verification and calculation checks do not constitute an independent audit, certification or predictive validation. Market valuation, peer comparison and full regulatory-capital modelling are outside scope.

Python / pandas · SQLite / SQL · Power BI / Power Query · source reconciliation · financial analysis.

Independent educational portfolio project by **Ricardo Serôdio**. Not affiliated with Millennium bcp. Not investment advice.
