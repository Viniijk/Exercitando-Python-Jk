''''Faça um prograam que leia o
nome completo de uma pessoa,
mostrando em seguida o priomeiro e
ultimo nome separadamente.
'''

n = str(input('Qual é o seu nome? ')).strip()

print('Prazer em te conhecer!')

nome = n.split()
print(nome)
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu ultimo nome é {}'.format(nome[len(nome)-1 ]))
