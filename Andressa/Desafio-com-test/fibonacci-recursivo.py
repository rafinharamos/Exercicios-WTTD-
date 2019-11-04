import unittest
from functools import lru_cache



@lru_cache(maxsize=10000)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)


for n in range(0, 10):
    print(fib(n))


assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(9) == 34

if __name__ == '__main__':
    unittest.main()

