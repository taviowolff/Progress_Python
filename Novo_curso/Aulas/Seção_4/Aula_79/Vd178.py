# reduce - faz a redução de uma lista para um único valor
from functools import reduce

produtos = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 55.55},
    {'nome': 'p3', 'preco': 5.59},
    {'nome': 'p4', 'preco': 22},
    {'nome': 'p5', 'preco': 81},
]

def funcao_do_reduce(acumulador, produto):
    print(acumulador)
    print(produto)
    print()
    return 1

total = reduce(
    funcao_do_reduce,
    produtos,
    0
)




# total = 0

# for p in produtos:
#     total += p['preco']


# print(f'Total: {total}')