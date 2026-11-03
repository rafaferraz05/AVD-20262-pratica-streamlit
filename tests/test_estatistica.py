import unittest

import pandas as pd

from src.estatistica import correlacoes_spearman


class CorrelacaoTest(unittest.TestCase):
    def test_pares_ausentes_nao_removem_observacoes_de_outros_pares(self):
        df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [8, 6, 4, 2], "c": [None, 1, None, 1]})
        dados = correlacoes_spearman(df, ["a", "b", "c"])
        self.assertEqual(len(dados), 1)
        self.assertEqual(dados.iloc[0]["observacoes"], 4)
        self.assertAlmostEqual(dados.iloc[0]["correlacao"], -1)

    def test_poucos_pares_e_colunas_constantes_nao_criam_correlacao(self):
        for df in [pd.DataFrame({"a": [1, 2], "b": [2, 3]}),
                   pd.DataFrame({"a": [1, 1, 1], "b": [1, 2, 3]})]:
            self.assertTrue(correlacoes_spearman(df, ["a", "b"]).empty)

    def test_zero_e_uma_variavel(self):
        df = pd.DataFrame({"a": [1, 2, 3]})
        self.assertTrue(correlacoes_spearman(df, []).empty)
        self.assertTrue(correlacoes_spearman(df, ["a"]).empty)


if __name__ == "__main__":
    unittest.main()
