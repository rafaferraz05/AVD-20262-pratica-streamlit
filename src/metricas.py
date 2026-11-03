"""Cálculos dos indicadores; não dependem da interface Streamlit."""

import json

import pandas as pd


COLUNAS = {
    "gols": "Performance_Gls",
    "amarelos": "Performance_CrdY",
    "vermelhos": "Performance_CrdR",
}


def soma_conhecida(serie):
    valor = serie.sum(min_count=1)
    return None if pd.isna(valor) else float(valor)


def calcular_metricas(df):
    # Numerador e denominador usam as MESMAS linhas válidas.
    pares = df[["Standard_SoT", "Standard_Sh"]].dropna()
    pares = pares[(pares["Standard_Sh"] >= 0) & (pares["Standard_SoT"] >= 0)
                  & (pares["Standard_SoT"] <= pares["Standard_Sh"])]
    chutes = soma_conhecida(pares["Standard_Sh"])
    alvo = soma_conhecida(pares["Standard_SoT"])
    valores = {nome: soma_conhecida(df[coluna]) for nome, coluna in COLUNAS.items()}
    valores.update(
        pontaria=100 * alvo / chutes if chutes and chutes > 0 else None,
        chutes=chutes, chutes_alvo=alvo, linhas_chutes=len(pares),
        ausentes={nome: int(df[coluna].isna().sum()) for nome, coluna in COLUNAS.items()},
    )
    return valores


def _identidade(nome, nascimento):
    ano = None if pd.isna(nascimento) else int(nascimento)
    return json.dumps([str(nome), ano], ensure_ascii=False)


def identidades(df):
    return pd.Series(
        [_identidade(n, a) for n, a in zip(df["player"], df["born_"])], index=df.index,
        dtype="string",
    )


def agrupar_jogadores(df):
    # Um jogador pode ter várias linhas por transferências entre clubes.
    colunas = list(COLUNAS.values())
    agrupado = df.groupby(["player", "born_"], dropna=False)[colunas].sum(min_count=1).reset_index()
    agrupado["identidade"] = identidades(agrupado)
    repetidos = agrupado["player"].duplicated(keep=False)
    agrupado["rotulo"] = [
        f"{nome} ({'ano desconhecido' if pd.isna(ano) else int(ano)})" if repetido else str(nome)
        for nome, ano, repetido in zip(agrupado["player"], agrupado["born_"], repetidos)
    ]
    return agrupado


def top_jogadores(df, metrica, limite=5):
    coluna = COLUNAS[metrica]
    agrupado = agrupar_jogadores(df)
    return (agrupado[agrupado[coluna].gt(0)]
            .sort_values([coluna, "player", "born_"], ascending=[False, True, True], kind="stable")
            .head(limite).reset_index(drop=True))


def filtrar_jogadores(df, selecionados):
    return df[identidades(df).isin(selecionados)] if selecionados else df
