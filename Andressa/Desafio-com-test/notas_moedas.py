"""
Notas e moedas

Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.
Entrada

O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
Saída

Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

"""

montante = float(input("Digite o valor para saber a quantidade respectiva de notas e moedas: "))
cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("Notas:")

for nota in cedulas:
    qtd_nota = int(montante / nota)
    print("{} nota(s) de R$ {:.2f}".format(qtd_nota, nota))
    montante -= qtd_nota * nota

print("Moedas")

for moeda in moedas:
    qtd_moeda = int(montante / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moeda, moeda))
    montante -= qtd_moeda * moeda

assert moeda >= 0.01 < 1
assert nota >= 2 < 100
assert qtd_nota >= 0
assert qtd_moeda >= 0
