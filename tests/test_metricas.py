import unittest

import pandas as pd

from src.metricas import calcular_metricas, filtrar_jogadores, top_jogadores


def base():
    return pd.DataFrame({
        "player": ["Ana", "Ana", "Bia", "Bia"], "born_": [1990, 1990, 1991, 1992],
        "Performance_Gls": [2, 3, 4, 0], "Performance_CrdY": [1, 2, 0, 4],
        "Performance_CrdR": [0, 1, 0, 0], "Standard_Sh": [10, 90, 1000, 0],
        "Standard_SoT": [10, 0, None, 0],
    })


class MetricasTest(unittest.TestCase):
    def test_pontaria_e_razao_dos_totais_com_pares_validos(self):
        valores = calcular_metricas(base())
        self.assertEqual(valores["pontaria"], 10)
        self.assertEqual(valores["chutes"], 100)
        self.assertEqual(valores["gols"], 9)

    def test_nao_confunde_ausencia_com_zero_ou_divide_por_zero(self):
        df = base().iloc[:1].copy()
        df["Standard_Sh"] = 0
        df["Standard_SoT"] = 0
        df["Performance_CrdR"] = float("nan")
        valores = calcular_metricas(df)
        self.assertIsNone(valores["pontaria"])
        self.assertIsNone(valores["vermelhos"])
        self.assertEqual(valores["amarelos"], 1)
        self.assertIsNone(calcular_metricas(df.iloc[:0])["gols"])

    def test_soma_transferencias_e_separa_homonimos(self):
        ranking = top_jogadores(base(), "gols")
        self.assertEqual(list(ranking["Performance_Gls"]), [5, 4])
        self.assertEqual(ranking.iloc[0]["player"], "Ana")
        jogadores = top_jogadores(base(), "amarelos")
        self.assertEqual(len(jogadores), 2)
        self.assertEqual(jogadores.iloc[0]["born_"], 1992)
        selecionados = filtrar_jogadores(base(), [ranking.iloc[0]["identidade"]])
        self.assertEqual(len(selecionados), 2)
        self.assertEqual(calcular_metricas(selecionados)["gols"], 5)

    def test_empate_por_nome_e_zero_nao_entra_no_top(self):
        df = base()
        df.loc[2, "Performance_Gls"] = 5
        ranking = top_jogadores(df, "gols", limite=1)
        self.assertEqual(list(ranking["player"]), ["Ana"])
        df["Performance_Gls"] = 0
        self.assertTrue(top_jogadores(df, "gols").empty)


if __name__ == "__main__":
    unittest.main()
