'''Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução,
mostre a media entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.'''
n = 0
valor = 1
soma = 0
maior = 0
menor = 0
first = int(input('Quantos valores irá inserir?::: '))
while n != first:
    n += 1
    valor = int(input(f'Digite o {n}ª Valor: '))
    soma += valor
    if n == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor


media = soma / first
print('=' * 50)
print(f'A Soma total é [{soma}], e A Média é [{media:.2f}]')
print(f'O Maior número digitado é [{maior}] e o Menor é [{menor}]')
print('=' * 50)