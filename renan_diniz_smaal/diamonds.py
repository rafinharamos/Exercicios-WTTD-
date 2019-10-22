alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # noqa
letra = input("Digite a letra que deseja no meio do diamante: ")
letra = letra.upper()

if letra in alpha:
    n = alpha.index(letra)  # Pega a posição da letra na lista
else:
    print('Digite uma letra de A-Z')

num = 65  # Valor de A na tabela ASCII

for i in range(n):
    print(" "*(n-i) + chr(num) + " "*(2*i) + chr(num))
    num += 1

for j in range(n+1):
    print(" "*(j) + chr(num) + " "*((2*n-j)-j) + chr(num))
    num -= 1
