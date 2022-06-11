''' Refaça o DESAFIO 35 dos triangulo,
 acrescentando o recurso de mostrar que
  tipo de triangulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno - Todos os lados diferentes'''

n1 = float(input('Digite o comprimento do primeiro lado: '))
n2 = float(input('Digite o comprimento do segundo lado: '))
n3 = float(input('Digite o comprimento do terceiro lado: '))

if n1 == n2 == n3:
    print('Triângulo EQUILÁTERO')
elif n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2 and n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
    print('Triângulo ISÓSCELES')
elif n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Triângulo ESCALENO')
else:
    print('Essas medidas não podem formar um triângulo')