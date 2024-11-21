# Uma lista é uma estrutura de dados que permite armazenar uma coleção de elementos.

# Exemplos de listas:

lista = [1, 2, 3, 4, 5]

lista2 = ['a', 'b', 'c', 'd', 'e']

lista3 = [1, 2.2, 'a', 'Otávio']

print(type(lista)) # retorna o tipo da variavel

for a in lista3: # retorna todos os itens da lista
    print(a)

print(lista2[1]) # retorna um item específico da lista

print(len(lista)) # retorna o tamanho da lista

# lista são mutáveis e podem ser alteradas

lista[2] = 'Buffon' # altera o item especifico da lista

print(lista)

lista.append('Dárius') # adiciona um item ao final da lista

print(lista)

lista.insert(1, 'Otávio') # insere um item na lista na posicao especificada

print(lista)

lista4 = lista2 + lista3 # concatena as listas

print(lista4)

# lista.sort() # ordena a lista

# print(lista) # TypeError: '<' not supported between instances of 'str' and 'int'