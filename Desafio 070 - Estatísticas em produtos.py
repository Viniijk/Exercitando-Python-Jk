'''Crie um programa que leia o nome eo preço de varios produtos. o programa deverá perguntar se o usuario vaic ontinuar. No final, mostre
A) Qual é o TOTAL gasto na compra.
B) Quantos produtos custam mais de R$1000,00
C) Qual é o nome do produto mais BARATO.'''
soma = maior = menor = cont = precoalto = 0
menornome = ''
print('='*40)
print('{:^12}MERCADO BARATÃO'.format(''))
print('='*40)
while True:
    cont += 1
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: '))
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar not in 'SN':
        print('COMANDO ERRADO, TENTE NVOAMENTE')
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    print('_' * 40)
    soma += preco
    if cont == 1:
        maior = preco
        menor = preco
        menornome = nome
    else:
        if preco > maior:
            maior = preco
        if preco < menor:
            menor = preco
            menornome = nome
    if preco > 1000:
        precoalto += 1
    if continuar == 'N':
        break
print('=' * 40)
print(f'''   Total gasto foi de R${soma}
   {precoalto} Produtos custam mais de R$1000,00
   O Produto mais barato foi {menornome} de {menor}''')
print('='*40)


