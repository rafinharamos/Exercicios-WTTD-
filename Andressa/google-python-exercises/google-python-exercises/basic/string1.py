#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
# A. rosquinhas
# Dada uma contagem int de um número de rosquinhas, retorne uma string
# do formulário 'Número de rosquinhas: <count>', em que <count> é o número
# passou. No entanto, se a contagem for 10 ou mais, use a palavra 'many'
# em vez da contagem real.
# So donuts (5) retorna 'Number of donuts: 5'
# and donuts (23) retorna 'Número de donuts: muitos'

def donuts(count):
    #se o tamanho da string for menor que 10
    if count < 10:
        #retorna o numero de donuts
        return 'Number of donuts: ' + str(count)
    else:
        #senao retorna numero de donuts = muitos
        return 'Number of donuts: many'

    return 'Number of donuts: %s' % count
def donuts(count):
    if count >= 10:
        qtd = 'many'
    else:
        qtd = str(count)

    return 'Number of donuts: ' + qtd





# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
# Dado uma string qualquer `s`, retonar uma string
# composta dos 2 primeiros e os 2 últimos caracteres, exemplo:
#
# panela ----> pala
# bala   ----> bala
# mao    ----> maao
# ja     ----> jaja
#
# Caso a string `s` contenha menos que 2 caracteres,
# retornar "" (string de cumprimento zero).

def both_ends(s):
    #se a string for menor que 2, retorna '' que significa string vazia
    if len(s) < 2:
        return ''
    #senao retorna a concatenacao da slice (capacidade de se obter parte de uma string, lista, tuplas) nas
    #duas primeiras posicoes e a slice das duas ultimas posicoes representadas por -2:
    else:
        return s[:2] + s[-2:]


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    #atribuiu a variavel inicio na posicao 0 da string
    inicio = s[0]
    # atribuiu a variavel fim apos a posicao 1
    fim = s[1:]
    #variavel sub recebe o inicio e a string que tiver a mesma letra e substituida por "*"
    sub = fim.replace(inicio, "*")
    #retorna o inicio mais oq foi substituido
    return inicio + sub


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length; 2 or more.
def mix_up(a, b):
    #b recebendo a string b ate a posicao 2 + a recebendo a string apos a posicao 2
    vara = b[:2] + a[2:]

    #a recebendo a string b ate a posicao 2 + b recebendo a string apos a posicao 2
    varb = a[:2] + b[2:]
    #retornando o valor de vara + string vazia + varb
    return vara + ' ' + varb





# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('donuts')
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
