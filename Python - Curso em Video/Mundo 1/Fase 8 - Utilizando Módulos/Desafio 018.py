from fractions import Fraction


#Faça um progreama que leia um angulo
# qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse angulo.
print('O que deseja calcular? ')
CO = int(input('Digite o valor do cateto OPOSTO: '))
CA = int(input('Digite o valor do outro ADJACENTE: '))
H = int(input('Digite o valor da Hipotenusa: '))

sen = Fraction(CO, H)
cos = Fraction(CA, H)
tan = Fraction(CO, CA)

print('----------')
print('Sen: {}'.format(sen))
print('Con: {}'.format(cos))
print('Tan: {}'.format(tan))
print('----------')
