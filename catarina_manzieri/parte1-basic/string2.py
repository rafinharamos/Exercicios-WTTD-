#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
    if len(s) >=3 and s.endswith('ing'):
        return s + 'ly'
    elif len(s) >=3:
        return s + 'ing'
    else:
        return s

# def verbing(s):
#     if len(s) >=3 and 'ing' not in s:
#         return s + 'ing'
#     elif len(s) >=3:
#         return s + 'ly'
#     else:
#         return s

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

# Achar o 'not' na string // verificar se tem 'bad' depois de 'not'
# se sim, replace 'not...bad' por 'good'

def not_bad(s):
    snot = s.find('not')
    sbad = s.find('bad')

    if sbad > snot:
        s = s.replace(s[snot:(sbad+3)], 'good')

    return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

# Considere dividir uma string em duas metades.
# Se o comprimento for regular, as metades da frente e de trás terão o mesmo comprimento.
# Se o comprimento for ímpar, diremos que o caractere extra fica na metade da frente.
# por exemplo. 'abcde', a metade da frente é 'abc', a parte de trás 'de'.

def front_back(a, b):
    a_metade = len(a) // 2
    b_metade = len(b) // 2

    if (len(a) % 2) == 0:
        a_inicio = a_fim = a_metade
    else:
        a_inicio = a_metade + 1
        a_fim = a_metade + 1

    if (len(b) % 2) == 0:
        b_inicio = b_fim = b_metade
    else:
        b_inicio = b_metade + 1
        b_fim = b_metade + 1

    resultado = a[:a_inicio] + b[:b_inicio] + a[a_fim:] + b[b_fim:]    

    return resultado

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
