# Array em python  
# Estruturas de dados que armazenam uma coleçao de elementos, mas diferem
# um pouco das listas. Enquanto listas podem conter dados de tipos variados,
# arrays tradicionais em Python, geralmente suportam um único tipo de dado.
# Em python, arrays não são uma estrutra nativa como em outras linguagens,
# mas há várias maneiras de trabalhar com eles.abs


## 1 Usando lista para arrays

# lista = [1,2,3,4,5] # observe que há apenas um tipo de dado nessa lista
# print(lista)

## 2 Importando da biblioteca Array

# import array

# # Criação de um array de inteiros

# arr = array.array('i',[1,2,3,4,5])
# # print(arr)

# for i in arr:
#     print(i)
# print()
# print(arr[2])


## Arrays com Numpy
# biblioteca ideal para manipulaçao numérica e cientifica. Arrays em Numpy são mais rápidos e têm ampla variedade de funções para calculo

# import numpy as np

# #criação de array

# np_array = np.array([1,2,3,4,5])

# for i in np_array:
#     print(i)