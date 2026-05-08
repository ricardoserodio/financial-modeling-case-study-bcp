# Sources

This file lists the public sources used for the financial modeling case study on **Millennium bcp / Banco Comercial Português**.

The project uses only publicly available information. No internal, confidential, client-level or non-public banking information is used.

---

## Source Usage Principles

The project follows these source usage principles:

- Use only public and verifiable information.
- Prioritise official company publications.
- Prioritise annual reports and financial statements for historical financial data.
- Use investor presentations for business context, management commentary and key performance indicators.
- Use market disclosures and public market data only when required for valuation inputs.
- Clearly distinguish between reported figures and own calculations.
- Do not copy full reports or reproduce copyrighted material.
- Reference sources instead of republishing source documents.

---

## Primary Official Sources

| Source | Type | Intended Use |
|---|---|---|
| Millennium bcp Annual Reports | Official annual reports | Historical financial statements, balance sheet data, income statement data, capital ratios, asset quality, business overview |
| Millennium bcp Quarterly Results | Official quarterly results page | Press releases, financial statements, earnings presentations, fact sheets and analyst conference materials |
| Millennium bcp Investor Relations | Official investor relations page | Investor materials, financial calendar, corporate information and shareholder information |
| Millennium bcp FY2025 Earnings Presentation | Official results presentation | 2025 financial performance, key ratios, profitability trends and management commentary |
| Millennium bcp 2025 Annual Report | Official annual report | Full-year 2025 financial statements, notes, risk information and governance information |

---

## Public Market and Regulatory Sources

| Source | Type | Intended Use |
|---|---|---|
| Euronext Lisbon | Public market data / exchange information | Share price, market information, listed company reference data and market disclosures |
| CMVM | Portuguese securities market regulator | Regulatory filings, market disclosures and official company communications |
| Banco de Portugal | Central bank / banking sector data | Portuguese banking sector context, macro-financial indicators and regulatory environment |
| European Banking Authority | European banking regulator | Banking sector indicators, prudential context and European regulatory references |
| European Central Bank | Central bank / supervisory authority | Euro area banking context, interest rate environment and macro-financial background |

---

## Secondary Public Sources

Secondary public sources may be used only for additional context or cross-checking, not as the primary source for reported company figures.

| Source | Type | Intended Use |
|---|---|---|
| Reuters | Financial news | Context on financial results, banking sector developments and market events |
| Yahoo Finance | Public market data provider | Share price history, market capitalisation and basic market multiples |
| MarketWatch | Public market data provider | Cross-checking selected market data |
| Investing.com | Public market data provider | Cross-checking selected market data |
| Company peer annual reports | Public company reports | Basic peer comparison, if relevant |

---

## Historical Period Covered

The financial model is expected to use the following structure:

| Period | Type | Description |
|---|---|---|
| 2022A | Actual | Full-year reported historical data |
| 2023A | Actual | Full-year reported historical data |
| 2024A | Actual | Full-year reported historical data |
| 2025A | Actual | Full-year reported historical data |
| 2026E | Estimate | Forecast year |
| 2027E | Estimate | Forecast year |
| 2028E | Estimate | Forecast year |

Since full-year 2025 results are available, the model should use **2025A** as an actual historical year instead of using **9M 2025A** as the latest reported period.

---

## Source Mapping Methodology

Each key financial figure used in the model should be mapped to a source.

The source mapping should identify:

- financial item;
- reported value;
- reporting period;
- source document;
- page or section, where available;
- whether the figure is reported or calculated;
- notes on assumptions or adjustments.

A separate file named `source_mapping.csv` will be used to document this mapping.

---

## Data Quality Checks

The project should include basic data validation checks, including:

- checking that reporting periods are consistent;
- checking whether values are reported in EUR, EUR thousand or EUR million;
- checking that calculated ratios match reported ratios where possible;
- checking that balance sheet and income statement items are not mixed incorrectly;
- checking whether ratios use average or year-end balances;
- documenting missing values;
- separating actual data from forecast assumptions;
- avoiding unsupported conclusions.

---

## Priority of Sources

When different sources provide overlapping information, the project should use the following priority order:

1. Official annual report
2. Official financial statements
3. Official earnings presentation
4. Official press release
5. Official regulatory filing
6. Exchange or regulator data
7. Public financial data providers
8. Financial news sources

---

## Notes

The model should not rely on private information, professional experience from any employer, internal banking systems, confidential documents or client-level information.

All figures must be traceable to public sources or clearly marked as own calculations or assumptions.

The project is for educational and portfolio purposes only and does not constitute investment advice.
