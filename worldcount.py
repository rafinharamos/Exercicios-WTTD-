import sys


def word_count_dict(filename):
    # dicionario que vai contar as palavras
    wordcount = {}  
    # abre o filename no arquivo f
    f = open(filename, 'r') 
    # le e separa numa lista de strings
    words = f.read().split() 
    for word in words:
        # coloca tudo em minusculo
        word = word.lower()  
        # loop para contar quantas vezes cada palavra aparece
        if not word in wordcount: 
            # se nao tinha, salva no dicionario wordcount o numero 1
            wordcount[word] = 1 
        else:
            # se ja tinha, soma essa nova ocorrencia
            wordcount[word] = wordcount[word] + 1 
    return wordcount


def print_top(filename): # mostra as 20 primeiras palavras mais usadas
    # recebe o retorno da funcao
    wordcount = word_count_dict(filename) 
    # coloca os itens em ordens, pela chave definina na funcao get_count, do maior para o menor
    items = sorted(wordcount.items(), key=get_count, reverse=True) 
    for item in items[:20]: 
        # mostra a palavra, seguida da quantidade de vezes que aconteceu
        print('> ', item[0],'apears', item[1],'times in text.') 


def get_count(wordcount):
    # define a chave que vai ser usada como referencia para ordenar na funcao anterior
    return wordcount[1] 


def print_words(filename): # mostra todas as palavras em ordem alfabetica e mostra quantas vezes cada um foi usada
    # recebe o retorno na funcao  
    wordcount = word_count_dict(filename) 
    # ordem alfabetica
    wordcount_sort = sorted(wordcount) 
    # para cada palavra em worldcount...
    for word in wordcount_sort: 
        # imprimir quantas vezes cada uma aparece
        print('> ',word, 'appears', wordcount[word], 'times in text') 

def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file.')
        # python worldcoutn.py count small.txt 
        # ou python worldcoutn.py topcount small.txt
        # ou python worldcoutn.py (count ou topcount) (arquivo.txt)
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()