# Banking Model Structure

This file documents the intended structure of the simplified banking financial model for **Millennium bcp / Banco Comercial Português**.

The Excel model will be created in:

`model/banking_model.xlsx`

The model is for educational and portfolio purposes only and does not constitute investment advice.

---

## Model Objective

The objective of the banking model is to demonstrate a simplified financial modeling approach for a listed bank using only publicly available information.

The model will cover:

- historical financials;
- banking income statement items;
- balance sheet drivers;
- key banking ratios;
- forecast assumptions;
- scenario analysis;
- valuation multiples;
- sensitivity analysis;
- source validation.

---

## Model Period

The model will use the following period structure:

| Period | Type | Description |
|---|---|---|
| 2022A | Actual | Reported historical year |
| 2023A | Actual | Reported historical year |
| 2024A | Actual | Reported historical year |
| 2025A | Actual | Reported historical year |
| 2026E | Estimate | Forecast year |
| 2027E | Estimate | Forecast year |
| 2028E | Estimate | Forecast year |

---

## Excel Workbook Tabs

The Excel workbook should include the following tabs:

| Tab | Purpose |
|---|---|
| `Cover` | Model title, author, purpose and disclaimer |
| `Sources` | Summary of public sources used |
| `Historical Financials` | Reported historical income statement and balance sheet data |
| `Ratios` | Banking ratios for profitability, efficiency, asset quality, liquidity, capital and valuation |
| `Assumptions` | Forecast assumptions for 2026E–2028E |
| `Forecast` | Simplified forecast for income statement, balance sheet and ratios |
| `Scenarios` | Conservative, Base and Optimistic scenarios |
| `Valuation` | Price-to-book, price-to-earnings and dividend yield logic |
| `Sensitivity` | Sensitivity tables for key assumptions |
| `Checks` | Data quality and consistency checks |

---

## 1. Cover Tab

The `Cover` tab should include:

- project title;
- company analysed;
- model period;
- author;
- purpose;
- disclaimer;
- last update date.

Suggested disclaimer:

> This model is for educational and portfolio purposes only and does not constitute investment advice.

---

## 2. Sources Tab

The `Sources` tab should summarise the public sources used in the model.

It should include:

| Field | Description |
|---|---|
| Source name | Name of the public source |
| Source type | Annual report, presentation, market data, regulator, exchange |
| Year / period | Reporting period |
| Used for | Financials, ratios, market data, valuation, context |
| Link / reference | Public source reference |
| Notes | Any relevant validation notes |

---

## 3. Historical Financials Tab

The `Historical Financials` tab should include the main historical financial data.

Expected income statement items:

| Item | Description |
|---|---|
| Net interest income | Core banking interest income net of interest expense |
| Fees and commissions | Non-interest client-related income |
| Other operating income | Other banking income items |
| Operating income | Total banking income / operating income |
| Operating costs | Staff, administrative and operating expenses |
| Impairments and provisions | Credit impairments and other provisions |
| Profit before tax | Profit before income tax |
| Net income | Consolidated net income |

Expected balance sheet items:

| Item | Description |
|---|---|
| Loans to customers | Customer loan book |
| Customer deposits | Customer deposit base |
| Total assets | Consolidated total assets |
| Equity | Total equity or equity attributable to shareholders |
| Risk-weighted assets | Used for capital analysis, if available |
| CET1 capital | Used for CET1 validation, if available |

---

## 4. Ratios Tab

The `Ratios` tab should include key banking ratios.

| Ratio | Category |
|---|---|
| ROE | Profitability |
| ROA | Profitability |
| Net interest margin | Profitability |
| Cost-to-income | Efficiency |
| Cost of risk | Asset quality |
| NPL / NPE ratio | Asset quality |
| NPL coverage ratio | Asset quality |
| Loan-to-deposit ratio | Liquidity / Funding |
| CET1 ratio | Capital |
| Total capital ratio | Capital |
| EPS | Per share |
| Book value per share | Per share |
| Price-to-book | Valuation |
| Price-to-earnings | Valuation |
| Dividend yield | Valuation / Capital return |
| Payout ratio | Capital return |

---

## 5. Assumptions Tab

The `Assumptions` tab should document all forecast assumptions for 2026E–2028E.

Assumption areas:

- net interest income growth;
- fees and commissions growth;
- other operating income;
- operating cost growth;
- impairments and provisions;
- cost of risk;
- loan growth;
- deposit growth;
- equity evolution;
- dividend / payout assumptions, if applicable;
- valuation multiples.

Each assumption should be clearly separated by scenario:

| Assumption | Conservative | Base | Optimistic |
|---|---:|---:|---:|
| Net interest income growth | Pending | Pending | Pending |
| Fees and commissions growth | Pending | Pending | Pending |
| Operating cost growth | Pending | Pending | Pending |
| Cost of risk | Pending | Pending | Pending |
| Loan growth | Pending | Pending | Pending |
| Deposit growth | Pending | Pending | Pending |

---

## 6. Forecast Tab

The `Forecast` tab should calculate the estimated financials for:

- 2026E;
- 2027E;
- 2028E.

The forecast should link directly to the assumptions tab.

Forecast outputs should include:

- income statement forecast;
- balance sheet forecast;
- selected banking ratios;
- capital-related outputs, where possible;
- valuation inputs.

Forecast years must be clearly marked as estimates.

---

## 7. Scenarios Tab

The `Scenarios` tab should compare:

| Scenario | Description |
|---|---|
| Conservative | Lower profitability, weaker revenue growth, higher cost pressure or higher cost of risk |
| Base | Moderate continuation of recent trends based on public information |
| Optimistic | Stronger profitability, better efficiency, lower cost of risk or stronger revenue growth |

The model should avoid presenting any scenario as a guaranteed outcome.

---

## 8. Valuation Tab

The `Valuation` tab should include a simplified educational valuation.

Potential methods:

| Method | Description |
|---|---|
| Price-to-book | Market value compared with book value |
| Price-to-earnings | Market value compared with net income |
| Dividend yield | Dividend per share compared with share price |
| Peer comparison | Optional market context |
| Scenario valuation | Conservative, Base and Optimistic outcomes |

The valuation must not include investment recommendation language.

Avoid:

- buy;
- sell;
- hold;
- target price;
- guaranteed upside;
- investment opportunity.

Use:

- illustrative valuation range;
- scenario-based analysis;
- sensitivity-based approach;
- educational valuation exercise.

---

## 9. Sensitivity Tab

The `Sensitivity` tab should test how valuation or key outputs change when assumptions change.

Possible sensitivity variables:

| Variable | Purpose |
|---|---|
| ROE | Key driver of bank valuation |
| Cost of equity | Important valuation assumption |
| Earnings growth | Affects earnings-based valuation |
| Cost-to-income | Affects profitability |
| Cost of risk | Affects impairments and net income |
| P/B multiple | Affects book-value-based valuation |
| P/E multiple | Affects earnings-based valuation |
| Dividend payout | Affects dividend yield and retained capital |

---

## 10. Checks Tab

The `Checks` tab should include model validation checks.

Suggested checks:

| Check | Purpose |
|---|---|
| Source check | Confirm all key figures are mapped to public sources |
| Unit check | Confirm EUR, EUR million and percentage consistency |
| Period check | Confirm correct year / reporting period |
| Formula check | Confirm formulas are consistent |
| Ratio check | Compare reported ratios with calculated ratios |
| Balance check | Confirm balance sheet figures are logical |
| Scenario check | Confirm assumptions differ correctly across scenarios |
| Disclaimer check | Confirm no investment advice language is used |

---

## Data Quality Rules

The model should follow these data quality rules:

- use only public information;
- document each source;
- separate actual data from estimates;
- separate reported figures from calculated figures;
- keep units consistent;
- avoid unsupported conclusions;
- apply human review before publication.

---

## Final Model Output

The final model should allow a reviewer to understand:

- how historical data was collected;
- how key ratios were calculated;
- what assumptions drive the forecast;
- how scenarios affect the model;
- how valuation multiples are applied;
- what limitations exist;
- how source validation was performed.

---

## Disclaimer

This model structure is part of an educational financial modeling case study.

It uses only publicly available information and does not include personal data, internal banking information or confidential information.

The model does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.
