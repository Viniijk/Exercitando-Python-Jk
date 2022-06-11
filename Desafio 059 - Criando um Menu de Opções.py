from time import sleep

'''Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso.'''
print('------ SEJA BEM VINDO, EU SOU A VEGAS ------')
n1 = int(input('Digite o Primeiro Valor: '))
n2 = int(input('Digite o Segundo Valor: '))
n = 0
while n != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    n = int(input('::: '))
    if n == 1:
        print('A Soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    elif n == 2:
        print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, n1 * n2))
    elif n == 3:
        if n1 > n2:
            print('{} é Maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é Maior que {}'.format(n2, n1))
        else:
            print('Os Valores {} e {} são iguais'.format(n1, n2))
    elif n == 4:
        print('Okay, Tente novamente abaixo')
        n1 = int(input('Digite o Primeiro Valor: '))
        n2 = int(input('Digite o Segundo Valor: '))
    elif n == 5:
        print('Finalizando...')
    else:
        print('INDISPONIVEL, TENTE NOVAMENTE')
    print('-=-' * 15)
    sleep(1)