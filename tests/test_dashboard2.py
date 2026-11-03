import json
from pathlib import Path
import unittest

import pandas as pd
from streamlit.testing.v1 import AppTest


RAIZ = Path(__file__).resolve().parents[1]


def valores_esperados(df):
    pares = df[["Standard_Sh", "Standard_SoT"]].dropna()
    pares = pares[(pares.Standard_Sh >= 0) & (pares.Standard_SoT >= 0) & (pares.Standard_SoT <= pares.Standard_Sh)]
    pontaria = 100 * pares.Standard_SoT.sum() / pares.Standard_Sh.sum()
    return [f"{pontaria:.1f}%".replace(".", ","), *[
        f"{df[c].sum():,.0f}".replace(",", ".")
        for c in ["Performance_Gls", "Performance_CrdY", "Performance_CrdR"]
    ]]


class Dashboard2Test(unittest.TestCase):
    def test_kpis_recalculam_por_clube_mas_nao_por_intervalo_do_dashboard1(self):
        df = pd.read_csv(RAIZ / "data/clean/futebol.csv")
        app = AppTest.from_file(str(RAIZ / "app.py"), default_timeout=180).run()
        self.assertFalse(app.exception)
        esperado = df[df.season.eq(df.season.max())]
        self.assertEqual([m.value for m in app.metric], valores_esperados(esperado))
        codigo = int(df.season.max())
        app.slider(key=f"intervalo_age__{codigo}").set_value((25.0, 30.0)).run()
        self.assertFalse(app.exception)
        self.assertEqual([m.value for m in app.metric], valores_esperados(esperado))
        app.multiselect(key="ligas").set_value(["ENG-Premier League"]).run()
        app.multiselect(key="clubes").set_value(["Arsenal"]).run()
        esperado = esperado[esperado.league.eq("ENG-Premier League") & esperado.team.eq("Arsenal")]
        self.assertFalse(app.exception)
        self.assertEqual([m.value for m in app.metric], valores_esperados(esperado))

    def test_ranking_altair_tem_selecao_de_jogador_e_figuras_reais(self):
        app = AppTest.from_file(str(RAIZ / "app.py"), default_timeout=180).run()
        self.assertFalse(app.exception)
        graficos = [n for n in app.tabs[1] if n.type == "vega_lite_chart"]
        self.assertEqual(len(graficos), 1)
        spec = json.loads(graficos[0].proto.spec)
        self.assertEqual(spec["params"][0]["name"], "jogador")
        self.assertEqual(spec["params"][0]["select"]["fields"], ["identidade"])
        self.assertEqual(len(app.metric), 4)
        self.assertEqual(len(app.get("image")), 16)
        self.assertFalse(any("a calcular" in t.value for t in app.caption))
        app.selectbox(key="metrica_ranking").set_value("vermelhos").run()
        self.assertFalse(app.exception)


if __name__ == "__main__":
    unittest.main()
