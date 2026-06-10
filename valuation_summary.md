# Valuation Summary – Millennium bcp / Portuguese Listed Bank

## 1. Purpose

This document presents an educational valuation framework for the Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank project.

The purpose of this file is to explain how valuation could be approached in an educational banking analysis context, while avoiding unsupported market claims, target prices or investment recommendations.

This document is part of a public portfolio project focused on:

- Banking analytics
- Financial modeling
- Financial data quality
- Scenario analysis
- SQL and Power BI reporting
- Human-reviewed analytical workflows

This is not an investment recommendation.

---

## 2. Important Disclaimer

This document is for educational, analytical and portfolio purposes only.

It does not constitute:

- Financial advice
- Investment advice
- Valuation advice
- A target price
- A recommendation to buy, sell or hold any financial instrument
- Official research
- Official projections from Millennium bcp

The author is not affiliated with Millennium bcp for the purpose of this project.

All valuation logic, assumptions and potential future outputs require human review before any professional use.

---

## 3. Scope of the Current Version

This version includes:

- A banking valuation framework
- The rationale for using P/B and P/E in bank analysis
- A conservative approach to market data validation
- Scenario logic for future valuation work
- Clear limitations and data quality notes

This version does not include final calculated market multiples because dated market data has not yet been selected and validated.

The following valuation metrics are therefore not calculated in this version:

- Price-to-book
- Price-to-earnings
- Dividend yield
- Market capitalisation-based valuation
- Peer multiple comparison
- Implied valuation range

These metrics can be added in a future version after selecting a specific market data date and documenting the exact source.

---

## 4. Why Valuation Requires Additional Validation

Unlike historical banking ratios, valuation multiples depend on market data that changes over time.

For example:

- Share price changes daily
- Market capitalisation changes with share price and number of shares
- P/E depends on both share price and earnings per share
- P/B depends on both share price and book value per share
- Dividend yield depends on share price and dividend per share
- Peer multiples depend on selected comparable banks and the observation date

Because of this, valuation metrics should not be presented without a clear date and source.

---

## 5. Market Data Inputs Required

Before calculating valuation multiples, the following inputs should be collected and validated.

| Input | Description | Current Status |
|---|---|---|
| Share price | Public market price at a selected date | Not included in current version |
| Market capitalisation | Equity market value at a selected date | Not included in current version |
| Number of shares | Shares outstanding or weighted average shares | Not included in current version |
| Earnings per share | Reported EPS from public-source data | Available in structured ratio dataset |
| Book value per share | Reported book value per share from public-source data | Available from 2023A onward in structured ratio dataset |
| Dividend per share | Reported or declared dividend per share | To be validated |
| Peer valuation multiples | Public data from comparable banks, if used | Not included in current version |

---

## 6. Available Per-Share Inputs

The structured dataset `data/banking_ratios.csv` includes selected per-share indicators.

| Metric | 2022A | 2023A | 2024A | 2025A | Unit | Status |
|---|---:|---:|---:|---:|---|---|
| EPS | 0.011 | 0.056 | 0.058 | 0.066 | EUR | Reviewed |
| Book value per share | n/a | 0.412 | 0.469 | 0.528 | EUR | Reviewed |

These figures can support future valuation calculations once a dated share price is selected.

---

## 7. Banking Valuation Methods Considered

### 7.1 Price-to-Book Ratio

Price-to-book is commonly used in bank valuation because banks are balance-sheet intensive institutions.

Formula:

`P/B = Share price / Book value per share`

Interpretation:

- A higher P/B may suggest stronger expected profitability, asset quality, capital generation or franchise value.
- A lower P/B may suggest weaker profitability, higher perceived risk, lower expected returns or market scepticism.
- P/B should be interpreted together with ROE and cost of equity.

In banking analysis, P/B is often linked to the relationship between ROE and cost of equity.

---

### 7.2 Price-to-Earnings Ratio

Price-to-earnings compares market price with earnings per share.

Formula:

`P/E = Share price / Earnings per share`

Interpretation:

- A higher P/E may suggest stronger expected earnings growth, lower perceived risk or higher investor confidence.
- A lower P/E may suggest lower growth expectations, earnings quality concerns or higher perceived risk.
- P/E can be distorted by one-off earnings, impairments, restructuring costs or exceptional tax impacts.

For banks, P/E should be reviewed together with earnings quality, capital strength, asset quality and interest rate sensitivity.

---

### 7.3 Dividend Yield

Dividend yield compares dividend per share with market price.

Formula:

`Dividend yield = Dividend per share / Share price`

Interpretation:

- A higher dividend yield may be attractive from an income perspective.
- However, dividend yield must be assessed together with payout ratio, capital requirements, profitability sustainability and regulatory constraints.
- A high dividend yield can also reflect a lower share price or higher perceived risk.

Dividend yield is not calculated in this version until dividend data and share price data are both validated.

---

## 8. Illustrative Scenario Framework

The project includes forecast scenarios for educational purposes:

- Conservative
- Base
- Optimistic

These scenarios are useful for understanding how different assumptions may affect future profitability, efficiency, credit risk and capital metrics.

However, this version does not convert those scenarios into an implied share price or valuation range.

| Scenario | Description | Valuation Output | Comment |
|---|---|---|---|
| Conservative | Lower profitability and/or lower valuation multiple | Not calculated in current version | Educational scenario only |
| Base | Balanced assumptions | Not calculated in current version | Educational scenario only |
| Optimistic | Stronger profitability and/or higher valuation multiple | Not calculated in current version | Educational scenario only |

---

## 9. Why No Target Price Is Included

This project intentionally does not include a target price.

Reasons:

- The project is educational and portfolio-oriented.
- Market prices change over time.
- Valuation outputs require dated market data.
- Peer selection can materially influence valuation ranges.
- Assumptions require professional judgement and human review.
- The project should not be interpreted as investment research or investment advice.

Instead, the project focuses on showing a robust analytical workflow.

---

## 10. Optional Future Valuation Extension

An optional future version may include a dated valuation snapshot after the required market data has been selected and validated.

That extension should include:

1. Selected valuation date
2. Share price source
3. Number of shares source
4. EPS and book value per share source
5. Calculated P/E
6. Calculated P/B
7. Dividend yield, if validated
8. Peer group selection
9. Peer multiple table
10. Sensitivity table
11. Clear disclaimer

Suggested future structure:

| Metric | Value | Source | Date | Status |
|---|---:|---|---|---|
| Share price | To be added | To be added | To be added | To be validated |
| EPS | Available in structured dataset | data/banking_ratios.csv | 2025A | Reviewed |
| Book value per share | Available in structured dataset | data/banking_ratios.csv | 2025A | Reviewed |
| P/E | To be calculated | Based on share price and EPS | To be added | To be validated |
| P/B | To be calculated | Based on share price and BVPS | To be added | To be validated |

---

## 11. Data Quality Notes

Valuation work should follow the same data quality principles used across the project:

- Use public sources only.
- Document the exact source.
- Document the observation date.
- Separate reported figures from calculated figures.
- Avoid unsupported precision.
- Do not present assumptions as facts.
- Do not imply an investment recommendation.
- Use human review before publishing final conclusions.

---

## 12. Portfolio Relevance

This valuation summary demonstrates:

- Awareness of banking valuation methods
- Understanding of market data limitations
- Ability to separate historical reported ratios from market-based valuation metrics
- Conservative analytical judgement
- Data quality discipline
- Responsible communication in a regulated financial context

This is relevant for roles in:

- Banking Analytics
- Financial Data Quality
- Finance Transformation
- Investment Support
- Financial Research Support
- Risk and Regulatory Reporting
- Power BI / SQL Finance Analytics

---

## 13. Conclusion

The current version provides a responsible valuation framework without presenting unsupported market multiples or target prices.

An optional future step would be to create a dated valuation snapshot using validated public market data.

Until then, valuation multiples remain excluded from the current version to preserve analytical integrity and avoid misleading conclusions.

---

## 14. Disclaimer

This document is for educational, analytical and portfolio purposes only.

It does not constitute financial advice, investment advice, valuation advice, legal advice or a recommendation to buy, sell or hold any financial instrument.

The author is not affiliated with Millennium bcp for the purpose of this project.

All figures, assumptions, interpretations and potential future valuation outputs require human review before publication or professional use.
