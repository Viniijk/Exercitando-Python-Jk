#Crie um algoritmo que leia um numero
# e mostre o seu dobro. triplo e raiz
#quadrada.

n = int(input('Digite um número'))

d = n * 2
t = n * 3
r = n ** (1/2)

print('Numero {}, seu Dobro é {}'
      ' \n seu triplo é {}'
      ' \n e sua Raiz Quadrada é {:.2f}'
      .format(n, d, t, r))
