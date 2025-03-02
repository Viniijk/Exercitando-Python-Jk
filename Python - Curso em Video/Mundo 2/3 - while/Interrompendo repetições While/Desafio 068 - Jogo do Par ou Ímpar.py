from random import randint
'''Faça um programa que jogue PAR ou IMPAR
com o computador. O jogo só será interrompido
quando o jogador PERDER. Mostrando o total
de vitorias consecutivas que ele conquistou
no final do jogo'''
print('=' * 45)
print('SEJA BEM VINDO AO JOGO PAR OU IMPAR')
print('EU SOU A VEGAS, JOGARES COM VOCÊ, PREPARADO?')
print('=' * 45)
cont = 0
while True:
    computador = randint(0, 10)
    n = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()
    while escolha not in 'PI':
        print('Opção incorreta, digite [P ou I]')
        escolha = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    soma = computador + n
    par = soma % 2 == 0
    print('=' * 45)
    print(f'Você jogou {n} e o computador {computador}. Total de {soma} | ', end='')
    print('DEU PAR' if par is True else 'DEU IMPAR')
    print('=' * 45)

    if escolha in 'PI':
        if par is True:
            if escolha == 'P':
                print('{:^17}VOCÊ GANHOU'.format(''))
                print('=' * 45)
                cont += 1
            elif escolha == 'I':
                print('''VOCÊ PERDEU
                GAME OVER''')
                print('=' * 45)
                break
        elif par is False:
            if escolha == 'I':
                print('{:^17}VOCÊ GANHOU'.format(''))
                print('=' * 45)
                cont += 1
            elif escolha == 'P':
                print('''VOCÊ PERDEU
                GAME OVER''')
                print('=' * 45)
                break
print(f'Você ganhou {cont} partidas')
