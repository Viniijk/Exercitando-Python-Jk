from datetime import date

'''Faça um programa que leia o ano de 
nascimento de um jovem e informe, de acordo 
com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se ja passou do tempo do alistamento.
- Se ja passou do tempo do alistamento.
Seu programa tam´bem deverá mostrar o tempo
 que falta ou que passou do prazo'''

print('Olá, eu sou a Vegas, sua IA Favorita')
print('''Diga-me, Seu Gênero? 
[ 1 ] Masculino
[ 2 ] Feminino''')
opcao = int(input('::: '))

if opcao == 2:
    print('Você não precisa fazer o Alistamento Militar Obrigatório.')
elif opcao >= 3:
    print('Digito Incorreto')

ano = int(input('Digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - ano

if idade < 18:
    n = idade - 18
    print(f'Você ainda vai se alista em {idade - 18} anos. Se prepare.')
elif idade == 18:
    print('Hoje é seu momento, aliste-se e venha fazer parte do Exército Brasileiro')
else:
    a = idade - 18
    print('Passou {} anos que você deveria ter se alistado. O prazo passou.'.format(a))
    b = atual - a
    print('Ano de Alistamento {}'.format(b))
