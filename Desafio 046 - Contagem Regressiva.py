from time import sleep

'''Faça um rpograma que mostre na tela uma 
contagem regressiva para o estouro de fogos de 
artificios, indo de 10 até 0, com uma pausa
 de 1 segundo entre eles.'''

for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('FIM')