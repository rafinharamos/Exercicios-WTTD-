notas = [100, 50, 20, 10, 2]
menor_nota = notas[-1]


def valor_desejado():
	# solicita o valor a ser sacado:
	# testa se valor < 10, invalido, pede para digitar novamente
	while True:
		valor = int(input('Valor do saque: '))
		if valor < menor_nota:
			print(f'Valor invalido! Saque mínimo: R${menor_nota}')
		elif valor % menor_nota != 0:
			print(f'Valor invalido! Somente notas de {notas}')
		else:
			break
	return valor


def saque(valor):
	d = {}
	for valor_nota in notas:
		qtd_notas = valor // valor_nota
	
		if qtd_notas != 0:
			valor -= qtd_notas * valor_nota
			d[valor_nota] = qtd_notas

	return d

def relatorio(notas_sacadas):
	print('SAQUE AUTORIZADO.')
	for valor, qtd in notas_sacadas.items():
		print(f'>> {qtd} notas de R${valor}.00')	


relatorio(saque(valor_desejado()))


# testes 
assert saque(2) == {2: 1}
assert saque(10) == {10: 1}
assert saque(100) == {100: 1}
assert saque(130) == {100: 1, 20: 1, 10: 1}
assert saque(1360) == {100: 13, 50: 1, 10: 1}
assert saque(546890) == {100: 5468, 50: 1, 20: 2}
