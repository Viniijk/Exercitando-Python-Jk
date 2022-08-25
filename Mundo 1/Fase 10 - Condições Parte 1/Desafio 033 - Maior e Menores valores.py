'''Faça um programa que leia três
numeros e mostre qual é o maior e
qual é o menor.'''

a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite um terceiro número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('MENOR número é {}'.format(menor))
print('Maior número é {}'.format(maior))
