'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h,
moster uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

carro = float(input('Qual sua velocidade? '))
multa = (carro - 80) * 7

if carro <= 80:
    print('Okay, Prossiga sua viagem')
else:
    print('Você ultrapassou a velocidade, por isso pagará multa de R${}'.format(multa))
