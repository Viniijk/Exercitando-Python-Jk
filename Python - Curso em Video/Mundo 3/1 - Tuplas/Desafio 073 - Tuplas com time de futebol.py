'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense'''

tabela = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo')
#print(tabela)
print('=' * 60)
print('{:^60}'.format('TABELA BRASILEIRÃO'))
print('=' * 60)
print(f'OS Primeiros 5 colocados são {tabela[0:5]}')
print('=' * 60)
print(f'Os Ultimos 4 Colocados são {tabela[16:]}')
print('=' * 60)
print(f'Lista em Ordem Alfabética {sorted(tabela)}')
print('=' * 60)
for c in range(0, len(tabela)):
    if tabela[c] == 'Palmeiras':
        print(f'Palmeiras está em {c+1}º Colocação na Tabela')
        break
print('{:=^60}'.format(' FIM '))
