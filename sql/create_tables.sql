-- CSV-aligned SQLite schema. Generated from current headers; reviewed 2026-09-28.
-- Run only against a disposable/local case-study database.

DROP TABLE IF EXISTS "financial_data";
CREATE TABLE "financial_data" (
    "bank_name" TEXT,
    "period" TEXT,
    "metric" TEXT,
    "category" TEXT,
    "value" NUMERIC,
    "unit" TEXT,
    "data_type" TEXT,
    "source_document" TEXT,
    "source_section_or_page" TEXT,
    "reported_or_calculated" TEXT,
    "validation_status" TEXT,
    "notes" TEXT
);

DROP TABLE IF EXISTS "banking_ratios";
CREATE TABLE "banking_ratios" (
    "ratio" TEXT,
    "category" TEXT,
    "formula" TEXT,
    "2022A" NUMERIC,
    "2023A" NUMERIC,
    "2024A" NUMERIC,
    "2025A" NUMERIC,
    "unit" TEXT,
    "source_status" TEXT,
    "notes" TEXT
);

DROP TABLE IF EXISTS "source_mapping";
CREATE TABLE "source_mapping" (
    "item" TEXT,
    "category" TEXT,
    "period" TEXT,
    "value" NUMERIC,
    "unit" TEXT,
    "source_document" TEXT,
    "source_type" TEXT,
    "source_section_or_page" TEXT,
    "reported_or_calculated" TEXT,
    "calculation_method" TEXT,
    "validation_status" TEXT,
    "notes" TEXT
);

DROP TABLE IF EXISTS "extraction_tracker";
CREATE TABLE "extraction_tracker" (
    "data_item" TEXT,
    "category" TEXT,
    "period" TEXT,
    "source_document" TEXT,
    "page_or_section" TEXT,
    "value_extracted" NUMERIC,
    "unit" TEXT,
    "entered_in_file" TEXT,
    "validation_status" TEXT,
    "review_notes" TEXT
);

DROP TABLE IF EXISTS "forecast_assumptions";
CREATE TABLE "forecast_assumptions" (
    "scenario" TEXT,
    "assumption_category" TEXT,
    "assumption" TEXT,
    "2026E" NUMERIC,
    "2027E" NUMERIC,
    "2028E" NUMERIC,
    "unit" TEXT,
    "rationale" TEXT,
    "source_or_basis" TEXT,
    "validation_status" TEXT,
    "notes" TEXT
);

DROP TABLE IF EXISTS "forecast_financials";
CREATE TABLE "forecast_financials" (
    "scenario" TEXT,
    "line_item" TEXT,
    "period" TEXT,
    "value" NUMERIC,
    "unit" TEXT,
    "calculation_method" TEXT,
    "source_or_basis" TEXT,
    "validation_status" TEXT,
    "notes" TEXT
);

DROP TABLE IF EXISTS "forecast_ratios";
CREATE TABLE "forecast_ratios" (
    "scenario" TEXT,
    "ratio" TEXT,
    "category" TEXT,
    "period" TEXT,
    "value" NUMERIC,
    "unit" TEXT,
    "calculation_method" TEXT,
    "source_or_basis" TEXT,
    "validation_status" TEXT,
    "notes" TEXT
);

DROP TABLE IF EXISTS "scenario_analysis";
CREATE TABLE "scenario_analysis" (
    "scenario" TEXT,
    "period" TEXT,
    "metric" TEXT,
    "category" TEXT,
    "value" NUMERIC,
    "unit" TEXT,
    "base_case_value" NUMERIC,
    "variance_vs_base" NUMERIC,
    "variance_vs_base_percent" NUMERIC,
    "scenario_logic" TEXT,
    "main_driver" TEXT,
    "risk_level" TEXT,
    "interpretation" TEXT,
    "source_or_basis" TEXT,
    "validation_status" TEXT,
    "notes" TEXT
);

DROP TABLE IF EXISTS "interim_financials";
CREATE TABLE "interim_financials" (
    "bank_name" TEXT,
    "period" TEXT,
    "metric" TEXT,
    "category" TEXT,
    "value" NUMERIC,
    "unit" TEXT,
    "data_type" TEXT,
    "source_document" TEXT,
    "source_section_or_page" TEXT,
    "reported_or_calculated" TEXT,
    "validation_status" TEXT,
    "notes" TEXT
);

DROP TABLE IF EXISTS "interim_ratios";
CREATE TABLE "interim_ratios" (
    "ratio" TEXT,
    "category" TEXT,
    "formula" TEXT,
    "period" TEXT,
    "value" NUMERIC,
    "unit" TEXT,
    "source_status" TEXT,
    "notes" TEXT
);
