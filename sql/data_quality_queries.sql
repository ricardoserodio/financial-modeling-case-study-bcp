-- Financial Modeling Case Study – Data Quality Queries
-- Purpose:
-- SQL queries for reviewing validation status, missing values and source traceability.
--
-- Disclaimer:
-- This file supports a data quality review workflow for an educational portfolio project.

-- ============================================================
-- 1. Financial data by validation status
-- ============================================================

SELECT
    validation_status,
    COUNT(*) AS row_count
FROM financial_data
GROUP BY validation_status
ORDER BY row_count DESC;


-- ============================================================
-- 2. Financial data pending review
-- ============================================================

SELECT
    bank_name,
    period,
    metric,
    category,
    value,
    unit,
    validation_status,
    reported_or_calculated,
    source_document,
    notes
FROM financial_data
WHERE validation_status <> 'Reviewed'
ORDER BY period, category, metric;


-- ============================================================
-- 3. Missing values in financial data
-- ============================================================

SELECT
    bank_name,
    period,
    metric,
    category,
    value,
    unit,
    validation_status,
    source_document,
    notes
FROM financial_data
WHERE value IS NULL
ORDER BY period, category, metric;


-- ============================================================
-- 4. Banking ratios by source status
-- ============================================================

SELECT
    source_status,
    COUNT(*) AS ratio_count
FROM banking_ratios
GROUP BY source_status
ORDER BY ratio_count DESC;


-- ============================================================
-- 5. Banking ratios pending review
-- ============================================================

SELECT
    ratio,
    category,
    "2022A",
    "2023A",
    "2024A",
    "2025A",
    unit,
    source_status,
    notes
FROM banking_ratios
WHERE source_status <> 'Reviewed'
ORDER BY category, ratio;


-- ============================================================
-- 6. Source mapping review
-- ============================================================

SELECT
    dataset,
    field,
    source_document,
    source_section,
    source_period,
    validation_status,
    notes
FROM source_mapping
ORDER BY dataset, field;


-- ============================================================
-- 7. Source mapping items pending review
-- ============================================================

SELECT
    dataset,
    field,
    source_document,
    source_section,
    source_period,
    validation_status,
    notes
FROM source_mapping
WHERE validation_status <> 'Reviewed'
ORDER BY dataset, field;


-- ============================================================
-- 8. Extraction tracker status summary
-- ============================================================

SELECT
    extraction_status,
    validation_status,
    COUNT(*) AS item_count
FROM extraction_tracker
GROUP BY extraction_status, validation_status
ORDER BY item_count DESC;


-- ============================================================
-- 9. Extraction tracker pending items
-- ============================================================

SELECT
    item,
    category,
    source_document,
    period,
    extraction_status,
    validation_status,
    notes
FROM extraction_tracker
WHERE extraction_status <> 'Completed'
   OR validation_status <> 'Reviewed'
ORDER BY period, category, item;


-- ============================================================
-- 10. Forecast outputs requiring review
-- ============================================================

SELECT
    'forecast_financials' AS dataset,
    scenario,
    period,
    line_item AS item,
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
    validation_status,
    notes
FROM scenario_analysis
WHERE validation_status <> 'Reviewed'

ORDER BY dataset, scenario, period, item;
