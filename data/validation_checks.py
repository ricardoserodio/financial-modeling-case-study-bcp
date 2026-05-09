"""
Validation Checks – Financial Modeling Case Study

This script performs basic data quality checks for the Millennium bcp financial
modeling case study.

The objective is to validate structure, missing values, units, periods,
validation statuses and basic file consistency before using the data in the
financial model.

This project uses only publicly available information and is for educational
and portfolio purposes only. It does not constitute investment advice.
"""

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent

SOURCE_MAPPING_FILE = BASE_DIR / "source_mapping.csv"
HISTORICAL_FINANCIALS_FILE = BASE_DIR / "historical_financials.csv"
BANKING_RATIOS_FILE = BASE_DIR / "banking_ratios.csv"
FORECAST_TEMPLATE_FILE = BASE_DIR / "forecast_template.csv"
SCENARIO_ASSUMPTIONS_FILE = BASE_DIR / "scenario_assumptions.csv"
MARKET_DATA_TEMPLATE_FILE = BASE_DIR / "market_data_template.csv"
PEER_COMPARISON_TEMPLATE_FILE = BASE_DIR / "peer_comparison_template.csv"
EXTRACTION_TRACKER_FILE = BASE_DIR / "extraction_tracker.csv"
SOURCE_LINKS_FILE = BASE_DIR / "source_links.csv"

EXPECTED_ACTUAL_PERIODS = ["2022A", "2023A", "2024A", "2025A"]
EXPECTED_FORECAST_PERIODS = ["2026E", "2027E", "2028E"]
EXPECTED_PERIODS = EXPECTED_ACTUAL_PERIODS + EXPECTED_FORECAST_PERIODS

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
    file_name: str,
) -> list[str]:
    """Check whether a DataFrame contains all required columns."""
    issues = []

    missing_columns = [column for column in required_columns if column not in df.columns]

    if missing_columns:
        issues.append(f"{file_name}: missing required columns: {missing_columns}")

    return issues


def check_missing_values(
    df: pd.DataFrame,
    key_columns: list[str],
    file_name: str,
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


def check_period_columns(
    df: pd.DataFrame,
    expected_periods: list[str],
    file_name: str,
) -> list[str]:
    """Check whether expected period columns exist."""
    issues = []

    missing_periods = [period for period in expected_periods if period not in df.columns]

    if missing_periods:
        issues.append(f"{file_name}: missing expected period columns: {missing_periods}")

    return issues


def check_validation_status(df: pd.DataFrame, file_name: str) -> list[str]:
    """Check whether validation status values are recognised."""
    issues = []

    possible_status_columns = ["validation_status", "source_status"]

    for column in possible_status_columns:
        if column in df.columns:
            invalid_values = sorted(set(df[column].dropna()) - VALIDATION_STATUS_VALUES)

            if invalid_values:
                issues.append(
                    f"{file_name}: invalid values in '{column}': {invalid_values}"
                )

    return issues


def check_unexpected_period_values(
    df: pd.DataFrame,
    period_column: str,
    file_name: str,
    allowed_extra_values: set[str] | None = None,
) -> list[str]:
    """Check unexpected values in a period column."""
    issues = []

    if period_column not in df.columns:
        return issues

    allowed_values = set(EXPECTED_PERIODS)

    if allowed_extra_values:
        allowed_values = allowed_values | allowed_extra_values

    invalid_periods = sorted(set(df[period_column].dropna()) - allowed_values)

    if invalid_periods:
        issues.append(f"{file_name}: unexpected periods found: {invalid_periods}")

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
    issues.extend(check_unexpected_period_values(df, "period", file_name))

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
    issues.extend(check_period_columns(df, EXPECTED_ACTUAL_PERIODS, file_name))
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
    issues.extend(check_period_columns(df, EXPECTED_ACTUAL_PERIODS, file_name))
    issues.extend(
        check_missing_values(
            df,
            ["ratio", "category", "formula", "unit", "source_status"],
            file_name,
        )
    )
    issues.extend(check_validation_status(df, file_name))

    return issues


def validate_forecast_template() -> list[str]:
    """Validate the forecast_template.csv file."""
    file_name = "forecast_template.csv"
    df = load_csv(FORECAST_TEMPLATE_FILE)

    required_columns = [
        "metric",
        "category",
        "2025A",
        "2026E",
        "2027E",
        "2028E",
        "forecast_driver",
        "scenario",
        "unit",
        "notes",
    ]

    issues = []
    issues.extend(check_required_columns(df, required_columns, file_name))
    issues.extend(check_period_columns(df, ["2025A", "2026E", "2027E", "2028E"], file_name))
    issues.extend(
        check_missing_values(
            df,
            ["metric", "category", "forecast_driver", "scenario", "unit"],
            file_name,
        )
    )

    return issues


def validate_scenario_assumptions() -> list[str]:
    """Validate the scenario_assumptions.csv file."""
    file_name = "scenario_assumptions.csv"
    df = load_csv(SCENARIO_ASSUMPTIONS_FILE)

    required_columns = [
        "assumption",
        "category",
        "conservative",
        "base",
        "optimistic",
        "unit",
        "notes",
    ]

    issues = []
    issues.extend(check_required_columns(df, required_columns, file_name))
    issues.extend(
        check_missing_values(
            df,
            ["assumption", "category", "unit"],
            file_name,
        )
    )

    return issues


def validate_market_data_template() -> list[str]:
    """Validate the market_data_template.csv file."""
    file_name = "market_data_template.csv"
    df = load_csv(MARKET_DATA_TEMPLATE_FILE)

    required_columns = [
        "item",
        "category",
        "date",
        "value",
        "unit",
        "source",
        "source_type",
        "validation_status",
        "notes",
    ]

    issues = []
    issues.extend(check_required_columns(df, required_columns, file_name))
    issues.extend(
        check_missing_values(
            df,
            ["item", "category", "unit", "source", "source_type", "validation_status"],
            file_name,
        )
    )
    issues.extend(check_validation_status(df, file_name))

    return issues


def validate_peer_comparison_template() -> list[str]:
    """Validate the peer_comparison_template.csv file."""
    file_name = "peer_comparison_template.csv"
    df = load_csv(PEER_COMPARISON_TEMPLATE_FILE)

    required_columns = [
        "peer_name",
        "country",
        "business_type",
        "market_data_date",
        "market_cap_eur_m",
        "share_price",
        "price_to_book",
        "price_to_earnings",
        "roe",
        "cet1_ratio",
        "cost_to_income",
        "npl_or_npe_ratio",
        "dividend_yield",
        "source",
        "validation_status",
        "notes",
    ]

    issues = []
    issues.extend(check_required_columns(df, required_columns, file_name))
    issues.extend(
        check_missing_values(
            df,
            ["peer_name", "country", "business_type", "source", "validation_status"],
            file_name,
        )
    )
    issues.extend(check_validation_status(df, file_name))

    return issues


def validate_extraction_tracker() -> list[str]:
    """Validate the extraction_tracker.csv file."""
    file_name = "extraction_tracker.csv"
    df = load_csv(EXTRACTION_TRACKER_FILE)

    required_columns = [
        "data_item",
        "category",
        "period",
        "source_document",
        "page_or_section",
        "value_extracted",
        "unit",
        "entered_in_file",
        "validation_status",
        "review_notes",
    ]

    issues = []
    issues.extend(check_required_columns(df, required_columns, file_name))
    issues.extend(
        check_missing_values(
            df,
            ["data_item", "category", "period", "source_document", "entered_in_file", "validation_status"],
            file_name,
        )
    )
    issues.extend(check_validation_status(df, file_name))
    issues.extend(
        check_unexpected_period_values(
            df,
            "period",
            file_name,
            allowed_extra_values={"Valuation Date"},
        )
    )

    return issues


def validate_source_links() -> list[str]:
    """Validate the source_links.csv file."""
    file_name = "source_links.csv"
    df = load_csv(SOURCE_LINKS_FILE)

    required_columns = [
        "source_name",
        "year",
        "source_type",
        "language",
        "url",
        "intended_use",
        "validation_status",
        "notes",
    ]

    issues = []
    issues.extend(check_required_columns(df, required_columns, file_name))
    issues.extend(
        check_missing_values(
            df,
            ["source_name", "year", "source_type", "language", "url", "intended_use", "validation_status"],
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
        validate_forecast_template,
        validate_scenario_assumptions,
        validate_market_data_template,
        validate_peer_comparison_template,
        validate_extraction_tracker,
        validate_source_links,
    ]

    for check in checks:
        try:
            all_issues.extend(check())
        except FileNotFoundError as error:
            all_issues.append(str(error))
        except pd.errors.EmptyDataError as error:
            all_issues.append(f"Empty CSV file error in {check.__name__}: {error}")
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
