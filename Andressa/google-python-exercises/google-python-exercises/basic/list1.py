#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.


# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += worksExercícios básicos da lista
# # Preencha o código para as funções abaixo. main () já está configurado
# # para chamar as funções com algumas entradas diferentes,
# # imprimindo 'OK' quando cada função estiver correta.
# # O código inicial para cada função inclui um 'retorno'
# #, que é apenas um espaço reservado para o seu código.
# # Tudo bem se você não concluir todas as funções, e lá
# # são algumas funções adicionais para experimentar no list2.py..
def match_ends(words):
    #contador iniciado com 0
    count = 0
    #for chamado word no parametro words
    for word in words:
        #se tamanho da word for maior ou igual a 2 e word na posicao 0 for igual word na posicao -1
        if len(word) >= 2 and word[0] == word[-1]:
            #contador soma mais 1
            count += 1
    #retorna o valor do contador
    return count

def match_ends(words):
    c = 0
    for palavra in words:
        if len(palavra) >= 2 and palavra[0] == palavra[-1]:
            c += 1
    return c
# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.





def front_x(words):
    lista_x = []
    lista_normal = []

    for word in words:
        if word[0] == "x":
            lista_x.append(word)
        else:
            lista_normal.append(word)

    lista_x.sort()
    lista_normal.sort()

    return lista_x + lista_normal

def front_x(words):
    def _key(w):
        if w[0] == 'x':
            prefix = '@' if w.startswith('x') else ''
            return prefix + w

    return sorted(words, key=_key)




# C. sort_last
# Given a list of non-empty tuples, return a list sorted
# in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):


    def last(a):
        return a[-1]
    return sorted(tuples, key=last)


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xa'
                                              'a']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
