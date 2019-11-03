# process
def fibonacci(sequence):
	if sequence == 1 or sequence == 2:
		v = 1
	else:
		v = fibonacci(sequence - 1) + fibonacci(sequence - 2)	
	return v


# output
def value(sequence):
	print('A sequencia Fibonacci é a sequinte: ')
	lista = []
	for item in range(1, sequence +1):
		lista.append((fibonacci(item)))
	print(lista)


# input
while True:
	sequence = int(input('Digite a quantidade de números para a sequencia que deseja gerar: '))
	value(sequence)
	answer = str(input('Deseja gerar outra sequencia? (S/N) '))
	if answer in 'Nn':
		break


#test
if __name__ == '__main__':
	assert fibonacci(1) == 1
	assert fibonacci(2) == 1
	
	assert fibonacci(6) == 8
	assert fibonacci(7) == 13
	
	assert fibonacci(10) == 55
	assert fibonacci(30) == 832040
