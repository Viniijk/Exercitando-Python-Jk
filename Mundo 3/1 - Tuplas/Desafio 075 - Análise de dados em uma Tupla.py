'''Desenvolva um programa que leia quatro valores do teclado e guarde-os em um tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro 3.
C) Quais foram os numeros pares'''

n1= int(input('Digite um Valor: '))
n2 = int(input('Digite mais um Valor: '))
n3 = int(input('Digite outro Valor: '))
n4 = int(input('Digite o ultimo Valor: '))
nove = tres = par = jota = 0
lista = (n1, n2, n3, n4)
print(lista)
if 9 in lista:
    nove += 1
for c in range(0, len(lista)):
    if lista[c] == 3:
        tres = c + 1
    if lista[c] % 2 == 0:
        par = len(lista[c])
print(f'O Valor 9 apareceu {nove} vezes.')
print(f'O Valor 3 apareceu na {tres}º posição')
print(f'Os Números pares na lista são {par}')
