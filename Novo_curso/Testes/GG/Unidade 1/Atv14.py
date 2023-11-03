'''
Escreva um programa que converta uma temperatura digitada em 
Graus C e converta para Graus F

(0 °C × 9/5) + 32 = 32 °F
'''

c = float(input('Quantos graus Celsius está fazendo? '))

f = 32 + (c * (9/5))

print(f'A temperatura em farenheit é {f}')