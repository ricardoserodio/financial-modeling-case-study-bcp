-- Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank
-- SQL Schema
--
-- Purpose:
-- This schema structures public financial data for banking analytics,
-- financial modeling, forecast assumptions, scenario analysis and
-- financial data quality validation.
--
-- This project is for educational and portfolio purposes only.
-- It does not constitute investment advice.

-- ============================================================
-- 1. Financial Statements
-- ============================================================

CREATE TABLE financial_statements (
    id INTEGER PRIMARY KEY,
    bank_name TEXT NOT NULL,
    period TEXT NOT NULL,
    metric TEXT NOT NULL,
    category TEXT NOT NULL,
    value REAL,
    unit TEXT,
    data_type TEXT NOT NULL,
    source_document TEXT,
    source_section_or_page TEXT,
    validation_status TEXT,
    notes TEXT
);

-- Expected data_type values:
-- actual
-- forecast
-- calculated
-- estimated

-- ============================================================
-- 2. Banking Ratios
-- ============================================================

CREATE TABLE banking_ratios (
    id INTEGER PRIMARY KEY,
    bank_name TEXT NOT NULL,
    period TEXT NOT NULL,
    ratio_name TEXT NOT NULL,
    category TEXT NOT NULL,
    value REAL,
    unit TEXT,
    formula TEXT,
    reported_or_calculated TEXT,
    source_document TEXT,
    source_section_or_page TEXT,
    validation_status TEXT,
    notes TEXT
);

-- Expected reported_or_calculated values:
-- reported
-- calculated
-- estimated

-- ============================================================
-- 3. Source Mapping
-- ============================================================

CREATE TABLE source_mapping (
    id INTEGER PRIMARY KEY,
    data_item TEXT NOT NULL,
    category TEXT,
    period TEXT,
    value REAL,
    unit TEXT,
    source_document TEXT NOT NULL,
    source_type TEXT,
    source_section_or_page TEXT,
    reported_or_calculated TEXT,
    validation_status TEXT,
    notes TEXT
);

-- ============================================================
-- 4. Data Quality Checks
-- ============================================================

CREATE TABLE data_quality_checks (
    id INTEGER PRIMARY KEY,
    check_name TEXT NOT NULL,
    check_category TEXT NOT NULL,
    related_table TEXT,
    related_field TEXT,
    period TEXT,
    check_result TEXT,
    severity TEXT,
    validation_status TEXT,
    review_notes TEXT
);

-- Expected check_result values:
-- pass
-- warning
-- fail
-- pending

-- Expected severity values:
-- low
-- medium
-- high

-- ============================================================
-- 5. Forecast Assumptions
-- ============================================================

CREATE TABLE forecast_assumptions (
    id INTEGER PRIMARY KEY,
    assumption_name TEXT NOT NULL,
    category TEXT NOT NULL,
    period TEXT,
    scenario TEXT NOT NULL,
    value REAL,
    unit TEXT,
    assumption_logic TEXT,
    source_basis TEXT,
    validation_status TEXT,
    notes TEXT
);

-- Expected scenario values:
-- base
-- downside
-- upside

-- ============================================================
-- 6. Scenario Analysis
-- ============================================================

CREATE TABLE scenario_analysis (
    id INTEGER PRIMARY KEY,
    bank_name TEXT NOT NULL,
    period TEXT NOT NULL,
    scenario TEXT NOT NULL,
    metric TEXT NOT NULL,
    category TEXT NOT NULL,
    value REAL,
    unit TEXT,
    assumption_reference TEXT,
    validation_status TEXT,
    notes TEXT
);

-- ============================================================
-- 7. Market Data
-- ============================================================

CREATE TABLE market_data (
    id INTEGER PRIMARY KEY,
    bank_name TEXT NOT NULL,
    market_data_date TEXT NOT NULL,
    metric TEXT NOT NULL,
    value REAL,
    unit TEXT,
    source TEXT,
    validation_status TEXT,
    notes TEXT
);

-- ============================================================
-- 8. Peer Comparison
-- ============================================================

CREATE TABLE peer_comparison (
    id INTEGER PRIMARY KEY,
    peer_name TEXT NOT NULL,
    country TEXT,
    business_type TEXT,
    market_data_date TEXT,
    metric TEXT NOT NULL,
    value REAL,
    unit TEXT,
    source TEXT,
    validation_status TEXT,
    notes TEXT
);

-- ============================================================
-- 9. Suggested Period Convention
-- ============================================================

-- Main model periods:
-- 2022A
-- 2023A
-- 2024A
-- 2025A
-- 2026E
-- 2027E

-- A = Actual published historical data
-- E = Estimate / forecast

-- ============================================================
-- 10. Suggested Validation Status Convention
-- ============================================================

-- Pending
-- Reviewed
-- Validated
-- Needs Review
-- Not Available
-- Calculated

-- ============================================================
-- End of schema
-- ============================================================