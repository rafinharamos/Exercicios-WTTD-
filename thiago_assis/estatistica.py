"""
Sua tarefa é processar uma seqüência de números inteiros para determinar as seguintes estatísticas:

- Valor mínimo
- Valor máximo
- Número de elementos na seqüência
- Valor médio
Por exemplo para uma seqüência de números "6, 9, 15, -2, 92, 11", temos como saída:

- Valor mínimo: -2
- Valor máximo: 92
- Número de elementos na seqüência: 6
- Valor médio: 18.1666666
"""

import random


def sequence(size):
    lista = []
    for i in range(size):
        number = random.randint(1,100)
        if number in lista:
            temp = random.randint(1,100)
            if temp != number:
                lista.append(number)
        else:    
            lista.append(number)
    lista.sort()

    print('O menor valor da lista é {}'.format(lista[0]))
    print('O maior valor da lista é {}'.format(lista[-1]))
    print('A quantidadede de elementos da lista é: {}'.format(len(lista)))
    print('A média extraída dos valores da Lista é: {}'.format(sum(lista)/len(lista)))

    return lista
    