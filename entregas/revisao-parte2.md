# Revisão independente da parte 2 — 03/11/2026

## Método e resultado

Um agente revisor separado, sem acesso ao histórico da conversa de implementação, leu as 18 páginas de `slidesAVD2.pdf`, os critérios da Aula 22 em `ROTEIRO.md` e o projeto. A revisão foi somente de leitura; o revisor não alterou arquivos nem criou commits. Este documento resume seu parecer, incluindo as limitações que ele registrou.

**Parecer: nenhum bloqueio técnico identificado para a parte 2 nos arquivos auditados.** Isso não garante nota, autoria acadêmica ou ausência absoluta de defeitos. A entrega acadêmica ainda tem as pendências do aluno descritas abaixo.

## Evidências verificadas independentemente

- 12 testes automatizados passaram, incluindo casos de 0, 1 e 2 ou mais variáveis, filtros combinados, constantes, recorte vazio, atualização dos indicadores e as regras das métricas.
- A base tratada possui 22.414 registros e 181 colunas, sem duplicatas exatas ou pela chave do registro. Os arquivos `futebol.csv` e `dataset.csv` correspondem à mesma base tratada.
- O revisor reproduziu em memória o tratamento a partir do bruto de 22.929 registros e 178 colunas; todas as colunas corresponderam ao CSV tratado com tolerância numérica de `1e-12`.
- As correlações e seus pares válidos foram confrontados com `scipy.stats.spearmanr` em 24 recortes. Foram serializadas 240 especificações de histogramas, sem erro.
- As quatro métricas estão dentro da faixa de 3 a 5 dos slides. Fórmulas, variáveis, público, decisões apoiadas e limites estão documentados. Transferências e homônimos são considerados nos rankings.
- O notebook de validação foi reexecutado em memória pelo revisor: quatro células de código, sem erro. O notebook adaptado foi novamente conferido após execução integral: 47 células de código, incluindo as exportações, sem outputs de erro.
- `eda.ipynb` é uma cópia byte a byte da análise original local do aluno. O notebook da professora foi preservado.
- A foto do Dashboard 2 em `entregas/` é idêntica ao arquivo anteriormente localizado em `prompts/`. Os links Markdown locais foram conferidos.
- A declaração de uso de IA permaneceu com o SHA-256 `8777bcc2347b4964e1bb930bef37828da519b0d9977321bb4e34c817318f97cd`.

O revisor identificou uma descrição antiga na seção de exportação que ainda mencionava preservar o exemplo Heart Disease. O texto foi corrigido para explicar os dois CSVs de futebol tratado, e o notebook adaptado foi executado novamente antes do fechamento da revisão.

## Pendências acadêmicas do aluno

1. **Declaração de IA da parte 2:** o slide 17 pede atualização, mas o usuário solicitou explicitamente que ela não fosse preenchida. O arquivo foi preservado. Identificação, avaliação das sugestões e registro dessa etapa devem ser tratados pelo aluno.
2. **Rascunho próprio do Dashboard 1:** pendência herdada da Aula 21. O exemplo da professora não deve ser apresentado como desenho do aluno. O rascunho fornecido pelo aluno corresponde ao Dashboard 2.

## Limitações e finalização

- AppTest não simula cliques reais de seleção em gráficos Altair. O revisor conferiu a especificação; o implementador verificou separadamente no navegador o clique em uma barra, a atualização dos indicadores e a limpeza por duplo clique.
- Não foi feita instalação em ambiente limpo pelo revisor, nem auditoria própria do navegador ou verificação remota do GitHub. A conexão com o repositório e o envio dos commits são conferidos no fechamento pelo implementador.
- A organização dos commits separa o Dashboard 1, o Dashboard 2 e a documentação/validação. O histórico anterior foi preservado.
- A parte 3 e a publicação no Streamlit Community Cloud não fazem parte desta revisão.

Comandos e verificações usados pelo revisor: `git status`, `git diff`, `git log`, `git branch -vv`, `git ls-files data/clean`, hashes dos arquivos, `python -m unittest discover -s tests -v`, execução em memória com `nbclient` e comparações independentes em pandas/SciPy.
