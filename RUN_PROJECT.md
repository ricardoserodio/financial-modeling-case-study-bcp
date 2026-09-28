# Reproduce the current case study

## Current analytical revision - 29 September 2026

From the repository root, with Python 3.10 or later:

```shell
python revisions/2026-09-29/reproduce_model.py
```

The revised model uses only the Python standard library. Input snapshots are in `revisions/2026-09-29/inputs/data`; generated CSVs and source records are in `revisions/2026-09-29/data`; checks are in `revisions/2026-09-29/checks.json`.

The reproduction checks 81 financial cells, 36 conversion sensitivities, 27 retention sensitivities, the net-income bridge and NPE coverage arithmetic. See [revisions/2026-09-29/METHODOLOGY.md](revisions/2026-09-29/METHODOLOGY.md) for assumptions and limitations.

The [current PDF](reports/bcp_complete_case_study_en_2026-09-29.pdf) contains the revised calculations and nine native historical Power BI pages. The old PBIX forecast page is not included and has not been refreshed to the new model.

## Previous v5 pipeline - historical reproduction only

The following commands rebuild the **superseded v5 scenario model**, not the current report. Use them only to reproduce that edition and the historical SQL/Power BI pipeline.


Use Python 3.10+ in a local virtual environment. From the repository root:

```shell
python -m pip install -r requirements.txt
python scripts/build_forecast_financials.py
python scripts/build_forecast_ratios.py
python scripts/build_scenario_analysis.py
python scripts/validate_publication.py
python scripts/load_sqlite_database.py
python scripts/run_sql_analysis.py
```

The first three commands regenerate scenario outputs from the historical/interim CSVs and assumptions. Validation checks source-register coverage, unique keys, historical arithmetic, Decimal-based forecast calculations and every active SQL query. The SQLite loader creates a local ignored database with ten tables. `sql/create_tables.sql` and its compatibility alias `sql/schema.sql` are for a disposable local database: they drop and recreate case-study tables.

To rebuild the analytical PDFs after validation:

```shell
python scripts/build_reports.py
```

Open `powerbi/millennium_bcp_banking_dashboard_v5_validated.pbix` in Power BI Desktop. Set the `DataFolder` Power Query parameter to the local repository's `data` folder, including the trailing slash, then Refresh. Keep historical annual and interim series separate. The saved report contains data; an account is not required to inspect it locally.

`reports/` holds shareable outputs and is tracked by Git. `outputs/`, virtual environments and SQLite databases are generated locally and ignored. Archived working templates under `data/archive/` are excluded from the active model. Original PDFs are linked rather than redistributed; SHA-256 values identify the evidence copies used.
