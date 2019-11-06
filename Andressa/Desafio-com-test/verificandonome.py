#Verifica se o nome digitado corresponde a string andressa

import unittest


class pessoa():

    nome = str(input("Digite um nome:"))
    while nome != 'andressa':
        nome = str(input("Digite outro nome:"))

class TestNome(unittest.TestCase):
    def testando(self):
        self.assertEqual(pessoa.nome, 'andressa')
        self.assertEqual(pessoa.nome.count('andressa'), 1)
        self.assertEqual(pessoa.nome[-1], 'a')
        self.assertEqual(pessoa.nome[1], 'n')


if __name__ == '__main__':
    unittest.main()