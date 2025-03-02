'''Crie um programa que tenha um tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagrem de preços, organizando os dados em forma tabular.
'''

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'livro', 34.90)
print('_' * 41)
print('{:^41}'.format('LISTAGEM DE PREÇOS'))
print('-' * 41)
print('{:.<30}'.format(lista[0]), 'R$ ', '{: >5}'.format(lista[1]))
print('{:.<30}'.format(lista[2]), 'R$ ', '{: >5}'.format(lista[3]))
print('{:.<30}'.format(lista[4]), 'R$ ', '{: >5}'.format(lista[5]))
print('{:.<30}'.format(lista[6]), 'R$ ', '{: >5}'.format(lista[7]))
print('{:.<30}'.format(lista[8]), 'R$ ', '{: >5}'.format(lista[9]))
print('{:.<30}'.format(lista[10]), 'R$ ', '{: >5}'.format(lista[11]))
print('{:.<30}'.format(lista[12]), 'R$ ', '{: >5}'.format(lista[13]))
print('{:.<30}'.format(lista[14]), 'R$ ', '{: >5}'.format(lista[15]))
print('{:.<30}'.format(lista[16]), 'R$ ', '{: >5}'.format(lista[17]))
print('_' * 41)
