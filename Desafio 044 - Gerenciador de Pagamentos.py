from time import sleep
'''Elabore um programa que calcule
o valor a ser pago por um produto,
considerando o seu preço normal e condição
de pagamento:
'''

print('\033[34m{:=^40}'.format(' LOJAS VEGAS '))

preco = float(input('Qual preço do produto? '))
sleep(0.3)
print('Qual será a forma de pagamento?')
print('''Forma de Pagamento
[ 1 ] Á vista 
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
condicao = int(input('Qual opção::: '))

if condicao == 1:
    preco = preco - (preco * 0.1)
    print('Parabéns você ganhou 10% de desconto. \n TOTAL R${}'.format(preco))
    print('OBRIGADO POR COMPRAR COM A VÊNUS, SUA INTELIGÊNCIA ARTIFICIAL FAVORITA!!!')
elif condicao == 2:
    preco = preco - (preco * 0.05)
    print('Parabéns, você conseguiu 5% de desconto na sua compra. \n TOTAL R${}'.format(preco))
    print('OBRIGADO POR COMPRAR COM A VÊNUS, SUA INTELIGÊNCIA ARTIFICIAL FAVORITA!!!')
elif condicao == 3:
    preco /= 2
    print('Sua compra ficou no TOTAL R${}'.format(preco))
    print('OBRIGADO POR COMPRAR COM A VÊNUS, SUA INTELIGÊNCIA ARTIFICIAL FAVORITA!!!')
elif condicao == 4:
    pp = int(input('Com acréscimo de juros de 20% mensais \nEm quantas parcelas: '))
    preco = preco + (preco * 0.2)
    parcela = preco / pp
    print('Sua compra ficou no TOTAL R${} com parcelas mensais de R${}'.format(preco, parcela))
    print('OBRIGADO POR COMPRAR COM A VÊNUS, SUA INTELIGÊNCIA ARTIFICIAL FAVORITA!!!')

else:
    print('\033[1;32mOpção invalida de Pagamento\033[m')