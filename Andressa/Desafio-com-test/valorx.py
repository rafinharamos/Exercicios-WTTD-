"""


Leia 2 valores inteiros e armazene-os nas variáveis A e B.
Efetue a soma de A e B atribuindo o seu resultado na variável X.
Imprima X.
Não apresente mensagem alguma além daquilo que está sendo especificado.
Entrada

A entrada contém 2 valores inteiros.
Saída

Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X
e pelo final de linha. Cuide para que tenha um espaço antes e depois do sinal de igualdade.

"""

import unittest


class somax():
     def soma(self):
        A = int(input("Digite um número: "))
        B = int(input("Digite outro número: "))
        X = A + B
        print("X = %s" % X)
        return X
class TestSoma(unittest.TestCase):
    def testx(self):
       self.assertTrue(somax.soma(self), True)


if __name__ == '__main__':
    unittest.main()