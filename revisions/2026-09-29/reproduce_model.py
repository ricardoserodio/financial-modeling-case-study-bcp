"""Reproducible 29 September document revision. Does not change the published v5."""
from pathlib import Path
from decimal import Decimal as D
import csv, json, math, shutil, hashlib, re, sys, importlib.util

ROOT = Path(__file__).resolve().parent
WORK = ROOT
SOURCE = ROOT / 'inputs'
DATA = ROOT / 'data'
for path in (ROOT, DATA): path.mkdir(parents=True, exist_ok=True)
PERIODS = ['2026E', '2027E', '2028E']
SCENARIOS = ['Conservative', 'Base', 'Optimistic']
DRIVERS = ['Net interest income growth', 'Other operating income growth', 'Operating costs growth', 'Cost of risk', 'Customer loans growth', 'Deposits and other customer resources growth']
FACTOR = D('.48')

def read(path):
    with path.open(encoding='utf-8-sig', newline='') as f: return list(csv.DictReader(f))
def write(name, rows):
    with (DATA / name).open('w', encoding='utf-8-sig', newline='') as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def get(rows, key, **criteria):
    found=[x for x in rows if all(x[k]==v for k,v in criteria.items())]
    assert len(found)==1, criteria
    return D(found[0][key])

def prepare_data():
    for name in ['financial_data.csv','banking_ratios.csv','interim_financials.csv','interim_ratios.csv','source_mapping.csv','source_manifest.json']:
        shutil.copyfile(SOURCE/'data'/name, DATA/name)
    assumptions=[r for r in read(SOURCE/'data/forecast_assumptions.csv') if r['assumption'] in DRIVERS]
    for r in assumptions:
        r['rationale']='Illustrative operating path; not issuer guidance. Capital policy is evaluated separately.'
        if r['scenario']=='Base' and r['assumption']=='Cost of risk':
            r['rationale']='40 bp in 2026/27 is a cautious normalisation reference near FY2024 adjusted 39 bp, not continuation of latest 32 bp; 45 bp in 2028 is an explicit additional stress.'
        r['notes']='2026 growth applies to H2/H1 flows or December/June stocks; later growth is annual. Conversion reference is 48%; separate sensitivities include 46%, 50% and H1 2026 50.2621%. No CET1 or reported-basis ROE forecast.'
    write('forecast_assumptions.csv',assumptions)
    inter=read(DATA/'interim_financials.csv')
    half={r['metric']:D(r['value']) for r in inter if r['period']=='2026H1A'}
    half['Other operating income']=half['Operating income']-half['Net interest income']
    half['Pre-provision operating profit']=half['Operating income']-half['Operating costs']
    flows=['Net interest income','Other operating income','Operating income','Operating costs','Pre-provision operating profit','Net credit impairments','Net income']
    metrics=flows+['Customer loans','Deposits and other customer resources']
    rows=[]; exact={}; sensitivities=[]; policies=[]; ratio_rows=[]
    factors=[D('.46'),D('.48'),D('.50'),half['Net income']/(half['Pre-provision operating profit']-half['Net credit impairments'])]
    def calc(scenario, factor, number=D):
        h={k:number(str(v)) for k,v in half.items()}; prior=h.copy(); out={}; hundred=number('100')
        for period in PERIODS:
            a=lambda name:number(str(get(assumptions,period,scenario=scenario,assumption=name)))
            cur={}
            for metric,driver in [('Net interest income',DRIVERS[0]),('Other operating income',DRIVERS[1]),('Operating costs',DRIVERS[2]),('Customer loans',DRIVERS[4]),('Deposits and other customer resources',DRIVERS[5])]:
                cur[metric]=prior[metric]*(1+a(driver)/hundred)
            cur['Operating income']=cur['Net interest income']+cur['Other operating income']
            cur['Pre-provision operating profit']=cur['Operating income']-cur['Operating costs']
            cur['Net credit impairments']=cur['Customer loans']*a('Cost of risk')/number('10000')*(number('.5') if period=='2026E' else 1)
            cur['Net income']=(cur['Pre-provision operating profit']-cur['Net credit impairments'])*number(str(factor))
            if period=='2026E':
                for metric in flows:cur[metric]+=h[metric]
            out[period]=cur;prior=cur
        return out
    checked=0
    for scenario in SCENARIOS:
        exact[scenario]=calc(scenario,FACTOR)
        # Independently recompute each period from compounded input growth, not the recursive production loop.
        for period_i,period in enumerate(PERIODS):
            def compounded(metric,driver,is_flow):
                rates=[get(assumptions,y,scenario=scenario,assumption=driver)/100 for y in PERIODS[:period_i+1]]
                v=half[metric]*(1+rates[0])
                if is_flow:v+=half[metric]
                for rate in rates[1:]:v*=1+rate
                return v
            independent={m:compounded(m,d,m in flows) for m,d in [('Net interest income',DRIVERS[0]),('Other operating income',DRIVERS[1]),('Operating costs',DRIVERS[2]),('Customer loans',DRIVERS[4]),('Deposits and other customer resources',DRIVERS[5])]}
            independent['Operating income']=independent['Net interest income']+independent['Other operating income']
            independent['Pre-provision operating profit']=independent['Operating income']-independent['Operating costs']
            charge=independent['Customer loans']*get(assumptions,period,scenario=scenario,assumption='Cost of risk')/10000
            independent['Net credit impairments']=charge if period_i else charge/2+half['Net credit impairments']
            residual=independent['Pre-provision operating profit']-independent['Net credit impairments']
            independent['Net income']=residual*FACTOR if period_i else half['Net income']+(residual-(half['Pre-provision operating profit']-half['Net credit impairments']))*FACTOR
            cur=exact[scenario][period]
            for metric in metrics:
                assert abs(cur[metric]-independent[metric])<D('.00000001'),(scenario,period,metric)
                checked+=1
                rows.append(dict(scenario=scenario,line_item=metric,period=period,value=str(cur[metric].quantize(D('.1'))),unit='EUR million',conversion_factor='0.48',validation_status='Model checked'))
            for name,v in [('Cost-to-income ratio',cur['Operating costs']/cur['Operating income']*100),('Loan-to-deposit ratio',cur['Customer loans']/cur['Deposits and other customer resources']*100)]:
                ratio_rows.append(dict(scenario=scenario,period=period,ratio=name,value=str(v.quantize(D('.001'))),unit='%'))
        for factor in factors:
            values=calc(scenario,factor)
            for period in PERIODS:
                sensitivities.append(dict(scenario=scenario,period=period,conversion_factor=str(factor),net_income=str(values[period]['Net income'].quantize(D('.1'))),unit='EUR million'))
        for retention in [D('0'),D('.1'),D('.2')]:
            equity=half['Equity']
            for period in PERIODS:
                eligible=exact[scenario][period]['Net income']-(half['Net income'] if period=='2026E' else 0)
                equity+=eligible*retention
                policies.append(dict(scenario=scenario,period=period,retention=str(retention),closing_book_equity=str(equity.quantize(D('.1'))),unit='EUR million',scope='Isolated retention sensitivity; no OCI, buybacks or regulatory adjustments; not CET1'))
    write('forecast_financials.csv',rows);write('forecast_ratios.csv',ratio_rows);write('conversion_sensitivity.csv',sensitivities);write('retention_sensitivity.csv',policies)
    sources=json.loads((DATA/'source_manifest.json').read_text())
    supplement=[]
    bridge=[('Net income','502.3','565.8'),('Pre-provision operating profit','1164.4','1230.1'),('Net credit impairments','89.8','104.4'),('Other impairments and provisions','280.6','188.5'),('Modification results','-5.1','-0.8'),('Income taxes','218.4','282.7'),('Non-controlling interests','68.2','87.9')]
    for item,a,b in bridge:
        for period,value in [('2025H1A',a),('2026H1A',b)]:supplement.append(dict(item=item,period=period,value=value,unit='EUR million',source='H12026.pdf',pdf_page=29,url=sources[-1]['url']))
    for item,a,b in [('NPE stock','1503','1442'),('Total loan impairment allowance stock','1366','1402')]:
        for period,value,source,page,url in [('2025A',a,'FY2025.pdf',20,sources[2]['url']),('2026H1A',b,'H12026.pdf',19,sources[-1]['url'])]:supplement.append(dict(item=item,period=period,value=value,unit='EUR million',source=source,pdf_page=page,url=url))
    supplement.append(dict(item='Cost of risk excluding specific reversal',period='2024A',value='39',unit='bps',source='FY2025.pdf',pdf_page=3,url=sources[2]['url']))
    write('supplemental_source_register.csv',supplement)
    deltas=[D('65.7'),D('-14.6'),D('92.1'),D('4.3'),D('-64.3'),D('-19.7')]
    assert D('502.3')+sum(deltas)==D('565.8')
    assert len(rows)==81 and len(sensitivities)==36 and len(policies)==27 and len(assumptions)*3==54
    for period in PERIODS:
        assert exact['Conservative'][period]['Net income']<exact['Base'][period]['Net income']<exact['Optimistic'][period]['Net income']
    assert abs(D('1366')/1503*100-D('90.9'))<D('.05')
    assert abs(D('1402')/1442*100-D('97.2'))<D('.05')
    # Cross-check sensitivities using linear conversion and cumulative retention identities.
    for row in sensitivities:
        sc,y,k=row['scenario'],row['period'],D(row['conversion_factor'])
        ref=exact[sc][y]['Net income']
        expected=(ref-half['Net income'])*k/FACTOR+half['Net income'] if y=='2026E' else ref*k/FACTOR
        assert abs(D(row['net_income'])-expected)<=D('.05')
    for row in policies:
        cumulative=sum(exact[row['scenario']][y]['Net income'] for y in PERIODS[:PERIODS.index(row['period'])+1])-half['Net income']
        expected=half['Equity']+cumulative*D(row['retention'])
        assert abs(D(row['closing_book_equity'])-expected)<=D('.05')
    checks={'status':'PASS','revision_date':'2026-09-29','information_cutoff':'2026-09-28','operating_inputs':54,'reference_conversion_factor':0.48,'independently_recomputed_forecast_cells':checked,'conversion_sensitivity_cells':len(sensitivities),'retention_sensitivity_cells':len(policies),'historical_core_observations':182,'supplemental_source_records_including_overlaps':len(supplement),'profit_bridge_reconciled':True,'cet1_projection':False,'roe_roa_projection':False}
    (ROOT/'checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
    print(json.dumps(checks))

if __name__=='__main__':prepare_data()
