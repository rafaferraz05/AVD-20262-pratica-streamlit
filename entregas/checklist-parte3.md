# Entrega 3 — conferência final

Referências: `AVD3.pdf` (16 páginas) e a atividade “Prática - Streamlit” enviada pelo aluno.

## Aplicação e repositório

- [x] `app.py` na raiz, com dois dashboards separados por abas.
- [x] Repositório acessível para leitura sem credenciais; a revisão também confirmou sua visibilidade pública.
- [x] Painel lateral com seletor de variáveis e filtros de intervalo.
- [x] Dashboard 1 com mapa de calor de Spearman e um histograma para cada variável quantitativa selecionada.
- [x] Dashboard 2 com quatro métricas e três visuais explícitos de barras no recorte padrão, além do gol, chuteiras e cartões.
- [x] Filtros, vazios, constantes, ausências e somas por jogador tratados nos testes.
- [x] Dados tratados versionados e carregados por caminho relativo; nenhum segredo é necessário para executar o app.
- [x] Identidade visual versionada em `.streamlit/config.toml`.
- [x] Notebooks original, adaptado e de validação disponíveis no repositório.
- [x] Dois arquivos de rascunho em `entregas/`, com procedência indicada abaixo.

## Procedência dos rascunhos

`rascunho-dashboard2.png` é a foto fornecida pelo aluno. `rascunho-dashboard1.png` é um esquema digital do layout, elaborado nesta etapa final; não é apresentado como foto ou evidência de desenho feito antes da implementação. Se a professora exigir especificamente essa evidência anterior, o aluno deverá fornecer seu material original.

## Publicação — ainda pendente de autenticação

- [ ] Login do aluno no Streamlit Community Cloud e autorização do repositório.
- [ ] Criar app público do repositório `rafaferraz05/AVD-20262-pratica-streamlit`, branch `main`, arquivo `app.py`.
- [ ] Escolher Python compatível, preferencialmente 3.13, conforme as opções disponíveis no serviço.
- [ ] Aguardar o deploy e copiar a URL efetivamente fornecida pelo serviço.
- [ ] Inserir essa URL real no README; não usar endereço presumido como se já estivesse publicado.
- [ ] Abrir o app sem sessão/autenticação e testar widgets e ambas as abas.
- [ ] Conferir que a URL do README aponta para a aplicação publicada.

O acesso à conta, o aceite dos termos e eventuais permissões do GitHub devem ser concluídos pelo aluno. A página foi encontrada sem sessão autenticada durante a preparação desta entrega.

## Declaração de uso de IA

O arquivo foi preservado por instrução do aluno. A atividade exige a declaração no template indicado pela professora: o aluno deve preencher e conferir essa parte antes da submissão acadêmica.

## Como reproduzir os testes locais

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m streamlit run app.py
```

O teste local não substitui o teste do app publicado solicitado pela professora.

Validação local em 03/11/2026: os 12 testes automatizados passaram após os ajustes da parte 3. O revisor independente repetiu a suíte com o mesmo resultado.
