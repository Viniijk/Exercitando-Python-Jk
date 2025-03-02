n = int(input('Digite um Valor: '))
f = 1
for c in range(n, 0, -1,):
    f *= c
    c -= 1
print('Fatorial de {} é = {}'.format(n, f))