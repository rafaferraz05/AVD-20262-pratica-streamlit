# Revisão independente — entrega 3

Um agente separado, sem histórico da implementação, leu as 16 páginas de `AVD3.pdf`, os requisitos da atividade e os arquivos locais e remotos. Sua auditoria foi somente de leitura.

## Parecer

**Implementação local validada; entrega acadêmica final ainda incompleta por publicação e pendências do aluno.** Não foi identificado novo bloqueio técnico no código local auditado. Não há garantia de nota ou de ausência absoluta de defeitos.

## Evidências independentes

- 12 testes passaram em 61,541 segundos.
- D1 contém heatmap e um histograma para cada uma das cinco variáveis selecionáveis.
- D2 contém quatro métricas, três gráficos Altair no recorte padrão e os pictogramas do rascunho.
- 80 correlações foram comparadas com SciPy e 80 histogramas foram serializados nas oito temporadas, sem divergência ou erro.
- Métricas e rankings das oito temporadas foram recalculados independentemente, sem divergências.
- CSV tratado: 22.414 registros × 181 colunas; cópias tratadas idênticas, sem duplicatas exatas.
- EDA original preservada; notebook adaptado com 47 células de código executadas e validação com quatro, sem saídas de erro.
- Repositório identificado como público pelo conector GitHub. A implementação também confirmou leitura por Git sem credenciais.
- Nenhum padrão comum de segredo ou chave privada foi encontrado nos arquivos versionados. A varredura por padrões não é garantia absoluta.
- Declaração de IA intacta: SHA-256 `8777bcc2347b4964e1bb930bef37828da519b0d9977321bb4e34c817318f97cd`.

## Achados e providências

1. **Publicação pendente (bloqueio da entrega final):** a conta do Streamlit estava sem sessão. Deploy, URL real no README e teste em janela anônima não foram atestados. Não se deve apresentar o app como publicado antes dessas verificações.
2. **Commit/push:** na auditoria, as correções da parte 3 ainda não estavam no GitHub. O fechamento do implementador deve enviar os arquivos revisados; o histórico registra essa operação separadamente da auditoria.
3. **Declaração de IA:** academicamente incompleta, mas preservada conforme a instrução do aluno. O preenchimento do template da professora permanece a cargo do aluno.
4. **Rascunho do D1:** há um esquema digital retrospectivo, descrito honestamente na imagem. Ele não comprova um desenho feito antes da implementação. A professora poderá exigir a evidência original.
5. **Documentação herdada:** o texto sobre a etapa de publicação e os itens já cumpridos da pasta `entregas/` foram alinhados após o apontamento do revisor.

## Limites

O revisor não executou instalação limpa, não refez toda a EDA nesta auditoria e não realizou cliques reais nem teste do app publicado. AppTest não substitui o teste público da professora. A ausência de URL real impede declarar a entrega final concluída.
