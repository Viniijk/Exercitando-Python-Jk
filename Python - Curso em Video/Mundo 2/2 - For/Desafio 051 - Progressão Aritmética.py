'''Desenvolva um programa que leia o
primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão'''

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
a = p
decimo = p + (10 - 1) * r
print(p)
for c in range(p, decimo + r, r):
    a = a + r
    print('{}'.format(c), end=' -> ')
print('FIM')
