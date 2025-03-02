'''Escreva um programa que pergunte
o salario de um funcionario e
calcule o valor do seu aumento.
- PARA salario superiores a 1250, calcule
um aumento de 10%
 - PARA os inferiores ou iguais, o aumentoé de 15%'''

sal = float(input('Digite seu Salário: '))
if sal > 1250:
    sal1 = sal * 0.1
    print('Seu Aumento de salário é de R$ {}. Totalizando R${}'.format(sal1, sal+sal1))
else:
    sal2 = sal * 0.15
    print('Seu aumento de salario é de R$ {}. Totalizando R${}'.format(sal2, sal+sal2))
