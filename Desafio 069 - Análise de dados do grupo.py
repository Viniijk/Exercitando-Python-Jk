'''Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuario quer ou não continuar. no final mostre:
A - quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados.
C - Quantas mulheres tem menos de 20 anos.'''
homem = mulher = maior = 0
while True:
    print('=' * 45)
    print('{:^12}CADASTRE UMA PESSOA'.format(''))
    print('=' * 45)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo not in 'MF':
        print('-'*12, '| ENTRADA ERRADO |', '-'*13)
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F] ')).upper().strip()
    continuar = str(input('Quer Continuar? [S/N] ')).upper().strip()
    if continuar not in 'SN':
        print('-'*6, 'COMANDO ERRADO | Digite [S ou N]', '-'*7)
        while continuar not in 'SN':
            continuar = str(input('::: ')).upper().strip()
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    if idade > 18:
        maior += 1
    if continuar == 'N':
        break
print('=' * 45)
print(f'''        Total maiores de 18: {maior}
        Total de Homens Cadastrados: {homem}
        Total Mulheres menores de 20: {mulher}''')
print('=' * 45)
