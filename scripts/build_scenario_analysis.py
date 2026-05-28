import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

FORECAST_FINANCIALS_PATH = PROJECT_ROOT / "data" / "forecast_financials.csv"
FORECAST_RATIOS_PATH = PROJECT_ROOT / "data" / "forecast_ratios.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "scenario_analysis.csv"


def get_value(df, filters, value_column="value"):
    rows = df.copy()

    for column, expected_value in filters.items():
        rows = rows[rows[column] == expected_value]

    if rows.empty:
        raise ValueError(f"Missing value for filters: {filters}")

    value = rows.iloc[0][value_column]

    if pd.isna(value):
        raise ValueError(f"NaN value for filters: {filters}")

    return float(value)


def scenario_risk_level(scenario):
    if scenario == "Optimistic":
        return "Lower risk / upside case"
    if scenario == "Conservative":
        return "Higher risk / downside case"
    return "Moderate risk / central case"


def scenario_logic(scenario):
    if scenario == "Optimistic":
        return "Upside scenario assuming stronger profitability, controlled risk costs and resilient capital."
    if scenario == "Conservative":
        return "Downside scenario assuming weaker revenue development, higher cost pressure and higher credit risk costs."
    return "Central scenario assuming moderate normalisation, controlled costs and stable capital."


def interpretation(metric, scenario, period, value, base_value, unit):
    if scenario == "Base":
        return f"{period} base case reference for {metric}: {value:.3f} {unit}."

    variance = value - base_value

    if variance > 0:
        direction = "above"
    elif variance < 0:
        direction = "below"
    else:
        direction = "in line with"

    return (
        f"{period} {scenario} case is {direction} the Base case for {metric}. "
        f"Scenario value: {value:.3f} {unit}; Base case: {base_value:.3f} {unit}."
    )


def add_row(
    rows,
    scenario,
    period,
    metric,
    category,
    value,
    unit,
    base_value,
    source,
):
    variance_absolute = value - base_value

    if base_value != 0:
        variance_percent = (variance_absolute / abs(base_value)) * 100
    else:
        variance_percent = 0.0

    rows.append(
        {
            "scenario": scenario,
            "period": period,
            "metric": metric,
            "category": category,
            "value": round(value, 3),
            "unit": unit,
            "base_case_value": round(base_value, 3),
            "variance_vs_base": round(variance_absolute, 3),
            "variance_vs_base_percent": round(variance_percent, 3),
            "scenario_logic": scenario_logic(scenario),
            "main_driver": "Linked to forecast assumptions and scenario-based financial model",
            "risk_level": scenario_risk_level(scenario),
            "interpretation": interpretation(metric, scenario, period, value, base_value, unit),
            "source_or_basis": source,
            "validation_status": "To Review",
            "notes": (
                "Educational scenario analysis only; not an official projection, "
                "investment advice or financial recommendation"
            ),
        }
    )


def main():
    financials_df = pd.read_csv(FORECAST_FINANCIALS_PATH)
    ratios_df = pd.read_csv(FORECAST_RATIOS_PATH)

    scenarios = ["Base", "Optimistic", "Conservative"]
    periods = ["2026E", "2027E", "2028E"]

    rows = []

    financial_metrics = [
        ("Operating income", "Profitability", "EUR million"),
        ("Operating costs", "Efficiency", "EUR million"),
        ("Pre-provision operating profit", "Profitability", "EUR million"),
        ("Impairments and provisions", "Asset Quality", "EUR million"),
        ("Net income", "Profitability", "EUR million"),
        ("Customer loans", "Balance Sheet", "EUR million"),
        ("Customer deposits", "Balance Sheet", "EUR million"),
        ("Equity", "Capital", "EUR million"),
    ]

    ratio_metrics = [
        ("ROE", "Profitability", "%"),
        ("ROA", "Profitability", "%"),
        ("Cost-to-income ratio", "Efficiency", "%"),
        ("Loan-to-deposit ratio", "Liquidity", "%"),
        ("Cost of risk", "Asset Quality", "bps"),
        ("CET1 ratio assumption", "Capital", "%"),
    ]

    for period in periods:
        for metric, category, unit in financial_metrics:
            base_value = get_value(
                financials_df,
                {
                    "scenario": "Base",
                    "line_item": metric,
                    "period": period,
                },
            )

            for scenario in scenarios:
                value = get_value(
                    financials_df,
                    {
                        "scenario": scenario,
                        "line_item": metric,
                        "period": period,
                    },
                )

                add_row(
                    rows=rows,
                    scenario=scenario,
                    period=period,
                    metric=metric,
                    category=category,
                    value=value,
                    unit=unit,
                    base_value=base_value,
                    source="forecast_financials.csv",
                )

        for metric, category, unit in ratio_metrics:
            base_value = get_value(
                ratios_df,
                {
                    "scenario": "Base",
                    "ratio": metric,
                    "period": period,
                },
            )

            for scenario in scenarios:
                value = get_value(
                    ratios_df,
                    {
                        "scenario": scenario,
                        "ratio": metric,
                        "period": period,
                    },
                )

                add_row(
                    rows=rows,
                    scenario=scenario,
                    period=period,
                    metric=metric,
                    category=category,
                    value=value,
                    unit=unit,
                    base_value=base_value,
                    source="forecast_ratios.csv",
                )

    output_df = pd.DataFrame(rows)
    output_df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

    print(f"Created: {OUTPUT_PATH}")
    print()
    print(output_df.head(45).to_string(index=False))


if __name__ == "__main__":
    main()
