# Active publication scope

As of 28 September 2026, the active model contains ten CSV tables: financial_data (52 rows), banking_ratios (18 wide rows / 72 cells), interim_financials (26), interim_ratios (32), source_mapping (182), extraction_tracker (182), forecast_assumptions (24 rows / 72 parameters), forecast_financials (141), forecast_ratios (72), scenario_analysis (126).

`source_links.csv` and `source_manifest.json` provide the seven official evidence references. The complete appendix is `reports/bcp_validation_appendix_2026-09-28.pdf`.

Annual and interim data remain separate to prevent comparing six-month income with full-year income. Stocks refer to their respective balance-sheet dates. No blank forecasts or valuation placeholders are counted as observations.

`data/archive/pre-validation-2026-09-28/` retains the previous working data, including the 40 empty Pending source-mapping rows. Historical_financials, market_data_template and peer_comparison_template entry points now contain headers only; archived drafts must not be loaded as current data. Price multiples, dividend yield, peer comparison and market-date selection are outside the active study.
