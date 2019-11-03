# Calculate the distance between two poins on the xy plane.

def calc_distance(x1, y1, x2, y2):
	d = ((x2 - x1) ** 2 + (y2 - y1 ) ** 2) ** (1/2)
	return round(d,4)

while True:
	print('CALCULO DA DISTANCIA ENTRE DOIS PONTOS NO PLANO XY')
	x1 = int(input('Digite o valor de x1: '))
	y1 = int(input('Digite o valor de y1: '))
	x2 = int(input('Digite o valor de x2: '))
	y2 = int(input('Digite o valor de y2: '))
	print(calc_distance(x1, y1, x2, y2))
	answer = str(input('Deseja fazer outro cálculo? (S/N) '))
	if answer in 'Nn':
		break


if __name__ == '__main__':
	assert calc_distance(1,1,2,2) == 1.4142
	assert calc_distance(2,2,4,4) == 2.8284
	assert calc_distance(10,5,8,12) == 7.2801
	assert calc_distance(5,7,8,6) == 3.1623
