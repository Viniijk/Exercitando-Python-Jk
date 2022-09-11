from random import randint
''''Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
Depois disso mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla
'''
lista = tuple(randint(i + 1, 9) for i in range(randint(1, 5)))
print(lista)

maior = menor = 0
for c in lista:
    if c == 1:
        maior = c
        menor = c
    if maior > lista:
        maior = lista
    if menor < lista:
        menor = lista
print(f'O Menor valor da lista é {menor}, e o maior valor é {maior}')

