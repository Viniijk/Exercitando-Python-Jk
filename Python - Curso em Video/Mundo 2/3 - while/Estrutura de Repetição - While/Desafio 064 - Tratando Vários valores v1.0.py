'''Crie um programa que leia vários numeros inteiros pelo teclado. O programa vai parar quando
o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros
foram digitados e qual foi a SOMA entre eles.(desconsiderando o flag).'''

n = 0
n2 = 1
soma = 0
while n2 != 999:
    n += 1
    n1 = int(input('Digite o {}ª Valor: '.format(n)))
    soma = soma + n1
    if n >= 2:
        n2 = int(input('''DIGITE para FINALIZAR [999] ou DIGITE para CONTINUAR [0]: '''))
print('Total de {} Entrada, somam {}'.format(n, soma))
