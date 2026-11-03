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

## Publicação — atualizada em 03/11/2026

- [x] Login e criação do app concluídos pelo aluno no Streamlit Community Cloud.
- [x] App do projeto publicado e acessível sem solicitar login.
- [x] Serviço executando o app; a versão exata do Python na nuvem não foi inspecionada nesta auditoria.
- [x] URL real fornecida pelo aluno e aberta na revisão: https://avd-20262-pratica-app-hhtks5cg2embjiatbgns4y.streamlit.app/
- [x] URL real inserida no README.
- [x] Ambas as abas e controles conferidos em sessão separada de navegador, sem usar o login do Edge do aluno. Evidências em `revisao-publicacao.md`.
- [x] Endereço do README corresponde ao app efetivamente aberto.
- [ ] Aluno repetir o teste em uma janela anônima do próprio navegador, conforme o enunciado.

A publicação deixou de ser uma pendência. O teste sem login foi realizado pelo navegador de revisão; ele não é apresentado como abertura literal de uma janela anônima do Edge. A confirmação final dessa etapa fica com o aluno.

## Declaração de uso de IA

O arquivo foi preservado por instrução do aluno. A atividade exige a declaração no template indicado pela professora: o aluno deve preencher e conferir essa parte antes da submissão acadêmica.

## Como reproduzir os testes locais

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m streamlit run app.py
```

O teste local não substitui o teste do app publicado solicitado pela professora.

Validação local em 03/11/2026: os 12 testes automatizados passaram após os ajustes da parte 3. O revisor independente repetiu a suíte com o mesmo resultado.
