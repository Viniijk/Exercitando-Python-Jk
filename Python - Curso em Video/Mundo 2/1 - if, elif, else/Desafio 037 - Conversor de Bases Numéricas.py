from time import sleep

'''Escreva um programa que leia um numero inteiro
qualquer e peça para o  usuario escolher
qual será a base de conversão:
 - 1 BINARIO
 - 2 OCTAL
 - 3 HEXADECIMAL'''

print('-=-' * 15)
print('\033[1;34;40mOlá, eu sou a Vegas, a IA que irá te ajudar\033[m')
print('-=-' * 15)
n = int(input('\033[4mDigite um número que queira converter: \033[m'))
print('Ok...')
sleep(1)
m = int(input('Digite 1 para BINÁRIO: \nDigite 2 para OCTAL: \nDigite 3 para HEXADECIMAL: '))

if m == 1:
    binario = bin(n)
    print('{} em Bínario é {}'.format(m, binario[2::]))
elif m == 2:
    octal = oct(n)
    print('{} em Octal é {}'.format(m, octal[2::]))
elif m == 3:
    hexadecimal = hex(n)
    print('{} em Hexadecimal é {}'.format(m, hexadecimal[2::]))
else:
    print('Opção Invalida')
