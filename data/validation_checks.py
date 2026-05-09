"""
Validation Checks – Financial Modeling Case Study

This script performs basic data quality checks for the Millennium bcp financial
modeling case study.

The objective is to validate structure, missing values, units, periods and
basic source mapping consistency before using the data in the financial model.

This project uses only publicly available information and is for educational
and portfolio purposes only. It does not constitute investment advice.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent

SOURCE_MAPPING_FILE = BASE_DIR / "source_mapping.csv"
HISTORICAL_FINANCIALS_FILE = BASE_DIR / "historical_financials.csv"
BANKING_RATIOS_FILE = BASE_DIR / "banking_ratios.csv"


EXPECTED_PERIODS = ["2022A", "2023A", "2024A", "2025A"]
EXPECTED_FORECAST_PERIODS = ["2026E", "2027E", "2028E"]

VALIDATION_STATUS_VALUES = {
    "Pending",
    "Reviewed",
    "Validated",
    "Needs Review",
    "Not Available",
    "Calculated",
}


def load_csv(file_path: Path) -> pd.DataFrame:
    """Load a CSV file and return a pandas DataFrame."""
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return pd.read_csv(file_path)


def check_required_columns(
    df: pd.DataFrame,
    required_columns: list[str],
    file_name: str
) -> list[str]:
    """Check whether a DataFrame contains all required columns."""
    issues = []

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        issues.append(
            f"{file_name}: missing required columns: {missing_columns}"
        )

    return issues


def check_missing_values(
    df: pd.DataFrame,
    key_columns: list[str],
    file_name: str
) -> list[str]:
    """Check missing values in key columns."""
    issues = []

    for column in key_columns:
        if column in df.columns:
            missing_count = df[column].isna().sum()

            if missing_count > 0:
                issues.append(
                    f"{file_name}: column '{column}' has {missing_count} missing values"
                )

    return issues


def check_period_columns(df: pd.DataFrame, file_name: str) -> list[str]:
    """Check whether expected actual period columns exist."""
    issues = []

    missing_periods = [period for period in EXPECTED_PERIODS if period not in df.columns]

    if missing_periods:
        issues.append(
            f"{file_name}: missing expected period columns: {missing_periods}"
        )

    return issues


def check_validation_status(df: pd.DataFrame, file_name: str) -> list[str]:
    """Check whether validation status values are recognised."""
    issues = []

    possible_status_columns = ["validation_status", "source_status"]

    for column in possible_status_columns:
        if column in df.columns:
            invalid_values = sorted(
                set(df[column].dropna()) - VALIDATION_STATUS_VALUES
            )

            if invalid_values:
                issues.append(
                    f"{file_name}: invalid values in '{column}': {invalid_values}"
                )

    return issues


def validate_source_mapping() -> list[str]:
    """Validate the source_mapping.csv file."""
    file_name = "source_mapping.csv"
    df = load_csv(SOURCE_MAPPING_FILE)

    required_columns = [
        "item",
        "category",
        "period",
        "value",
        "unit",
        "source_document",
        "source_type",
        "source_section_or_page",
        "reported_or_calculated",
        "calculation_method",
        "validation_status",
        "notes",
    ]

    issues = []
    issues.extend(check_required_columns(df, required_columns, file_name))
    issues.extend(
        check_missing_values(
            df,
            ["item", "category", "period", "unit", "source_document", "validation_status"],
            file_name,
        )
    )
    issues.extend(check_validation_status(df, file_name))

    if "period" in df.columns:
        invalid_periods = sorted(
            set(df["period"].dropna()) - set(EXPECTED_PERIODS + EXPECTED_FORECAST_PERIODS)
        )

        if invalid_periods:
            issues.append(
                f"{file_name}: unexpected periods found: {invalid_periods}"
            )

    return issues


def validate_historical_financials() -> list[str]:
    """Validate the historical_financials.csv file."""
    file_name = "historical_financials.csv"
    df = load_csv(HISTORICAL_FINANCIALS_FILE)

    required_columns = [
        "metric",
        "category",
        "2022A",
        "2023A",
        "2024A",
        "2025A",
        "unit",
        "source_status",
        "notes",
    ]

    issues = []
    issues.extend(check_required_columns(df, required_columns, file_name))
    issues.extend(check_period_columns(df, file_name))
    issues.extend(
        check_missing_values(
            df,
            ["metric", "category", "unit", "source_status"],
            file_name,
        )
    )
    issues.extend(check_validation_status(df, file_name))

    return issues


def validate_banking_ratios() -> list[str]:
    """Validate the banking_ratios.csv file."""
    file_name = "banking_ratios.csv"
    df = load_csv(BANKING_RATIOS_FILE)

    required_columns = [
        "ratio",
        "category",
        "formula",
        "2022A",
        "2023A",
        "2024A",
        "2025A",
        "unit",
        "source_status",
        "notes",
    ]

    issues = []
    issues.extend(check_required_columns(df, required_columns, file_name))
    issues.extend(check_period_columns(df, file_name))
    issues.extend(
        check_missing_values(
            df,
            ["ratio", "category", "formula", "unit", "source_status"],
            file_name,
        )
    )
    issues.extend(check_validation_status(df, file_name))

    return issues


def run_all_checks() -> None:
    """Run all validation checks and print results."""
    all_issues = []

    checks = [
        validate_source_mapping,
        validate_historical_financials,
        validate_banking_ratios,
    ]

    for check in checks:
        try:
            all_issues.extend(check())
        except FileNotFoundError as error:
            all_issues.append(str(error))
        except pd.errors.EmptyDataError as error:
            all_issues.append(f"Empty CSV file error: {error}")
        except Exception as error:
            all_issues.append(f"Unexpected error in {check.__name__}: {error}")

    print("Financial Modeling Case Study – Data Validation Checks")
    print("=" * 60)

    if not all_issues:
        print("No validation issues found.")
    else:
        print(f"{len(all_issues)} validation issue(s) found:")
        print()

        for index, issue in enumerate(all_issues, start=1):
            print(f"{index}. {issue}")

    print()
    print("Validation complete.")


if __name__ == "__main__":
    run_all_checks()
