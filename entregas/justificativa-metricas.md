# Justificativa das métricas — Dashboard 2

## Público e recorte

O painel se destina a torcedores e pessoas que fazem uma análise inicial de jogadores das cinco principais ligas europeias. O objetivo é identificar produção de gols, frequência de chutes no alvo e volume de cartões, sem exigir a leitura das 181 colunas do dataset tratado.

Os filtros são temporada, ligas e clubes. Uma temporada por vez evita somar carreiras de durações diferentes. Os dados vêm de `data/clean/futebol.csv`. Cada linha representa um jogador em um clube e temporada; transferências podem gerar mais de uma linha para o mesmo jogador.

## Métrica 1: percentual de chutes no alvo

- **Variáveis:** `Standard_SoT` (chutes no alvo) e `Standard_Sh` (total de chutes).
- **Tipo:** proporção apresentada em percentual.
- **O que mede:** `100 × soma(Standard_SoT) / soma(Standard_Sh)` no recorte. As duas somas usam somente as mesmas linhas com ambos os valores conhecidos e coerentes (`0 ≤ SoT ≤ Sh`). Não é a média simples dos percentuais dos jogadores.
- **Por que foi escolhida:** resume a frequência com que as finalizações encontram o alvo e dá significado ao preenchimento do desenho do gol.
- **Público-alvo:** torcedores e analistas interessados em finalizações.
- **Qual decisão pode ser apoiada por essa métrica?** Identificar recortes ou jogadores que merecem uma investigação mais detalhada da pontaria.
- **O que comunica ao público-alvo:** “de cada 100 chutes registrados, aproximadamente X foram no alvo”. Não informa a porcentagem de gols nem a qualidade das chances.
- **Limites:** sem chutes válidos, mostrar “—” e explicar a ausência de denominador; não apresentar 0% como substituto. A quantidade de chutes e as linhas utilizadas ficam visíveis para contextualizar a proporção.

## Métrica 2: total de gols

- **Variável:** `Performance_Gls`.
- **Tipo:** contagem.
- **O que mede:** soma dos gols conhecidos dos jogadores no recorte escolhido.
- **Por que foi escolhida:** é uma medida de produção ofensiva de interpretação direta e permite construir o top 5 de artilheiros proposto no rascunho.
- **Público-alvo:** torcedores e pessoas interessadas em identificar artilheiros.
- **Qual decisão pode ser apoiada por essa métrica?** Selecionar jogadores para uma análise ofensiva posterior, considerando também minutos, posição e xG.
- **O que comunica ao público-alvo:** o volume de gols registrado no recorte; no ranking, quais jogadores marcaram mais.
- **Limites:** maior total não significa automaticamente melhor jogador. Jogadores com mais minutos tiveram mais oportunidades. Não se trata de gols por 90 minutos nem de uma avaliação causal de desempenho.

## Métrica 3: total de cartões amarelos

- **Variável:** `Performance_CrdY`.
- **Tipo:** contagem.
- **O que mede:** soma dos cartões amarelos conhecidos no recorte.
- **Por que foi escolhida:** resume o volume de advertências e permite destacar os cinco jogadores com mais amarelos.
- **Público-alvo:** torcedores e pessoas que acompanham a disciplina dos jogadores.
- **Qual decisão pode ser apoiada por essa métrica?** Identificar jogadores cujo histórico de advertências merece acompanhamento, junto com contexto de posição e tempo em campo.
- **O que comunica ao público-alvo:** quantas advertências foram registradas e quem concentra os maiores totais.
- **Limites:** o total não é uma taxa por partida e não determina sozinho agressividade, gravidade das faltas ou suspensão. As regras de suspensão não são inferidas deste indicador.

## Métrica 4: total de cartões vermelhos

- **Variável:** `Performance_CrdR`.
- **Tipo:** contagem.
- **O que mede:** soma dos valores conhecidos de cartões vermelhos na coluna fornecida pela fonte.
- **Por que foi escolhida:** diferencia os vermelhos dos amarelos e permite um ranking próprio, sem misturar os dois tipos de cartão.
- **Público-alvo:** torcedores e pessoas que acompanham ocorrências disciplinares.
- **Qual decisão pode ser apoiada por essa métrica?** Escolher jogadores e recortes para investigar as ocorrências de cartões vermelhos.
- **O que comunica ao público-alvo:** o volume registrado de vermelhos e os jogadores com mais ocorrências.
- **Limites:** não somamos `Performance_2CrdY` a `Performance_CrdR`, evitando inventar uma definição de “todas as expulsões”. O painel mostra o indicador da fonte e não reconstrói o motivo das ocorrências.

## Rankings, figuras e interatividade

- Quatro cartões `st.metric` resumem as quatro métricas. Os quinze lugares nos rankings são visualizações dessas contagens, não quinze KPIs diferentes.
- Antes do top 5, somamos os registros de cada jogador usando nome e ano de nascimento; isso reúne transferências e reduz a mistura de homônimos. Sem identificador único na fonte, homônimos com o mesmo ano ainda são uma limitação.
- Cada ranking é independente. Só entram valores positivos e conhecidos; podem aparecer menos de cinco jogadores. Empates são ordenados por nome e ano de nascimento, mantendo o limite de cinco.
- O gol preenche de 0 a 100% conforme a pontaria. A altura preenchida da chuteira e de cada tipo de cartão é proporcional ao líder do respectivo ranking no recorte exibido. Essa escala é relativa, e a quantidade real aparece junto da figura.
- Um gráfico Altair de barras agrupa a métrica escolhida por jogador e mostra o top 5. Selecionar barras filtra os indicadores e as demais figuras; dois cliques no gráfico limpam a seleção. Os filtros da lateral continuam sendo aplicados antes dessa seleção.
- Valores ausentes não são convertidos automaticamente em zero. Somas totalmente desconhecidas são mostradas como “—”; somas parciais são identificadas como baseadas nos valores conhecidos. As proporções informam sua base válida.

## Validação antes da aplicação

Os cálculos e um gráfico prévio podem ser reproduzidos em `notebooks/validacao-metricas.ipynb`. Os testes em `tests/` cobrem razão dos totais, denominador zero, ausências, transferências, homônimos e empates, além dos cenários de widgets exigidos no slide 16.
