'''Desenvolva um programa que leia seis
numeros inteiro e mostre a soma apenas daqueles
que forem pares. Se o vallr digitado for ímpar,
desconsidere-o'''

print('Digite 6 números abaixo')
s = 0
con = 0
for c in range(1, 7):
    n = int(input('Digite o {}º Número: '.format(c)))
    if n % 2 == 0:
        s += n
        con += 1
print('{} Números são pares e a soma deles é: {}'.format(con, s))
