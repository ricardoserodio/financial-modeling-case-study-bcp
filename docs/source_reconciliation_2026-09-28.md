> Historical working note retained for provenance. The current H1 2026 release is described in the root README, reports and docs/forecast_methodology.md. Status labels below describe an earlier revision.

> Follow-up: the definitions, 2023 ratios and BVPS discrepancy below were subsequently addressed in [metric migration](metric_migration_2026-09-28.md). This document preserves the first-pass findings; the migration record describes current CSV/script behavior.

# Official-source reconciliation — 28 September 2026

Local corrections; author review, forecast consistency and Power BI refresh remain pending.

## Net commissions

`Fees and commissions` means group **net commissions**, not gross fee revenue or Portugal-only activity. Tables were extracted and visually checked. The values retain each year's existing disclosure vintage; this is not a uniformly restated series.

| Period | EUR million | Official source | Locator and basis |
|---|---:|---|---|
| 2022A | 771.9 | [FY2022](https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/ResultadosTrimestrais/2022/Resultados-Millenniumbcp-FY22-27022023.pdf) | PDF/printed p10; as reported |
| 2023A | 771.7 | [FY2024](https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/ResultadosTrimestrais/2024/Resultados_Millenniumbcp_FY24_final_26022025.pdf) | PDF/printed p9; FY2024 comparative |
| 2024A | 812.7 | [FY2025](https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/ApresentacaoResultados/2025/Resultados_Millenniumbcp_FY25_f_25022026.pdf) | PDF/printed p10; restated comparative |
| 2025A | 847.4 | Same FY2025 release | PDF/printed p10; reported |

FY2024 originally reported 808.5 for 2024. FY2025 p3 explains the +4.2 commission reclassification to 812.7. The FY2025 annual report also reclassifies 2023 (rounded total 775, printed p64). Do not present the 771.7→812.7 change as purely organic growth. A uniform-vintage series requires coordinated restatement of affected metrics.

Values are consistent across financial_data, source_mapping and extraction_tracker. `Needs Review` records pending author review.

## Impairments

FY2025 p2 separately reports credit impairment net of recoveries (2024: 183.3; 2025: 199.5) and other impairments and provisions (674.2; 625.9). Its p3 explains a 0.9 reclassification in 2024. The 183.3 is supported as the credit component only.

The existing 2022 value 1056.2 is a sum; 2023–2025 are credit-only components. Values and names are preserved, marked `Needs Review`. The broad mapping blank for 2024 is retained. No automatic summation or renaming.

Next: model separate components, choose the vintage, then migrate forecast drivers, SQL and Power BI coherently. build_forecast_financials.py uses the broad label in the 2025 baseline and net-income bridge; build_forecast_ratios.py uses it in cost of risk. A global rename would not resolve the semantics.

## Book value per share

[Annual Report 2022](https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/RelatorioContas/2022/Relatorio-Grupo-BCP-2022.pdf), printed p24 / PDF p25: **EUR 0.314**, entered as reported with a mapping row. Note (2) refers to shares net of treasury shares. This was not inferred from the displayed equity.

Existing 2023 **0.412** differs from **0.417** in [Annual Report 2024](https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/RelatorioContas/2024/RABCP2024Vol1PT.pdf), printed p25 / PDF p26. Existing 2023 value retained pending vintage/definition reconciliation. Global `Reviewed` removed.

## Customer funds

FY2025 p2 separately reports total customer funds **111782** and deposits and other customer resources **89749**, EUR million. Existing `Customer deposits` 2025 contains the former. Review flag corrected without changing numbers. Forecast loan-to-deposit ratios require denominator reconciliation.

## SQL verification

The schema now mirrors all eight current CSV headers. Four quality queries were repaired to use actual source_mapping and extraction_tracker columns. All **31 SELECTs** in banking_ratio_queries.sql, data_quality_queries.sql and forecast_queries.sql were executed in memory; four fee source→CSV→SQL matches are recorded in ROUND TABLET's sql_validation.json.

Additional `queries.sql` uses an incompatible schema: 18 of 20 SELECTs fail against current CSV tables. It is outside the three analytical query files documented by sql/README.md, is preserved, and must not be advertised as executable on the current database.

Power BI, forecast outputs and report PDFs have not been refreshed or certified. historical_financials.csv remains untouched and outside scope.
