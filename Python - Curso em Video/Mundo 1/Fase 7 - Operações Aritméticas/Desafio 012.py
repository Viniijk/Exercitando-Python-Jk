#Faça um algoritmo que leia o preço
#de um produto e mostre seu novo preço,
#com 5% de desconto.

preco = float(input('Preço do Produto: R$'))

desconto = preco - (preco * 0.05)

print(f'Novo Preço com desconto: {desconto:.2f}')
