"""Independent numeric and relational checks for the publication datasets."""
import csv,json,sqlite3,re
from pathlib import Path
from decimal import Decimal as N, ROUND_HALF_EVEN
ROOT=Path(__file__).resolve().parents[1]
def rows(name):
    with (ROOT/'data'/f'{name}.csv').open(encoding='utf-8-sig',newline='') as f:
        out=list(csv.DictReader(f))
    assert all(None not in r for r in out),name
    return out
def index(data,keys):
    result={tuple(r[k] for k in keys):r for r in data}
    assert len(result)==len(data),('Duplicate keys',keys)
    return result
def near(actual,expected,tolerance='.000001'):
    assert abs(N(str(actual))-N(str(expected)))<=N(tolerance),(actual,expected)
def main():
    financial=rows('financial_data'); ratios=rows('banking_ratios'); interim=rows('interim_financials');ir=rows('interim_ratios')
    mapping=index(rows('source_mapping'),['item','period']);tracker=index(rows('extraction_tracker'),['data_item','period'])
    assert len(financial)==52 and len(ratios)==18 and len(interim)==26 and len(ir)==32
    assert len(mapping)==len(tracker)==182
    assert sum(r['validation_status']=='Source verified' for r in mapping.values())==176
    assert sum(r['validation_status']=='Recalculated' for r in mapping.values())==6
    points=[(r['metric'],r['period'],r['value']) for r in financial+interim]+[(r['ratio'],p,r[p]) for r in ratios for p in ('2022A','2023A','2024A','2025A')]+[(r['ratio'],r['period'],r['value']) for r in ir]
    assert len(set((m,p) for m,p,v in points))==182
    for m,p,v in points:
        near(v,mapping[m,p]['value']);near(v,tracker[m,p]['value_extracted'])
        assert mapping[m,p]['source_section_or_page'].startswith('PDF p')
        assert 'https://ind.millenniumbcp.pt/' in mapping[m,p]['notes']
    allf=index(financial+interim,['metric','period'])
    for period in ('2022A','2023A','2024A','2025A','2025H1A','2026H1A'):
        v=lambda m:N(allf[m,period]['value'])
        near(v('Impairments and provisions'),v('Net credit impairments')+v('Other impairments and provisions'))
        near(v('Customer loans')/v('Deposits and other customer resources')*100,mapping['Loan-to-deposit ratio',period]['value'],'.055')
    forecast=index(rows('forecast_financials'),['scenario','period','line_item'])
    fr=index(rows('forecast_ratios'),['scenario','period','ratio'])
    assumptions=index(rows('forecast_assumptions'),['scenario','assumption'])
    assert len(forecast)==141 and len(fr)==72 and len(assumptions)==24
    flows=['Net interest income','Other operating income','Operating income','Operating costs','Pre-provision operating profit','Net credit impairments','Net income']
    stocks=['Customer loans','Deposits and other customer resources','Total assets','Equity']
    half={m:N(allf[m,'2026H1A']['value']) for m in flows+stocks if m not in ('Other operating income','Pre-provision operating profit')}
    half['Other operating income']=half['Operating income']-half['Net interest income'];half['Pre-provision operating profit']=half['Operating income']-half['Operating costs']
    factor=half['Net income']/(half['Pre-provision operating profit']-half['Net credit impairments'])
    checked=0
    for scenario in ('Base','Optimistic','Conservative'):
        previous=dict(half)
        for period in ('2026E','2027E','2028E'):
            a=lambda key:N(assumptions[scenario,key][period])
            n={m:previous[m]*(1+a(m+' growth')/100) for m in ['Net interest income','Other operating income','Operating costs','Customer loans','Deposits and other customer resources']}
            n['Operating income']=n['Net interest income']+n['Other operating income'];n['Pre-provision operating profit']=n['Operating income']-n['Operating costs']
            n['Total assets']=previous['Total assets']*(1+(a('Customer loans growth')+a('Deposits and other customer resources growth'))/200)
            n['Net credit impairments']=n['Customer loans']*a('Cost of risk')/10000/(2 if period=='2026E' else 1)
            n['Net income']=(n['Pre-provision operating profit']-n['Net credit impairments'])*factor
            n['Equity']=previous['Equity']+n['Net income']*a('Earnings retention')/100
            if period=='2026E':
                for m in flows:n[m]+=half[m]
            for m in flows+stocks:
                near(forecast[scenario,period,m]['value'],n[m],'.051');checked+=1
            near(forecast[scenario,period,'CET1 ratio assumption']['value'],a('CET1 ratio assumption'));checked+=1
            previous=n
            v=lambda m:N(forecast[scenario,period,m]['value'])
            pairs={'ROE':v('Net income')/v('Equity')*100,'ROA':v('Net income')/v('Total assets')*100,'Cost-to-income ratio':v('Operating costs')/v('Operating income')*100,'Loan-to-deposit ratio':v('Customer loans')/v('Deposits and other customer resources')*100,'Cost of risk':v('Net credit impairments')/v('Customer loans')*10000,'CET1 ratio assumption':a('CET1 ratio assumption')}
            for m,x in pairs.items():near(fr[scenario,period,m]['value'],x,'.000501');checked+=1
    # Baseline values must remain annual actuals, not half-year values.
    for (s,p,m),r in forecast.items():
        if p=='2025A':
            expected=N(allf[m,p]['value']) if m in stocks or m in ('Net interest income','Operating income','Operating costs','Net credit impairments','Net income') else N(allf['Operating income',p]['value'])-N(allf['Net interest income' if m=='Other operating income' else 'Operating costs',p]['value'])
            near(r['value'],expected)
    for r in rows('scenario_analysis'):
        table=forecast if r['source_or_basis']=='forecast_financials.csv' else fr
        actual=table[r['scenario'],r['period'],r['metric']]['value'];base=table['Base',r['period'],r['metric']]['value']
        near(r['value'],actual);near(r['base_case_value'],base);near(r['variance_vs_base'],N(actual)-N(base),'.000501')
        near(r['variance_vs_base_percent'],(N(actual)-N(base))/abs(N(base))*100,'.000501')
    for period in ('2026E','2027E','2028E'):
        assert N(forecast['Conservative',period,'Net income']['value'])<N(forecast['Base',period,'Net income']['value'])<N(forecast['Optimistic',period,'Net income']['value'])
    db=sqlite3.connect(':memory:');db.executescript((ROOT/'sql/create_tables.sql').read_text(encoding='utf-8-sig'))
    names=['financial_data','banking_ratios','interim_financials','interim_ratios','source_mapping','extraction_tracker','forecast_assumptions','forecast_financials','forecast_ratios','scenario_analysis']
    counts={}
    for name in names:
        data=rows(name);counts[name]=len(data)
        assert all(r.get('validation_status',r.get('source_status','')) in {'Source verified','Recalculated','Model checked','Scenario assumption'} for r in data),name
        db.executemany(f'INSERT INTO "{name}" VALUES ('+','.join('?' for c in data[0])+')',[list(r.values()) for r in data])
    count=0
    for path in sorted((ROOT/'sql').glob('*.sql')):
        if path.name in ('create_tables.sql','schema.sql'):continue
        sql=re.sub(r'--[^\n]*','',path.read_text(encoding='utf-8-sig'))
        for statement in filter(str.strip,sql.split(';')):
            db.execute(statement).fetchall();count+=1
    assert db.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
    result={'status':'PASS','historical_cells':182,'reported_cells':176,'recalculated_cells':6,'scenario_parameters':72,'forecast_cells_recomputed':checked,'scenario_comparisons':126,'sql_statements':count,'tables':counts,'h1_conversion':float(factor),'scope':'Data and calculation validation; issuer guidance and independent audit are not claimed.'}
    out=ROOT/'docs/validation_results.json';out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
    return result
if __name__=='__main__':main()
