'''Escreva um programa para aprovar
o emprestimo bancario para a acompra
de uma casa. O programa vai perguntar
o valor da casa, o salario do comprador
e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal,
sabendo que ela nao pode exceder 30% do salario
ou entao o emprestimo será negado.'''

print('-=-' * 27)
print('Olá, eu sou a IA Vegas, e irei te ajudar a aprovar seu financiamento imobiliario')
print('-=-' * 27)

valor = float(input('Qual o preço do Imovel? '))
salario = float(input('Qual sua renda mensal? '))
ano = int(input('Em quantos anos pretende pagar? '))

parcela = salario * 0.3
financiamento = valor / (ano * 12)

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, ano), end='')
print(' A Prestação será de R${:.2f}'.format(financiamento))
if financiamento <= parcela:
    print('Parabéns, Crédito APROVADO!.')
    print('Você pagará parcelas de R${} mensais.'.format(parcela))
else:
    print('Crédito REPROVADO!')
