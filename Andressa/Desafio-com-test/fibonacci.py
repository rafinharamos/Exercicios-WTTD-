"""
Leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci

"""
import unittest
from functools import lru_cache
from unittest import TestCase


@lru_cache(maxsize= 1000)

class Fibonacci():

    num = int(input("Quantos termos você gostaria de mostrar?"))
    n1 = 0
    n2 = 1
    print(n1,n2)
    cont_inicio = 3

    while cont_inicio <= num:
        n3 = n1 + n2
        print(n3)
        n1 = n2

        n2 = n3

        cont_inicio += 1

class Test_Fib(TestCase):
   def test_fib0(self):
    self.assertEqual(Fibonacci.n1, 0)
    self.assertEqual(Fibonacci.n2, 1)

    if __name__ == '__main__':
        unittest.main()

