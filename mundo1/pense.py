from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador "Pensar"
print(' -=- ' * 20)
jogador = int(input('Em que numero pensei entre 0 e 5? '))
print(' -=- ' * 20)
jogador = int(input('Em que numero pensei? '))
print('Processando... ')
sleep(2)
if jogador == computador:
    print('parabens vo me venceu!')
else:
    print('Ganhei {}'.format(computador,jogador))