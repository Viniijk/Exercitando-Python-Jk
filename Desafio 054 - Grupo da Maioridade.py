from datetime import date
'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas ja sao maiores. *Considere a maioridade a partir dos 21 anos'''

maioridade = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input('Ano de nascimento da {} pessoa: '.format(c)))
    data = atual - ano
    if data >= 21:
        maioridade += 1
    else:
        menor += 1
print('Hoje em {}, {} Pessoas são Maiores de Idade.'.format(atual, maioridade))
print('Hoje em {}, {} Pessoas são Menores de Idade.'.format(atual, menor))

