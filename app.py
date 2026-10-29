import pandas as pd
import streamlit as st

from src.data_loader import load_data
from src.pictogramas import chuteira_svg, cartao_svg, gol_svg


st.set_page_config(page_title="Futebol nas cinco grandes ligas", layout="wide")
st.title("Futebol nas cinco grandes ligas")

try:
    df = load_data()
except FileNotFoundError:
    st.error("Execute o notebook e exporte os dados tratados para data/clean/futebol.csv.")
    st.stop()

# Mesmas variáveis quantitativas usadas na EDA de futebol.
VARS_QUANT = ["age_", "Playing Time_Min", "Performance_Gls", "Expected_xG", "Total_Cmp%"]
NOMES = {
    "age_": "Idade",
    "Playing Time_Min": "Minutos jogados",
    "Performance_Gls": "Gols",
    "Expected_xG": "Gols esperados (xG)",
    "Total_Cmp%": "Acerto de passes (%)",
}

colunas_necessarias = set(VARS_QUANT + ["season", "league", "team", "perfil"])
if not colunas_necessarias.issubset(df.columns):
    st.error("O CSV não corresponde ao futebol tratado. Confira a exportação do notebook.")
    st.stop()


def nome_temporada(temporada):
    codigo = str(int(temporada))
    return f"20{codigo[:2]}/{codigo[2:]}"


with st.sidebar:
    st.header("Navegação")
    dashboard = st.radio(
        "Dashboard",
        ["1 · Correlação e distribuição", "2 · Indicadores: meu rascunho"],
        key="dashboard",
    )
    st.header("Filtros")
    temporada = st.selectbox(
        "Temporada",
        sorted(df["season"].dropna().unique(), reverse=True),
        format_func=nome_temporada,
        key="temporada",
    )
    ligas = st.multiselect(
        "Ligas",
        sorted(df["league"].dropna().unique()),
        default=sorted(df["league"].dropna().unique()),
        key="ligas",
    )

df_base = df[df["season"].eq(temporada) & df["league"].isin(ligas)]
with st.sidebar:
    clubes = st.multiselect(
        "Clubes",
        sorted(df_base["team"].dropna().unique()),
        help="Deixe vazio para incluir todos os clubes das ligas escolhidas.",
        key="clubes",
    )
if clubes:
    df_base = df_base[df_base["team"].isin(clubes)]

st.caption(f"Temporada {nome_temporada(temporada)} · {len(df_base):,} registros jogador–clube–temporada")
if df_base.empty:
    st.warning("Nenhum registro neste recorte. Selecione pelo menos uma liga ou ajuste os clubes.")
    st.stop()

if dashboard.startswith("1"):
    st.header("Dashboard 1 · Correlação e distribuição")
    st.caption("Esqueleto da primeira entrega: selecione as variáveis e teste os filtros de intervalo.")

    with st.sidebar:
        variaveis = st.multiselect(
            "Variáveis quantitativas", VARS_QUANT, default=VARS_QUANT,
            format_func=NOMES.get, key="variaveis",
        )
        separar_por_classe = st.toggle(
            "Distinguir atacantes das demais posições", key="separar_por_classe",
            help="Planejado para colorir o histograma pela coluna perfil da EDA.",
        )
        intervalos = {}
        for var in variaveis:
            serie = df_base[var].dropna()
            if serie.empty:
                st.caption(f"{NOMES[var]}: sem valores disponíveis.")
                continue
            if pd.api.types.is_integer_dtype(serie):
                minimo, maximo, passo = int(serie.min()), int(serie.max()), 1
            else:
                minimo, maximo, passo = float(serie.min()), float(serie.max()), 0.1
            if minimo == maximo:
                st.caption(f"{NOMES[var]}: valor único neste recorte ({minimo:g}).")
                continue
            inicio, fim = st.slider(
                NOMES[var], min_value=minimo, max_value=maximo,
                value=(minimo, maximo), step=passo,
                key=f"intervalo_{var}_{temporada}",
            )
            # O intervalo completo preserva as ausências estruturais da EDA.
            # Ao restringir o intervalo, ficam apenas os valores conhecidos dentro dele.
            if (inicio, fim) != (minimo, maximo):
                intervalos[var] = (inicio, fim)

    df_filtrado = df_base
    for var, (inicio, fim) in intervalos.items():
        df_filtrado = df_filtrado[df_filtrado[var].between(inicio, fim)]
    st.caption(f"{len(df_filtrado):,} de {len(df_base):,} registros após os filtros de intervalo.")
    if df_filtrado.empty:
        st.warning("Os intervalos selecionados não contêm registros. Amplie os filtros.")

    col_correlacao, col_distribuicao = st.columns([1, 1.5])
    with col_correlacao, st.container(border=True, height=280):
        st.subheader("Correlação")
        if len(variaveis) < 2:
            st.warning("Selecione pelo menos duas variáveis para a correlação.")
        else:
            st.info("Espaço reservado para a matriz de correlação.")
        # TODO: calcular Spearman, como na EDA, e desenhar o heatmap na etapa de gráficos.
    with col_distribuicao, st.container(border=True, height=280):
        st.subheader("Distribuição")
        if variaveis:
            variavel_histograma = st.selectbox(
                "Variável do histograma", variaveis,
                format_func=NOMES.get, key="variavel_histograma",
            )
            st.info("Espaço reservado para o histograma.")
            if separar_por_classe:
                st.caption("Comparação planejada: Atacante × Demais.")
        else:
            st.info("Selecione uma variável na barra lateral.")
        # TODO: histograma de df_filtrado; usar perfil quando separar_por_classe estiver ativo.

else:
    st.header("Dashboard 2 · Indicadores de futebol")
    st.info("Rascunho visual: as figuras mostram o layout planejado. Os valores e preenchimentos serão calculados na etapa de KPIs.")

    with st.container(border=True):
        texto, desenho = st.columns([1, 2])
        with texto:
            st.subheader("Chutes no alvo")
            st.metric("Percentual de acerto", "—")
            st.caption("Chutes no alvo ÷ total de chutes × 100. O percentual preencherá o desenho do gol.")
        with desenho:
            st.image(gol_svg(), width="stretch", alt="Rascunho de um gol com rede, ainda sem preenchimento de dados.")
        # TODO: razão dos totais de Standard_SoT e Standard_Sh no recorte; sem chutes = indefinido.

    st.subheader("Top 5 · Jogadores com mais gols")
    for posicao, coluna in enumerate(st.columns(5), start=1):
        with coluna, st.container(border=True):
            st.markdown(f"**{posicao}º lugar**")
            st.image(chuteira_svg(), width="stretch", alt=f"Chuteira reservada ao {posicao}º jogador do ranking de gols.")
            st.caption("Jogador a calcular")
            st.metric("Gols", "—")

    for titulo, cor, tipo in [
        ("Top 5 · Cartões amarelos", "#eab308", "amarelos"),
        ("Top 5 · Cartões vermelhos", "#dc2626", "vermelhos"),
    ]:
        st.subheader(titulo)
        for posicao, coluna in enumerate(st.columns(5), start=1):
            with coluna, st.container(border=True):
                st.markdown(f"**{posicao}º lugar**")
                st.image(cartao_svg(cor), width="stretch", alt=f"Cartão reservado ao {posicao}º jogador do ranking de cartões {tipo}.")
                st.caption("Jogador a calcular")
                st.metric("Cartões", "—")

    st.caption("Escala planejada: o líder de cada ranking terá a figura cheia; os demais, preenchimento proporcional. Os números reais aparecerão junto das figuras.")
    # TODO: somar por jogador antes de selecionar o top 5; considerar transferências e homônimos.
    # TODO: calcular cada ranking separadamente, tratar empates e ausência de valores positivos.

with st.expander("Dados do recorte selecionado"):
    dados_exibidos = df_filtrado if dashboard.startswith("1") else df_base
    st.dataframe(
        dados_exibidos[["player", "team", "league", *VARS_QUANT]],
        hide_index=True, column_config=NOMES,
    )
