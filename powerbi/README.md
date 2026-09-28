# Power BI v5

Current file: millennium_bcp_banking_dashboard_v5_validated.pbix.

Ten pages: Cover, H1 2026 Update, Executive Overview, Liquidity & Funding, Asset Quality, Profitability, Efficiency, Capital, Data Quality, Forecast & Scenarios. Annual pages retain 2022-2025 history. The H1 page compares H1 2025 with H1 2026. Data Quality summarises the historical observation register; the appendix provides all 182 rows.

Set the DataFolder parameter to your local data folder (trailing slash required), then Refresh. Ten CSV sources are used, with annual banking ratios unpivoted for visuals. H1 data are kept in separate tables so six-month income is not mixed with full-year income. DimPeriod and DimScenario support the original forecast filtering.

Forecasts contain H1 2026 actuals plus H2 estimates, then 2027/28 scenarios. ROE and ROA forecasts are closing-balance proxies; CET1 is an assumption. Refer to docs/forecast_methodology.md.

The save/reopen, data comparison and visual verification record is v5_validation.json. Earlier PBIX versions remain historical artifacts. Use the v5 report and its PDF preview for publication.
