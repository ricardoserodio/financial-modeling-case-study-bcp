# Power BI v5 refresh workflow

Current release: `millennium_bcp_banking_dashboard_v5_validated.pbix`. Its local save/reopen, data comparison and visual checks are recorded in `v5_validation.json`.

1. Update the official-source observation register and the annual/interim CSVs. Preserve units, source definitions and disclosed restatements.
2. Follow [RUN_PROJECT.md](../RUN_PROJECT.md) to regenerate the forecasts, validate calculations and rebuild SQLite and SQL outputs.
3. Open v5 in Power BI Desktop. Set the Power Query `DataFolder` parameter to your repository's `data` directory, including the trailing slash.
4. Refresh all ten CSV sources. The model has twelve tables including the two dimensions; annual banking ratios are unpivoted.
5. Compare the refreshed model with the CSVs. The current release contains 909 model rows. Counts may change with future releases; investigate changes rather than forcing this count.
6. Review all ten report pages, including filters, chronological sorting, H1 comparisons and source status. Annual and interim flows remain separate.
7. Save, reopen and export to PDF. Review the exported pages before committing and publishing the updated PBIX, reports and validation record.

The complete source register is in the validation appendix. `Source verified` and `Recalculated` describe historical evidence; `Scenario assumption` and `Model checked` describe the illustrative model. Earlier working notes and PBIX versions are historical artifacts.
