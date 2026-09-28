# Fundamento e conclusões do estudo

## Pergunta e objetivo

Como evoluíram a rendibilidade, a eficiência, a qualidade do crédito, a liquidez e o capital do Millennium bcp, e como variam resultados ilustrativos quando alteramos as hipóteses operacionais?

O objetivo é demonstrar análise financeira e engenharia de dados reproduzível: documentos públicos oficiais → observações com fonte e página → CSV → cálculos Python → consultas SQL → Power BI → relatórios e anexo. O âmbito cobre 2022–2025 e a comparação 1S2025/1S2026.

## Conclusões sustentadas pelos dados

- O resultado líquido do Grupo no 1S2026 foi 565,8 milhões de euros. O emitente reporta +12,7%; a divisão dos montantes arredondados publicados resulta em +12,6%. Preservamos e identificamos ambas as medidas.
- O rácio NPE diminuiu de 2,7% para 2,2% e a cobertura subiu de 84,5% para 97,2%. O custo do risco, contudo, aumentou de 30 para 32 pontos base: a melhoria não abrange todos os indicadores de risco.
- A eficiência manteve-se próxima de 37% (37,0% → 36,9%). O CET1 fully implemented diminuiu de 16,2% para 15,1%; o valor de junho de 2026 é estimado e inclui 10% dos resultados intercalares não auditados.

Fonte: [comunicado oficial 1S2026, páginas PDF 1–3](https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/ApresentacaoResultados/2026/20260729_Resultados_Millennium_BCP_1S26.pdf). Estes resultados permitem descrever a evolução; não estabelecem o valor justo da ação nem uma decisão de investimento.

## O que os cenários permitem concluir

| Resultado líquido estimado, milhões de euros | Conservador | Base | Otimista |
|---|---:|---:|---:|
| 2026E | 1.049,9 | 1.115,3 | 1.162,1 |
| 2027E | 922,8 | 1.111,1 | 1.217,4 |
| 2028E | 875,2 | 1.125,2 | 1.257,9 |

Fonte: `data/forecast_financials.csv`. Em 2026 somamos o 1S realizado ao 2S estimado; nos saldos de balanço projetamos junho para dezembro, sem somar dois saldos. A divergência entre cenários demonstra sensibilidade conjunta a receitas, custos, crédito e custo do risco. Não é um intervalo de confiança, nem uma previsão probabilística. Não isolámos estatisticamente a contribuição de cada driver.

## Como verificar o trabalho

1. Selecionar uma observação em `data/source_mapping.csv` e confrontar valor, unidade, período e página com a fonte. Há 176 valores reportados e seis totais recalculados.
2. Executar os comandos de `RUN_PROJECT.md`. A validação verifica cobertura, duplicados, seis somas, 162 células de previsão, 126 comparações e 36 instruções SQL. Não volta a ler automaticamente cada PDF: a rastreabilidade documental é uma etapa distinta.
3. Conferir as 72 hipóteses em `data/forecast_assumptions.csv` e as fórmulas em `docs/forecast_methodology.md`.
4. Abrir a v5 e comparar os visuais com os CSV. A verificação local registou 909 linhas correspondentes após gravação e reabertura; as dez páginas exportadas foram revistas.

## Limitações que condicionam a interpretação

- A série anual preserva versões de divulgação documentadas; não é uma série integralmente reexpressa numa única base. O 1S2025 e o 1S2026 vêm do mesmo comunicado, com comparativos reexpressos.
- O modelo usa um fator agregado de conversão do lucro calibrado no 1S2026. Impostos, minoritários e outras imparidades não têm projeções autónomas.
- ROE/ROA projetados usam saldos finais e não são diretamente comparáveis aos rácios históricos do emitente. CET1 é uma hipótese direta; não modelámos ativos ponderados pelo risco.
- As hipóteses são sensibilidades escolhidas para o estudo, sem validação preditiva fora da amostra. Avaliação de mercado e comparação com concorrentes estão fora do âmbito.

A conclusão técnica é que os dados e cálculos do âmbito documentado foram reconciliados. A validação assistida por IA não equivale a auditoria independente, certificação externa ou garantia de desempenho futuro.
