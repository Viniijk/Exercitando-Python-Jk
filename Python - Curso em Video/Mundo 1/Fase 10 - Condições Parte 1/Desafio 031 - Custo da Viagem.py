'''Desenvolva um programa que pergunte
 a distancia de uma viagem em KM.
 Calcule o preço da passagem. cobando
 R$0.50 por KM para viagens de até 200km
 e 0.45 para viagens mais longas.'''

km = int(input('Qual a distancia da viagem?'))

if km <= 200:
    passagem = km * 0.5
    print('Preço da passagem é: R${}'.format(passagem))
else:
    passagem_longa = km * 0.45
    print('Preço da Passagem é: R${}'.format(passagem_longa))
