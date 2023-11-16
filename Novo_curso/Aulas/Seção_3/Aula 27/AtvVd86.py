'''
Exercício
Exiba os índices da lista
'''

lista = ['Otávio', 'Wolff', 'Buffon']

lista.append('Dárius')

indices = range(len(lista)) 


for indice in indices:
    print(indice, lista[indice])
    