# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# get - obtém uma chave

pessoa = {
    'nome' : 'Otávio',
    'idade' : '25',
    'sobrenome' : 'Buffon'
}

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# for valor in pessoa.values():
#     print(valor)
# for chave, valor in pessoa.items():
#     print(chave, valor)

print(len(pessoa))

print(list(pessoa.keys()))
print(tuple(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))