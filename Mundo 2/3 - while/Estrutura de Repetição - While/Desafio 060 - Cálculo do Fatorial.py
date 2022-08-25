from math import factorial
'''Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5x4x3x2x1=120'''
n1 = 1
print('>>> Eu sou a Calculadora Vegas de Fatorial <<<')
print('-' * 46)
print('Para fechar o programa Digite 0')
while n1 != 0:
    n1 = int(input('Digite um número para saber seu Factorial: '))
    print('Fatorial de {} é = {}'.format(n1, factorial(n1)))
    print('Para fechar o programa Digite 0')
    print('=' * 40)