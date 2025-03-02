import math

#Crie um programa que leia um numero
# Real qualquer pelo teclado e mostre
# na tela a sua porção inteira.

# Ex: Digite um umero: 6.127
# O numero 6.127 tem a parte inteira 6.


num = float(input('Digite um Número Real: '))

print('O Número real tem a parte inteira {}'.format(math.trunc(num)))
