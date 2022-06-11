from datetime import date

'''A confederação nacional de natação precisa de
um programa que leia o ano de nascimento de um atleta
e msotre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima MASTER'''
atual = date.today().year
nascimento = int(input('Ano de Nascimento do Atleta: '))
idade = atual - nascimento

if idade <= 9:
    print('O Atleta tem {} anos.'.format(idade))
    print('Parabéns, Seja Bem-Vindo a Clube MIRIM')
elif idade <=14:
    print('O Atleta tem {} anos.'.format(idade))
    print('Parabéns Criança, seja Bem Vindo ao Clube INFANTIL')
elif idade <=19:
    print('O Atleta tem {} anos'.format(idade))
    print('Seja Bem Vindo Jovem ao sub JUNIOR')
elif idade >=20:
    print('O Atleta tem {} anos.'.format(idade))
    print('Seja muito bem recebido aos SÊNIOR')
else:
    print('O Atleta tem {} anos.'.format(idade))
    print('Você se tornou um MASTER, comemore')
