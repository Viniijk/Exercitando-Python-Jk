'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-la por extenso.'''

extenso = ('zero', 'um', 'dois', 'três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
escolha = int(input('Digite um número entre 0 e 20: '))
while escolha > 20 or escolha < 0:
    escolha = int(input('Número Errado | Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[escolha]}')
