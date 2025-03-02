#Faça um programa que leia o
# comprimento do cateto oposto
# e do cateto adjacente de um
# traingulo retangulo, calcule e mostre
# o comprimeiro da hipotenusa.

cateto = float(input('Cateto Oposto: '))
cateto2 = float(input('Cateto Adjacente: '))

hipotenusa = (cateto ** 2 + cateto2 ** 2) ** (1/2)

print('O Comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))
