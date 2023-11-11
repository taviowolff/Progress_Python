'''
Faça um programa que leia um ângulo qualquer e mostra na tela o valor do seno, cosseno e
tangente desse ângulo.
'''

# # Solicita ao usuário para inserir o ângulo em graus
# angulo = float(input("Digite o valor do ângulo em graus: "))

# # Converte o ângulo de graus para radianos
# angulo_em_radianos = angulo * (3.14159265359 / 180.0)

# # Calcula o seno, cosseno e tangente do ângulo
# seno = angulo_em_radianos
# cosseno = angulo_em_radianos
# tangente = angulo_em_radianos

# # Exibe os resultados
# print(f"Seno do ângulo: {seno}")
# print(f"Cosseno do ângulo: {cosseno}")
# print(f"Tangente do ângulo: {tangente}")

import math

# Solicita ao usuário para inserir o ângulo em graus
angulo = float(input("Digite o valor do ângulo em graus: "))

# Converte o ângulo de graus para radianos, pois as funções trigonométricas em Python usam radianos
angulo_em_radianos = math.radians(angulo)

# Calcula o seno, cosseno e tangente do ângulo
seno = math.sin(angulo_em_radianos)
cosseno = math.cos(angulo_em_radianos)
tangente = math.tan(angulo_em_radianos)

# Exibe os resultados
print(f"Seno do ângulo: {seno}")
print(f"Cosseno do ângulo: {cosseno}")
print(f"Tangente do ângulo: {tangente}")