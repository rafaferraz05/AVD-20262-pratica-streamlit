from pathlib import Path
import unittest
from unittest.mock import patch

import pandas as pd
from streamlit.testing.v1 import AppTest


RAIZ = Path(__file__).resolve().parents[1]


def iniciar():
    return AppTest.from_file(str(RAIZ / "app.py"), default_timeout=180).run()


def graficos_primeira_aba(app):
    return [n for n in app.tabs[0] if n.type == "vega_lite_chart"]


class Dashboard1Test(unittest.TestCase):
    def test_zero_uma_duas_variaveis_e_classes(self):
        app = iniciar()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.tabs), 2)
        for variaveis, quantidade in [([], 0), (["age_"], 1), (["age_", "Performance_Gls"], 3)]:
            app.multiselect(key="variaveis").set_value(variaveis).run()
            self.assertFalse(app.exception)
            self.assertEqual(len(graficos_primeira_aba(app)), quantidade)
        app.toggle(key="separar_por_classe").set_value(True).run()
        self.assertFalse(app.exception)
        self.assertIn('"perfil"', graficos_primeira_aba(app)[-1].proto.spec)

    def test_filtros_em_combinacao_e_recorte_vazio(self):
        app = iniciar()
        app.selectbox(key="temporada").set_value(1718).run()
        app.multiselect(key="ligas").set_value(["ENG-Premier League"]).run()
        app.multiselect(key="clubes").set_value(["Arsenal"]).run()
        app.slider(key="intervalo_age__1718").set_value((25.0, 30.0)).run()
        self.assertFalse(app.exception)
        dados = app.dataframe[0].value
        self.assertFalse(dados.empty)
        self.assertTrue(dados["age_"].between(25, 30).all())
        self.assertEqual(set(dados["team"]), {"Arsenal"})
        self.assertEqual(set(dados["league"]), {"ENG-Premier League"})
        app.multiselect(key="ligas").set_value([]).run()
        self.assertFalse(app.exception)
        self.assertTrue(any("Nenhum registro" in w.value for w in app.warning))

    def test_constantes_nao_quebram_slider_nem_correlacao(self):
        df = pd.DataFrame({
            "player": ["A", "B", "C"], "born_": [2000] * 3,
            "season": [2425] * 3, "league": ["Liga"] * 3, "team": ["Time"] * 3,
            "perfil": ["Demais"] * 3, "age_": [24.0] * 3,
            "Playing Time_Min": [90] * 3, "Performance_Gls": [0] * 3,
            "Expected_xG": [0.0] * 3, "Total_Cmp%": [80.0] * 3,
            "Standard_Sh": [0] * 3, "Standard_SoT": [0] * 3,
            "Performance_CrdY": [0] * 3, "Performance_CrdR": [0] * 3,
        })
        with patch("src.data_loader.load_data", return_value=df):
            app = iniciar()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.slider), 0)
        self.assertTrue(any("valores distintos" in w.value for w in app.warning))


if __name__ == "__main__":
    unittest.main()
