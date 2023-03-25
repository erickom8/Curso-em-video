from random import randint
from time import sleep

computador = randint (0,10) #faz o computador 'PENSAR'
print( '\033[33m-=-\033[m' *15)
print('\033[34mVou pensar em um número entre 0 e 10... Tente adivinhar.\033[m')
print( '\033[33m-=-\033[m' *15)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('\033[32mPARABÉNS, você acertou\033[m')
else:
    print('\033[31mPERDEU! Eu pensei no número {} e não no {}\033[m'.format (computador, jogador))