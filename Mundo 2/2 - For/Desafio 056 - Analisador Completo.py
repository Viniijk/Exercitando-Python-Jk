'''Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.'''

idade = 0
cont = 0
maior = 0
soma = 0
for c in range(1, 5):
    nome = str(input('Nome da {}º Pessoa: '.format(c)))
    idade = int(input('Idade da {}º Pessoa: '.format(c)))
    print('''Sexo da {}º Pessoa:
        [ 1 ] Para Masculino
        [ 2 ] Para Feminino'''.format(c))
    sexo = int(input('::: '))
    soma += idade
    media = soma/4
    if sexo == 2 and idade < 20:
            cont += +1
    if sexo == 1:
        if idade > maior:
            maior = idade
            nom = nome
    else:
            nom = 'Não tem Homem na Lista'

print('A idade média do grupo é {:.1f}.'.format(media))
print('Nome do Homem mais velho: {}.'.format(nom))
print('{} Mulheres menores de 20 anos compõe o grupo.'.format(cont))

