"""
Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD.
A seguir mostre a variável PROD com mensagem correspondente.
Entrada

O arquivo de entrada contém 2 valores inteiros.
Saída

Imprima a variável PROD com um espaço em branco antes e depois da igualdade.

"""
import unittest


class produto():
     def mult(self):
        num1 = int(input("Digite um número inteiro: "))
        num2 = int(input("Digite outro número inteiro: "))
        PROD = num1*num2
        print("PROD = %s" % PROD)
        return PROD
class raizquad():
     def raiz(self):
        val1 = int(input("Digite o número para saber a raiz: "))
        result1 = val1 ** (1/2)
        list = []
        list.append(result1)
        print("Lista contendo o valor da raiz: ", list)
        return result1


class TestMult(unittest.TestCase):
    def testando(self):

        self.assertTrue(produto.mult(self), True)
        self.assertTrue(raizquad.raiz(self), True)




if __name__ == '__main__':
    unittest.main()