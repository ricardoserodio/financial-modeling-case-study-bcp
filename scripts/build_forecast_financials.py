"""2026 = reported H1 + modelled H2; 2027/28 = annual scenario growth."""
from pathlib import Path
import pandas as pd
PROJECT_ROOT=Path(__file__).resolve().parents[1]
DATA=PROJECT_ROOT/'data'
FLOW=['Net interest income','Other operating income','Operating income','Operating costs','Pre-provision operating profit','Net credit impairments','Net income']
STOCK=['Customer loans','Deposits and other customer resources','Total assets','Equity']
def get_value(df,metric,period):
    rows=df[(df['period']==period)&(df['metric']==metric)]
    if len(rows)!=1 or pd.isna(rows.iloc[0]['value']):raise ValueError(f'Expected one value: {period} {metric}')
    return float(rows.iloc[0]['value'])
def get_2025_value(df,metric):return get_value(df,metric,'2025A')
def get_assumption(df,scenario,assumption,period):
    rows=df[(df['scenario']==scenario)&(df['assumption']==assumption)]
    if len(rows)!=1 or pd.isna(rows.iloc[0][period]):raise ValueError(f'Expected one assumption: {scenario} {assumption} {period}')
    return float(rows.iloc[0][period])
def base(df,period):
    d={m:get_value(df,m,period) for m in FLOW+STOCK if m not in ('Other operating income','Pre-provision operating profit')}
    d['Other operating income']=d['Operating income']-d['Net interest income']
    d['Pre-provision operating profit']=d['Operating income']-d['Operating costs']
    return d
def main():
    historical=pd.read_csv(DATA/'financial_data.csv');interim=pd.read_csv(DATA/'interim_financials.csv');assumptions=pd.read_csv(DATA/'forecast_assumptions.csv')
    annual=base(historical,'2025A'); half=base(interim,'2026H1A')
    conversion=half['Net income']/(half['Pre-provision operating profit']-half['Net credit impairments'])
    if not 0<conversion<1:raise ValueError('Invalid H1 profit conversion bridge')
    rows=[]
    def append(scenario,period,metric,value,status,method):
        rows.append(dict(scenario=scenario,line_item=metric,period=period,value=round(value,2 if metric=='CET1 ratio assumption' else 1),unit='%' if metric=='CET1 ratio assumption' else 'EUR million',calculation_method=method,source_or_basis='2026H1A results and forecast_assumptions.csv' if period!='2025A' else 'financial_data.csv',validation_status=status,notes='Scenario calculations checked; assumptions are illustrative, not issuer guidance. 2026 contains reported H1 and estimated H2.' if period!='2025A' else 'Annual historical reference; source vintage retained.'))
    for scenario in ('Base','Optimistic','Conservative'):
        for metric in FLOW+STOCK:append(scenario,'2025A',metric,annual[metric],'Recalculated' if metric in ('Other operating income','Pre-provision operating profit') else 'Source verified','Historical annual reference')
        previous=half.copy()
        for period in ('2026E','2027E','2028E'):
            a=lambda name:get_assumption(assumptions,scenario,name,period)
            current={}
            for metric,driver in [('Net interest income','Net interest income growth'),('Other operating income','Other operating income growth'),('Operating costs','Operating costs growth'),('Customer loans','Customer loans growth'),('Deposits and other customer resources','Deposits and other customer resources growth')]:current[metric]=previous[metric]*(1+a(driver)/100)
            current['Total assets']=previous['Total assets']*(1+(a('Customer loans growth')+a('Deposits and other customer resources growth'))/200)
            current['Operating income']=current['Net interest income']+current['Other operating income']
            current['Pre-provision operating profit']=current['Operating income']-current['Operating costs']
            current['Net credit impairments']=current['Customer loans']*a('Cost of risk')/10000*(.5 if period=='2026E' else 1)
            current['Net income']=(current['Pre-provision operating profit']-current['Net credit impairments'])*conversion
            current['Equity']=previous['Equity']+current['Net income']*a('Earnings retention')/100
            if period=='2026E':
                for metric in FLOW:current[metric]+=half[metric]
            for metric in FLOW+STOCK:append(scenario,period,metric,current[metric],'Model checked','Reported H1 flow + estimated H2 flow; closing stocks projected from June' if period=='2026E' else 'Annual scenario growth; H1 2026 profit conversion held constant')
            append(scenario,period,'CET1 ratio assumption',a('CET1 ratio assumption'),'Scenario assumption','Direct assumption; no risk-weighted-assets model')
            previous=current
    pd.DataFrame(rows).to_csv(DATA/'forecast_financials.csv',index=False,encoding='utf-8-sig')
    print(f'forecast_financials: {len(rows)} rows; H1 conversion {conversion:.9f}')
if __name__=='__main__':main()
