'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- o nome com todas as letras maisculas e minusculas.
- Quantas letras ao todo (sem considerar espaços.)
- Qauntos letras tem o primeiro nome'''

nome = input('Digite seu Nome Completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

#split transforma a string NOME em uma LISTA ['Vinicius' 'Cunha' 'Borges']
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
