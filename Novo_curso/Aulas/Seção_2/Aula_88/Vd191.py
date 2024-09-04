
#  Maneira não recomendade de se fazer uma função com parâmetros mutáveis.
# def adiciona_clientes(nome, lista = []):
#     lista.append(nome)
#     return lista

# cliente1 = adiciona_clientes('Luiz')
# adiciona_clientes('Joana', cliente1)
# print(cliente1)

# output: ['Luiz', 'Joana']

# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Maria', cliente2)
# print(cliente2)

# output: ['Luiz', 'Joana', 'Helena', 'Maria']

# A forma correta de se usar parâmetros mutáveis
def adiciona_clientes(nome, lista = None):
    if lista is None: 
        lista = []
    lista.append(nome)
    return lista

lista1 = []
cliente1 = adiciona_clientes('Luiz', lista1)
adiciona_clientes('Joana', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
print(cliente2)

cliente3 = adiciona_clientes('Coraline')
adiciona_clientes('Bernardo', cliente3)
cliente3.append('Daisy')
print(cliente3)