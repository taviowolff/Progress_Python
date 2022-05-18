"""
Formatando valores com modificadores
:s - Texto (strings)
:d - Inteiros(int)
:f - Numeros de ponto flutuante (float)
:. (numero)f - quantidade de casa decimais (float)
: (caractere) (> ou < ou ^)(quantidade)(tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
print(f'{num2:0<10}')
print(f'{num2:0<5}')
print(f'{num2:0<2}')
print(f'{num2:0<1}')

nome = 'Otavio'

print(nome.lower()) # tudo minusculo
print(nome.title()) # toda palavra começa com letra maiuscula
print(nome.upper()) # toda maiuscula

print(f'{nome:#^10}')
print(f'{nome:#<10}')
print(f'{nome:#>10}')


