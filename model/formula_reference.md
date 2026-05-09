# Formula Reference

This document defines the main formulas used in the **Millennium bcp / Banco Comercial Português** financial modeling case study.

The purpose is to make the model transparent, auditable and easy to review.

This project is for educational and portfolio purposes only and does not constitute investment advice.

---

## 1. Purpose

The formula reference supports:

- financial model transparency;
- ratio validation;
- source documentation;
- human review;
- data quality checks;
- clear separation between reported, calculated and estimated figures.

Where possible, reported figures from official public sources should be preferred. Calculated figures should be used only when the formula and inputs are clearly documented.

---

## 2. Income Statement Formulas

| Item | Formula / Logic | Notes |
|---|---|---|
| Operating income | Net interest income + fees and commissions + other operating income | Use reported figure where available |
| Operating profit before impairments | Operating income - operating costs | Check sign convention |
| Profit before tax | Operating profit before impairments - impairments and provisions | Use reported figure where available |
| Net income | Profit after tax and minority interests, where applicable | Use consistent definition across years |

---

## 3. Balance Sheet Formulas

| Item | Formula / Logic | Notes |
|---|---|---|
| Total assets | Reported consolidated total assets | Use annual report figure |
| Loans to customers | Reported customer loan book | Confirm gross or net definition |
| Customer deposits | Reported customer deposits | Use consistent definition across years |
| Equity | Reported total equity or equity attributable to shareholders | Document definition used |
| Average equity | (Equity current year + equity previous year) / 2 | Used for ROE if reported ROE is unavailable |
| Average assets | (Total assets current year + total assets previous year) / 2 | Used for ROA if reported ROA is unavailable |

---

## 4. Profitability Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---:|---|
| ROE | Net income / average equity | % | Prefer reported ROE where available |
| ROA | Net income / average total assets | % | Calculate only with consistent average asset data |
| Net interest margin | Net interest income / average interest-earning assets | % | Prefer reported figure due to definition complexity |

---

## 5. Efficiency Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---:|---|
| Cost-to-income | Operating costs / operating income | % | Use absolute value of costs if costs are reported as negative |
| Cost growth | Current year operating costs / prior year operating costs - 1 | % | Check sign convention before calculating |
| Operating leverage | Revenue growth - cost growth | percentage points | Optional analytical metric |

---

## 6. Asset Quality Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---:|---|
| Cost of risk | Loan impairments / average loans to customers | % or bps | Prefer reported figure where available |
| NPL / NPE ratio | Non-performing loans or exposures / total loans or exposures | % | Use official reported definition |
| NPL / NPE coverage ratio | Impairment allowances / non-performing loans or exposures | % | Use official reported definition where available |

---

## 7. Liquidity and Funding Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---:|---|
| Loan-to-deposit ratio | Loans to customers / customer deposits | % | Use consistent customer loan and deposit definitions |
| Deposit growth | Current year deposits / prior year deposits - 1 | % | Use customer deposits only |
| Loan growth | Current year loans / prior year loans - 1 | % | Confirm gross or net loans |

---

## 8. Capital Ratios

| Ratio | Formula | Unit | Notes |
|---|---|---:|---|
| CET1 ratio | Common Equity Tier 1 capital / risk-weighted assets | % | Prefer official reported regulatory ratio |
| Total capital ratio | Total capital / risk-weighted assets | % | Prefer official reported regulatory ratio |
| Leverage ratio | Tier 1 capital / leverage exposure | % | Prefer official reported regulatory ratio where available |

---

## 9. Per-Share Data

| Item | Formula | Unit | Notes |
|---|---|---:|---|
| Earnings per share | Net income attributable to shareholders / weighted average shares | EUR | Prefer reported EPS where available |
| Book value per share | Equity attributable to shareholders / number of shares | EUR | Use consistent share count |
| Dividend per share | Total dividend / number of shares | EUR | Prefer reported DPS where available |

---

## 10. Valuation Multiples

| Multiple | Formula | Unit | Notes |
|---|---|---:|---|
| Price-to-book | Market capitalisation / equity attributable to shareholders | x | Use market data from selected valuation date |
| Price-to-earnings | Market capitalisation / net income attributable to shareholders | x | Use positive and normalised earnings only where meaningful |
| Dividend yield | Dividend per share / share price | % | Use same valuation date for share price |
| Payout ratio | Dividends paid / net income attributable to shareholders | % | Use consistent dividend and earnings definitions |

---

## 11. Forecast Formulas

| Forecast Item | Formula / Logic | Notes |
|---|---|---|
| Forecast net interest income | Prior year net interest income x (1 + NII growth assumption) | Scenario-driven |
| Forecast fees and commissions | Prior year fees and commissions x (1 + fee growth assumption) | Scenario-driven |
| Forecast operating costs | Prior year operating costs x (1 + cost growth assumption) | Scenario-driven |
| Forecast loans | Prior year loans x (1 + loan growth assumption) | Scenario-driven |
| Forecast deposits | Prior year deposits x (1 + deposit growth assumption) | Scenario-driven |
| Forecast equity | Prior year equity + retained earnings | Simplified educational approach |
| Forecast net income | Derived from operating income, costs, impairments and tax logic | Simplified educational approach |

---

## 12. Scenario Analysis Logic

The model uses three educational scenarios:

| Scenario | Description |
|---|---|
| Conservative | Lower revenue growth, higher cost pressure, higher cost of risk or lower valuation multiples |
| Base | Moderate continuation of current trends based on public information |
| Optimistic | Stronger profitability, better efficiency, lower cost of risk or higher valuation multiples |

Scenario outputs should be presented as illustrative ranges, not as predictions.

---

## 13. Validation Rules for Formulas

Before accepting a formula output, check:

- are all input figures sourced or clearly calculated?
- are units consistent?
- are percentages and decimals correctly applied?
- are costs and impairments using the correct sign?
- are actual and forecast figures separated?
- are market data inputs dated?
- are calculated ratios reasonable compared with reported ratios?
- is the output presented neutrally and not as investment advice?

---

## 14. Common Formula Risks

| Risk | Example | Mitigation |
|---|---|---|
| Unit mismatch | EUR vs EUR million | Standardise units before calculation |
| Sign error | Operating costs entered as negative and subtracted again | Check sign convention |
| Wrong denominator | ROE using ending equity instead of average equity | Document denominator |
| Mixed periods | 9M result compared with full-year result | Use full-year data for actual years |
| Market date mismatch | Share price and market cap from different dates | Use one valuation date |
| Regulatory definition mismatch | Calculating CET1 differently from reported figure | Prefer official reported ratio |
| Overconfidence | Treating forecast as prediction | Use scenario language |

---

## Disclaimer

This formula reference is part of an educational financial modeling case study.

It uses only publicly available information and does not include personal data, internal banking information or confidential information.

The project does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.
