# Relatório de Modelação Financeira – Millennium bcp / Banco Cotado Português

## 1. Sumário Executivo

Este relatório apresenta um estudo de caso de modelação financeira e análise bancária baseado em informação pública, utilizando o Millennium bcp como referência de estudo.

O objectivo é demonstrar um fluxo de trabalho analítico estruturado que combina dados financeiros históricos, análise de rácios bancários, pressupostos de forecast, análise de cenários, reporting em Power BI, consultas SQL analíticas e revisão de qualidade dos dados.

Este relatório destina-se exclusivamente a fins educativos, de portefólio e desenvolvimento profissional. Não constitui aconselhamento financeiro, aconselhamento de investimento, aconselhamento de avaliação, aconselhamento de crédito, aconselhamento legal ou recomendação de compra, venda ou detenção de qualquer instrumento financeiro.

## 2. Objectivo do Projecto

O projecto pretende demonstrar capacidade para:

- Estruturar dados financeiros públicos em datasets reutilizáveis
- Analisar métricas de rentabilidade, eficiência, qualidade dos activos, liquidez e capital
- Construir pressupostos de forecast por cenário
- Gerar demonstrações financeiras e rácios forecast
- Comparar cenários Base, Optimistic e Conservative
- Criar outputs em Power BI
- Construir uma camada analítica em SQL
- Aplicar controlos de qualidade dos dados e revisão humana

## 3. Âmbito da Análise

O projecto cobre os seguintes períodos:

- 2022A
- 2023A
- 2024A
- 2025A
- 2026E
- 2027E
- 2028E

Os períodos históricos são baseados em informação pública estruturada.

Os períodos forecast são estimativas educativas baseadas em cenários e estão marcados como requerendo revisão.

## 4. Fontes de Dados e Estrutura

O projecto utiliza datasets CSV estruturados com base em informação pública disponível.

Os principais datasets incluem:

- `data/financial_data.csv`
- `data/banking_ratios.csv`
- `data/source_mapping.csv`
- `data/extraction_tracker.csv`
- `data/forecast_assumptions.csv`
- `data/forecast_financials.csv`
- `data/forecast_ratios.csv`
- `data/scenario_analysis.csv`

A estrutura dos dados suporta rastreabilidade, revisão do estado de validação e reutilização analítica em Python, Power BI e SQL.

## 5. Análise Financeira Histórica

O dataset financeiro histórico inclui métricas seleccionadas das demonstrações financeiras bancárias, incluindo:

- Margem financeira
- Produto bancário / proveitos operacionais
- Custos operacionais
- Imparidades e provisões
- Resultado líquido
- Crédito a clientes
- Depósitos de clientes
- Activos totais
- Capital próprio

Estas métricas constituem a base do modelo forecast e da análise de cenários.

## 6. Análise de Rácios Bancários

O dataset de rácios bancários inclui indicadores de rentabilidade, eficiência, qualidade dos activos, liquidez e capital.

As principais categorias de rácios incluem:

- Rentabilidade: ROE, ROA, margem financeira
- Eficiência: cost-to-income ratio
- Qualidade dos activos: custo do risco, rácio NPE, cobertura NPE
- Liquidez: loan-to-deposit ratio, LCR, NSFR
- Capital: rácios CET1 e total capital
- Métricas por acção: EPS e valor contabilístico por acção
- Rácios de valorização, quando disponíveis

Para 2025A, são usados rácios reportados sempre que disponíveis. Isto evita sobrestimar a precisão quando cálculos simplificados podem não replicar totalmente metodologias de reporte de gestão, definições regulatórias ou metodologias com saldos médios.

## 7. Metodologia de Forecast

O forecast é construído a partir dos valores reais de 2025A e de pressupostos por cenário.

O forecast cobre:

- 2026E
- 2027E
- 2028E

Os três cenários são:

- Base
- Optimistic
- Conservative

Os pressupostos de forecast incluem:

- Crescimento da margem financeira
- Crescimento de outros proveitos operacionais
- Crescimento dos custos operacionais
- Custo do risco
- Crescimento do crédito a clientes
- Crescimento dos depósitos de clientes
- Pressuposto de rácio CET1

Os outputs forecast são gerados através de scripts Python e estão marcados como `To Review`.

## 8. Tratamento do Ano Base

O ano 2025A é tratado como o ano base do forecast.

Os valores históricos das demonstrações financeiras de 2025A são retirados de `data/financial_data.csv`.

Os rácios bancários históricos de 2025A são retirados de `data/banking_ratios.csv`.

Os rácios reportados de 2025A são usados sempre que disponíveis, uma vez que os rácios bancários reportados podem depender de definições específicas, saldos médios, bases regulatórias ou abordagens de reporte de gestão.

## 9. Forecast de Proveitos

O modelo faz forecast de:

- Margem financeira
- Outros proveitos operacionais
- Proveitos operacionais / produto bancário

As comissões não são forecast directamente porque o valor está actualmente marcado como pendente no dataset.

Em alternativa, o modelo utiliza:

`Other operating income = Operating income - Net interest income`

Esta abordagem evita sobrestimar a precisão quando a linha subjacente ainda não está totalmente validada.

## 10. Forecast de Custos e Risco

Os custos operacionais são projectados com base em pressupostos de crescimento por cenário.

O modelo deriva:

`Pre-provision operating profit = Operating income - Operating costs`

As imparidades e provisões são estimadas utilizando um pressuposto de custo do risco aplicado ao crédito a clientes:

`Impairments and provisions = Customer loans × Cost of risk / 10,000`

O custo do risco é expresso em basis points.

## 11. Forecast do Balanço

O modelo faz forecast de:

- Crédito a clientes
- Depósitos de clientes
- Activos totais
- Capital próprio

O crédito a clientes e os depósitos de clientes crescem com base em pressupostos por cenário.

Os activos totais são estimados através de uma proxy simplificada baseada na média entre o crescimento do crédito a clientes e o crescimento dos depósitos de clientes.

O capital próprio é estimado através de uma ponte simplificada de resultados retidos:

`Equity = Prior year equity + 50% of estimated net income`

Esta é uma simplificação educativa e não modela integralmente dividendos, recompras de acções, outro rendimento integral, deduções regulatórias ou activos ponderados pelo risco.

## 12. Rácios Forecast

Os rácios forecast incluem:

- ROE
- ROA
- Cost-to-income ratio
- Loan-to-deposit ratio
- Custo do risco
- Pressuposto de rácio CET1

Para 2025A, são utilizados os rácios reportados presentes em `banking_ratios.csv`.

Para 2026E–2028E, os rácios são calculados a partir dos outputs forecast ou retirados directamente dos pressupostos de forecast.

## 13. Análise de Cenários

A análise de cenários compara os casos Base, Optimistic e Conservative em várias métricas financeiras e rácios-chave.

Para cada métrica, a análise inclui:

- Valor do cenário
- Valor do cenário Base
- Variação absoluta face ao Base
- Variação percentual face ao Base
- Lógica do cenário
- Principal driver
- Nível de risco
- Interpretação
- Estado de validação

Isto suporta uma visão estruturada de como os pressupostos afectam rentabilidade, eficiência, qualidade dos activos, liquidez e indicadores de capital.

## 14. Dashboard Power BI

O dashboard Power BI fornece uma camada visual para o projecto.

As páginas do dashboard incluem:

- Executive Overview
- Liquidity & Funding
- Asset Quality
- Profitability
- Efficiency
- Capital
- Data Quality

O dashboard foi concebido como um output de business intelligence de portefólio e não deve ser interpretado como uma ferramenta de recomendação de investimento.

## 15. Camada Analítica SQL

A camada SQL demonstra como os datasets do projecto podem ser consultados num fluxo de trabalho analítico.

Os ficheiros SQL incluem:

- `sql/create_tables.sql`
- `sql/banking_ratio_queries.sql`
- `sql/data_quality_queries.sql`
- `sql/forecast_queries.sql`
- `sql/README.md`

A camada SQL suporta:

- Revisão de rácios históricos
- Revisão de qualidade dos dados
- Revisão de pressupostos de forecast
- Revisão dos outputs forecast
- Comparação de cenários
- Fluxo de revisão humana

## 16. Qualidade dos Dados e Revisão Humana

O projecto inclui um fluxo de qualidade dos dados que cobre:

- Estado de validação
- Mapeamento de fontes
- Tracking de extracção
- Valores em falta
- Classificação Reviewed vs To Review
- Revisão de outputs forecast
- Checklist final de publicação

A validação pode ser executada com:

`python data/validation_checks.py`

Os outputs forecast permanecem marcados como `To Review` até serem revistos manualmente.

## 17. Workflow Assistido por IA e Revisto por Humanos

Este projecto segue um workflow assistido por IA e revisto por humanos.

Ferramentas de IA podem apoiar a estruturação da documentação, enquadramento analítico, geração de código, verificações de consistência e revisão da qualidade dos dados.

No entanto, todos os valores financeiros, pressupostos, interpretações e outputs finais requerem revisão humana pelo autor antes da publicação.

## 18. Principais Limitações

Este projecto tem várias limitações:

- Utiliza apenas informação pública.
- É um modelo educativo simplificado.
- Não replica metodologias internas de forecast bancário.
- Não modela integralmente dinâmicas de capital regulatório.
- Não modela detalhadamente activos ponderados pelo risco.
- Não modela integralmente dividendos, recompras de acções ou OCI.
- Não fornece aconselhamento de avaliação.
- Não fornece recomendações de investimento.
- Não deve ser interpretado como forecast oficial.

## 19. Relevância Profissional

Este estudo de caso demonstra competências práticas relevantes para:

- Banking analytics
- Qualidade de dados financeiros
- Modelação financeira
- Reporting em Power BI
- Workflows analíticos em SQL
- Análise de cenários
- Interpretação financeira com consciência de risco
- Workflows financeiros assistidos por IA de forma responsável

O projecto foi desenhado para ser claro, adequado a recrutadores e alinhado com funções em financial data quality, banking analytics, financial research, risk operations, business intelligence e finance transformation.

## 20. Disclaimer

Este relatório destina-se exclusivamente a fins educativos, analíticos e de portefólio.

Não constitui aconselhamento financeiro, aconselhamento de investimento, aconselhamento de avaliação, aconselhamento de crédito, aconselhamento legal ou recomendação de compra, venda ou detenção de qualquer instrumento financeiro.

Todos os valores forecast são estimativas baseadas em cenários e devem ser interpretados como outputs de modelação analítica, não como projecções oficiais.

O autor não está afiliado ao Millennium bcp para efeitos deste projecto. O projecto utiliza apenas informação pública.
