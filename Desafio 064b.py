num = cont = soma = 0
num = int(input('Digite um número [999 para para]::: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para para]::: '))
print('Você Digitou {} números e a soma entre ele foi {}'.format(cont, soma))
