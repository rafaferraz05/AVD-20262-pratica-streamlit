# Planejamento do Dashboard 2: indicadores de futebol

## Contexto

Projeto da disciplina Análise e Visualização de Dados, baseado na EDA de jogadores das cinco principais ligas europeias. Este rascunho planeja o Dashboard 2, de KPIs. O Dashboard 1 continua destinado à correlação e à distribuição das variáveis quantitativas.

## Entrada

Rascunho original do aluno: [rascunho-dashboard2.png](../entregas/rascunho-dashboard2.png).

Fonte dos dados tratados: `data/clean/futebol.csv`.

Decisões confirmadas pelo aluno:

- Aba lateral de filtros, conforme o desenho.
- Um desenho de gol preenchido conforme o percentual de chutes no alvo sobre o total de chutes.
- Chuteiras mais preenchidas quanto maior a quantidade de gols.
- Cartões amarelos e vermelhos mais preenchidos quanto maior a quantidade de cartões de cada tipo.
- Os rankings devem mostrar os cinco jogadores com mais gols e os cinco com mais cartões, dentro dos filtros escolhidos. Cada figura representa um jogador, com nome e quantidade visíveis.

Organização proposta: um top 5 de gols, um top 5 de cartões amarelos e um top 5 de cartões vermelhos. Os jogadores podem ser diferentes em cada lista.

Regras dos indicadores:

| Indicador | Colunas | Regra |
| --- | --- | --- |
| Chutes no alvo | `Standard_SoT`, `Standard_Sh` | `100 * soma(Standard_SoT) / soma(Standard_Sh)` no recorte selecionado. Usar a razão dos totais, sem fazer média simples dos percentuais de cada linha. |
| Gols | `Performance_Gls` | Somar por jogador no recorte selecionado e mostrar os cinco maiores totais em chuteiras. |
| Cartões amarelos | `Performance_CrdY` | Somar por jogador no recorte selecionado e mostrar os cinco maiores totais em cartões amarelos. |
| Cartões vermelhos | `Performance_CrdR` | Somar por jogador no recorte selecionado e mostrar os cinco maiores totais em cartões vermelhos. |

Se não houver chutes, mostrar “Sem chutes” para o percentual. Dado ausente não deve ser apresentado automaticamente como zero.

Escala proposta para as quantidades: o líder de cada ranking tem o desenho completamente preenchido. Os demais usam `quantidade do jogador / quantidade do líder`. Exemplo: se o líder tem 20 gols, um jogador com 10 gols terá a chuteira preenchida pela metade. Informar na tela que o preenchimento é relativo ao líder do recorte; o número ao lado continua sendo a quantidade real. Cada tipo de cartão possui sua própria referência.

Se não houver valores positivos, mostrar uma mensagem de ausência de gols ou cartões registrados no recorte, sem dividir por zero. Mostrar menos de cinco jogadores quando não houver cinco com valor positivo e conhecido. Em caso de empate, usar uma ordem estável por nome, informando que jogadores empatados podem ficar fora do limite de cinco.

Somar os registros do mesmo jogador antes de ordenar, considerando que ele pode ter atuado em mais de um clube. Usar nome e ano de nascimento, quando disponíveis, para reduzir a mistura entre homônimos. A seleção de temporada precisa ficar explícita: somar várias temporadas produz um ranking acumulado, não o ranking de uma temporada.

Decisão ainda a definir antes da implementação dos gráficos:

- Quais filtros usar: liga, temporada, clube e/ou jogador.

## Restrições

- Seguir o rascunho e usar Streamlit.
- Nesta etapa, planejar a estrutura com espaços reservados para os indicadores.
- Exibir o valor numérico junto de cada figura quando os gráficos forem implementados.
- Manter a mesma escala entre itens comparáveis e informar a referência usada para o preenchimento.
- Preservar os dados tratados; a visualização não deve alterar o CSV.
- Carregar os dados pelo módulo `src/data_loader.py` quando o aplicativo for adaptado.

## Formato de saída

Na etapa de criação do esqueleto, produzir a estrutura da tela com filtros e espaços reservados para gol, top 5 de artilheiros, top 5 de cartões amarelos e top 5 de cartões vermelhos. Documentar os cálculos pendentes com comentários `TODO`. A implementação dos gráficos será feita na etapa de KPIs do plano da disciplina.
