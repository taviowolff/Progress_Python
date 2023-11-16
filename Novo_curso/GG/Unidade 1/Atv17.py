'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. 
'''

cat_op = float(input('Qual é o cateto oposto: '))

cat_ad = float(input('Qual é o cateto adjacente: '))

hip = (cat_op**2) + (cat_ad**2)

hip = hip**(0.5)

print(f'A hipotensa é {hip}')