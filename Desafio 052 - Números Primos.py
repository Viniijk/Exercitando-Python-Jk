'''Faça um programa que leia um número
inteiro e diga se ele é ou não um número primo.'''

p = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[36m', end='')
        p += +1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m')
if p == 2:
    print('{} É PRIMO'.format(n))
else:
    print('{} NÃO É PRIMO'.format(n))
