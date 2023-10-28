"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3   4   5
# lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
# lista.append(50)
# lista.pop(0)
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)
# print(lista, 'Removido,', ultimo_valor)

# print(len(lista))

# lista2 = [10,20,30,40,50,60,70,80,90] # Definição da lista2

# lista2.append(100) # append adiciona objeto ao final da lista 

# print(lista2)

# print(lista2.index(30)) # esse index ele retorna na lista a posição que o tal objeto está na lista 

# lista2.insert(3, 33) # insere um objeto de acordo com a localização ao índice determinado (índice, objeto)

# print(lista2)

# lista2.pop(2) # pop ele exclui o objeto a partir do seu índice 

# print(lista2)

# lista3 = [1,2,3,4,5,6,7,8,9] # Definição da lista3

# lista2.extend(lista3) # retorna a união das duas listas com a lista inserida dentro do objeito aparecendo nos índices finais

# lista2.sort() # retorna com a organização dos objetos da lista em ordem crescente para números e ordem alfabética para strings

# print(lista2)

'''
Concatenação de listase extensão Video 82
'''
# lista_a = [1,2,3,4]
# lista_b = [5,6,7,8]

# lista_c = lista_a + lista_b

# print(lista_c)
# print(lista_a)

# lista_a.extend(lista_b)
# print(lista_a)


'''
deletanta um objeto da lista
'''

lista_h = [1,2,3,4]

del lista_h[-1]
