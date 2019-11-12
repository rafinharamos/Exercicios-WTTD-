"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir 
o volume. Certifique-se de que o número do canal e o nível do volume permanecem 
dentro de faixas válidas.
"""
class TV:

    def canal(self, num):
        validos = ('2', '4', '5', '7', '9', '11', '13')
        if str(num) in validos:
            saida = str(num)
        else:
            saida =  'Canal não existe.'
        
        return saida


    def volume(self, vol):
        v = 0
        if vol in range(0, 101):
            if vol < v:
                v = vol
            som = f'Vol {vol}'
        else:
            som = 'Volume fora da faixa.'

        return som

# testes        
tv = TV()
assert tv.canal(2) == '2'
assert tv.canal(3) == 'Canal não existe.'
assert tv.canal(13) == '13'
assert tv.canal(30) == 'Canal não existe.'

assert tv.volume(2) == 'Vol 2'
assert tv.volume(101) == 'Volume fora da faixa.'
assert tv.volume(-1) == 'Volume fora da faixa.'


# Programa principal
tv = TV()
print(tv.canal(132), tv.volume(20))
