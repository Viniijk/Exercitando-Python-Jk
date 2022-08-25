'''Crie um programa que leia varios numeros inteiros
pelo teclado. O Prograama só vai aprar quando o usuario
digitar o valor 999, que é a condição de parada. No final, mostre
qquantos numeros foram digitados e qual foi a soma entre eles
(descondiderando o flag)'''

cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para sair): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'O Total de valores inseridos foram {cont}, e a soma total é {soma}')
