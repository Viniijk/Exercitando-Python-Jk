'''Faça um programa que calcule a soma
entre todos os números impares que são multiplos
de tres e que se encontram no intervalo
 de 1 até 500'''

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'Soma de todos os {cont} valores multiplos \nde três em um intervalo de 1 ~ 500 é ({s})')
print('{:=^50}'.format(' FIM '))
