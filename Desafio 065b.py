resp = 'S'
soma = quantidade = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}'.format(quantidade, media))
print('O Maior número é {} e o menor é {}'.format(maior, menor))