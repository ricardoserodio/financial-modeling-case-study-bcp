from pathlib import Path
import csv,json,shutil,re,html
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
ROOT=Path(__file__).resolve().parents[1]; P=ROOT;D=P/'data';R=P/'reports'
def read(n):
    with (D/f'{n}.csv').open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
fin=read('financial_data');rat=read('banking_ratios');inter=read('interim_financials');ir=read('interim_ratios');mapping=read('source_mapping');assum=read('forecast_assumptions');ff=read('forecast_financials');fr=read('forecast_ratios');sources=json.loads((D/'source_manifest.json').read_text());valid=json.loads((P/'docs/validation_results.json').read_text())
navy=colors.HexColor('#1c3557');teal=colors.HexColor('#007c83');gray=colors.HexColor('#eef2f5');ink=colors.HexColor('#263646')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleBCP',fontName='Helvetica-Bold',fontSize=28,leading=32,textColor=navy,spaceAfter=18))
styles.add(ParagraphStyle(name='Deck',fontSize=13,leading=18,textColor=ink,spaceAfter=16))
styles.add(ParagraphStyle(name='BodyBCP',fontSize=9.5,leading=14,textColor=ink,spaceAfter=10))
styles.add(ParagraphStyle(name='SmallBCP',fontSize=7.5,leading=10,textColor=ink,spaceAfter=5))
styles.add(ParagraphStyle(name='Cell',fontSize=8,leading=10,textColor=ink))
styles.add(ParagraphStyle(name='HeadCell',fontSize=8,leading=10,textColor=colors.white,fontName='Helvetica-Bold'))
styles['Heading1'].textColor=navy;styles['Heading1'].fontSize=18;styles['Heading1'].leading=23
styles['Heading2'].textColor=teal;styles['Heading2'].fontSize=12
def para(s,style='BodyBCP'):return Paragraph(s,styles[style])
def table(headers,rows,widths=None,size='Cell',compact=False):
    cells=[[para(html.escape(str(c)),'HeadCell') for c in headers]]+[[para(html.escape(str(c)),size) for c in row] for row in rows]
    t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,gray]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,0),1,teal)]))
    if compact:t.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
    return t
def fmt(v,d=1):return f'{float(v):,.{d}f}'
def val(data,**kw):return next(r for r in data if all(r[k]==v for k,v in kw.items()))['value']
def page(canvas,doc):
    canvas.setStrokeColor(teal);canvas.setLineWidth(1);canvas.line(43,802,552,802)
    canvas.setFont('Helvetica',8);canvas.setFillColor(navy);canvas.drawString(43,815,'RICARDO SERODIO  /  BANKING ANALYTICS')
    canvas.setFillColor(ink);canvas.setFont('Helvetica',7);canvas.drawString(43,26,'Millennium bcp case study | Updated 28 Sep 2026 | Public-source educational analysis')
    canvas.drawRightString(552,26,str(doc.page))
def build(path,story,title):
    SimpleDocTemplate(str(path),pagesize=A4,leftMargin=43,rightMargin=43,topMargin=58,bottomMargin=43,title=title,author='Ricardo Serodio').build(story,onFirstPage=page,onLaterPages=page)
def t(pt,en,lang):return pt if lang=='pt' else en
def add(story,s,style='BodyBCP'):story.append(para(s,style))
annual_table=[[m]+[fmt(val(fin,metric=m,period=p)) for p in ['2022A','2023A','2024A','2025A']] for m in dict.fromkeys(r['metric'] for r in fin)]
keyrat=['ROE','Net interest margin','Cost-to-income ratio','NPE ratio','LCR','CET1 fully implemented ratio']
source_ids={s['file']:f'S{i+1}' for i,s in enumerate(sources)}
for lang in ['pt','en']:
    story=[];md=[]
    title=t('Millennium bcp\nAnálise financeira e bancária','Millennium bcp\nFinancial and banking analysis',lang)
    add(story,title.replace('\n','<br/>'),'TitleBCP');add(story,t('Histórico 2022-2025 · Atualização do 1.º semestre de 2026 · Cenários 2026-2028','2022-2025 history · H1 2026 update · 2026-2028 scenarios',lang),'Deck')
    add(story,t('Estudo de caso de Ricardo Serodio | Dados disponíveis em 28 de setembro de 2026','Case study by Ricardo Serodio | Information available on 28 September 2026',lang),'SmallBCP')
    story.append(Spacer(1,18))
    story.append(table(['H1 2026','ROE','NPE','SOURCE COVERAGE'],[['EUR 565.8m','14.6%','2.2%','182 / 182'],['Net income','Reported ratio','Reported ratio','176 reported + 6 calculated']],[127,127,127,127]))
    story.append(Spacer(1,20));add(story,t('Leitura executiva','Executive view',lang),'Heading1')
    executive=t('O resultado líquido do Grupo atingiu 565,8 milhões de euros no primeiro semestre de 2026, mais 12,7% do que no período homólogo. O produto bancário aumentou 5,5% e os custos operacionais 5,4%, mantendo o rácio de eficiência próximo de 37%. A descida das outras imparidades e provisões ajudou o crescimento do resultado, enquanto as imparidades de crédito aumentaram.','Group net income reached EUR 565.8 million in H1 2026, up 12.7% year on year. Operating income rose 5.5% and operating costs 5.4%, keeping cost-to-income close to 37%. Lower other impairments and provisions supported earnings growth, while credit impairment charges increased.',lang)
    add(story,executive)
    add(story,t('A qualidade do crédito melhorou: o NPE passou de 2,7% para 2,2% e a cobertura subiu de 84,5% para 97,2%. O CET1 fully implemented foi de 15,1%, com a qualificação de estimativa da fonte e inclusão de 10% dos resultados intercalares não auditados.','Credit quality improved: NPE fell from 2.7% to 2.2% and coverage increased from 84.5% to 97.2%. Fully implemented CET1 was 15.1%, retaining the source qualification as an estimate including 10% of unaudited interim earnings.',lang))
    add(story,t('O projeto liga fontes oficiais, dados CSV, cálculos Python, consultas SQL e Power BI. Os cenários são hipóteses educativas; os seus cálculos foram verificados, mas não constituem projeções do banco.','The project connects official sources, CSV data, Python calculations, SQL queries and Power BI. Scenarios are educational assumptions: their arithmetic is checked, but they are not bank forecasts.',lang))
    add(story,t('Fonte principal da atualização: comunicado de resultados de 29/07/2026, páginas PDF 2, 3 e 9. O anexo apresenta o registo completo dos 182 valores, respetivas páginas, fontes e qualificações.','Update source: results release dated 29 July 2026, PDF pages 2, 3 and 9. The appendix provides all 182 observations, page references, sources and qualifications.',lang),'SmallBCP')
    md+=['# '+title.replace('\n',' - '),'',executive,'']
    story.append(PageBreak());add(story,t('01 / Histórico anual','01 / Annual history',lang),'Heading1')
    add(story,t('Milhões de euros. Valores anuais do Grupo; crédito líquido. Os comparativos de 2023 seguem a divulgação FY2024 e os de 2024 a divulgação FY2025.','EUR million. Full-year Group figures; net customer loans. 2023 comparatives follow the FY2024 release and 2024 comparatives follow the FY2025 release.',lang))
    story.append(table(['Metric','2022A','2023A','2024A','2025A'],annual_table,[221,72,72,72,72]))
    story.append(Spacer(1,14));story.append(table(['Ratio (%)','2022A','2023A','2024A','2025A'],[[m]+[next(r for r in rat if r['ratio']==m)[p] for p in ['2022A','2023A','2024A','2025A']] for m in keyrat],[221,72,72,72,72]))
    add(story,t('A trajetória anual agrega fontes de diferentes datas. Não representa uma série integralmente reexpressa numa única base. O total de imparidades é a soma das duas componentes identificadas; não inclui resultados de modificações.','Annual history combines different source vintages. It is not a fully restated single-vintage series. Total impairments is the sum of the two identified components; modification results are excluded.',lang),'SmallBCP')
    md+=['## Annual history','', '| Metric | 2022A | 2023A | 2024A | 2025A |','|---|---:|---:|---:|---:|']+['| '+' | '.join(row)+' |' for row in annual_table]+['']
    story.append(PageBreak());add(story,t('02 / Atualização semestral','02 / Half-year update',lang),'Heading1')
    add(story,t('Comparação 1S2026 / 1S2025 reexpresso. Fluxos de seis meses; balanços em 30 de junho. As duas bases ficam separadas das séries anuais.','H1 2026 versus restated H1 2025. Six-month flows; balance sheets as at 30 June. These observations remain separate from annual series.',lang))
    selected=['Net interest income','Fees and commissions','Operating income','Operating costs','Net credit impairments','Other impairments and provisions','Net income','Customer loans','Deposits and other customer resources','Total assets','Equity']
    growth=[]
    for m in selected:
        a=float(val(inter,metric=m,period='2025H1A'));b=float(val(inter,metric=m,period='2026H1A'));growth.append([m,fmt(a),fmt(b),f'{(b/a-1)*100:+.1f}%'])
    story.append(table(['EUR million','H1 2025','H1 2026','YoY calc.'],growth,[254,85,85,85]))
    add(story,t('Variações calculadas a partir dos montantes arredondados apresentados. No resultado líquido, este cálculo dá 12,6%; a variação oficial reportada é 12,7%.','Changes calculated from the displayed rounded amounts. For net income this gives 12.6%; the official reported change is 12.7%.',lang),'SmallBCP')
    story.append(Spacer(1,12));rr=['ROE','Net interest margin','Cost-to-income ratio','Cost of risk','NPE ratio','NPE coverage ratio','Loan-to-deposit ratio','LCR','NSFR','CET1 fully implemented ratio']
    story.append(table(['Ratio','H1 2025','H1 2026','Unit'],[[m,val(ir,ratio=m,period='2025H1A'),val(ir,ratio=m,period='2026H1A'),next(r['unit'] for r in ir if r['ratio']==m)] for m in rr],[254,85,85,85]))
    add(story,t('Reexpressão: os reverse repos foram excluídos do crédito; impacto de 96 M€ em junho de 2025. Os repos foram excluídos dos depósitos, sem impacto no comparativo de junho de 2025. NPE e cobertura seguem o glossário da fonte.','Restatement: reverse repos were excluded from loans, with a EUR 96m impact in June 2025. Repos were excluded from deposits, with no impact on the June 2025 comparative. NPE and coverage retain the source glossary definitions.',lang),'SmallBCP')
    md+=['## H1 2026 update','','| Metric | H1 2025 | H1 2026 | YoY calculated |','|---|---:|---:|---:|']+['| '+' | '.join(row)+' |' for row in growth]+['','Calculated from rounded amounts: net income 12.6%, versus the official reported 12.7%.','']
    story.append(PageBreak());add(story,t('03 / Hipóteses dos cenários','03 / Scenario assumptions',lang),'Heading1')
    add(story,t('2026E combina o 1S2026 reportado com um segundo semestre estimado. Em 2026, as taxas de crescimento abaixo aplicam-se ao 2S face ao 1S ou ao balanço de dezembro face a junho. Em 2027 e 2028 são taxas anuais.','2026E combines reported H1 2026 with an estimated second half. For 2026, growth rates below apply to H2 versus H1 flows or December versus June balances. In 2027 and 2028 they are annual rates.',lang))
    short={'Deposits and other customer resources growth':'Deposits/resources growth','Other operating income growth':'Other income growth','Net interest income growth':'Net interest income growth','Operating costs growth':'Operating costs growth','Customer loans growth':'Net customer loans growth','CET1 ratio assumption':'CET1 assumption','Earnings retention':'Earnings retention','Cost of risk':'Cost of risk'}
    for scenario in ['Base','Optimistic','Conservative']:
        add(story,scenario,'Heading2');story.append(table(['Driver','2026E','2027E','2028E','Unit'],[[short[r['assumption']],r['2026E'],r['2027E'],r['2028E'],r['unit']] for r in assum if r['scenario']==scenario],[221,72,72,72,72],compact=True));story.append(Spacer(1,8))
    add(story,t('Os valores traduzem escolhas de sensibilidade do autor, sem probabilidades atribuídas. O CET1 é introduzido diretamente; a retenção não modela recompras, OCI ou requisitos de capital.','Values represent author-selected sensitivities, with no assigned probabilities. CET1 is entered directly; retention does not model buybacks, OCI or regulatory capital requirements.',lang),'SmallBCP')
    story.append(PageBreak());add(story,t('04 / Resultados e limites do modelo','04 / Model outcomes and limits',lang),'Heading1')
    scenario_rows=[]
    for p in ['2026E','2027E','2028E']:
        for s in ['Conservative','Base','Optimistic']:
            scenario_rows.append([p,s,fmt(val(ff,scenario=s,period=p,line_item='Net income')),fmt(val(fr,scenario=s,period=p,ratio='ROE'),2),fmt(val(fr,scenario=s,period=p,ratio='Cost-to-income ratio'),2),fmt(val(fr,scenario=s,period=p,ratio='CET1 ratio assumption'),1)])
    story.append(table(['Year','Scenario','Net income M€','ROE proxy %','C/I %','CET1 %'],scenario_rows,[55,93,95,90,90,86]));story.append(Spacer(1,15))
    add(story,t('Como se calcula','Calculation approach',lang),'Heading2')
    model=t('Margem financeira, outros proveitos e custos evoluem pelos drivers de cada cenário. O crédito e os depósitos são projetados a partir de junho de 2026. Os ativos crescem à média das taxas de crédito e depósitos. A imparidade do 2S corresponde a crédito líquido projetado × custo do risco / 10 000 × 0,5.','Net interest income, other income and costs follow scenario drivers. Loans and deposits are projected from June 2026. Assets grow at the average of loan and deposit growth rates. H2 credit impairments equal projected net loans × cost of risk / 10,000 × 0.5.',lang)
    add(story,model)
    add(story,t('O fator de conversão do lucro é 565,8 / (1 950,3 - 720,2 - 104,4) = 50,2621%. Este fator absorve implicitamente outras imparidades, modificações, impostos e interesses minoritários. Mantê-lo fixo é uma simplificação importante. Em 2026 somam-se os fluxos reais do 1S aos fluxos estimados do 2S; os saldos de balanço não são somados.','The profit conversion factor is 565.8 / (1,950.3 - 720.2 - 104.4) = 50.2621%. It implicitly absorbs other impairments, modification results, taxes and non-controlling interests. Holding it fixed is a material simplification. For 2026, actual H1 flows are added to estimated H2 flows; balance-sheet stocks are not added.',lang))
    add(story,t('ROE e ROA projetados dividem o lucro pelo saldo final de capitais próprios e ativos. São proxies diferentes dos indicadores reportados, que usam médias e ajustamentos próprios. A passagem de 2025A a 2026E não deve ser interpretada como uma variação diretamente comparável do ROE.','Forecast ROE and ROA divide profit by closing equity and assets. These proxies differ from reported indicators, which use averages and issuer-specific adjustments. The transition from 2025A to 2026E must not be read as a directly comparable change in reported ROE.',lang))
    add(story,t('A retenção de resultados afeta apenas o lucro estimado futuro. Não existe previsão autónoma de taxas de imposto, carteiras por risco, RWA, dividendos ou recompras. As hipóteses não foram calibradas por um modelo estatístico nem validadas por backtesting.','Earnings retention affects only future estimated profit. There is no separate tax, risk-portfolio, RWA, dividend or buyback forecast. Assumptions are not statistically calibrated or backtested.',lang),'SmallBCP')
    md+=['## Scenario outcomes','','| Year | Scenario | Net income EUR m | ROE proxy % | C/I % | CET1 % |','|---|---|---:|---:|---:|---:|']+['| '+' | '.join(row)+' |' for row in scenario_rows]+['',model,'']
    story.append(PageBreak());add(story,t('05 / Validação, fontes e reprodução','05 / Validation, sources and reproduction',lang),'Heading1')
    story.append(table(['Check','Result'],[['Source register','182 unique historical cells: 124 annual + 58 interim'],['Evidence classification','176 source-verified reported cells; 6 recalculated totals'],['Active data completeness','No blank values or duplicate metric-period keys'],['Scenario validation','72 parameters; 162 forecast cells recomputed'],['Scenario comparison checks','126 values and variances reconciled'],['SQLite checks','10 tables; 36 SQL statements passed']],[215,294]))
    story.append(Spacer(1,12));add(story,t('Estados com significado explícito','Explicit status definitions',lang),'Heading2')
    add(story,t('<b>Source verified</b>: valor confrontado com a fonte e o período identificados. <b>Recalculated</b>: soma verificada. <b>Model checked</b>: cálculo reconciliado. <b>Scenario assumption</b>: hipótese educativa documentada. Estes estados não afirmam revisão por auditor independente.','<b>Source verified</b>: value matched to the specified source and period. <b>Recalculated</b>: arithmetic total checked. <b>Model checked</b>: calculation reconciled. <b>Scenario assumption</b>: documented educational assumption. These labels do not claim independent audit assurance.',lang))
    add(story,t('As 40 linhas antigas marcadas Pending no mapa eram espaços de planeamento sem valores. O histórico foi preservado no arquivo e substituído por um registo único das observações efetivamente usadas. O anexo inclui todas as observações, não apenas as primeiras linhas visíveis no dashboard.','The 40 old Pending mapping rows were empty planning placeholders. The history is preserved in the archive and replaced by a unique register of observations actually used. The appendix contains every observation, beyond the rows visible in the dashboard.',lang))
    add(story,t('Fontes oficiais (links)','Official sources (links)',lang),'Heading2')
    for s in sources:add(story,f'{source_ids[s["file"]]} - <link href="{s["url"]}" color="#007c83">{s["file"]}</link>','SmallBCP')
    add(story,t('Reprodução: seguir RUN_PROJECT.md. Os CSV alimentam os scripts Python, a base SQLite e as consultas Power Query. A pasta de dados do Power BI deve corresponder à cópia local do repositório. Código, anexo e registo das fontes acompanham o estudo.','Reproduction: follow RUN_PROJECT.md. CSV files feed Python scripts, SQLite and Power Query. Set the Power BI data folder to the local repository copy. Code, appendix and source register accompany this case study.',lang),'SmallBCP')
    add(story,t('Âmbito: análise educativa de desempenho bancário. Avaliação de mercado e comparação com pares permanecem fora do modelo. Não constitui recomendação de investimento.','Scope: educational banking-performance analysis. Market valuation and peer comparison remain outside the model. This is not an investment recommendation.',lang),'SmallBCP')
    target=R/f'ricardo_serodio_bcp_banking_analytics_case_study_{lang}.pdf';build(target,story,title)
    md+=['## Validation','',json.dumps(valid,indent=2),'','## Sources','']+[f'- [{source_ids[s["file"]]} - {s["file"]}]({s["url"]})' for s in sources]+['','See [validation appendix](bcp_validation_appendix_2026-09-28.pdf) for the complete observation register.','']
    (R/f'financial_modeling_report_{lang}.md').write_text('\n'.join(md),encoding='utf-8')

story=[]
for period in ['2022A','2023A','2024A','2025A','2025H1A','2026H1A']:
    if story:story.append(PageBreak())
    add(story,'Validation appendix / Anexo de validação','Heading1');add(story,period+' - complete observation register','Heading2')
    add(story,'Amounts are EUR million unless the unit says otherwise. SV = Source verified; RC = Recalculated. PDF page numbers count the cover page. Each annual period has 31 cells; each interim period has 29.','SmallBCP')
    data=[]
    for row in mapping:
        if row['period']==period:
            pg=re.search(r'PDF p(\d+)',row['source_section_or_page']).group(1)
            data.append([row['item'],fmt(row['value'],3 if row['item'] in ('EPS','Book value per share') else 2 if row['item']=='Net interest margin' else 1),row['unit'].replace('EUR million','EUR m'),source_ids[row['source_document']]+' p'+pg,'RC' if row['validation_status']=='Recalculated' else 'SV'])
    story.append(table(['Metric / Indicador','Value','Unit','Source','Status'],data,[267,73,55,64,50],compact=True))
    add(story,'RC totals = net credit impairments + other impairments and provisions. Reported ROE/ROA, per-share values and capital ratios preserve the issuer methodology and qualifiers. See source catalogue and report methodology.','SmallBCP')
story.append(PageBreak());add(story,'Source catalogue / Catálogo de fontes','Heading1')
add(story,'Retrieved and verified on 28 September 2026. SHA-256 identifies the exact local evidence file used. Original issuer PDFs remain at the official links.','BodyBCP')
for s in sources:
    add(story,f'{source_ids[s["file"]]} / {s["file"]}','Heading2');add(story,f'<link href="{s["url"]}" color="#007c83">Official PDF / PDF oficial</link>','SmallBCP');add(story,'SHA-256: '+s['sha256'][:32]+'<br/>'+s['sha256'][32:],'SmallBCP')
add(story,'Source vintages: 2022 from FY2022; 2023 from FY2024 comparative; 2024 from FY2025 comparative; 2025 from FY2025. Per-share data use annual report tables. H1 2025 and H1 2026 both use the H1 2026 release. Capital values preserve source estimates. Reclassification details are in the main report.','SmallBCP')
build(R/'bcp_validation_appendix_2026-09-28.pdf',story,'BCP - Validation appendix - 28 September 2026')
print('Created PT and EN reports plus complete validation appendix.')
