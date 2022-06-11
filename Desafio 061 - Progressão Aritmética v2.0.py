'''Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e a Razão de um PA,
mostrando os 10 primeiros termos da progressão usando a estrutura WHILE'''

primeiro = int(input('Digite O primeiro termo: '))
razao = int(input('Digite A Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
