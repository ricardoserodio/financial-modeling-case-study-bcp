-- Financial Modeling Case Study – Forecast Queries
-- Purpose:
-- SQL queries for analysing forecast assumptions, forecast financials,
-- forecast ratios and scenario analysis outputs.
--
-- Disclaimer:
-- These queries are for educational and portfolio purposes only.
-- Forecast figures are scenario-based estimates and should not be interpreted
-- as official projections, investment advice or financial recommendations.

-- ============================================================
-- 1. View all forecast assumptions
-- ============================================================

SELECT
    scenario,
    assumption_category,
    assumption,
    "2026E",
    "2027E",
    "2028E",
    unit,
    rationale,
    source_or_basis,
    validation_status,
    notes
FROM forecast_assumptions
ORDER BY scenario, assumption_category, assumption;


-- ============================================================
-- 2. Forecast financials by scenario and period
-- ============================================================

SELECT
    scenario,
    period,
    line_item,
    value,
    unit,
    calculation_method,
    source_or_basis,
    validation_status
FROM forecast_financials
ORDER BY scenario, period, line_item;


-- ============================================================
-- 3. Forecast income statement extract
-- ============================================================

SELECT
    scenario,
    period,
    line_item,
    value,
    unit,
    validation_status
FROM forecast_financials
WHERE line_item IN (
    'Net interest income',
    'Other operating income',
    'Operating income',
    'Operating costs',
    'Pre-provision operating profit',
    'Impairments and provisions',
    'Net income'
)
ORDER BY scenario, period,
    CASE line_item
        WHEN 'Net interest income' THEN 1
        WHEN 'Other operating income' THEN 2
        WHEN 'Operating income' THEN 3
        WHEN 'Operating costs' THEN 4
        WHEN 'Pre-provision operating profit' THEN 5
        WHEN 'Impairments and provisions' THEN 6
        WHEN 'Net income' THEN 7
        ELSE 8
    END;


-- ============================================================
-- 4. Forecast balance sheet extract
-- ============================================================

SELECT
    scenario,
    period,
    line_item,
    value,
    unit,
    validation_status
FROM forecast_financials
WHERE line_item IN (
    'Customer loans',
    'Customer deposits',
    'Total assets',
    'Equity'
)
ORDER BY scenario, period,
    CASE line_item
        WHEN 'Customer loans' THEN 1
        WHEN 'Customer deposits' THEN 2
        WHEN 'Total assets' THEN 3
        WHEN 'Equity' THEN 4
        ELSE 5
    END;


-- ============================================================
-- 5. Forecast ratios by scenario and period
-- ============================================================

SELECT
    scenario,
    period,
    ratio,
    category,
    value,
    unit,
    calculation_method,
    source_or_basis,
    validation_status
FROM forecast_ratios
ORDER BY scenario, period, category, ratio;


-- ============================================================
-- 6. Base case forecast ratios
-- ============================================================

SELECT
    period,
    ratio,
    category,
    value,
    unit,
    validation_status
FROM forecast_ratios
WHERE scenario = 'Base'
ORDER BY period, category, ratio;


-- ============================================================
-- 7. Scenario comparison for net income
-- ============================================================

SELECT
    scenario,
    period,
    metric,
    value,
    unit,
    base_case_value,
    variance_vs_base,
    variance_vs_base_percent,
    risk_level,
    interpretation
FROM scenario_analysis
WHERE metric = 'Net income'
ORDER BY period,
    CASE scenario
        WHEN 'Base' THEN 1
        WHEN 'Optimistic' THEN 2
        WHEN 'Conservative' THEN 3
        ELSE 4
    END;


-- ============================================================
-- 8. Scenario comparison for ROE
-- ============================================================

SELECT
    scenario,
    period,
    metric,
    value,
    unit,
    base_case_value,
    variance_vs_base,
    variance_vs_base_percent,
    risk_level,
    interpretation
FROM scenario_analysis
WHERE metric = 'ROE'
ORDER BY period,
    CASE scenario
        WHEN 'Base' THEN 1
        WHEN 'Optimistic' THEN 2
        WHEN 'Conservative' THEN 3
        ELSE 4
    END;


-- ============================================================
-- 9. Scenario comparison for cost of risk
-- ============================================================

SELECT
    scenario,
    period,
    metric,
    value,
    unit,
    base_case_value,
    variance_vs_base,
    variance_vs_base_percent,
    risk_level,
    interpretation
FROM scenario_analysis
WHERE metric = 'Cost of risk'
ORDER BY period,
    CASE scenario
        WHEN 'Base' THEN 1
        WHEN 'Optimistic' THEN 2
        WHEN 'Conservative' THEN 3
        ELSE 4
    END;


-- ============================================================
-- 10. Full scenario analysis table
-- ============================================================

SELECT
    scenario,
    period,
    metric,
    category,
    value,
    unit,
    base_case_value,
    variance_vs_base,
    variance_vs_base_percent,
    scenario_logic,
    main_driver,
    risk_level,
    interpretation,
    source_or_basis,
    validation_status
FROM scenario_analysis
ORDER BY period, category, metric,
    CASE scenario
        WHEN 'Base' THEN 1
        WHEN 'Optimistic' THEN 2
        WHEN 'Conservative' THEN 3
        ELSE 4
    END;


-- ============================================================
-- 11. Forecast outputs requiring human review
-- ============================================================

SELECT
    'forecast_financials' AS dataset,
    scenario,
    period,
    line_item AS item,
    value,
    unit,
    validation_status,
    notes
FROM forecast_financials
WHERE validation_status <> 'Reviewed'

UNION ALL

SELECT
    'forecast_ratios' AS dataset,
    scenario,
    period,
    ratio AS item,
    value,
    unit,
    validation_status,
    notes
FROM forecast_ratios
WHERE validation_status <> 'Reviewed'

UNION ALL

SELECT
    'scenario_analysis' AS dataset,
    scenario,
    period,
    metric AS item,
    value,
    unit,
    validation_status,
    notes
FROM scenario_analysis
WHERE validation_status <> 'Reviewed'

ORDER BY dataset, scenario, period, item;
