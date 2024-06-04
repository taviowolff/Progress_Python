# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 
# 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area_parede = float(input('Informe área da parede a ser pintada: '))

cobertura_por_lata = 18 * 6

cobertura_por_galao = 3.6 * 6

# calcula a quantidade de latas de tinta necessárias
quantidade_de_latas = math.ceil(area_parede/cobertura_por_lata)

# calcula a quantidade de galões de tinta necessárias
quantidade_de_galoes = math.ceil(area_parede/cobertura_por_galao)

# calcula a quantidade de latas ou galões de tinta necessárias
print('Somente latas de 18L:')
print(quantidade_de_latas * 80)
print()
print('Somente galões de 3.6L:')
print(quantidade_de_galoes * 25)
print()

# calcula a quantidade de latas e galões de tinta necessárias
listros_necessarios_folga = (area_parede / 6) * 1.1
quantidade_de_latas_f = listros_necessarios_folga // 18

listros_necessarios_folga_faltando = listros_necessarios_folga - (quantidade_de_latas_f * 18)
quantidade_de_galoes_f = math.ceil(listros_necessarios_folga_faltando / 3.6)

custo_mix = (quantidade_de_latas_f * 80) + (quantidade_de_galoes_f * 25)

print('Misturando latas e galões:')
print(f'o cliente prefica comprar {quantidade_de_galoes_f} latas e {quantidade_de_galoes_f} galões, que custarão {custo_mix}')
