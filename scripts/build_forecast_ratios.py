import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

FORECAST_FINANCIALS_PATH = PROJECT_ROOT / "data" / "forecast_financials.csv"
BANKING_RATIOS_PATH = PROJECT_ROOT / "data" / "banking_ratios.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "forecast_ratios.csv"


def get_forecast_value(forecast_df, scenario, line_item, period):
    rows = forecast_df[
        (forecast_df["scenario"] == scenario)
        & (forecast_df["line_item"] == line_item)
        & (forecast_df["period"] == period)
    ]

    if rows.empty:
        raise ValueError(
            f"Missing forecast value: scenario={scenario}, line_item={line_item}, period={period}"
        )

    value = rows.iloc[0]["value"]

    if pd.isna(value):
        raise ValueError(
            f"NaN forecast value: scenario={scenario}, line_item={line_item}, period={period}"
        )

    return float(value)


def get_reported_2025_ratio(ratios_df, ratio):
    rows = ratios_df[ratios_df["ratio"] == ratio]

    if rows.empty:
        raise ValueError(f"Missing reported 2025A ratio: {ratio}")

    value = rows.iloc[0]["2025A"]

    if pd.isna(value):
        raise ValueError(f"Reported 2025A ratio is NaN: {ratio}")

    return float(value)


def append_ratio(
    rows,
    scenario,
    ratio,
    category,
    period,
    value,
    unit,
    calculation_method,
    source_or_basis,
    validation_status,
    notes,
):
    rows.append(
        {
            "scenario": scenario,
            "ratio": ratio,
            "category": category,
            "period": period,
            "value": round(value, 3),
            "unit": unit,
            "calculation_method": calculation_method,
            "source_or_basis": source_or_basis,
            "validation_status": validation_status,
            "notes": notes,
        }
    )


def main():
    forecast_df = pd.read_csv(FORECAST_FINANCIALS_PATH)
    ratios_df = pd.read_csv(BANKING_RATIOS_PATH)

    scenarios = ["Base", "Optimistic", "Conservative"]
    forecast_periods = ["2026E", "2027E", "2028E"]

    rows = []

    reported_ratio_map = [
        ("ROE", "Profitability", "%"),
        ("ROA", "Profitability", "%"),
        ("Cost-to-income ratio", "Efficiency", "%"),
        ("Loan-to-deposit ratio", "Liquidity", "%"),
        ("Cost of risk", "Asset Quality", "bps"),
        ("CET1 fully implemented ratio", "Capital", "%"),
    ]

    for scenario in scenarios:
        for ratio, category, unit in reported_ratio_map:
            output_ratio_name = (
                "CET1 ratio assumption"
                if ratio == "CET1 fully implemented ratio"
                else ratio
            )

            append_ratio(
                rows=rows,
                scenario=scenario,
                ratio=output_ratio_name,
                category=category,
                period="2025A",
                value=get_reported_2025_ratio(ratios_df, ratio),
                unit=unit,
                calculation_method="Reported historical ratio from banking_ratios.csv",
                source_or_basis="banking_ratios.csv",
                validation_status="Reviewed",
                notes="Reported 2025A ratio used as forecast base year",
            )

        for period in forecast_periods:
            net_income = get_forecast_value(forecast_df, scenario, "Net income", period)
            equity = get_forecast_value(forecast_df, scenario, "Equity", period)
            total_assets = get_forecast_value(forecast_df, scenario, "Total assets", period)
            operating_income = get_forecast_value(forecast_df, scenario, "Operating income", period)
            operating_costs = get_forecast_value(forecast_df, scenario, "Operating costs", period)
            customer_loans = get_forecast_value(forecast_df, scenario, "Customer loans", period)
            customer_deposits = get_forecast_value(forecast_df, scenario, "Customer deposits", period)
            impairments = get_forecast_value(forecast_df, scenario, "Impairments and provisions", period)
            cet1_value = get_forecast_value(forecast_df, scenario, "CET1 ratio assumption", period)

            notes = (
                "Educational scenario-based ratio only; not an official projection, "
                "investment advice or financial recommendation"
            )

            append_ratio(rows, scenario, "ROE", "Profitability", period, (net_income / equity) * 100, "%", "Net income / equity", "forecast_financials.csv", "To Review", notes)
            append_ratio(rows, scenario, "ROA", "Profitability", period, (net_income / total_assets) * 100, "%", "Net income / total assets", "forecast_financials.csv", "To Review", notes)
            append_ratio(rows, scenario, "Cost-to-income ratio", "Efficiency", period, (operating_costs / operating_income) * 100, "%", "Operating costs / operating income", "forecast_financials.csv", "To Review", notes)
            append_ratio(rows, scenario, "Loan-to-deposit ratio", "Liquidity", period, (customer_loans / customer_deposits) * 100, "%", "Customer loans / customer deposits", "forecast_financials.csv", "To Review", notes)
            append_ratio(rows, scenario, "Cost of risk", "Asset Quality", period, (impairments / customer_loans) * 10000, "bps", "Impairments and provisions / customer loans", "forecast_financials.csv", "To Review", notes)
            append_ratio(rows, scenario, "CET1 ratio assumption", "Capital", period, cet1_value, "%", "Direct scenario assumption", "forecast_assumptions.csv", "To Review", "Educational capital assumption only")

    output_df = pd.DataFrame(rows)
    output_df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

    print(f"Created: {OUTPUT_PATH}")
    print()
    print(output_df.head(40).to_string(index=False))


if __name__ == "__main__":
    main()
