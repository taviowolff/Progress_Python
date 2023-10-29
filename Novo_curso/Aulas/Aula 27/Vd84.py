'''
cuidados com dados mutáveis 
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''

# nome = 'Otávio'
# outro_nome = nome
# nome = 'Wolff'

# print(nome)
# print(outro_nome)

lista_a = ['Otávio', 'Wolff', 1, True, 1.2] # essas linhas fazem para que a mesma variável apontem para o mesmo valor
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)