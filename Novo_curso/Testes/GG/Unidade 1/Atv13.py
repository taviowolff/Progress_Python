'''
Faça um programa que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento
'''


salario = float(input('Valor do salário: '))

aumento = salario + (salario * 0.15)

print(f'O valor do salário foi de R${salario:.2f} para R${aumento:.2f} com 15% de aumento.')