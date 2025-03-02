'''Escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequencia de Fibonacci.'''
print('~' * 23)
print('SEQUÊNCIAS DE FIBONACCI')
print('~' * 23)
n = int(input('Quantos Termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('{} -> {}'.format(t1, t2), end='')
while cont <= n:
    cont += 1
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
print(' -> FIM')
print('=' * 23)
