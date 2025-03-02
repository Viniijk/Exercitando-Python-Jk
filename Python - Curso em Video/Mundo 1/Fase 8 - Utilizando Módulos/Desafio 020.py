import random

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

lista = [a1, a2, a3, a4]

sorteio1 = random.choice(lista)
sorteio2 = random.choice(lista)
sorteio3 = random.choice(lista)
sorteio4 = random.choice(lista)

print('O Aluno sorteado foi: {} \nO Segundo Sorteado foi: {} \nO Terceiro Sorteado foi: {} \nO Ultimo Sorteado foi: {}'.format(sorteio1, sorteio2, sorteio3, sorteio4))
