'''Fçaa um programa que mostra a tabuada
de varios numeros, um de cada vez, para cada
valor digitado pelo usuario. o programa sera
interrompido quando o numero solicitado for negativo.
'''
cont = multi = 0
print('{:^10}TABUADA v3.0'.format(''))
n = int(input('Quer ver a tabuada de qual valor?: '))
while cont != 10:
    if n < 0:
        break
    cont += 1
    multi = n * cont
    print(f'{n} X {cont} = {multi}')
    if cont == 10:
        print('-' * 40)
        n = int(input('Quer ver a tabuada de qual valor?: '))
        print('-' * 40)
        cont = 0
        continue

print('='*10, 'FIM', '=' * 10)

