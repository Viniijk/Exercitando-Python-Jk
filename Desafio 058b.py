from random import randint
computador = randint(0, 10)
print('Acabei de pensar em um número ntre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} palpites'.format(palpite))
