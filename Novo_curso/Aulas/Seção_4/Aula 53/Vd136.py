"""
list comprehension
é basicamente um for dentro de uma lista
"""
# lista1 = []
# for n in range(10):
#     lista1.append(n)
    
# print(lista1)


# lista = [numero for numero in range(10)]

# print(lista)


# quadrados = [x**2 for x in range(1,6)]
# print(quadrados)

# numeros_pares = [x for x in range(10) if x % 2 == 0]
# print(numeros_pares)

# palavra = 'Python'
# caracteres = [letra for letra in palavra]
# print(caracteres)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
diagonal = [linha[i] for i, linha in enumerate(matriz)]
print(diagonal)