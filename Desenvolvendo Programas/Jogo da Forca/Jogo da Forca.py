'''
Listas
'''

import csv
import random

# Função para ler palavras do arquivo CSV
def carregar_palavras_csv(arquivo):
    with open(arquivo, mode='r', encoding='utf-8') as file:
        leitor = csv.reader(file)
        palavras = [linha[0] for linha in leitor]  # Assumindo uma palavra por linha
    return palavras

# Função para escolher uma palavra aleatória da lista
def escolher_palavra_aleatoria(palavras):
    return random.choice(palavras)

# Carregar palavras do arquivo CSV
palavras = carregar_palavras_csv('palavras.csv')

# Escolher uma palavra aleatória
palavra_secreta = escolher_palavra_aleatoria(palavras)
print(f'A palavra secreta é: {palavra_secreta}')

digitadas = []
letras_erradas = []


# Inicia o laço de repetição

print('Bem vindo ao Vênus Forca')
chances = int(input('Digite quantas chances quer ter no jogo: '))


while True:
    if chances <= 0:    # Verifica quantas chances existem
        print('Você perdeu!!!')
        print(f'A Palavra era {palavra_secreta}')
        break

    letra = str(input('Digite uma Letra: ')).strip().lower()    # Entrada str do usuario
    if len(letra) > 1 or letra in '123456789':  # Verifica se o usuario enviou apenas UMA letra e sem números.
        print('Digite apenas UMA letra')
        continue

    # Adiciona a letra enviada do usuario em uma nova lista
    digitadas.append(letra)
    letras_erradas.append(letra)

    if letra in palavra_secreta:    # Verificando se letra está correta
        print(f' A letra {letra} existe na palavra secreta')
        letras_erradas.pop()  # excluindo se estiver correta
    else:
        print(f' A letra {letra} não existe')
        digitadas.pop()  # e excluindo se estiver incorreta

    #   Onde acontece a comparação da variavel secreta com as letras de entrada do usuario
    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '-'


    if secreto_temporario == palavra_secreta:
        print(f'Parabéns, você GANHOOOU!!!!! A Palavra era {secreto_temporario}')
        break
    else:
        print(f'A forca está assim: {secreto_temporario}')

    if letra not in palavra_secreta:
        chances -= 1
    print(f'Você ainda tem {chances} chances')
    print(f'Letras erradas ja digitadas: {letras_erradas}')


'''
Explicação: Linha 58 à 64 | Onde acontece a verificação da palavra secreta

secreto_temporario = '':
Aqui, é criada uma variável chamada secreto_temporario que começa como uma string vazia. 
Essa variável vai ser preenchida com a letra secreta ou com o símbolo *, dependendo de se a letra foi ou não adivinhada.

for letra_secreta in secreto::
Esse for percorre cada letra da palavra secreta, que está armazenada na variável secreto. 
A cada iteração do loop, a variável letra_secreta recebe o valor de uma letra da palavra secreta.

if letra_secreta in digitadas::
Essa linha verifica se a letra da palavra secreta (letra_secreta) já foi adivinhada pelo jogador. 
A variável digitadas é uma lista ou conjunto que contém todas as letras que o jogador já tentou adivinhar até o momento.
Se a letra já foi digitada (ou seja, se ela está em digitadas), o programa entra na condição if.

secreto_temporario += letra_secreta:
Se a letra foi adivinhada corretamente, ela é adicionada à string secreto_temporario, 
que está construindo a versão visível da palavra secreta para o jogador.
Por exemplo, se o jogador acertou a letra 'a' e a palavra secreta era "banana", 
o secreto_temporario pode ficar assim: b*a*a**.

else::
Se a letra não foi adivinhada (ou seja, se ela não está na lista digitadas), o programa entra na condição else.

secreto_temporario += '*':
Caso a letra não tenha sido adivinhada, em vez de mostrar a letra verdadeira, o programa coloca um * no lugar da letra. 
Isso é o que é mostrado ao jogador, representando as letras ainda não adivinhadas.

Exemplo de como funciona:
Imagina que a palavra secreta é "banana" e o jogador já adivinhou as letras 'a' e 'b'. O código iria gerar o seguinte:

secreto = 'banana'
digitadas = ['a', 'b']
Aqui está o que aconteceria durante o loop:

Na primeira iteração, letra_secreta será 'b', e como 'b' está em digitadas, ela será adicionada ao secreto_temporario, resultando em: b
Na segunda iteração, letra_secreta será 'a', e como 'a' está em digitadas, ela será adicionada ao secreto_temporario, resultando em: ba
Na terceira iteração, letra_secreta será 'n', e como 'n' não está em digitadas, será adicionado *, resultando em: ba*
Na quarta iteração, letra_secreta será novamente 'a', e como 'a' está em digitadas, ela será adicionada ao secreto_temporario, resultando em: ba*a
E assim por diante, até que a string final seja: **ba*a** (ou seja, as letras que o jogador adivinhou e * para as não adivinhadas).
Resultado final:
O valor de secreto_temporario depois de todo o loop será uma string onde as letras adivinhadas são visíveis, 
e as não adivinhadas são substituídas por asteriscos (*). O objetivo é mostrar ao jogador o progresso no jogo de forca.
'''
