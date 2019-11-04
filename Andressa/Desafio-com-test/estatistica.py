"""
Sua tarefa é processar uma seqüência de números inteiros para determinar as seguintes estatísticas:

    Valor mínimo
    Valor máximo
    Número de elementos na seqüência
    Valor médio

"""
import unittest


class EstatisticaSimples():
    def menor(seq):

        return min(seq)

    def maior(seq):

        return max(seq)

    def quantidade(seq):

        return len(seq)

    def media(seq):

        return sum(seq)/len(seq)

class Test_est(unittest.TestCase):

    def test_menor(self):
        seq = (6, 9, 15, -2, 92, 11)
        self.assertEqual(EstatisticaSimples.menor(seq), -2)

    def test_maior(self):
        seq = (6, 9, 15, -2, 92, 11)
        self.assertEqual(EstatisticaSimples.maior(seq), 92)

    def test_qtd(self):
        seq = (6, 9, 15, -2, 92, 11)
        self.assertEqual(EstatisticaSimples.quantidade(seq), 6)

    def test_media(self):
        seq = (6, 9, 15, -2, 92, 11)
        self.assertEqual(EstatisticaSimples.media(seq), 21.833333333333332)

#seq = (6, 9, 15, -2, 92, 11)
#print("O menor número da sequência é: ",min(seq))
#print("O maior número da sequência é: ",max(seq))
#print("O número de valores é de:", len(seq))
#print("Média é igual:", sum(seq)/len(seq))