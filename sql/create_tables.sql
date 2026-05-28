-- Financial Modeling Case Study – Millennium bcp / Portuguese Listed Bank
-- SQL schema for analytical exploration of the project datasets.
--
-- Purpose:
-- This SQL layer is designed for portfolio, documentation and analytical demonstration purposes.
-- It mirrors the structure of the CSV files used in the project.
--
-- Disclaimer:
-- This project uses publicly available information and scenario-based educational estimates.
-- It does not constitute financial advice, investment advice, valuation advice or a recommendation
-- to buy, sell or hold any financial instrument.

DROP TABLE IF EXISTS financial_data;
DROP TABLE IF EXISTS banking_ratios;
DROP TABLE IF EXISTS source_mapping;
DROP TABLE IF EXISTS extraction_tracker;
DROP TABLE IF EXISTS forecast_assumptions;
DROP TABLE IF EXISTS forecast_financials;
DROP TABLE IF EXISTS forecast_ratios;
DROP TABLE IF EXISTS scenario_analysis;

CREATE TABLE financial_data (
    bank_name TEXT,
    period TEXT,
    metric TEXT,
    category TEXT,
    value NUMERIC,
    unit TEXT,
    validation_status TEXT,
    reported_or_calculated TEXT,
    source_document TEXT,
    notes TEXT
);

CREATE TABLE banking_ratios (
    ratio TEXT,
    category TEXT,
    formula TEXT,
    "2022A" NUMERIC,
    "2023A" NUMERIC,
    "2024A" NUMERIC,
    "2025A" NUMERIC,
    unit TEXT,
    source_status TEXT,
    notes TEXT
);

CREATE TABLE source_mapping (
    dataset TEXT,
    field TEXT,
    source_document TEXT,
    source_section TEXT,
    source_period TEXT,
    validation_status TEXT,
    notes TEXT
);

CREATE TABLE extraction_tracker (
    item TEXT,
    category TEXT,
    source_document TEXT,
    period TEXT,
    extraction_status TEXT,
    validation_status TEXT,
    notes TEXT
);

CREATE TABLE forecast_assumptions (
    scenario TEXT,
    assumption_category TEXT,
    assumption TEXT,
    "2026E" NUMERIC,
    "2027E" NUMERIC,
    "2028E" NUMERIC,
    unit TEXT,
    rationale TEXT,
    source_or_basis TEXT,
    validation_status TEXT,
    notes TEXT
);

CREATE TABLE forecast_financials (
    scenario TEXT,
    line_item TEXT,
    period TEXT,
    value NUMERIC,
    unit TEXT,
    calculation_method TEXT,
    source_or_basis TEXT,
    validation_status TEXT,
    notes TEXT
);

CREATE TABLE forecast_ratios (
    scenario TEXT,
    ratio TEXT,
    category TEXT,
    period TEXT,
    value NUMERIC,
    unit TEXT,
    calculation_method TEXT,
    source_or_basis TEXT,
    validation_status TEXT,
    notes TEXT
);

CREATE TABLE scenario_analysis (
    scenario TEXT,
    period TEXT,
    metric TEXT,
    category TEXT,
    value NUMERIC,
    unit TEXT,
    base_case_value NUMERIC,
    variance_vs_base NUMERIC,
    variance_vs_base_percent NUMERIC,
    scenario_logic TEXT,
    main_driver TEXT,
    risk_level TEXT,
    interpretation TEXT,
    source_or_basis TEXT,
    validation_status TEXT,
    notes TEXT
);
