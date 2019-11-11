"""
Dado um nome, identificar se o gênero da pessoa é feminino ou masculino.
Buscar os dados na API https://genderapi.io/api.
"""
import requests


def genderfinder(name):
	t = requests.get('https://genderapi.io/api/?name={}&key=5dc96f71756fae29625f4312'.format(name)).json()['gender']
	if t == 'null':
		t = 'not a name.'
	return t
