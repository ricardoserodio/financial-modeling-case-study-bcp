-- Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank
-- SQL Queries
--
-- Purpose:
-- Example SQL queries for banking analytics, financial modeling,
-- forecast review, scenario analysis and financial data quality checks.
--
-- This project is for educational and portfolio purposes only.
-- It does not constitute investment advice.

-- ============================================================
-- 1. View all financial statement data
-- ============================================================

SELECT
    bank_name,
    period,
    category,
    metric,
    value,
    unit,
    data_type,
    validation_status
FROM financial_statements
ORDER BY
    period,
    category,
    metric;

-- Explanation:
-- This query gives a clean view of the main financial data by year,
-- category and metric.
-- In Power BI, this type of output can feed KPI cards and trend charts.

-- ============================================================
-- 2. Profitability metrics by period
-- ============================================================

SELECT
    period,
    metric,
    value,
    unit,
    data_type,
    validation_status
FROM financial_statements
WHERE category = 'Profitability'
ORDER BY
    period,
    metric;

-- Explanation:
-- This query filters only profitability-related metrics, such as
-- net income, net interest income, fees and commissions, ROE and ROA.

-- ============================================================
-- 3. Key banking ratios by period
-- ============================================================

SELECT
    period,
    ratio_name,
    category,
    value,
    unit,
    reported_or_calculated,
    validation_status
FROM banking_ratios
ORDER BY
    ratio_name,
    period;

-- Explanation:
-- This query organises the main banking ratios across time.
-- It is useful for Power BI line charts showing ratio evolution.

-- ============================================================
-- 4. Efficiency analysis
-- ============================================================

SELECT
    period,
    ratio_name,
    value,
    unit,
    validation_status
FROM banking_ratios
WHERE ratio_name = 'Cost-to-income ratio'
ORDER BY period;

-- Explanation:
-- Cost-to-income is one of the most important banking efficiency ratios.
-- It shows how much cost is required to generate income.
-- A lower ratio usually indicates better operating efficiency.

-- ============================================================
-- 5. Asset quality analysis
-- ============================================================

SELECT
    period,
    ratio_name,
    value,
    unit,
    validation_status
FROM banking_ratios
WHERE category = 'Asset Quality'
ORDER BY
    ratio_name,
    period;

-- Explanation:
-- Asset quality is critical in banking because loan losses can strongly
-- affect profitability and capital.
-- This query focuses on metrics such as NPL ratio, NPE ratio,
-- coverage ratio and cost of risk.

-- ============================================================
-- 6. Capital strength analysis
-- ============================================================

SELECT
    period,
    ratio_name,
    value,
    unit,
    validation_status
FROM banking_ratios
WHERE category = 'Capital'
ORDER BY
    ratio_name,
    period;

-- Explanation:
-- Capital ratios show the bank's ability to absorb losses.
-- CET1 is especially important because it measures high-quality capital
-- relative to risk-weighted assets.

-- ============================================================
-- 7. Loans and deposits trend
-- ============================================================

SELECT
    period,
    metric,
    value,
    unit,
    validation_status
FROM financial_statements
WHERE metric IN (
    'Customer loans',
    'Customer deposits'
)
ORDER BY
    metric,
    period;

-- Explanation:
-- Loans and deposits are core banking balance sheet items.
-- Comparing them helps understand lending growth and funding stability.

-- ============================================================
-- 8. Actual vs forecast data
-- ============================================================

SELECT
    period,
    metric,
    category,
    value,
    unit,
    data_type,
    validation_status
FROM financial_statements
WHERE data_type IN ('actual', 'forecast')
ORDER BY
    metric,
    period;

-- Explanation:
-- This query separates actual historical data from forecast data.
-- This is important because a professional analysis must clearly
-- distinguish published figures from estimates.

-- ============================================================
-- 9. Forecast assumptions by scenario
-- ============================================================

SELECT
    scenario,
    period,
    assumption_name,
    category,
    value,
    unit,
    assumption_logic,
    validation_status
FROM forecast_assumptions
ORDER BY
    scenario,
    period,
    assumption_name;

-- Explanation:
-- Forecast assumptions explain the logic behind the model.
-- In Power BI, these assumptions can support the Forecast & Scenarios page.

-- ============================================================
-- 10. Scenario analysis output
-- ============================================================

SELECT
    scenario,
    period,
    metric,
    category,
    value,
    unit,
    validation_status
FROM scenario_analysis
ORDER BY
    metric,
    scenario,
    period;

-- Explanation:
-- Scenario analysis allows comparison between base, downside and upside cases.
-- It helps users understand sensitivity to different assumptions.

-- ============================================================
-- 11. Source validation status
-- ============================================================

SELECT
    validation_status,
    COUNT(*) AS number_of_items
FROM source_mapping
GROUP BY validation_status
ORDER BY number_of_items DESC;

-- Explanation:
-- This query summarises how many data points are pending, reviewed,
-- validated or need review.
-- This is very useful for a Power BI Data Quality page.

-- ============================================================
-- 12. Items still pending validation
-- ============================================================

SELECT
    data_item,
    category,
    period,
    value,
    unit,
    source_document,
    source_section_or_page,
    validation_status
FROM source_mapping
WHERE validation_status = 'Pending'
ORDER BY
    period,
    category,
    data_item;

-- Explanation:
-- This query identifies which data points still need review.
-- It supports financial data quality and human-in-the-loop validation.

-- ============================================================
-- 13. Missing values check
-- ============================================================

SELECT
    bank_name,
    period,
    metric,
    category,
    validation_status
FROM financial_statements
WHERE value IS NULL
ORDER BY
    period,
    category,
    metric;

-- Explanation:
-- Missing values can create errors in analysis, dashboards and forecasts.
-- This query identifies fields that still need to be completed.

-- ============================================================
-- 14. Data quality checks summary
-- ============================================================

SELECT
    check_category,
    check_result,
    severity,
    COUNT(*) AS number_of_checks
FROM data_quality_checks
GROUP BY
    check_category,
    check_result,
    severity
ORDER BY
    check_category,
    severity;

-- Explanation:
-- This query summarises the result of data quality checks.
-- It can feed a Power BI visual showing pass, warning, fail and pending checks.

-- ============================================================
-- 15. Market data for valuation
-- ============================================================

SELECT
    bank_name,
    market_data_date,
    metric,
    value,
    unit,
    source,
    validation_status
FROM market_data
ORDER BY
    market_data_date,
    metric;

-- Explanation:
-- Market data is used for valuation multiples such as price-to-book
-- and price-to-earnings.
-- The market data date is important because market prices change over time.

-- ============================================================
-- 16. Peer comparison
-- ============================================================

SELECT
    peer_name,
    country,
    business_type,
    market_data_date,
    metric,
    value,
    unit,
    source,
    validation_status
FROM peer_comparison
ORDER BY
    metric,
    peer_name;

-- Explanation:
-- Peer comparison helps place Millennium bcp in context.
-- However, peer analysis must be interpreted carefully because banks
-- may differ by geography, business mix, risk profile and capital structure.

-- ============================================================
-- 17. Power BI executive KPI extract
-- ============================================================

SELECT
    fs.period,
    fs.metric,
    fs.category,
    fs.value,
    fs.unit,
    fs.data_type,
    fs.validation_status
FROM financial_statements fs
WHERE fs.metric IN (
    'Net income',
    'Net interest income',
    'Fees and commissions',
    'Operating income',
    'Operating costs',
    'Customer loans',
    'Customer deposits',
    'Total assets',
    'Equity'
)
ORDER BY
    fs.period,
    fs.metric;

-- Explanation:
-- This query prepares a compact KPI extract for the Power BI Executive Summary page.

-- ============================================================
-- 18. Power BI ratio extract
-- ============================================================

SELECT
    br.period,
    br.ratio_name,
    br.category,
    br.value,
    br.unit,
    br.reported_or_calculated,
    br.validation_status
FROM banking_ratios br
WHERE br.ratio_name IN (
    'ROE',
    'ROA',
    'Cost-to-income ratio',
    'NPL ratio',
    'Cost of risk',
    'CET1 ratio',
    'Loan-to-deposit ratio',
    'Price-to-book',
    'Price-to-earnings'
)
ORDER BY
    br.ratio_name,
    br.period;

-- Explanation:
-- This query prepares the main ratio dataset for Power BI trend charts.

-- ============================================================
-- 19. Historical period filter
-- ============================================================

SELECT
    period,
    metric,
    value,
    unit
FROM financial_statements
WHERE period IN ('2022A', '2023A', '2024A', '2025A')
ORDER BY
    metric,
    period;

-- Explanation:
-- This query isolates actual historical data.
-- It should not mix historical actuals with forecast estimates.

-- ============================================================
-- 20. Forecast period filter
-- ============================================================

SELECT
    period,
    metric,
    value,
    unit
FROM financial_statements
WHERE period IN ('2026E', '2027E')
ORDER BY
    metric,
    period;

-- Explanation:
-- This query isolates forecast periods.
-- Forecast figures should always be clearly labelled as estimates.

-- ============================================================
-- End of queries
-- ============================================================