''' 
Faça um programa que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
'''

produto = float(input('Valor do produto: '))

desconto = produto - (produto * 0.05)

print(f'O valor do produto foi de R${produto:.2f} para R${desconto:.2f} com 5% de desconto.')