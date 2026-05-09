# Data Extraction Plan

This file defines the data extraction plan for the **Millennium bcp / Banco Comercial Português** financial modeling case study.

The purpose is to ensure that financial data is collected from public sources in a structured, consistent and traceable way before being used in the model.

This project uses only publicly available information and is for educational and portfolio purposes only.

---

## 1. Objective

The objective of the data extraction process is to collect the key financial figures required to build a simplified banking financial model.

The extracted data will be used for:

- historical financial analysis;
- banking ratio analysis;
- forecast assumptions;
- valuation multiples;
- source validation;
- data quality checks;
- investment-style memo preparation.

---

## 2. Historical Period

The project will use the following historical periods:

| Period | Type |
|---|---|
| 2022A | Actual |
| 2023A | Actual |
| 2024A | Actual |
| 2025A | Actual |

Forecast periods:

| Period | Type |
|---|---|
| 2026E | Estimate |
| 2027E | Estimate |
| 2028E | Estimate |

---

## 3. Primary Source Documents

The primary documents for data extraction should be official public sources.

Priority sources:

1. Millennium bcp Annual Report 2025
2. Millennium bcp Annual Report 2024
3. Millennium bcp Annual Report 2023
4. Millennium bcp Annual Report 2022
5. Millennium bcp FY2025 earnings presentation
6. Millennium bcp results presentations
7. Millennium bcp official press releases
8. Euronext public market data
9. CMVM regulatory disclosures

Secondary public sources may be used only for cross-checking market data or contextual information.

---

## 4. Income Statement Data to Extract

The following income statement items should be extracted:

| Item | Preferred Unit | Source Priority |
|---|---:|---|
| Net interest income | EUR million | Annual report / earnings presentation |
| Fees and commissions | EUR million | Annual report / earnings presentation |
| Other operating income | EUR million | Annual report |
| Operating income | EUR million | Annual report / earnings presentation |
| Operating costs | EUR million | Annual report / earnings presentation |
| Impairments and provisions | EUR million | Annual report |
| Profit before tax | EUR million | Annual report |
| Net income | EUR million | Annual report / earnings presentation |

Notes:

- Use consolidated Group figures.
- Check whether net income is attributable to shareholders.
- Document any difference between annual report and earnings presentation.
- Be careful with signs for costs and impairments.

---

## 5. Balance Sheet Data to Extract

The following balance sheet items should be extracted:

| Item | Preferred Unit | Source Priority |
|---|---:|---|
| Loans to customers | EUR million | Annual report |
| Customer deposits | EUR million | Annual report |
| Total assets | EUR million | Annual report |
| Equity | EUR million | Annual report |
| Risk-weighted assets | EUR million | Annual report / regulatory disclosure |
| CET1 capital | EUR million | Annual report / regulatory disclosure |

Notes:

- Confirm whether loans are gross or net.
- Use customer deposits consistently across years.
- Distinguish total equity from equity attributable to shareholders.
- Avoid mixing consolidated and segment-level data.

---

## 6. Banking Ratios to Extract or Calculate

The following banking ratios should be collected or calculated:

| Ratio | Source / Calculation |
|---|---|
| ROE | Use reported figure where available; otherwise calculate |
| ROA | Calculate from net income and average assets |
| Cost-to-income | Use reported figure where available; otherwise calculate |
| Net interest margin | Use reported figure where available |
| Cost of risk | Use reported figure where available |
| NPL / NPE ratio | Use official reported figure |
| NPL / NPE coverage ratio | Use official reported figure where available |
| Loan-to-deposit ratio | Calculate from loans and deposits |
| CET1 ratio | Use official reported regulatory figure |
| Total capital ratio | Use official reported regulatory figure where available |
| EPS | Use reported figure where available |
| Book value per share | Calculate if inputs are available |

Notes:

- Reported ratios should be preferred when regulatory definitions are complex.
- Calculated ratios must include formula documentation.
- If reported and calculated ratios differ, document the difference.

---

## 7. Market Data to Extract

The following market data may be extracted for valuation:

| Item | Preferred Unit | Source |
|---|---:|---|
| Share price | EUR | Euronext / public market data |
| Market capitalisation | EUR million | Euronext / public market data |
| Number of shares | million shares | Annual report / market data |
| Dividend per share | EUR | Annual report / company disclosure |
| P/B multiple | x | Calculated |
| P/E multiple | x | Calculated |
| Dividend yield | % | Calculated |

Notes:

- Market data must be dated.
- Use the same valuation date for share price and market capitalisation.
- Market data changes over time and should not be treated as permanent.

---

## 8. Source Mapping Requirements

Every extracted figure should be recorded in:

`data/source_mapping.csv`

Each entry should include:

- item;
- category;
- period;
- value;
- unit;
- source document;
- source type;
- source section or page, where available;
- reported or calculated status;
- calculation method, where applicable;
- validation status;
- notes.

---

## 9. Extraction Workflow

Recommended workflow:

1. Open the official annual report.
2. Identify the consolidated financial statements.
3. Extract income statement figures.
4. Extract balance sheet figures.
5. Extract capital and asset quality ratios.
6. Cross-check key metrics with earnings presentation.
7. Enter values into `data/historical_financials.csv`.
8. Enter ratios into `data/banking_ratios.csv`.
9. Map each figure in `data/source_mapping.csv`.
10. Run `data/validation_checks.py`.
11. Review flagged issues.
12. Mark figures as Reviewed or Validated.

---

## 10. Data Validation Questions

Before accepting a figure into the model, answer:

- Is the source public?
- Is the source official?
- Is the reporting period correct?
- Is the value consolidated?
- Is the unit correct?
- Is the figure reported or calculated?
- Is the formula documented?
- Is the figure comparable across years?
- Is there any conflict between sources?
- Is the figure mapped in `source_mapping.csv`?

---

## 11. Common Extraction Risks

| Risk | Mitigation |
|---|---|
| Mixing EUR and EUR million | Standardise units before entering the model |
| Mixing quarterly and annual figures | Use only full-year data for historical years |
| Mixing segment and Group data | Use consolidated Group figures |
| Mixing gross and net loans | Document loan definition |
| Mixing total equity and shareholder equity | Use one definition consistently |
| Using outdated market data | Date all market inputs |
| Copying unsupported figures | Map each figure to a public source |
| Using investment advice language | Keep analysis educational and neutral |

---

## 12. Human Review Step

After extraction, the reviewer should confirm:

- source traceability;
- unit consistency;
- period consistency;
- formula logic;
- ratio consistency;
- no personal data;
- no internal information;
- no investment recommendation wording.

This review step supports the project’s human-in-the-loop approach.

---

## Disclaimer

This data extraction plan is part of an educational financial modeling case study.

It uses only publicly available information and does not include personal data, internal banking information or confidential information.

The project does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.
