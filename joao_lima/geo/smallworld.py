#!/usr/bin/python
# Exercicio http://dojopuzzles.com/problemas/exibe/um-mundo-pequeno/
import sys


print(
    """
    Considere o mundo plano
    latitude e a longitude são coordenadas cartesianas nesse plano
    Exemplo:
        Amigo: George
        Latitute: 12
        Longitute: -12

        Amigo: Jose
        Latitute: 14
        Longitute: -2

        Amigo: Lucas
        Latitute: 4
        Longitute: -5

        Amigo: Joao
        Latitute: 7
        Longitute: 0

        Amigo: Enzo
        Latitute: 20
        Longitute: -20
    Ouput esperado:
        George está mais perto de Jose, Lucas, Enzo
        Jose está mais perto de Lucas, George, Joao
        Lucas está mais perto de Joao, Jose, George
        Joao está mais perto de Lucas, Jose, George
        Enzo está mais perto de George, Jose, Lucas
        OBS: Ordem de proximidade
    """
)

getting_information = True
information_dict = {}
while getting_information:
    nome = input("Digite informe o nome do amigo: ")
    latitute = input("Digite informe a latitude do(a) {}: ".format(nome))
    longitude = input("Digite informe a longitude do(a) {}: ".format(nome))

    information_dict[nome] = {"latitute": latitute, "longitude": longitude}

    exit = input("Deseja adicionar mais amigos e sua localização? ( Y ou N ) ")

    if exit.lower() == 'n':
        print('\nCalculando distancia ...\n')
        getting_information = False
    elif exit.lower() == 'y':
        print('\nNovas informações do amigo: \n')
    else:
        print('\nOpção invalida')
        sys.exit(1)


def _get_distance(lat, lng):
    lat = float(lat).__abs__()
    lng = float(lng).__abs__()
    return lat + lng


for name, localizacao in information_dict.items():
    distance_dict = {}
    distance = _get_distance(localizacao['latitute'], localizacao['longitude'])
    for friend_name, friend_coord in information_dict.items():
        if name == friend_name:
            continue
        friend_distance = _get_distance(
                friend_coord['latitute'], friend_coord['longitude']
        )
        distance_dict[friend_name] = abs(friend_distance - distance) / 2

    sorted_friend_list = sorted(distance_dict.items(), key=lambda k: k[1])
    closest_friend = [friend_name for friend_name, _ in sorted_friend_list[:3]]
    print("{} está mais perto de {}".format(name, ", ".join(closest_friend)))
