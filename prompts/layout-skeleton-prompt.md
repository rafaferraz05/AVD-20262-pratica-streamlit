# Template: rascunho de layout → esqueleto do app

Preencha cada bloco e envie à ferramenta de IA.

## Contexto

Projeto da disciplina Análise e Visualização de Dados. Adaptar o esqueleto de Streamlit ao dataset de futebol analisado na Aula 11. Carregar `data/clean/futebol.csv`, com as variáveis `age_`, `Playing Time_Min`, `Performance_Gls`, `Expected_xG` e `Total_Cmp%`.

## Entrada

Referência do Dashboard 1: `entregas/prof_rascunho_dashboard1.png`, exemplo da professora, com sidebar, correlação à esquerda e distribuição à direita. Ainda não foi fornecido um rascunho próprio do aluno para essa primeira tela.

Rascunho próprio do Dashboard 2: `prompts/rascunho_dashboard2.png`. Criar uma segunda tela com um gol, cinco chuteiras para artilheiros e duas fileiras de cinco cartões (amarelos e vermelhos). As regras planejadas estão em `prompts/dashboard2-layout-prompt.md`.

<!-- Opcional, se a ferramenta de IA não aceitar imagem ou interpretar mal o rascunho: descreva o layout em poucas linhas (ex.: sidebar à esquerda com 2 filtros; topo com 3 métricas; abaixo, 2 gráficos lado a lado). -->

## Restrições

Usar Streamlit e carregar os dados via `src/data_loader.py`. Criar filtros funcionais por temporada, liga e clube. No Dashboard 1, preservar o seletor de variáveis e os filtros de intervalo, com áreas reservadas para os gráficos. No Dashboard 2, representar o desenho com contornos vetoriais e valores em branco. Não inventar nomes, rankings ou percentuais. Deixar os cálculos e os gráficos como `TODO` para a próxima etapa, conforme os slides 18 e 21.

## Formato de saída

Um `app.py` executável com navegação entre os dois dashboards. O carregamento fica em `src/data_loader.py` e os contornos SVG em `src/pictogramas.py`. Explicar o que já funciona e o que será implementado nas próximas aulas.
