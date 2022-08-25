'''Cire um programa que leia uma frase qualquer
e diga se ela é um PALINDROMO, desconsiderando
os espaços'''

frase = str(input('Escreva uma frase: ')).strip().upper()
c = frase.split()
frasejunta = ''.join(c)
inverso = ''
inverso = frasejunta[::-1]
'''for letra in range(len(frasejunta) -1, -1, -1):
    inverso += frasejunta[letra]'''
if inverso != frasejunta:
    print('A frase: {} não é um Palíndromo, pois'.format(frase))
    print('{} é diferente de {}'.format(frasejunta, inverso))
else:
    print('A frase: {} é um Palíndromo, pois'.format(frase))
    print('{} é igual a {}'.format(frasejunta, inverso))
