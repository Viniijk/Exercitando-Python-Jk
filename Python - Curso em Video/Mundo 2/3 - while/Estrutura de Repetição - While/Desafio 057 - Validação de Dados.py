'''Faça um programa que leia o sexo de uma  pessoa,
 mas so aceite os valores M ou F. Caso esteja errado,
 peça a digitação novamente até ter um valor correto.'''

sexo = 'P'
cont = 1
while sexo != 'M' or 'F':
    sexo = str(input('Digite seu Sexo [M/F]: ')).strip().upper()
    if sexo in 'MF':
        print('{} sexo Registrado, seu sexo é {}'.format(cont, sexo))
        cont += 1
    else:
       print('Por Favor, Digite um comando valido. [M/F]')
