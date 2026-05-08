# Model Review Checklist

This checklist defines the human review process used in this financial modeling case study.

The purpose is to reduce errors, avoid unsupported conclusions, improve financial data quality and ensure that the project remains suitable for educational and portfolio purposes.

---

## 1. Source Validation

Before using any financial figure in the model, check:

- Is the figure based on a public source?
- Is the source official or reliable?
- Is the source documented in `sources.md`?
- Is the figure mapped in `source_mapping.csv`?
- Is the reporting period clearly identified?
- Is the figure reported or calculated?
- Is there any difference between the annual report, results presentation and press release?

Priority of sources:

1. Official annual report
2. Official financial statements
3. Official results presentation
4. Official press release
5. Regulatory filing
6. Exchange data
7. Public financial data provider
8. Financial news source

---

## 2. Unit Consistency

Before entering figures into the model, check:

- Are figures reported in EUR, EUR thousand or EUR million?
- Are all model figures converted into the same unit?
- Are percentages entered consistently?
- Are ratios expressed as percentages or decimals?
- Are market values and accounting values clearly separated?
- Are period-end values and average values clearly distinguished?

Example checks:

- Net income should not be mixed between EUR and EUR million.
- CET1 ratio should be treated as a percentage.
- Price-to-book should use market capitalisation and book value consistently.
- ROE should ideally use average equity, where available.

---

## 3. Historical Financials Review

For each historical year, check:

- Are income statement items complete?
- Are balance sheet items complete?
- Are loans, deposits, total assets and equity correctly classified?
- Are impairments and provisions correctly identified?
- Are net interest income and fees clearly separated?
- Are consolidated Group figures used consistently?
- Are figures comparable across years?

Historical periods used:

| Period | Type |
|---|---|
| 2022A | Actual |
| 2023A | Actual |
| 2024A | Actual |
| 2025A | Actual |
| 2026E | Estimate |
| 2027E | Estimate |
| 2028E | Estimate |

---

## 4. Ratio Calculation Review

For each calculated ratio, check:

- Is the formula clearly defined?
- Does the ratio use the correct numerator and denominator?
- Is the denominator positive and meaningful?
- Is the ratio based on year-end or average balances?
- Does the calculated ratio match the reported ratio, where available?
- If there is a difference, is the difference explained?

Key ratios to review:

| Ratio | Review Focus |
|---|---|
| ROE | Net income and equity consistency |
| ROA | Net income and total assets consistency |
| Cost-to-income | Operating costs and operating income consistency |
| CET1 ratio | Use official reported figure |
| NPL / NPE ratio | Use official reported figure where possible |
| Loan-to-deposit ratio | Loans and customer deposits consistency |
| Cost of risk | Impairments and loan book consistency |
| EPS | Net income and share count consistency |
| Book value per share | Equity and share count consistency |
| P/B | Market capitalisation and book value consistency |
| P/E | Market capitalisation and net income consistency |

---

## 5. Forecast Assumption Review

For each forecast assumption, check:

- Is the assumption reasonable?
- Is the assumption based on historical trends?
- Is the assumption clearly documented in `assumptions.md`?
- Is the assumption too optimistic or too conservative?
- Is the assumption linked to a business driver?
- Is the same logic applied consistently across forecast years?
- Are base, conservative and optimistic scenarios clearly separated?

Forecast areas to review:

- Net interest income growth
- Fees and commissions growth
- Operating cost growth
- Cost-to-income ratio
- Impairments and provisions
- Cost of risk
- Loan growth
- Deposit growth
- Equity evolution
- Capital ratio assumptions
- Dividend or payout assumptions, if applicable

---

## 6. Bias Review

The model should be reviewed for common bias risks.

| Bias Type | Risk in This Project | Mitigation |
|---|---|---|
| Data bias | Using only favourable years or metrics | Use a multi-year historical period |
| Selection bias | Choosing only favourable peer comparisons | Explain peer selection criteria |
| Assumption bias | Forecasting overly optimistic outcomes | Use base, conservative and optimistic scenarios |
| Confirmation bias | Starting from a desired conclusion | Let the data drive the conclusion |
| Valuation bias | Selecting convenient multiples | Use sensitivity analysis and ranges |
| Source bias | Relying on secondary sources | Prioritise official public sources |
| AI output bias | Accepting generated analysis without review | Apply human review before publication |

---

## 7. Valuation Review

Before presenting any valuation output, check:

- Is the valuation clearly educational?
- Are valuation multiples appropriate for a bank?
- Are P/B and P/E calculations consistent?
- Are market data inputs dated and sourced?
- Are sensitivity ranges shown?
- Are outputs presented as scenarios rather than recommendations?
- Does the wording avoid buy, sell or hold language?
- Is the conclusion analytical rather than promotional?

Avoid wording such as:

- Buy
- Sell
- Hold
- Target price
- Undervalued as a recommendation
- Overvalued as a recommendation
- Investment opportunity
- Guaranteed upside

Preferred wording:

- Illustrative scenario
- Educational valuation exercise
- Sensitivity range
- Based on simplified assumptions
- Subject to limitations
- Not investment advice

---

## 8. Human-in-the-Loop Review

This project uses a human-in-the-loop review approach.

Before publishing any final output, the reviewer should confirm:

- The source is public.
- The figure is correctly extracted.
- The unit is correct.
- The formula is correct.
- The assumption is documented.
- The conclusion is supported by the data.
- The wording avoids investment advice.
- The analysis does not use internal or confidential information.
- The final output is suitable for a public GitHub portfolio.

Review flow:

Public source → Data extraction → Model input → Ratio calculation → Forecast assumption → Scenario analysis → Human review → Final publication

---

## 9. Final Publication Checklist

Before committing a file to GitHub, confirm:

- No personal data is included.
- No internal banking information is included.
- No confidential information is included.
- No screenshots of internal systems are included.
- No employer-specific internal information is included.
- All key figures are traceable to public sources.
- All assumptions are documented.
- All limitations are stated.
- The disclaimer is respected.
- The file is professionally written.
- The content is suitable for CV, LinkedIn and recruiter review.

---

## 10. Reviewer Sign-Off

For each major project file, the reviewer should confirm:

| File | Review Required |
|---|---|
| `historical_financials.csv` | Source, units and periods |
| `banking_ratios.csv` | Ratio formulas and consistency |
| `source_mapping.csv` | Source traceability |
| `banking_model.xlsx` | Model logic and assumptions |
| `sensitivity_analysis.xlsx` | Sensitivity inputs and outputs |
| `ratio_analysis.md` | Ratio interpretation |
| `valuation_summary.md` | Valuation language and limitations |
| `investment_memo.md` | Final wording and no-investment-advice check |

---

## Purpose of This Checklist

This checklist strengthens the project by showing that the financial model is not only built, but also reviewed.

It demonstrates awareness of:

- financial data quality;
- source validation;
- model risk;
- assumption risk;
- bias mitigation;
- human oversight;
- AI finance evaluation;
- responsible financial communication.

This is especially relevant for financial research, banking analytics, financial data validation and AI finance evaluation roles.
