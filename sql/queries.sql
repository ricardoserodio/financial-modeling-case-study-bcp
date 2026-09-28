-- Current quick-start queries; annual and interim periods remain separate.
SELECT period, metric, value, unit FROM financial_data ORDER BY period, metric;
SELECT period, metric, value, unit FROM interim_financials ORDER BY period, metric;
SELECT period, ratio, value, unit FROM interim_ratios ORDER BY period, ratio;
SELECT validation_status, COUNT(*) AS cells FROM source_mapping GROUP BY validation_status;
SELECT scenario, period, value AS net_income_eur_m FROM forecast_financials WHERE line_item = 'Net income' ORDER BY period, scenario;
