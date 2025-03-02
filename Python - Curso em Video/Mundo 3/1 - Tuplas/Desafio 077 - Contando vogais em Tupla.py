'''Crie um programa que tenha um tupla com varias palavras (nao usar acentos).
Deppois disso voce deve mostrar para cada palavra, quais sao as suas vogais.
'''
aprender = ''
lista = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
for c in range(0, len(lista)):
    if lista[c] in 'AEIOU':
        aprender = ' '
print(lista)
print(f'Na palavra {lista[0].upper()} temos {aprender}')