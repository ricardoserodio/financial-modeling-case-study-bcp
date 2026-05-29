# Ratio Analysis – Millennium bcp / Portuguese Listed Bank

## 1. Purpose

This document presents a structured ratio analysis for the Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank project.

The objective is to analyse selected historical banking ratios using public-source structured data and to explain the main profitability, efficiency, asset quality, liquidity, capital and per-share indicators used in the case study.

This analysis is for educational, portfolio and professional development purposes only.

It does not constitute financial advice, investment advice, valuation advice, credit advice, legal advice or a recommendation to buy, sell or hold any financial instrument.

---

## 2. Data Source and Review Status

The ratio analysis is based on the structured dataset:

`data/banking_ratios.csv`

The dataset includes selected reported ratios for:

`2022A | 2023A | 2024A | 2025A`

Where available, the ratios are based on public-source reported figures from Millennium bcp official public materials and are marked as reviewed in the structured dataset.

Some valuation-related metrics remain excluded from this version until dated market data is selected and validated.

For detailed definitions and interpretation notes, see:

`docs/banking_ratio_glossary.md`

---

## 3. Historical Banking Ratio Summary

| Ratio | Category | 2022A | 2023A | 2024A | 2025A | Unit | Status |
|---|---|---:|---:|---:|---:|---|---|
| ROE | Profitability | 4.0 | 15.1 | 13.8 | 14.1 | % | Reviewed |
| ROA | Profitability | 0.1 | 1.0 | 1.0 | 1.1 | % | Reviewed |
| Net interest margin | Profitability | 2.46 | 3.17 | 3.04 | 2.89 | % | Reviewed |
| Cost-to-income ratio | Efficiency | 37.4 | 30.8 | 36.5 | 37.1 | % | Reviewed |
| Cost-to-income ratio excluding specific items | Efficiency | 36.8 | 30.2 | 36.2 | 36.5 | % | Reviewed |
| Cost of risk | Asset Quality | 52.0 | 42.0 | 31.0 | 32.0 | bps | Reviewed |
| NPE ratio | Asset Quality | 3.8 | 3.5 | 3.1 | 2.4 | % | Reviewed |
| NPE coverage ratio | Asset Quality | 68.3 | 77.6 | 82.2 | 90.9 | % | Reviewed |
| Restructured loans ratio | Asset Quality | 3.2 | 3.3 | 2.6 | 1.8 | % | Reviewed |
| Loan-to-deposit ratio | Liquidity | 74.0 | 69.2 | 67.6 | 68.2 | % | Reviewed |
| Loan-to-balance-sheet-customer-resources ratio | Liquidity | 72.7 | 67.8 | 66.6 | 67.1 | % | Reviewed |
| LCR | Liquidity | 212.0 | 317.0 | 342.0 | 334.0 | % | Reviewed |
| NSFR | Liquidity | 154.0 | 177.0 | 181.0 | 180.0 | % | Reviewed |
| CET1 phased-in ratio | Capital | 12.6 | 15.2 | 16.4 | 16.1 | % | Reviewed |
| CET1 fully implemented ratio | Capital | 12.5 | 15.2 | 16.3 | 15.9 | % | Reviewed |
| Total capital fully implemented ratio | Capital | 16.8 | 19.6 | 20.6 | 19.9 | % | Reviewed |
| EPS | Per Share | 0.011 | 0.056 | 0.058 | 0.066 | EUR | Reviewed |
| Book value per share | Per Share | n/a | 0.412 | 0.469 | 0.528 | EUR | Reviewed |

---

## 4. Profitability Analysis

### ROE

ROE increased materially from 4.0% in 2022A to 15.1% in 2023A, before remaining at a double-digit level in 2024A and 2025A.

This suggests a significant improvement in profitability relative to equity after 2022, although ROE should always be interpreted together with capital strength, asset quality and business cycle conditions.

### ROA

ROA improved from 0.1% in 2022A to 1.0% in 2023A and 2024A, reaching 1.1% in 2025A.

For a banking institution, this indicates improved profitability relative to the asset base, although the metric should be reviewed alongside balance sheet size, risk-weighted assets, funding mix and interest rate conditions.

### Net Interest Margin

Net interest margin increased from 2.46% in 2022A to 3.17% in 2023A, before declining to 3.04% in 2024A and 2.89% in 2025A.

This pattern may reflect the impact of the interest rate cycle, deposit repricing, loan pricing dynamics and balance sheet mix. The decline after 2023A is analytically relevant because banks can experience margin pressure when funding costs rise or when rates normalise.

---

## 5. Efficiency Analysis

### Cost-to-Income Ratio

The cost-to-income ratio improved from 37.4% in 2022A to 30.8% in 2023A, before increasing to 36.5% in 2024A and 37.1% in 2025A.

A lower cost-to-income ratio generally indicates stronger operating efficiency. The 2023A figure suggests a particularly efficient year, while the later increase may reflect cost growth, revenue mix changes or normalisation after a stronger operating environment.

### Cost-to-Income Ratio Excluding Specific Items

The cost-to-income ratio excluding specific items follows a similar pattern:

- 36.8% in 2022A
- 30.2% in 2023A
- 36.2% in 2024A
- 36.5% in 2025A

This version can be useful to assess recurring efficiency trends, but the exact definition should be reviewed against official reporting methodology.

---

## 6. Asset Quality and Credit Risk Analysis

### Cost of Risk

Cost of risk decreased from 52 bps in 2022A to 42 bps in 2023A, 31 bps in 2024A and 32 bps in 2025A.

This indicates an improvement in credit impairment intensity over the period, with 2025A remaining close to the 2024A level. Cost of risk should be interpreted together with macroeconomic conditions, loan book composition, NPE formation and provisioning policy.

### NPE Ratio

The NPE ratio decreased steadily from 3.8% in 2022A to 2.4% in 2025A.

This is a positive asset quality trend, suggesting a lower proportion of non-performing exposures relative to the relevant exposure base.

### NPE Coverage Ratio

The NPE coverage ratio increased from 68.3% in 2022A to 90.9% in 2025A.

A higher coverage ratio may indicate a stronger provisioning buffer against non-performing exposures, although it should be assessed together with collateral values, NPE mix, write-offs and recovery assumptions.

### Restructured Loans Ratio

The restructured loans ratio decreased from 3.2% in 2022A to 1.8% in 2025A.

This supports the broader asset quality improvement narrative, although definitions and perimeter should be reviewed against official reporting.

---

## 7. Liquidity and Funding Analysis

### Loan-to-Deposit Ratio

The loan-to-deposit ratio decreased from 74.0% in 2022A to 67.6% in 2024A, before increasing slightly to 68.2% in 2025A.

This suggests a balance sheet that remains strongly deposit-funded, with customer deposits and customer resources continuing to support the loan book.

### LCR

LCR increased from 212% in 2022A to 342% in 2024A, before decreasing slightly to 334% in 2025A.

The ratio remains high across the period, indicating strong short-term liquidity resilience under the regulatory LCR framework.

### NSFR

NSFR increased from 154% in 2022A to 181% in 2024A, remaining broadly stable at 180% in 2025A.

This indicates a stable funding profile over a one-year horizon under the regulatory NSFR framework.

---

## 8. Capital Analysis

### CET1 Phased-In Ratio

The CET1 phased-in ratio increased from 12.6% in 2022A to 16.4% in 2024A, before decreasing slightly to 16.1% in 2025A.

This indicates a stronger capital position compared with 2022A, despite the slight decline in 2025A.

### CET1 Fully Implemented Ratio

The CET1 fully implemented ratio increased from 12.5% in 2022A to 16.3% in 2024A, before decreasing slightly to 15.9% in 2025A.

This remains a key indicator of regulatory capital strength and should be analysed together with profitability, risk-weighted assets, asset quality and shareholder distribution policy.

### Total Capital Fully Implemented Ratio

The total capital fully implemented ratio increased from 16.8% in 2022A to 20.6% in 2024A, before decreasing to 19.9% in 2025A.

This suggests a stronger total regulatory capital base compared with 2022A.

---

## 9. Per Share Metrics

### Earnings per Share

EPS increased from EUR 0.011 in 2022A to EUR 0.056 in 2023A, EUR 0.058 in 2024A and EUR 0.066 in 2025A.

This reflects an improvement in earnings attributable to ordinary shareholders over the period.

### Book Value per Share

Book value per share increased from EUR 0.412 in 2023A to EUR 0.469 in 2024A and EUR 0.528 in 2025A.

The 2022A value is not included in the current structured dataset and should not be inferred without validation.

---

## 10. Valuation Metrics

The structured dataset includes placeholders for valuation metrics such as:

- Price-to-book
- Price-to-earnings
- Dividend yield
- Payout ratio

These metrics are not included in the current version of this ratio analysis because they require dated and validated market data, including share price, market capitalisation and dividend data.

To avoid overstating precision, valuation metrics should only be added after selecting a specific market data date and documenting the source.

---

## 11. Key Analytical Takeaways

The historical ratio analysis suggests:

- Profitability improved significantly after 2022A, with ROE and ROA remaining materially stronger in 2023A–2025A.
- Net interest margin peaked in 2023A and declined in 2024A–2025A, which is relevant for forecast assumptions.
- Efficiency improved strongly in 2023A but normalised in 2024A and 2025A.
- Asset quality improved, supported by a declining NPE ratio and stronger NPE coverage.
- Liquidity ratios remained strong, with high LCR and NSFR levels.
- Capital ratios improved materially versus 2022A, despite a slight reduction in 2025A.
- Per-share metrics improved over the analysed period.

---

## 12. Data Quality and Interpretation Notes

The figures in this document are based on structured public-source data stored in:

`data/banking_ratios.csv`

Important interpretation notes:

- Some banking ratios are reported ratios and may not be fully reproducible from simplified public datasets.
- Official bank ratios may use average balances, regulatory definitions or internal classifications.
- Valuation ratios are excluded until dated market data is selected and validated.
- Historical figures marked as reviewed should still be subject to final human review before public promotion.
- Forecast and valuation outputs should not be interpreted as official projections or investment recommendations.

---

## 13. Disclaimer

This document is for educational, analytical and portfolio purposes only.

It does not constitute:

- Financial advice
- Investment advice
- Valuation advice
- Credit advice
- Legal advice
- A recommendation to buy, sell or hold any financial instrument

The author is not affiliated with Millennium bcp for the purpose of this project.

All figures, ratios, interpretations and assumptions require human review before publication or professional use.
