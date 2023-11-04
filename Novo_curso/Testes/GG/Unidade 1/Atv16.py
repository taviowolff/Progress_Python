from math import trunc
'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela 
a sua porção Inteira.
'''

# Há duas maneiras que podemos fazer isso.

num = float(input('Escreva um valor: '))

print(f'O valor que vc digitou foi {num} e  sua parte inteiro é {trunc(num)}')
# Ou 

# num = 6.172

# num_int = int(num) # seria convertendo o número float para int que mostraria ele em Inteiro

# print(num_int)



