# Data Dictionary

This file defines the main financial items, ratios and data fields used in the **Millennium bcp / Banco Comercial Português** financial modeling case study.

The purpose of this data dictionary is to ensure consistency, transparency and source traceability across the project.

This project uses only publicly available information and is for educational and portfolio purposes only.

---

## 1. General Data Fields

| Field | Definition |
|---|---|
| `metric` | Name of the financial statement item or market data item |
| `ratio` | Name of the calculated or reported banking ratio |
| `category` | Classification of the item, such as Income Statement, Balance Sheet, Capital, Valuation or Asset Quality |
| `period` | Reporting period, such as 2022A, 2023A, 2024A, 2025A, 2026E, 2027E or 2028E |
| `value` | Reported or calculated numerical value |
| `unit` | Unit of measurement, such as EUR million, %, EUR, million shares or x |
| `source_document` | Public document or data source used |
| `source_type` | Type of source, such as annual report, earnings presentation, market data or regulatory filing |
| `reported_or_calculated` | Indicates whether the figure is directly reported or calculated by the analyst |
| `calculation_method` | Formula or method used for calculated figures |
| `validation_status` | Review status of the figure |
| `notes` | Additional comments, assumptions or limitations |

---

## 2. Period Definitions

| Period | Meaning |
|---|---|
| 2022A | Full-year 2022 actual reported data |
| 2023A | Full-year 2023 actual reported data |
| 2024A | Full-year 2024 actual reported data |
| 2025A | Full-year 2025 actual reported data |
| 2026E | Estimated / forecast data for 2026 |
| 2027E | Estimated / forecast data for 2027 |
| 2028E | Estimated / forecast data for 2028 |

`A` means Actual.

`E` means Estimate.

---

## 3. Income Statement Items

| Item | Definition | Preferred Unit |
|---|---|---|
| Net interest income | Interest income minus interest expense. Core banking revenue generated from lending, deposits and interest-bearing assets/liabilities. | EUR million |
| Fees and commissions | Net fees and commissions from banking services, payments, cards, asset management, insurance distribution and other client-related services. | EUR million |
| Other operating income | Other income items not classified as net interest income or fees and commissions. May include trading income, gains/losses or other operating items depending on reporting classification. | EUR million |
| Operating income | Total banking income or total operating income before operating costs. | EUR million |
| Operating costs | Staff costs, administrative expenses, depreciation and other operating expenses. | EUR million |
| Impairments and provisions | Credit impairments, provisions and other impairment charges recognised in the income statement. | EUR million |
| Profit before tax | Profit before income tax expense. | EUR million |
| Net income | Consolidated net profit. Where possible, use net income attributable to shareholders for valuation and per-share calculations. | EUR million |

---

## 4. Balance Sheet Items

| Item | Definition | Preferred Unit |
|---|---|---|
| Loans to customers | Customer loan book. Definition must be checked to confirm whether values are gross or net of impairments. | EUR million |
| Customer deposits | Deposits from customers used as a key funding source. | EUR million |
| Total assets | Consolidated total assets of the Group. | EUR million |
| Equity | Total equity or equity attributable to shareholders. The chosen definition must remain consistent. | EUR million |
| Risk-weighted assets | Assets weighted by regulatory risk, used for capital ratio calculations. | EUR million |
| CET1 capital | Common Equity Tier 1 capital used in regulatory capital analysis. | EUR million |

---

## 5. Market Data Items

| Item | Definition | Preferred Unit |
|---|---|---|
| Share price | Public market price of the listed share at a selected date. | EUR |
| Market capitalisation | Share price multiplied by number of shares outstanding. | EUR million |
| Number of shares | Shares outstanding or weighted average shares, depending on the calculation. | million shares |
| Dividend per share | Dividend paid or proposed per share. | EUR |
| Dividends paid | Total dividends paid or proposed, depending on the analysis. | EUR million |

Market data must always be dated and sourced.

---

## 6. Profitability Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---|---|
| ROE | Net income / Average equity | % | Use reported ROE where available. If calculated, prefer average equity. |
| ROA | Net income / Average total assets | % | Use average total assets where available. |
| Net interest margin | Net interest income / Average interest-earning assets | % | Use reported figure where available. Only calculate if the correct denominator is available. |

---

## 7. Efficiency Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---|---|
| Cost-to-income | Operating costs / Operating income | % | Measures operating efficiency. Compare calculated figure with reported ratio where available. |

---

## 8. Asset Quality Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---|---|
| NPL ratio | Non-performing loans / Total loans | % | Use official reported figure where possible. |
| NPE ratio | Non-performing exposures / Total exposures | % | Use consistently if the bank reports NPE instead of NPL. |
| NPL coverage ratio | Impairment allowances / Non-performing loans | % | Check whether collateral is included in the reported metric. |
| Cost of risk | Loan impairments / Average loans to customers | % | Use reported cost of risk where available. |

---

## 9. Liquidity and Funding Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---|---|
| Loan-to-deposit ratio | Loans to customers / Customer deposits | % | Ensure loan and deposit definitions are consistent across years. |

---

## 10. Capital Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---|---|
| CET1 ratio | Common Equity Tier 1 capital / Risk-weighted assets | % | Use official reported regulatory ratio. |
| Total capital ratio | Total regulatory capital / Risk-weighted assets | % | Use official reported regulatory ratio where available. |
| Leverage ratio | Tier 1 capital / Total exposure measure | % | Use official reported figure where available. |

---

## 11. Per-Share Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---|---|
| EPS | Net income attributable to shareholders / Average number of shares | EUR | Use reported EPS where available. |
| Book value per share | Equity attributable to shareholders / Number of shares | EUR | Ensure equity and share count definitions are consistent. |

---

## 12. Valuation Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---|---|
| Price-to-book | Market capitalisation / Equity attributable to shareholders | x | Common bank valuation multiple. Use dated market data. |
| Price-to-earnings | Market capitalisation / Net income attributable to shareholders | x | Use dated market data and consistent earnings. |
| Dividend yield | Dividend per share / Share price | % | Historical dividend yield does not guarantee future dividends. |
| Payout ratio | Dividends paid / Net income attributable to shareholders | % | Use only if dividend data is available and clearly sourced. |

---

## 13. Validation Status Definitions

| Status | Meaning |
|---|---|
| Pending | Figure has not yet been reviewed |
| Reviewed | Figure has been checked against a public source |
| Validated | Figure has been checked and can be used in final outputs |
| Needs Review | Figure requires further checking |
| Not Available | Figure was not found in available public sources |
| Calculated | Figure was calculated from public data |

---

## 14. Data Quality Principles

All data used in the project should follow these principles:

- use only public sources;
- document the source of each key figure;
- keep units consistent;
- separate actual figures from forecast estimates;
- separate reported figures from calculated figures;
- document formulas;
- document assumptions;
- review outputs before publication;
- avoid unsupported conclusions;
- avoid investment recommendation language.

---

## Disclaimer

This data dictionary is part of an educational financial modeling case study.

It does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.
