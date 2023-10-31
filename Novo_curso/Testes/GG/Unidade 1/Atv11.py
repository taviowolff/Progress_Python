'''
Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
'''

larg = float(input('Qual é largura da parede? '))

alt = float(input('Qual é a altura da parede? '))

m2 = larg * alt

tinta = m2 / 2

print(f'Você vai precisar de {tinta} litros de tinta para pintar sua parede')