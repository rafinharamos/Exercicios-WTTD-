
fibo_cache = {}
number = 0
def fibo(n):
    number = n
    if type(number) != int:
        raise TypeError('A entrada deve ser um valor inteiro.') #não consegui implementar um teste assim
    elif number < 1:
        raise ValueError('O número deve ser um valor inteiro maior que zero.') #não consegui implementar um teste assim
    elif number == 1 or number == 2:
        value = 1
    elif number > 2:
        value = fibo(number-1) + fibo(number-2)
    
    fibo_cache[number] = value
    return value


assert fibo(2) == 1
assert fibo(3) == 2
assert fibo(7) == 13
assert fibo(8) == 21
#assert type(number) != int, 'Digite um número inteiro'
#assert number < 1, 'Digite um valor maior que 0' 
