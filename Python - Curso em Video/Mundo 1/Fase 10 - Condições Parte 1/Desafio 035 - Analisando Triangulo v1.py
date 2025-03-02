from time import sleep
'''Desenvolva um programa que leia o
comprimento de três retas e diga ao
usuario se elas podem ou não formar um
triangulo.'''

r1 = float(input('Digite o comprimento do primeiro lado: '))
r2 = float(input('Digite o comprimento do segundo lado: '))
r3 = float(input('Digite o comprimento do terceiro lado: '))

print('\033[1;36;40m-=-\033[m' * 20)
print('\033[1;36;40mAnalisador de Triângulos\033[m')
print('\033[1;36;40m-=-\033[m' * 20)

sleep(0.5)
print('Processando...')
sleep(3)
if r1 <  r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar TRIANGULO')
else:
    print('Os segmentos acima NÃO PODEM formar TRIANGULO')
print('--FIM--')
