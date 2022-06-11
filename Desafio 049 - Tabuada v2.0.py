'''Refaça o DESAFIO 009, mostrando a tabuada
de um numero que o usuario escolher,
só que agora o utilizando um laço for'''

print('{:-^40}'.format(' TABUADA '))
num = int(input('Digite um número: '))
for c in range(1, 11):
    r = num * c
    print(f'{num} X {c} = {r}')
print('{:=^40}'.format(' FIM '))