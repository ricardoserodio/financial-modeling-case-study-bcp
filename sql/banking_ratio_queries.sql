-- Financial Modeling Case Study – Banking Ratio Queries
-- Purpose:
-- Example analytical SQL queries for reviewing banking ratios across historical periods.
--
-- Disclaimer:
-- These queries are for educational and portfolio purposes only.
-- They do not constitute financial advice, investment advice or valuation advice.

-- ============================================================
-- 1. View all banking ratios
-- ============================================================

SELECT
    ratio,
    category,
    formula,
    "2022A",
    "2023A",
    "2024A",
    "2025A",
    unit,
    source_status,
    notes
FROM banking_ratios
ORDER BY category, ratio;


-- ============================================================
-- 2. Profitability ratios
-- ============================================================

SELECT
    ratio,
    "2022A",
    "2023A",
    "2024A",
    "2025A",
    unit,
    source_status
FROM banking_ratios
WHERE category = 'Profitability'
ORDER BY ratio;


-- ============================================================
-- 3. Efficiency ratios
-- ============================================================

SELECT
    ratio,
    "2022A",
    "2023A",
    "2024A",
    "2025A",
    unit,
    source_status
FROM banking_ratios
WHERE category = 'Efficiency'
ORDER BY ratio;


-- ============================================================
-- 4. Asset quality ratios
-- ============================================================

SELECT
    ratio,
    "2022A",
    "2023A",
    "2024A",
    "2025A",
    unit,
    source_status
FROM banking_ratios
WHERE category = 'Asset Quality'
ORDER BY ratio;


-- ============================================================
-- 5. Liquidity ratios
-- ============================================================

SELECT
    ratio,
    "2022A",
    "2023A",
    "2024A",
    "2025A",
    unit,
    source_status
FROM banking_ratios
WHERE category = 'Liquidity'
ORDER BY ratio;


-- ============================================================
-- 6. Capital ratios
-- ============================================================

SELECT
    ratio,
    "2022A",
    "2023A",
    "2024A",
    "2025A",
    unit,
    source_status
FROM banking_ratios
WHERE category = 'Capital'
ORDER BY ratio;


-- ============================================================
-- 7. Ratios with pending source status
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
-- 8. 2025A ratio snapshot
-- ============================================================

SELECT
    ratio,
    category,
    "2025A" AS value_2025A,
    unit,
    source_status
FROM banking_ratios
ORDER BY category, ratio;


-- ============================================================
-- 9. Year-over-year movement: 2024A to 2025A
-- ============================================================

SELECT
    ratio,
    category,
    "2024A" AS value_2024A,
    "2025A" AS value_2025A,
    ("2025A" - "2024A") AS change_2025_vs_2024,
    unit,
    source_status
FROM banking_ratios
WHERE "2024A" IS NOT NULL
  AND "2025A" IS NOT NULL
ORDER BY category, ratio;


-- ============================================================
-- 10. Key management ratio dashboard extract
-- ============================================================

SELECT
    ratio,
    category,
    "2025A" AS value_2025A,
    unit,
    source_status
FROM banking_ratios
WHERE ratio IN (
    'ROE',
    'ROA',
    'Net interest margin',
    'Cost-to-income ratio',
    'Cost of risk',
    'NPE ratio',
    'Loan-to-deposit ratio',
    'LCR',
    'NSFR',
    'CET1 fully implemented ratio'
)
ORDER BY
    CASE category
        WHEN 'Profitability' THEN 1
        WHEN 'Efficiency' THEN 2
        WHEN 'Asset Quality' THEN 3
        WHEN 'Liquidity' THEN 4
        WHEN 'Capital' THEN 5
        ELSE 6
    END,
    ratio;
