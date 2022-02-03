"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área
e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta
uma área de 2m²
"""
larg = float(input('Digite a largura em metros: '))
alt = float(input('Digite a altura em metros: '))
area = larg * alt
tinta = area / 2

print('Sua parede tem uma dimensão de {} x {} e sua área é de {}m²'.format(larg, alt, area))
print('Para pintar sua parede, você precisará de {} litros de tinta'.format(tinta))

#Este paragrafo foi modificado pelo github deskop
