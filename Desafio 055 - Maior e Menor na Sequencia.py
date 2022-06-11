'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''

maior = 0
menor = 1000

for c in range(1, 6):
    peso = float(input('O Peso da {}º Pessoa é: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O Menor peso é {}kg \nO Maior peso é {}kg'.format(menor, maior))
