""" Escreva um programa que ao receber um numero n mostre na 
tela seu correspondente na sequencia de Fibonacci.

Ex.: 
Fn = F(n-1) + F(n-2)
e valores iniciais,
F1 = 1 e F2 = 1

saida = 0 - 1 - 1 - 2 - 3 - 5 - 8...

"""
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# testes
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13
assert fibonacci(12) == 144
assert fibonacci(18) == 2584



