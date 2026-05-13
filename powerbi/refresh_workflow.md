# Power BI Refresh Workflow ? Millennium bcp Case Study

## Purpose

This document defines the recommended refresh workflow for the Power BI dashboard connected to the Millennium bcp case study CSV files.

The goal is to keep a controlled process between:

- public financial data extraction;
- CSV dataset updates;
- validation checks;
- Git version control;
- Power BI refresh;
- human-in-the-loop review.

This workflow is designed for a professional portfolio project and should remain simple, transparent and reproducible.

---

## Core Workflow

The recommended workflow is:

1. Update CSV files.
2. Run validation checks.
3. Review validation warnings.
4. Confirm Git status.
5. Commit and push changes.
6. Open Power BI Desktop.
7. Refresh the dashboard.
8. Review visuals.
9. Check data quality page.
10. Document any issues.

---

## Step 1 ? Update CSV Files

The core CSV files are:

| File | Purpose |
|---|---|
| `data/financial_data.csv` | Financial statement and balance sheet data |
| `data/banking_ratios.csv` | Banking ratios and per-share indicators |
| `data/source_mapping.csv` | Source traceability |
| `data/extraction_tracker.csv` | Extraction audit trail |

Future files may include:

| File | Purpose |
|---|---|
| `data/market_data_template.csv` | Market data and valuation date inputs |
| `data/peer_comparison_template.csv` | Peer comparison inputs |
| `data/forecast_assumptions.csv` | Forecast assumptions |
| `data/scenario_analysis.csv` | Scenario analysis |

---

## Step 2 ? Run Validation Checks

Before opening Power BI, run:

`python data/validation_checks.py`

Current acceptable warnings:

1. `market_data_template.csv`: column `category` has missing values.
2. `peer_comparison_template.csv`: column `business_type` has missing values.

These warnings are acceptable because both files are template-stage files for future phases.

Any new warning should be reviewed before refreshing the Power BI dashboard.

---

## Step 3 ? Review Validation Output

Expected current validation output:

| Issue | Status |
|---|---|
| `market_data_template.csv` missing `category` values | Acceptable template-stage warning |
| `peer_comparison_template.csv` missing `business_type` values | Acceptable template-stage warning |

Blocking issues would include:

- invalid period labels;
- invalid validation status values;
- missing required fields in active files;
- inconsistent source status values;
- missing categories in active analytical files;
- unexpected blank values in completed periods.

---

## Step 4 ? Check Git Status

Run:

`git status`

Expected output before Power BI refresh:

`nothing to commit, working tree clean`

If there are modified files, commit them before refreshing the dashboard.

This ensures the Power BI dashboard is refreshed from a documented project state.

---

## Step 5 ? Commit and Push Changes

Recommended command sequence:

`git add <file>`

`git commit -m "Clear commit message"`

`git push`

`git status`

Commit messages should be specific.

Examples:

| Change | Suggested Commit Message |
|---|---|
| Added financial data | `Add 2022A official financial data` |
| Added banking ratios | `Add 2022A official banking ratios` |
| Updated source mapping | `Add 2022A official source mapping entries` |
| Updated extraction tracker | `Update extraction tracker for 2022A official data` |
| Updated Power BI notes | `Add Power BI refresh workflow` |

---

## Step 6 ? Open Power BI Desktop

Open the Power BI Desktop file once created.

Recommended future file name:

`powerbi/millennium_bcp_banking_dashboard.pbix`

The `.pbix` file may be too large or unsuitable for regular GitHub versioning depending on file size.

If the `.pbix` file is included in the repository, document it clearly.

If not included, keep screenshots and documentation instead.

---

## Step 7 ? Refresh Data

In Power BI Desktop:

1. Open the dashboard.
2. Click `Refresh`.
3. Wait for all CSV files to reload.
4. Check for import errors.
5. Review visuals.

The dashboard should update automatically based on the latest CSV values.

---

## Step 8 ? Review Dashboard Pages

After refresh, review each page.

| Page | Review Focus |
|---|---|
| Executive Overview | Latest values and trend charts |
| Profitability | ROE, ROA, net interest margin, EPS |
| Efficiency | Cost-to-income and operating costs |
| Asset Quality | NPE, coverage, cost of risk |
| Liquidity & Funding | Customer loans, customer funds, LCR, NSFR |
| Capital | CET1 and total capital ratios |
| Data Quality | Reviewed, Needs Review and Pending items |

---

## Step 9 ? Human-in-the-Loop Review

Do not treat the dashboard as automatically final.

The following items require manual review:

| Review Item | Reason |
|---|---|
| Customer deposits vs customer funds | Terminology may differ across disclosures |
| 2022A impairments and provisions | Figure combines multiple components |
| 2022A book value per share | Still pending |
| Reexpressed comparative figures | Later reports may restate prior-year values |
| Reported vs calculated figures | Calculated items may differ from bank methodology |
| Phased-in vs fully implemented capital ratios | These should not be mixed |
| Valuation ratios | Pending until market data date is selected |

---

## Step 10 ? Document Issues

If a visual looks wrong, document the issue before changing the dashboard.

Recommended notes file:

`powerbi/dashboard_review_notes.md`

Example issue log:

| Date | Page | Issue | Action |
|---|---|---|---|
| YYYY-MM-DD | Profitability | ROE axis formatting unclear | Format as percentage |
| YYYY-MM-DD | Data Quality | Pending items not visible | Add table visual |
| YYYY-MM-DD | Liquidity | Customer funds label needs clarification | Add note to visual title |

---

## Recommended Refresh Checklist

Before Power BI refresh:

| Check | Status |
|---|---|
| CSV files updated | To confirm |
| Validation checks run | To confirm |
| Only acceptable warnings remain | To confirm |
| Git status clean | To confirm |
| Source mapping updated | To confirm |
| Extraction tracker updated | To confirm |
| Human review notes visible | To confirm |

After Power BI refresh:

| Check | Status |
|---|---|
| Dashboard refresh completed | To confirm |
| No import errors | To confirm |
| Periods display correctly | To confirm |
| Main visuals update correctly | To confirm |
| Data quality page reviewed | To confirm |
| Screenshots updated if needed | To confirm |

---

## Future AURA Integration

A future private AURA module could automate parts of this workflow.

Possible module:

`AURA / Wisestrike Command Center ? BCP Case Study Monitor`

Possible actions:

- detect changed CSV files;
- run `python data/validation_checks.py`;
- interpret acceptable warnings;
- check `git status`;
- generate Power BI refresh notes;
- create a Power BI readiness checklist;
- flag human-in-the-loop review items;
- suggest commit messages.

This should remain separate from the public repository unless a clean public version is created later.

---

## Portfolio Value

This workflow shows that the project is not just a static dashboard.

It demonstrates:

- data quality discipline;
- source validation;
- controlled refresh process;
- Git-based versioning;
- BI readiness;
- human review;
- responsible AI-assisted finance workflow.

This supports positioning for:

- Banking Analytics;
- Financial Data Quality;
- Reporting Analyst roles;
- Financial Research Support;
- AI Finance Evaluation;
- Data Validation roles.

---

## Disclaimer

The Power BI dashboard and refresh workflow are part of an educational and professional portfolio case study.

They do not provide investment advice, financial advice, valuation advice, a price target or a buy/sell/hold recommendation.

All figures should be independently verified before professional, academic or investment-related use.
