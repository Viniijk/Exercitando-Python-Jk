from datetime import date
'''Faça um programa que leia um ano
qualquer e moste se ele é bissexto'''

ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano de {} é BISSEXTO'.format(ano))
else:
    print('O Ano de {} NÃO é Bissexto'.format(ano))