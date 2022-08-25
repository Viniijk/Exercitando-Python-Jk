from time import sleep

'''Desenvolva uma lógica que leia o
peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo de Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 A 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

print('\033[1;34;40m-=-' * 20, '\033[m')
print('\033[1;34;40m' ' ' 'Olá, eu sou a Vênus, sua Inteligência Artificial Favorita', ' ', '\033[m')
print('\033[1;34;40m' ' ' * 16, 'Digite seus números abaixo', ' ' * 16, '\033[m')
print('\033[1;34;40m-=-' * 20, '\033[m')
peso = float(input('Digite seu Peso (kg): '))
altura = float(input('Digite sua Altura em Metros: '))

IMC = peso / (altura * altura)
print('Processando...')
sleep(3)
if IMC < 18.5:
    print('SEU IMC É {:.2f} - ABAIXO DO PESO'.format(IMC))
elif IMC <= 25:
    print('SEU IMC É {:.2f} - PESO IDEAL'.format(IMC))
    print('\033[33mPARABÉNS, CONTINUE EM FORMA\033[m')
elif IMC <= 30:
    print('SEU IMC É {:.2f} - SOBREPESO'.format(IMC))
elif IMC <= 40:
    print('SEU IMC É {:.2f} - OBESIDADE'.format(IMC))
else:
    print('SEU IMC É {:.2f} - OBESIDADE MÓRBIDA')
print('Obrigado por usar nossa calculadora IMC')