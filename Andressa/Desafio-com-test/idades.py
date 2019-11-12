"""
Idade em dias

Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364.

Entrada

O arquivo de entrada contém um valor inteiro
"""

class Idade():
    valor = int(input("Digite o valor da idade em dias: "))
    years = int(valor / 365)
    month = int((valor % 365) / 30)
    days = int((valor % 365) % 30)

    print(years, "ano(s)", month, "mes(es)", days, "dia(s)")

    assert years >= 0
    assert month < 12
    assert days < 30


