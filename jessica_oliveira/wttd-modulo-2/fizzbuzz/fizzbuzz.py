"""" 
Regras do Fizzbuzz

1. Se a posição for multupla de 3: fizz
2. Se a posição for multupla de 5: buzz
3. Se a posição for multupla de 3 e 5: fizzbuzz
4. Para qualquer outra posição, fale outro número
"""

def multiple_of(base, num):
    return num % base == 0

def multiple_of_3(num):
    return multiple_of(3, num)


def multiple_of_5(num):
    return multiple_of(5, num)


def robot(pos):
    say = str(pos)
    if multiple_of_3(pos) and multiple_of_5(pos):
        say =  'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'
    return say
