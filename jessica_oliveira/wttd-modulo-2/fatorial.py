"""
Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N
"""
from functools import lru_cache

@lru_cache(None)
def fatorial(num):
    fat = 1

    for n in range(1, num+1):
        fat = fat*n
    return fat


# def fatorial(num):
#     if num == 1:
#         return 1
#     return num*fatorial(num-1)
#
# def fatorial(num):
#     return num*fatorial(num-1) if num > 1 else 1


if __name__ == '__main__':
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(4) == 24
