import unittest

n = int(input('Termos da sequencia Fibonacci: '))
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1


class Test_fibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(9), 34)
if __name__ == '__main__':
    unittest.main()