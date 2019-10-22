import unittest
from unittest import TestCase

import EstatisticaSimples

class TestSoma(unittest.TestCase):
    """Classe responsavel por realizar os testes de estatisticas."""

    def test_menor(self):
        """Teste da função menor."""
        seq = (6, 9, 15, -2, 92, 11)
        self.assertEqual(EstatisticaSimples.menor(seq), -2)

    def test_maior(self):
        """Teste da função maior."""
        seq = (6, 9, 15, -2, 92, 11)
        self.assertEqual(EstatisticaSimples.maior(seq), 92)

    def test_quantidade(self):
        """Teste da função quantidade."""
        seq = (6, 9, 15, -2, 92, 11)
        self.assertEqual(EstatisticaSimples.quantidade(seq), 6)

    def test_media(self):
        """Teste da função media."""
        seq = (6, 9, 15, -2, 92, 11)
        self.assertEqual(EstatisticaSimples.media(seq), 21.833333333)