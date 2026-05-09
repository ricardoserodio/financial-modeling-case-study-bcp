# Data Validation Rules

This file defines the data validation rules used in the financial modeling case study on **Millennium bcp / Banco Comercial Português**.

The objective is to ensure that the financial model uses consistent, traceable and properly reviewed public-source data.

This project uses only publicly available information and does not include personal data, internal banking information or confidential information.

---

## 1. Source Validation

Each key financial figure must be traceable to a public source.

For each figure, the project should document:

| Field | Description |
|---|---|
| Financial item | Name of the metric or line item |
| Reporting period | Year or period used |
| Value | Reported or calculated value |
| Unit | EUR, EUR million, percentage, multiple, etc. |
| Source document | Annual report, presentation, financial statement or public market data source |
| Source type | Official report, regulatory filing, market data, etc. |
| Reported or calculated | Whether the figure is directly reported or calculated |
| Validation status | Pending, Reviewed or Validated |
| Notes | Any relevant assumptions, adjustments or limitations |

The source mapping file is:

`data/source_mapping.csv`

---

## 2. Source Priority

When sources provide overlapping information, the following priority order should be used:

1. Official annual report
2. Official financial statements
3. Official results presentation
4. Official press release
5. Regulatory filing
6. Exchange data
7. Public financial data provider
8. Financial news source

If two public sources show different values, the difference should be documented before using the figure in the model.

---

## 3. Public Information Only

The project may only use:

- annual reports;
- consolidated financial statements;
- investor presentations;
- market disclosures;
- public company announcements;
- public investor relations materials;
- public market data;
- regulatory disclosures;
- own calculations based on public information.

The project must not use:

- internal banking data;
- confidential information;
- employer data;
- client-level data;
- emails;
- screenshots of internal systems;
- private documents;
- information obtained through professional activity.

---

## 4. Unit Consistency

All figures must use consistent units.

Main model unit:

| Type | Preferred Unit |
|---|---|
| Income statement items | EUR million |
| Balance sheet items | EUR million |
| Capital figures | EUR million |
| Share price | EUR |
| Per-share figures | EUR |
| Ratios | % |
| Valuation multiples | x |

Validation checks:

- confirm whether the source reports in EUR, EUR thousand or EUR million;
- convert values where necessary;
- avoid mixing EUR and EUR million;
- avoid mixing decimals and percentages;
- clearly label all units in the model.

Example:

| Incorrect | Correct |
|---|---|
| 1,018.6 entered as EUR instead of EUR million | 1,018.6 EUR million |
| 0.15 shown as 0.15% instead of 15.0% | 15.0% |
| P/B shown as percentage | P/B shown as x |

---

## 5. Period Consistency

All data must be mapped to the correct reporting period.

The model uses:

| Period | Type |
|---|---|
| 2022A | Actual |
| 2023A | Actual |
| 2024A | Actual |
| 2025A | Actual |
| 2026E | Estimate |
| 2027E | Estimate |
| 2028E | Estimate |

Validation checks:

- do not mix quarterly and annual values without adjustment;
- do not mix 9M figures with full-year figures;
- clearly mark actual years and forecast years;
- ensure income statement figures are annual figures;
- ensure balance sheet figures are period-end figures unless stated otherwise;
- when using average balances, clearly document the calculation.

---

## 6. Reported vs Calculated Figures

The model must clearly distinguish between reported and calculated figures.

Examples of reported figures:

- net income;
- CET1 ratio;
- NPL / NPE ratio, where reported;
- cost-to-income ratio, where reported;
- total assets;
- customer deposits;
- loans to customers.

Examples of calculated figures:

- ROA;
- loan-to-deposit ratio;
- price-to-book;
- price-to-earnings;
- book value per share;
- dividend yield, where calculated from share price and dividend per share.

Validation checks:

- mark each figure as reported or calculated;
- document formulas for calculated figures;
- compare calculated ratios with reported ratios where possible;
- explain material differences.

---

## 7. Income Statement Validation

Income statement items should be reviewed for consistency.

Key items:

- net interest income;
- fees and commissions;
- other operating income;
- operating income;
- operating costs;
- impairments and provisions;
- profit before tax;
- net income.

Validation checks:

- confirm that figures are consolidated Group figures;
- confirm the sign convention for costs and impairments;
- avoid double-counting income items;
- check whether operating income matches the sum of relevant income lines;
- check whether net income is attributable to shareholders or total consolidated profit;
- document any non-recurring or exceptional items where relevant.

---

## 8. Balance Sheet Validation

Balance sheet items should be reviewed for consistency.

Key items:

- loans to customers;
- customer deposits;
- total assets;
- equity;
- risk-weighted assets;
- CET1 capital.

Validation checks:

- confirm whether loans are gross or net of impairments;
- use customer deposits consistently across years;
- distinguish total equity from equity attributable to shareholders;
- ensure total assets are consolidated Group figures;
- avoid mixing segment-level and Group-level data;
- document any changes in reporting definitions.

---

## 9. Ratio Validation

Each ratio must have a clear formula and consistent inputs.

Key validation checks:

| Ratio | Validation Rule |
|---|---|
| ROE | Use net income and average equity where possible |
| ROA | Use net income and average total assets where possible |
| Cost-to-income | Use operating costs and operating income consistently |
| NPL / NPE ratio | Prefer official reported ratio |
| Cost of risk | Confirm impairments and loan base definition |
| Loan-to-deposit ratio | Use consistent loans and deposits definition |
| CET1 ratio | Use official reported regulatory ratio |
| P/B | Use dated market data and consistent book value |
| P/E | Use dated market data and consistent net income |
| Dividend yield | Use dated share price and reported dividend per share |

---

## 10. Forecast Validation

Forecast figures must be clearly marked as estimates.

Forecast assumptions should be documented in:

`assumptions.md`

Validation checks:

- assumptions must be explicit;
- assumptions must be linked to historical trends or scenario logic;
- base, conservative and optimistic scenarios must be clearly separated;
- forecast outputs must not be presented as guaranteed outcomes;
- assumptions must avoid excessive optimism;
- sensitivity analysis should be used for key drivers.

---

## 11. Scenario Validation

The model should include three scenarios:

| Scenario | Validation Focus |
|---|---|
| Conservative | Lower profitability, higher risk or weaker efficiency |
| Base | Moderate continuation of current trends |
| Optimistic | Stronger performance but still plausible assumptions |

Validation checks:

- scenarios should differ logically;
- optimistic assumptions should remain realistic;
- conservative assumptions should not be extreme without explanation;
- each scenario should be documented;
- outputs should be presented as illustrative.

---

## 12. Market Data Validation

Market data should be dated and sourced.

Market data may include:

- share price;
- market capitalisation;
- number of shares;
- P/B;
- P/E;
- dividend yield;
- peer multiples.

Validation checks:

- record the date of market data;
- avoid mixing market data from different dates without explanation;
- prioritise Euronext or official public sources where possible;
- use secondary providers only for cross-checking;
- avoid presenting market multiples as fixed or permanent.

---

## 13. Peer Comparison Validation

Peer comparison should be treated with caution.

Validation checks:

- explain peer selection;
- avoid choosing only favourable peers;
- ensure peers are banks, not non-financial companies;
- document geography and business model differences;
- use peer comparison as context, not as a definitive valuation conclusion.

---

## 14. Bias and Human Review

The project should include a human review step to reduce errors and bias.

Key bias risks:

| Bias Type | Risk | Mitigation |
|---|---|---|
| Data bias | Using only favourable data | Use multi-year historical data |
| Selection bias | Choosing favourable peers | Explain peer selection criteria |
| Assumption bias | Overly optimistic forecasts | Use multiple scenarios |
| Confirmation bias | Forcing a preferred conclusion | Let the data drive the memo |
| Valuation bias | Choosing convenient multiples | Use sensitivity analysis |
| Source bias | Relying on weak sources | Prioritise official sources |
| AI output bias | Accepting generated analysis without review | Apply human review checklist |

The main review checklist is documented in:

`notes/model_review_checklist.md`

---

## 15. Publication Checklist

Before publishing any file to GitHub, confirm:

- no personal data is included;
- no internal banking information is included;
- no confidential information is included;
- no screenshots of internal systems are included;
- all key figures are traceable to public sources;
- actual data and forecast data are clearly separated;
- reported and calculated figures are clearly identified;
- assumptions are documented;
- limitations are stated;
- no investment recommendation language is used;
- the disclaimer is respected.

---

## 16. Validation Status

Suggested validation status labels:

| Status | Meaning |
|---|---|
| Pending | Figure has not yet been reviewed |
| Reviewed | Figure has been checked against a public source |
| Validated | Figure has been checked and can be used in final outputs |
| Needs Review | Figure requires further checking |
| Not Available | Figure was not found in available public sources |
| Calculated | Figure was calculated from public data |

---

## Disclaimer

These validation rules are part of an educational financial modeling case study.

They are designed to improve source traceability, data quality and responsible analysis.

They do not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.
