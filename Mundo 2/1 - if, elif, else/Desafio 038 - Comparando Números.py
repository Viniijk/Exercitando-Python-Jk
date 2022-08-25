'''Escreva um programa que leia dois
números inteiros e compare-os, mostrando
 na tela uma mensagem:
 - 1 O primeiro valor é maior
 - 2 O segundo valor pe maior
 - 3 N ão existe valor maior, os dois são iguais'''

n1 = int(input('Digite UM NÚMERO: '))
n2 = int(input('Digite OUTRO NÚMERO: '))

if n1 > n2:
    print('O Primeiro valor é maior')
elif n2 > n1:
    print('O Segundo valor é maior')
else:
    print('Não existe valor maior, Os dois são iguais')
