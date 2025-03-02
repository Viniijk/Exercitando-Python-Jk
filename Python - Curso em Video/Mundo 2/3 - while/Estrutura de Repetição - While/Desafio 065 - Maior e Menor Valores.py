'''Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução,
mostre a media entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.'''

n = 0
valor = 1
soma = 0
maior = 0
menor = 0
parar = 1
while parar != 0:
    n += 1
    valor = int(input(f'Digite o {n}ª Valor: '))
    if n >= 2:
        parar = int(input('Para continuar [ 1 ] | Para Parar [ 0 ]::: '))
    soma += valor
    if n == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
media = soma / n
print('=' * 50)
print(f'A Soma total é [{soma}], e A Média é [{media:.2f}]')
print(f'O Maior número digitado é [{maior}] e o Menor é [{menor}]')
print('=' * 50)
