"""
Sua tarefa é processar uma seqüência de números inteiros para determinar as seguintes estatísticas:

    Valor mínimo
    Valor máximo
    Número de elementos na seqüência
    Valor médio

Por exemplo para uma seqüência de números "6, 9, 15, -2, 92, 11", temos como saída:

    Valor mínimo: -2
    Valor máximo: 92
    Número de elementos na seqüência: 6
    Valor médio: 18.1666666
"""
import unittest

#seq = (6, 9, 15, -2, 92, 11)


#print("O menor número da sequência é: ",min(seq))
#print("O maior número da sequência é: ",max(seq))
#print("O número de valores é de:", len(seq))
#print("Média é igual:", sum(seq)/len(seq))

class EstatisticaSimples():
    """Clase responsavel por calcular as estatisticas."""

    def menor(seq):
        """Retorna o menor numero."""

        return min(seq)

    def maior(seq):
        """retorna o maior numero."""
        return max(seq)

    def quantidade(seq):
        """retorna a quantidade de numeros digitados."""
        return len(seq)

    def media(seq):
        """Retorna a media dos valores."""

        return sum(seq)/len(seq)

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

