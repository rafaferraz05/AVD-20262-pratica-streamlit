from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data(ttl=300, max_entries=4)
def load_data(path="data/clean/futebol.csv"):
    """Lê o futebol tratado; caminhos relativos partem da raiz do projeto."""
    arquivo = Path(path)
    if not arquivo.is_absolute():
        arquivo = Path(__file__).resolve().parent.parent / arquivo
    return pd.read_csv(arquivo)
