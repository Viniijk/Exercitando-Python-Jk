from random import randint
from time import sleep
'''Crie um programa que faça o computador jogar Jokenpô com você'''

lista = [0, 1, 2]
m = randint(1, 3)
print('\033[1;34;40m-=-\033[m' * 20)
print('\033[1;34;40m    EU SOU A VEGAS, SUA INTELIGÊNCIA ARTIFICAL FAVORITA     \033[m\n\033[1;34;40m                   VAMOS JOGAR JOKENPÔ?                     \033[m')
print('\033[1;34;40m                       ESTÁ PRONTO?                         \033[m')
print('\033[1;34;40m-=-\033[m' * 20)
sleep(0.7)
#nome = str(input('\033[31m                   Qual seu nome campeão?\n:::                 \033[m'))
#print(m)
sleep(0.5)
escolha = int(input(' Digite (1) para Pedra \n Digite (2) para Papel \n Digite (3) para Tesoura \n :::     '))
#PEDRA(1) PAPEL(2) TESOURA(3)

print('\033[34mProcessando...')
sleep(1.3)
if escolha == 1 and escolha + m == 4:
    print('Vegas -> \033[36mTESOURA\033[m VS PEDRA <- VOCÊ')
    print('\033[33;40mParabéns, Você ganhou.\033[m')
elif escolha == 2 and escolha + m == 3:
    print('Vegas -> \033[36mPEDRA\033[m VS PAPEL <- VOCÊ')
    print('\033[33;40mParabéns, Você ganhou.\033[m')
elif escolha == 3 and escolha + m == 5:
    print('Vegas -> \033[36mTESOURA\033[m VS PAPEL <- VOCÊ')
    print('\033[33;40mParabéns, Você Venceu!!!\033[m')
elif escolha == m:
    print('\033[32;40mOBJETOS IGUAIS, TENTE NOVAMENTE\033[m')
elif escolha == 1 and escolha - m <= 0:
    print('Vegas -> \033[36mPAPEL\033[m VS PEDRA <- VOCÊ')
    print('\033[34:40mParabéns pra mim, EU GANHEI e Você PERDEU.\033[m')
elif escolha == 2 and escolha - m <= 0:
    print('Vegas -> \033[36mTESOURA\033[m VS PAPEL <- VOCÊ')
    print('\033[34:40mParabéns pra mim, EU GANHEI e você PERDEU\033[m')
elif escolha == 3 and escolha - m == 2:
    print('Vegas -> \033[36mPEDRA\033[m VS TESOURA <- VOCÊ')
    print('\033[34:40mParabéns pra mim, EU GANHEI e VOCÊ PERDEU hahaha!!!\033[m')
sleep(1)
print('\033[34:40mObrigado por jogar comigo, vamos jogar de novo?\033[m')
