from random import randint
from time import sleep
'''Escreva um programa que faça o computador 'PENSAR' 
em um numero inteiro enter 0 e 5 e peça para o usuario
 tentar descobrir qual foi o numero escolhido pelo computador.
  O Porgrama deverpa escrever na tela se o usuario venceu ou perdeu'''

r = randint(0, 5)

print('-=-' * 8)
print('{} Vou Pensar em um número {} '.format('\033[1;34m', '\033[m'))
print('-=-' * 8)
sleep(1.2)
print(r)
usuario = int(input('Tente descobrir qual número estou pensando entre 0 e 5: '))


print('Processando... ')
sleep(1.5)

if usuario == r:
    print('{} Parabéns {}, {} Você acertou! {}'.format('\033[7;32;43m', '\033[m', '\033[7;33;42m', '\033[m'))
else:
    print('\033[7;34;40mPoxa, não foi dessa vez que você conseguiu. Pensei em {}. TENTE NOVAMENTE\033[m'.format(r))
print('----- FIM -----')
