# Faça um programa que leia largula
# e a altura de uma parede em metros.
# Calculea a sua área e a quantidade
# de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta
# uma área de 2m².

alt = float(input('Altura: '))
lar = float(input('Largura: '))

area = alt * lar
tinta = area / 2

print('A area da parede é de {}²m, '
      '\n e você deverá usar {:.1f} litros de tinta.'
      .format(area, tinta))

