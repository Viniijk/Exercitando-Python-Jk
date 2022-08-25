#Faça um algoritmo que leia o salario
# de um funcionario e mostre sue novo
# salario com 15% de aumento.

salario = float(input('Salario Atual: R$'))

salarionovo = salario + (salario * 0.15)

print(f'Seu novo salario é: R${salarionovo:.2f}')
