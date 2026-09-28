# Millennium bcp - Banking Analytics Case Study

Public financial disclosures transformed into a reproducible banking-performance dataset, scenario model and Power BI report.

**Updated 28 September 2026.** Annual history: 2022-2025. Latest results: **H1 2026**, released **29 July 2026**, compared with H1 2025 on the same source basis.

## Start here

| Deliverable | Link |
|---|---|
| Analytical report - English | [PDF](reports/ricardo_serodio_bcp_banking_analytics_case_study_en.pdf) |
| Relatório analítico - Português | [PDF](reports/ricardo_serodio_bcp_banking_analytics_case_study_pt.pdf) |
| Full validation appendix - 182 observations | [PDF](reports/bcp_validation_appendix_2026-09-28.pdf) |
| Power BI v5 - annual history and H1 2026 update | [PBIX](powerbi/millennium_bcp_banking_dashboard_v5_validated.pbix) |
| Dashboard preview | [PDF](reports/millennium_bcp_banking_dashboard_v5_validated.pdf) |
| Machine-readable source register | [CSV](data/source_mapping.csv) |
| Reproduce the model | [Run instructions](RUN_PROJECT.md) |
| Fundamento, conclusões e limites (PT) | [Guia de revisão](docs/fundamento_e_conclusoes.md) |

## What the analysis shows

H1 2026 group net income was EUR 565.8m, with reported year-on-year growth of 12.7%. NPE decreased to 2.2% and coverage increased to 97.2%. Fully implemented CET1 was 15.1%, retaining the source qualification as an estimate including 10% of unaudited interim earnings. Sources and precise definitions are in the reports and appendix.

The annual series preserves documented source vintages: 2022 from FY2022, 2023 from FY2024 comparatives, and 2024/25 from FY2025. Per-share values use annual reports. H1 2025 and H1 2026 both come from the H1 2026 release. Annual flows and half-year flows are stored separately.

## Evidence and reproducibility

- 182 unique historical values: 176 reported values matched to source pages and six arithmetic totals.
- 72 documented scenario parameters; 162 forecast cells recomputed; 126 scenario comparisons reconciled.
- Ten SQLite tables; 36 SQL statements passed. See [validation results](docs/validation_results.json).
- Forecasts distinguish reported H1 results from estimated H2 results. Assumptions and proxy-ratio limitations are documented in the [methodology](docs/forecast_methodology.md).
- Prior empty planning rows are preserved in `data/archive/`; they are excluded from the active model.

`Source verified` means a value was checked against the specified public source; `Recalculated` means arithmetic was checked; `Model checked` describes scenario calculations; `Scenario assumption` labels illustrative inputs. This is an AI-assisted portfolio case study, not an independent audit of the bank or a claim of external human certification.

## Tools and scope

Python / pandas · SQLite / SQL · Power BI / Power Query · source tracing · financial analysis · Portuguese and English reporting.

Market valuation and peer comparison are optional future extensions and are outside the active model. This educational project is not affiliated with Millennium bcp and does not provide investment advice.

Prepared by Ricardo Serodio. [Official source register](data/source_links.csv).
