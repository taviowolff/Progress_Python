"""
Fatiamento de strings 
- lembre-se que strings são iteráveis 
- elas são separadas por índices e eles podem ser manipulados

ex:
 0 1 2 3 4 5 6 7
 O l á m u n d o
-8-7-6-5-4-3-2-1

começando a partir do índice 0 se positivo 
e finalizando no índice -1 se negativo
- Isso serve para achar a palavra requisitada com coordenadas 

ex: 
texto = 'Olá mundo'
cortar_meio = texto[4:]
"""

# texto = "Olá mundo"
# cortar_meio_pra_frente = texto[4:]
# print(cortar_meio_pra_frente)


# texto = "Olá mundo"
# cortar_meio_pra_tras = texto[:4]
# print(cortar_meio_pra_tras)



"""
função len
- de uma certa maneira funciona como uma maneira de verficar a quantidade de
elementos dentro de um objeto 
- como também em 
listas 
tuplas 
strings
dicionários 
conjuntos
"""

# string
texto = 'olá mundo'
print(len(texto)) # retorna 9 (preste bem atenção pois ' ' espaços contam)

# lsita
lista = (1, 2, 3, 4, 5)
print(len(lista)) # retorna 5 pois é a quantidade de objetos na lista 

# tupla
tupla = ['olá', 'mundo', 1, 2, 3]
print(len(tupla)) # retorna 5 pois é a quantidade de objetos na tupla 

# dicionário
dicionario = {'a':1, 'b':2, 'c':3}
print(len(dicionario)) # retorna 3 pois é a quantidade de pares chave-valor é 3

# conjuntos
conjunto = {1, 2, 3, 4, 5}
print(len(conjunto)) # retorna 5, pois o conjunto só apresenta 5 elementos.