import unittest


def fib(n):
    if n == 0:
        resultado = 0
    if n == 1 or n == 2:
        resultado = 1
    elif n > 2:
        resultado = fib(n - 1) + fib(n - 2)
    return resultado

for n in range(10):
    print(fib(n))


class Test_fibo(unittest.TestCase):
    def test_fiboo(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(9), 34)
if __name__ == '__main__':
    unittest.main()


