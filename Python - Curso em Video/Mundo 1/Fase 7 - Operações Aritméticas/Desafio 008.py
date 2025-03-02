#Escreva um programa que leia um valor
#em metros e o exiba convertido em
#centimetros e milimetros.

metros = float(input('Digite valor em metros: '))
km = (metros / 1000)
c = (metros * 100)
m = (c * 10)
print('Em Metros {} \nEm Centimetros {}'.format(metros, c))
print('Em Milimetros {} '.format(m))
print('Em Quilomêtros {}'.format(km))