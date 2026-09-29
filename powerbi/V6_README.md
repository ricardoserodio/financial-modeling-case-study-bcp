# Current Power BI v6 - 29 September 2026

The saved PBIX contains the refreshed historical and revised scenario data. It can be viewed offline without signing into Power BI.

To refresh on another computer:
1. Clone or download the repository, retaining the `powerbi/v6-data` directory.
2. Open `millennium_bcp_banking_dashboard_v6_revised.pbix` in Power BI Desktop.
3. In Transform data / Edit parameters, set `DataFolder` to the absolute local path of `powerbi/v6-data`, including a trailing backslash.
4. Apply the parameter and Refresh. Do not point v6 at the root `data` directory, which preserves the previous v5 scenario outputs.

The 11 CSV snapshots correspond to 13 model tables (including two calculated dimensions) and eight relationships. The saved model was reopened and all 852 imported rows were compared field by field with these snapshots. This count includes supporting tables and repeated mappings; it is not the count of unique historical observations (182).

The period and scenario slicers were tested; the file is saved on Cover with no scenario/period selection. All ten exported PDF pages were visually reviewed. Historical line charts use automatic ranges; scenario column charts start at zero. Different chart types need not share a zero baseline.

The scenarios use the revised 48% conversion reference. Base net income is EUR 1,090.6m / 1,061.1m / 1,074.6m for 2026E / 2027E / 2028E. The report contains separate conversion and retention sensitivities. V6 does not project CET1, ROE or ROA. Historical capital ratios remain reported source values.

The CSVs are publication snapshots. Reproduce the current analytical model with `python revisions/2026-09-29/reproduce_model.py`; model changes require rebuilding the matching Power BI snapshot before refreshing. Validation does not constitute an independent audit or predictive assurance.
