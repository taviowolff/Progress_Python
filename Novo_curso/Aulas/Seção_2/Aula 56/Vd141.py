# dicionario = {
#     'produto': 'Caneta-preta',
#     'valor': 2.50,
#     'marca': 'BIC'
# }

# dc = {
#     chave.upper(): valor
#     if isinstance(chave, str) else chave
#     for chave, valor 
#     in dicionario.items()
#     # if chave == 'valor'   
# }

# lista = [
#     ('a', 'valor a'),
#     ('b', 'valor b'),
#     ('c', 'valor c')
# ]

# dc1 = {
#     chave: valor
#     for chave, valor in lista
# }

# print(dc1)

set = {x**2 for x in range(11)}

print(set)

# lista = list(range(11))

# lista_elevada_ao_quadrado = [item**0 for item in lista]

# set = set(lista_elevada_ao_quadrado)

# print(set)