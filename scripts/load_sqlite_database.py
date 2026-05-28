import sqlite3
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "bcp_case_study.sqlite"


CSV_TABLE_MAP = {
    "financial_data.csv": "financial_data",
    "banking_ratios.csv": "banking_ratios",
    "source_mapping.csv": "source_mapping",
    "extraction_tracker.csv": "extraction_tracker",
    "forecast_assumptions.csv": "forecast_assumptions",
    "forecast_financials.csv": "forecast_financials",
    "forecast_ratios.csv": "forecast_ratios",
    "scenario_analysis.csv": "scenario_analysis",
}


def read_csv_file(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing CSV file: {path}")

    return pd.read_csv(path, encoding="utf-8-sig")


def load_table(connection: sqlite3.Connection, csv_file: str, table_name: str) -> int:
    csv_path = DATA_DIR / csv_file
    dataframe = read_csv_file(csv_path)

    dataframe.to_sql(
        name=table_name,
        con=connection,
        if_exists="replace",
        index=False,
    )

    return len(dataframe)


def main() -> None:
    print("Financial Modeling Case Study – SQLite Loader")
    print("=" * 60)
    print(f"Database path: {DB_PATH}")
    print()

    with sqlite3.connect(DB_PATH) as connection:
        loaded_tables = []

        for csv_file, table_name in CSV_TABLE_MAP.items():
            row_count = load_table(connection, csv_file, table_name)
            loaded_tables.append((table_name, row_count))
            print(f"Loaded {csv_file} -> {table_name} ({row_count} rows)")

        print()
        print("Table row counts")
        print("-" * 60)

        for table_name, _ in loaded_tables:
            result = connection.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()
            print(f"{table_name}: {result[0]} rows")

    print()
    print("SQLite database created successfully.")
    print("This local database is for analytical testing and portfolio workflow demonstration only.")


if __name__ == "__main__":
    main()
