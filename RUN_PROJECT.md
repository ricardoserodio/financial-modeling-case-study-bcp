# Run Project Locally

This document explains how to run the project scripts locally.

The project is a simplified educational financial modeling case study based on public information about **Millennium bcp / Banco Comercial Português**.

It does not constitute investment advice.

---

## 1. Requirements

This project requires:

- Python 3.10 or higher
- pandas
- openpyxl

The required Python packages are listed in:

    requirements.txt

---

## 2. Clone the Repository

Clone the repository from GitHub:

    git clone https://github.com/ricardoserodio/financial-modeling-case-study-bcp.git

Enter the project folder:

    cd financial-modeling-case-study-bcp

---

## 3. Create a Virtual Environment

Create a virtual environment:

    python -m venv .venv

Activate the virtual environment.

On Windows:

    .venv\Scripts\activate

On macOS or Linux:

    source .venv/bin/activate

---

## 4. Install Dependencies

Install the required packages:

    pip install -r requirements.txt

---

## 5. Run Data Validation Checks

Run the validation script:

    python data/validation_checks.py

This script checks the structure and consistency of the project data templates.

It validates:

- required columns;
- missing values in key fields;
- validation status values;
- expected period columns;
- basic file consistency.

---

## 6. Generate the Banking Model Excel Template

Run the banking model template generator:

    python model/create_banking_model_template.py

This creates:

    model/banking_model.xlsx

The generated Excel file is a template for educational analysis and should be completed using only public information.

---

## 7. Generate the Sensitivity Analysis Excel Template

Run the sensitivity analysis template generator:

    python model/create_sensitivity_analysis_template.py

This creates:

    model/sensitivity_analysis.xlsx

The generated Excel file is a template for scenario and sensitivity analysis.

---

## 8. Suggested Workflow

Recommended workflow:

1. Review `sources.md`.
2. Review `data/source_links.csv`.
3. Extract public data into `data/extraction_tracker.csv`.
4. Enter historical figures into `data/historical_financials.csv`.
5. Enter banking ratios into `data/banking_ratios.csv`.
6. Map all figures in `data/source_mapping.csv`.
7. Run `python data/validation_checks.py`.
8. Generate the Excel templates.
9. Complete the model using public information.
10. Review the model using `notes/model_review_checklist.md`.
11. Update `investment_memo.md`.

---

## 9. Important Notes

This project uses only public information.

Do not include:

- client data;
- personal data;
- internal banking information;
- confidential documents;
- screenshots from internal systems;
- non-public information.

All outputs are for educational and portfolio purposes only.

---

## Disclaimer

This project is for educational and portfolio purposes only and does not constitute investment advice, financial advice or a recommendation to buy, sell or hold any financial instrument.
