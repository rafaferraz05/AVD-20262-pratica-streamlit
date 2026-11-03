"""Preparação dos dados dos gráficos, independente da interface Streamlit."""

from itertools import combinations

import pandas as pd


def correlacoes_spearman(df, variaveis):
    """Triângulo inferior com pelo menos 3 pares válidos e variância nas duas colunas."""
    linhas = []
    for x, y in combinations(variaveis, 2):
        pares = df[[x, y]].dropna()
        if len(pares) < 3 or (pares.nunique() < 2).any():
            continue
        linhas.append({
            "var_x": x, "var_y": y,
            "correlacao": pares[x].corr(pares[y], method="spearman"),
            "observacoes": len(pares),
        })
    return pd.DataFrame(linhas, columns=["var_x", "var_y", "correlacao", "observacoes"])
