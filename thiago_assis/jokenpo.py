# 1 para pedra, 2 para papel e 3 para tesoura
import random

def jokenpo(p1):
    player = p1
    number = random.randint(1,3)
    winner = ''
    if player == number:
        winner = 'Empate'
    elif player == 1 and number == 3 or player == 2 and number == 1 or player == 3 and number == 2:
        winner = ('Você venceu!', number)
    elif player == 1 and number == 2 or player == 2 and number == 3 or player == 3 and number == 1:
        winner = ('Você perdeu!', number)

    print (winner, number)
    return winner

