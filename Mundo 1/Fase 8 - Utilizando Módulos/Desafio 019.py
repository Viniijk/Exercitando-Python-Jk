import random

#um professor que sortear um dos alunos
# para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome deles e
# escrevendo o nome do escolhido.

num = random.randint(1, 5)
print('{}'.format(num))

if num == 1:
    print('Leonardo da Silva')
if num == 2:
    print('Cristiano Ronaldo')
if num == 3:
    print('Neymar Jr.')
if num == 4:
    print('Leonel Messi')
if num == 5:
    print('Pedro Alvarez Cabral')