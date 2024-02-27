import math
# medida_parede = float(input('Quantos metros quadrados de parede serão pintados? '))

# um_litro_tinta = medida_parede / 3

# valor_tintas = 80 * um_litro_tinta

# print(f'Você gastará R${valor_tintas:.2f} para pintar {medida_parede} metros quadrados de parede.')

# Péssima interpretação de leitura minha da atividade

area_parede = float(input('Quantos metros quadrados de parede serão pintados? '))

cobertura_por_lata = 18 * 3

quantidade_de_latas = math.ceil(area_parede/cobertura_por_lata)

preco_lata =  80
preco_total = quantidade_de_latas * preco_lata

print(f'A quantidade de latas necessárias será de {quantidade_de_latas:.2f} gastando R${preco_total:.2f}')

