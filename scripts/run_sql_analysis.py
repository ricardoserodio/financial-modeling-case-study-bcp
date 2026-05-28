import sqlite3
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "data" / "bcp_case_study.sqlite"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "sql_analysis"


QUERIES = {
    "table_row_counts": """
        SELECT 'financial_data' AS table_name, COUNT(*) AS row_count FROM financial_data
        UNION ALL
        SELECT 'banking_ratios', COUNT(*) FROM banking_ratios
        UNION ALL
        SELECT 'source_mapping', COUNT(*) FROM source_mapping
        UNION ALL
        SELECT 'extraction_tracker', COUNT(*) FROM extraction_tracker
        UNION ALL
        SELECT 'forecast_assumptions', COUNT(*) FROM forecast_assumptions
        UNION ALL
        SELECT 'forecast_financials', COUNT(*) FROM forecast_financials
        UNION ALL
        SELECT 'forecast_ratios', COUNT(*) FROM forecast_ratios
        UNION ALL
        SELECT 'scenario_analysis', COUNT(*) FROM scenario_analysis;
    """,

    "banking_ratios_2025_snapshot": """
        SELECT
            ratio,
            category,
            "2025A" AS value_2025A,
            unit,
            source_status,
            notes
        FROM banking_ratios
        ORDER BY category, ratio;
    """,

    "forecast_net_income_by_scenario": """
        SELECT
            scenario,
            period,
            line_item,
            value,
            unit,
            validation_status
        FROM forecast_financials
        WHERE line_item = 'Net income'
        ORDER BY period,
            CASE scenario
                WHEN 'Base' THEN 1
                WHEN 'Optimistic' THEN 2
                WHEN 'Conservative' THEN 3
                ELSE 4
            END;
    """,

    "forecast_roe_by_scenario": """
        SELECT
            scenario,
            period,
            ratio,
            value,
            unit,
            validation_status
        FROM forecast_ratios
        WHERE ratio = 'ROE'
        ORDER BY period,
            CASE scenario
                WHEN 'Base' THEN 1
                WHEN 'Optimistic' THEN 2
                WHEN 'Conservative' THEN 3
                ELSE 4
            END;
    """,

    "scenario_net_income_variance": """
        SELECT
            scenario,
            period,
            metric,
            value,
            unit,
            base_case_value,
            variance_vs_base,
            variance_vs_base_percent,
            risk_level,
            interpretation
        FROM scenario_analysis
        WHERE metric = 'Net income'
        ORDER BY period,
            CASE scenario
                WHEN 'Base' THEN 1
                WHEN 'Optimistic' THEN 2
                WHEN 'Conservative' THEN 3
                ELSE 4
            END;
    """,

    "forecast_outputs_requiring_review": """
        SELECT
            'forecast_financials' AS dataset,
            scenario,
            period,
            line_item AS item,
            value,
            unit,
            validation_status,
            notes
        FROM forecast_financials
        WHERE validation_status <> 'Reviewed'

        UNION ALL

        SELECT
            'forecast_ratios' AS dataset,
            scenario,
            period,
            ratio AS item,
            value,
            unit,
            validation_status,
            notes
        FROM forecast_ratios
        WHERE validation_status <> 'Reviewed'

        UNION ALL

        SELECT
            'scenario_analysis' AS dataset,
            scenario,
            period,
            metric AS item,
            value,
            unit,
            validation_status,
            notes
        FROM scenario_analysis
        WHERE validation_status <> 'Reviewed'

        ORDER BY dataset, scenario, period, item;
    """,
}


def run_query(connection: sqlite3.Connection, query_name: str, query: str) -> pd.DataFrame:
    dataframe = pd.read_sql_query(query, connection)
    output_path = OUTPUT_DIR / f"{query_name}.csv"
    dataframe.to_csv(output_path, index=False, encoding="utf-8-sig")
    return dataframe


def main() -> None:
    print("Financial Modeling Case Study – SQL Analysis Runner")
    print("=" * 60)

    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"SQLite database not found: {DB_PATH}. "
            "Run scripts/load_sqlite_database.py first."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Database path: {DB_PATH}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    with sqlite3.connect(DB_PATH) as connection:
        for query_name, query in QUERIES.items():
            dataframe = run_query(connection, query_name, query)
            print(f"Executed query: {query_name}")
            print(f"Rows exported: {len(dataframe)}")
            print(f"Output file: outputs/sql_analysis/{query_name}.csv")
            print("-" * 60)

    print()
    print("SQL analysis completed successfully.")
    print("Outputs are generated for analytical review and portfolio documentation.")


if __name__ == "__main__":
    main()
