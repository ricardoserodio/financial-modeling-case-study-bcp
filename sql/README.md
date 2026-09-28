# SQL workflow

Ten CSV-aligned tables are loaded by scripts/load_sqlite_database.py. Run scripts/validate_publication.py for schema compatibility and all 36 analytical statements. The query files cover historical banking ratios, source quality, forecasts and current annual/interim entry queries. Schema.sql is a compatibility copy of create_tables.sql; either recreates the local case-study tables. Generated databases and exports stay ignored.
