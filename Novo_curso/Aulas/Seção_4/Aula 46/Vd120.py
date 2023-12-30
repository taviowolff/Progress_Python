"""
Iterando com dicts
"""

# lista vazia para que os próximos códigos possam iterar sobre ela
pessoa = {}

pessoa['nome'] = 'Otávio'
pessoa['idade'] = 25
pessoa['cidade'] = 'Vitória'

# print(pessoa)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# for chave in pessoa:
#     print(chave)

for valor in pessoa:
    print(pessoa[valor])

print(pessoa['nome'])

pessoa.pop(['nome'])

print(pessoa)

del pessoa['cidade']

print(pessoa)

