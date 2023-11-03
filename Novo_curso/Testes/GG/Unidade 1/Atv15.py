'''
Escreva um programa que pergunte a quantidade de Km percorridos por um
carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule
preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado
'''
import os
DIARIA = 60.0
KM = 0.15

dias = float(input('Quantos dias o carro andou? '))

rodado = float(input('Quantos km o carro andou? '))

os.system('cls')

print(f'Voce pagará R${rodado*0.15:.2f} por Km rodado e R${dias*60:.2f} por dias rodados.\nTotalizando: R${(rodado*0.15)+(dias*60):.2f}')