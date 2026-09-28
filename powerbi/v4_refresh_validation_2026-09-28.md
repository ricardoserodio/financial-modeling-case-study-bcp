> Historical reference / optional extension. This file is outside the September 2026 active validation scope. Current deliverables and evidence are listed in the root README and PROJECT_STATUS.md.

# Power BI v4 — refresh and visual verification, 28 September 2026

Current local report: [v4 PBIX](millennium_bcp_banking_dashboard_v4_reconciled.pbix). The [nine-page PDF](../outputs/powerbi/millennium_bcp_banking_dashboard_v4_reconciled.pdf) was exported by Power BI Desktop. Earlier PBIX/PDF versions remain historical and were not overwritten.

Power BI Desktop 2.157.1354.0 x64 was installed with user authorization. No computer restart was required. All eight CSV queries now read `X:\03_PROJETOS\wisestrike\financial-modeling-case-study-bcp\data\`, replacing the obsolete pre-format Desktop path. Existing type conversions, unpivot, measures and visuals were preserved.

The v4 file was saved, Power BI closed and reopened, and all eight paths and 804 model rows verified against the source CSVs. Native Refresh then succeeded and the comparison passed again. Comparison normalizes blanks and capitalization in existing category/data_type labels. All 76 historical chart points match their source values.

EPS 2023 is EUR 0.054: consolidated note 18, Annual Report 2024, printed p244/PDF p245. Numerator EUR 856.050m minus EUR 37.000m AT1 interest; weighted-average shares 15,113,989,952. SQLite and six SQL exports were regenerated; seven semantic tests and 31 core SELECTs passed. Source versions remain mixed as documented in the metric migration notes.

All nine exported pages were visually inspected. Data Quality keeps the existing review statuses, and its five columns now fit without horizontal scrolling (fixed widths and text wrap). Its PDF table is a visible overview; the full source register is in the PBIX and `data/source_mapping.csv`. The forecast page retains all three scenarios and three forecast periods. The PDF was exported with the active page at 100% to avoid inconsistent scaling.

This is technical verification, not author sign-off. Source review and publication remain separate. No data was published to the Power BI service.
