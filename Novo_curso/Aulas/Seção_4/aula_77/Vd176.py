from functools import partial
from types import GeneratorType

def dobrar(numero):
    return numero * 2


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# quadrados = list(map(lambda n: n ** 2, numeros))

# print(quadrados)


dobrados = list(map(dobrar, numeros))
print(dobrados)
