from random import randint

'''Melhore o jogo do DESAFIO 028 onde o computador
 vai PENSAR em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''

r = randint(0, 10)
cont = 0
n = ''
while n != r:
    n = int(input('Descubra em qual número a Vegas está pensando: '))
    if n == r:
        cont += 1
        print('Parabéns, você acertou no {}ª palpite.'.format(cont))
    else:
        cont += 1
        print('\033[31mOps, você errou. Já teve {}ª palpites, tente novamente.\033[m'.format(cont))