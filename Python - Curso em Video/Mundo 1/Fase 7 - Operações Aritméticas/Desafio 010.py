# Crie um programa que leia quanto
# dinheiro uma pessoa tem na carteira
# e mostre quantos dolares ela pode comprar.

money = float(input('Quanto dinheiro você tem: R$'))

usd = 1
brl = 5.45

total = money / 5.45

print('Você pode comprar US${:.2f}'.format(total))
