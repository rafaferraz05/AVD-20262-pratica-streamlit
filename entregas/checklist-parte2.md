# Conferência da parte 2

Referência: slidesAVD2.pdf (18 páginas), especialmente slides 14, 15, 16 e 17, e a seção Aula 22 de `ROTEIRO.md`.

## Implementação e arquivos

- [x] Dashboard 1 com mapa de correlação de Spearman e histograma recalculados pelos filtros.
- [x] Testes com 0, 1 e 2 ou mais variáveis, classes, filtros combinados, recorte vazio e dados constantes.
- [x] Carregamento com `@st.cache_data` e caminhos relativos à raiz do projeto.
- [x] Identidade visual em `.streamlit/config.toml`: verde do campo, fundos neutros e fonte sem serifa; amarelo e vermelho identificam os cartões.
- [x] Dois dashboards separados por `st.tabs`.
- [x] Quatro métricas definidas, calculadas e justificadas com variável, tipo, significado, público e decisão apoiada.
- [x] Filtros definidos: temporada, ligas e clubes; seleção de jogadores no gráfico de barras.
- [x] Foto original do rascunho do aluno em `entregas/rascunho-dashboard2.png`.
- [x] Gráfico Altair de barras com dados agrupados por jogador e seleção vinculada aos indicadores.
- [x] Notebook de validação executado, com quatro células de código, comparação dos cálculos e gráfico prévio.
- [x] Notebooks organizados nos nomes do roteiro, mantendo as cópias históricas e a análise original sem alteração de conteúdo.
- [x] `eda-com-downloads.ipynb` executado integralmente: 47 células de código, sem erros, incluindo as exportações de bruto e tratado.

## Evidências de teste

Comando: `python -m unittest discover -s tests -v`.

Os testes verificam o recálculo da interface e, em dados construídos para checagem, a razão dos totais, ausência de denominador, contagens desconhecidas, transferências, homônimos e desempate.

Conferência no navegador em 03/11/2026, temporada 2024/25, todas as ligas e clubes:

- Pontaria: 33,4% (14.420 chutes no alvo / 43.176 chutes).
- Totais do recorte: 4.805 gols, 7.134 amarelos e 328 vermelhos.
- Clique na barra de Kylian Mbappé: indicadores passam para 49,3%, 31 gols, 3 amarelos e 1 vermelho.
- Dois cliques na barra limpam a seleção e restauram os indicadores do recorte completo.

## Pendências que não devem ser confundidas com implementação concluída

- A declaração `prompts/declaracao-uso-ia.md` foi preservada, sem preenchimento nesta etapa, por pedido explícito do aluno. O slide 17 pede sua atualização: o aluno deve cuidar dessa parte antes da entrega acadêmica.
- Ainda não foi fornecido um rascunho próprio do Dashboard 1. `entregas/prof_rascunho_dashboard1.png` é o exemplo da professora e não deve ser apresentado como desenho do aluno.
- A parte 3 e o deploy não foram realizados nesta etapa.

Os commits desta parte são separados entre Dashboard 1, Dashboard 2 e documentação/validação. O histórico da parte 1 é preservado.

O parecer independente e suas limitações estão em [revisao-parte2.md](revisao-parte2.md).
