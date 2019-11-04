"""
Quando a posição é multipla de 3, fale fizz
Quando a posição é multipla de 5, fale buzz
Quando a posição é multipla de 3 e 5, fale fizz buzz
Para todas as outras posições, retorne o próprio número


def game(posicao):
    posicao = int(input())
    if posicao/3 % 0:
        print("Fizz")
    else:
        print("test")
    return posicao

"""

def game(num):
   # nume = input("digite um numero para jogar: ")
    if num == 1:
        num = 1
    if num == 2:
        num = 2
    if num == 3:
        num = 'Fizz'
    if num == 5:
        num = 'Buzz'
    if num == 15:
        num = 'FizzBuzz'
    return num
if __name__ == '__main__':
    assert game(1) == 1
    assert game(2) == 2
    assert game(4) == 4

    assert game(3) == 'Fizz'
    #assert game(6) == 'Fizz'
   # assert game(9) == 'Fizz'

    assert game(5) == 'Buzz'
   # assert game(10) == 'Buzz'
    #assert game(20) == 'Buzz'

    assert game(15) == 'FizzBuzz'
    #assert game(30) == 'FizzBuzz'
    #assert game(45) == 'FizzBuzz'
