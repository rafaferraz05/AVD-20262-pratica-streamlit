"""Gráficos Altair usados nos dashboards de futebol."""

import altair as alt


VERDE = "#15803d"
CORES_PERFIL = alt.Scale(domain=["Atacante", "Demais"], range=["#15803d", "#60a5fa"])


def mapa_correlacao(dados, variaveis, nomes):
    dados = dados.assign(
        eixo_x=dados["var_x"].map(nomes), eixo_y=dados["var_y"].map(nomes)
    )
    base = alt.Chart(dados).encode(
        x=alt.X("eixo_x:N", title=None, sort=[nomes[v] for v in variaveis[:-1]],
                  axis=alt.Axis(labelAngle=-25, labelLimit=160)),
        y=alt.Y("eixo_y:N", title=None, sort=[nomes[v] for v in variaveis[1:]],
                  axis=alt.Axis(labelLimit=160)),
        tooltip=[alt.Tooltip("eixo_x:N", title="Variável 1"),
                 alt.Tooltip("eixo_y:N", title="Variável 2"),
                 alt.Tooltip("correlacao:Q", title="Spearman", format=".2f"),
                 alt.Tooltip("observacoes:Q", title="Pares válidos", format=".0f")],
    )
    celulas = base.mark_rect().encode(color=alt.Color(
        "correlacao:Q", title="Spearman", scale=alt.Scale(domain=[-1, 1], scheme="redblue", reverse=True)
    ))
    numeros = base.mark_text(fontSize=15).encode(
        text=alt.Text("correlacao:Q", format=".2f"),
        color=alt.condition("abs(datum.correlacao) > 0.5", alt.value("white"), alt.value("#111827")),
    )
    return (celulas + numeros).properties(height=340)


def histograma(df, variavel, nome, separar=False):
    dados = df[[variavel, "perfil"]].dropna(subset=[variavel])
    grafico = alt.Chart(dados).mark_bar(color=VERDE, opacity=0.75).encode(
        x=alt.X(field=variavel, type="quantitative", title=nome, bin=alt.Bin(maxbins=20)),
        y=alt.Y("count():Q", title="Registros jogador–clube–temporada", stack=None),
        tooltip=[alt.Tooltip("count():Q", title="Registros", format=".0f")],
    )
    if separar:
        grafico = grafico.encode(
            color=alt.Color("perfil:N", title="Perfil", scale=CORES_PERFIL),
            tooltip=[alt.Tooltip("perfil:N", title="Perfil"),
                     alt.Tooltip("count():Q", title="Registros", format=".0f")],
        )
    return grafico.properties(height=340)
