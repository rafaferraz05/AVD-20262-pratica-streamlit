# Revisão após a publicação — 03/11/2026

Referências: `AVD3.pdf`, com 16 páginas, e os requisitos finais da atividade enviados pelo aluno.

Aplicação: https://avd-20262-pratica-app-hhtks5cg2embjiatbgns4y.streamlit.app/

Repositório: https://github.com/rafaferraz05/AVD-20262-pratica-streamlit

## Parecer

A implementação examinada atende aos requisitos funcionais: duas abas, seletor de variáveis, intervalos, mapa de calor, histogramas por variável, quatro indicadores e três gráficos adicionais no Dashboard 2. O app publicado abriu sem solicitar autenticação. Não foi encontrada falha funcional que exigisse alterar o código nesta revisão.

A entrega acadêmica ainda depende do aluno: declaração de IA no template da professora, confirmação do rascunho anterior do Dashboard 1 e conferência final em janela anônima. A documentação foi atualizada para substituir o aviso antigo de publicação pendente pela URL real.

## Testes na aplicação publicada pelo agente principal

Navegador de revisão com sessão separada, sem utilizar o login do Edge do aluno. Abertura literal de janela anônima do Edge não foi realizada.

| Verificação | Resultado observado |
| --- | --- |
| Acesso pelo endereço público | App abriu e carregou os dados sem login. |
| Dashboard 1 padrão | Mapa de Spearman e cinco histogramas, um por variável selecionada. |
| Dashboard 2 padrão | Quatro indicadores, três rankings em barras e pictogramas. |
| Temporada | Troca de 2024/25 para 2023/24 atualizou os totais; gols passaram de 4.805 para 4.906. |
| Ligas | Recorte apenas ENG-Premier League em 2023/24 mostrou 580 registros. Sem liga selecionada, exibiu aviso de recorte vazio. |
| Clubes | Arsenal em 2023/24 mostrou 25 registros. |
| Intervalo | Idade restrita a 31 anos reduziu o D1 de 25 para 3 registros. |
| Variáveis | Remover Gols retirou seu controle de intervalo e histograma. |
| Distinção de posições | Ativar o controle acrescentou Atacante/Demais aos histogramas. |
| Seleção no gráfico | Clicar na barra de Mbappé atualizou os indicadores e figuras; dois cliques restabeleceram o total. |
| Métrica do ranking | Trocar para cartões vermelhos mudou o gráfico principal para Mario Martín e os demais líderes disciplinares. Cartões amarelos apresentou Facundo Medina como líder, com 15. |

Base padrão de 2024/25: 2.852 registros, 4.805 gols, 7.134 amarelos e 328 vermelhos. Pontaria: 14.420 chutes no alvo / 43.176 chutes = 33,4%. Selecionando Mbappé: 75/152 = 49,3%, 31 gols, 3 amarelos e 1 vermelho.

Os testes de navegador cobrem exemplos de cada tipo de controle; não esgotam todas as combinações possíveis. A suíte local complementa os casos de vazio, constantes, ausências e independência dos filtros do D1 em relação ao D2.

## Auditoria por agente independente

Foi criado um agente separado, sem o histórico da implementação, com instrução de auditar somente por leitura e procurar falhas contra o enunciado. Ele leu as 16 páginas do PDF e inspecionou os arquivos e os dados.

- 12 testes automatizados passaram em 54,657 segundos.
- GitHub confirmou repositório público e branch `main` no commit `a5a506ef35c2f6c5cec57d608a3194534fb7efe3`, anterior a esta atualização documental.
- Os hashes dos arquivos locais e remotos coincidiram para aplicação, dependências, configuração, dois CSVs tratados e dois rascunhos.
- A árvore pública contém notebooks, entregas e prompts; não contém `secrets.toml` nem CSV bruto.
- Dados tratados: 22.414 registros × 181 colunas. Não foram encontradas duplicatas na chave temporada/jogador/ano/clube, linhas agregadas “squads” ou incoerências entre chutes e chutes no alvo nas verificações realizadas.
- Não encontrou falha funcional que justificasse alteração no código.

Limite da independência: o revisor não conseguiu abrir o app público por seus próprios meios. Os cliques no serviço publicado são evidências do agente principal, descritas acima. O parecer independente sobre código e dados não é apresentado como uma segunda validação de navegador.

## Pendências acadêmicas e fechamento

1. **Declaração de IA:** preservada conforme instrução explícita do aluno. Deve ser preenchida pelo aluno no template indicado pela professora antes de entregar.
2. **Rascunho D1:** o arquivo existe, mas é um esquema digital retrospectivo, identificado dessa forma. Não comprova planejamento antes de programar. Caso haja rascunho original, o aluno deve fornecê-lo; se não houver, deve confirmar com a professora se aceita o esquema atual.
3. **Janela anônima:** aluno deve repetir a abertura e os testes básicos no próprio navegador, conforme a redação do enunciado. O teste sem login acima já demonstra acesso público, mas não substitui a confirmação literal dessa etapa.
4. **Submissão:** o aluno deve enviar o link do repositório público na atividade e a declaração exigida. Não foi feita submissão ao Classroom nesta revisão.

O achado do revisor sobre a ausência de URL no README foi corrigido nesta atualização. A versão exata do Python usada pelo serviço não foi inspecionada, nem foi refeita uma instalação limpa ou toda a EDA. Nenhuma auditoria garante nota ou ausência absoluta de defeitos.
