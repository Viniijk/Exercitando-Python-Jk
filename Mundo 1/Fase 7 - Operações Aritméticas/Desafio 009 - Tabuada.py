# Faça um programa que leia
# um numero inteiro qualquer
# e mostre na tela a sua taboada.

n = int(input())

t1 = n * 1
t2 = n * 2
t3 = n * 3
t4 = n * 4
t5 = n * 5
t6 = n * 6
t7 = n * 7
t8 = n * 8
t9 = n * 9

print('-' * 12)
print('A Tabuada do', n, 'é')
print("\n {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {}"
      " \n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {}"
      "\n {} x 7 = {} \n {} x 8 = {} \n {} x 9 = {}"
      .format(n, t1, n, t2, n, t3, n, t4, n, t5, n, t6, n, t7, n, t8, n, t9))
print('-' * 12)
