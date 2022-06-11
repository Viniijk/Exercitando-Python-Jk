from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('{:=^40}'.format(' JOGO JOKENPÔ '))



print('''Suas Opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
sleep(0.2)
print('JO...')
sleep(0.5)
print('KEN...')
sleep(0.5)
print('PÔ')

sleep(1)
print('=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=' * 10)

if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
if computador == 1: #PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
if computador == 2: #TESOURA
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')