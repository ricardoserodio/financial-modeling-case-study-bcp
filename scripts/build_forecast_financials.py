import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

FINANCIAL_DATA_PATH = PROJECT_ROOT / "data" / "financial_data.csv"
ASSUMPTIONS_PATH = PROJECT_ROOT / "data" / "forecast_assumptions.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "forecast_financials.csv"


def get_2025_value(financial_df: pd.DataFrame, metric: str) -> float:
    rows = financial_df[
        (financial_df["period"] == "2025A")
        & (financial_df["metric"] == metric)
    ]

    if rows.empty:
        raise ValueError(f"Missing 2025A value for metric: {metric}")

    value = rows.iloc[0]["value"]

    if pd.isna(value):
        raise ValueError(f"2025A value is NaN for metric: {metric}")

    return float(value)


def get_assumption(
    assumptions_df: pd.DataFrame,
    scenario: str,
    assumption: str,
    period: str,
) -> float:
    rows = assumptions_df[
        (assumptions_df["scenario"] == scenario)
        & (assumptions_df["assumption"] == assumption)
    ]

    if rows.empty:
        raise ValueError(
            f"Missing assumption: scenario={scenario}, assumption={assumption}"
        )

    value = rows.iloc[0][period]

    if pd.isna(value):
        raise ValueError(
            f"Missing value for assumption={assumption}, scenario={scenario}, period={period}"
        )

    return float(value)


def grow(previous_value: float, growth_rate_percent: float) -> float:
    return previous_value * (1 + growth_rate_percent / 100)


def main() -> None:
    financial_df = pd.read_csv(FINANCIAL_DATA_PATH)
    assumptions_df = pd.read_csv(ASSUMPTIONS_PATH)

    scenarios = ["Base", "Optimistic", "Conservative"]
    forecast_periods = ["2026E", "2027E", "2028E"]

    base_2025 = {
        "Net interest income": get_2025_value(financial_df, "Net interest income"),
        "Operating income": get_2025_value(financial_df, "Operating income"),
        "Operating costs": get_2025_value(financial_df, "Operating costs"),
        "Impairments and provisions": get_2025_value(financial_df, "Impairments and provisions"),
        "Net income": get_2025_value(financial_df, "Net income"),
        "Customer loans": get_2025_value(financial_df, "Customer loans"),
        "Customer deposits": get_2025_value(financial_df, "Customer deposits"),
        "Total assets": get_2025_value(financial_df, "Total assets"),
        "Equity": get_2025_value(financial_df, "Equity"),
    }

    base_2025["Other operating income"] = (
        base_2025["Operating income"] - base_2025["Net interest income"]
    )

    base_2025["Pre-provision operating profit"] = (
        base_2025["Operating income"] - base_2025["Operating costs"]
    )

    profit_after_impairments_2025 = (
        base_2025["Pre-provision operating profit"]
        - base_2025["Impairments and provisions"]
    )

    if profit_after_impairments_2025 <= 0:
        raise ValueError(
            "Invalid 2025A profit bridge: profit after impairments is not positive."
        )

    net_income_conversion_ratio = (
        base_2025["Net income"] / profit_after_impairments_2025
    )

    rows = []

    for scenario in scenarios:
        current = base_2025.copy()

        for metric in [
            "Net interest income",
            "Other operating income",
            "Operating income",
            "Operating costs",
            "Pre-provision operating profit",
            "Customer loans",
            "Customer deposits",
            "Total assets",
            "Equity",
            "Impairments and provisions",
            "Net income",
        ]:
            rows.append(
                {
                    "scenario": scenario,
                    "line_item": metric,
                    "period": "2025A",
                    "value": round(current[metric], 1),
                    "unit": "EUR million",
                    "calculation_method": "Historical actual from financial_data.csv",
                    "source_or_basis": "Public financial statements structured in project dataset",
                    "validation_status": "Reviewed",
                    "notes": "Historical actual used as forecast base year",
                }
            )

        for period in forecast_periods:
            nii_growth = get_assumption(
                assumptions_df, scenario, "Net interest income growth", period
            )

            other_income_growth = get_assumption(
                assumptions_df, scenario, "Other operating income growth", period
            )

            cost_growth = get_assumption(
                assumptions_df, scenario, "Operating costs growth", period
            )

            cost_of_risk_bps = get_assumption(
                assumptions_df, scenario, "Cost of risk", period
            )

            loans_growth = get_assumption(
                assumptions_df, scenario, "Customer loans growth", period
            )

            deposits_growth = get_assumption(
                assumptions_df, scenario, "Customer deposits growth", period
            )

            cet1_assumption = get_assumption(
                assumptions_df, scenario, "CET1 ratio assumption", period
            )

            current["Net interest income"] = grow(
                current["Net interest income"], nii_growth
            )

            current["Other operating income"] = grow(
                current["Other operating income"], other_income_growth
            )

            current["Operating income"] = (
                current["Net interest income"] + current["Other operating income"]
            )

            current["Operating costs"] = grow(
                current["Operating costs"], cost_growth
            )

            current["Customer loans"] = grow(
                current["Customer loans"], loans_growth
            )

            current["Customer deposits"] = grow(
                current["Customer deposits"], deposits_growth
            )

            current["Total assets"] = grow(
                current["Total assets"], (loans_growth + deposits_growth) / 2
            )

            current["Pre-provision operating profit"] = (
                current["Operating income"] - current["Operating costs"]
            )

            current["Impairments and provisions"] = (
                current["Customer loans"] * cost_of_risk_bps / 10000
            )

            current["Net income"] = (
                current["Pre-provision operating profit"]
                - current["Impairments and provisions"]
            ) * net_income_conversion_ratio

            current["Equity"] = current["Equity"] + (current["Net income"] * 0.5)

            for metric in [
                "Net interest income",
                "Other operating income",
                "Operating income",
                "Operating costs",
                "Pre-provision operating profit",
                "Customer loans",
                "Customer deposits",
                "Total assets",
                "Equity",
                "Impairments and provisions",
                "Net income",
            ]:
                rows.append(
                    {
                        "scenario": scenario,
                        "line_item": metric,
                        "period": period,
                        "value": round(current[metric], 1),
                        "unit": "EUR million",
                        "calculation_method": "Scenario-based educational forecast model",
                        "source_or_basis": "2025A actuals plus forecast_assumptions.csv",
                        "validation_status": "To Review",
                        "notes": (
                            "Educational estimate only; not an official projection, "
                            "investment advice or financial recommendation"
                        ),
                    }
                )

            rows.append(
                {
                    "scenario": scenario,
                    "line_item": "CET1 ratio assumption",
                    "period": period,
                    "value": round(cet1_assumption, 2),
                    "unit": "%",
                    "calculation_method": "Direct scenario assumption",
                    "source_or_basis": "forecast_assumptions.csv",
                    "validation_status": "To Review",
                    "notes": "Educational capital assumption only",
                }
            )

    output_df = pd.DataFrame(rows)
    output_df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

    print(f"Created: {OUTPUT_PATH}")
    print()
    print(output_df.head(30).to_string(index=False))


if __name__ == "__main__":
    main()
