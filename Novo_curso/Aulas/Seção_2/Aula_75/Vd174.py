# Combinations, Permutations e Product - itertools
# combinação - ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa - iterável + tamanho do grupo
# Produto - Ordem importa e repete valores únicos - iterável + tamanho do grupo
from itertools import combinations, permutations, product


def print_iter(iterador):
    print(*list(iterador), sep='\n')

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

camisetas = [
    ['preta', 'branca', 'azul'],
    ['P', 'M', 'G'],
    ['masculina', 'feminina', 'unissex'],
    ['manga longa', 'manga curta']
]

# print('Combinations:')
# print_iter(combinations(pessoas, 2)) # combinação
# print('Permutations:')
# print_iter(permutations(pessoas, 2)) # permutação

print_iter(product(*camisetas)) # produto