# filter é um filtro funcional que retorna um iterável com os elementos que passam por um teste

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

produtos = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 55.55},
    {'nome': 'p3', 'preco': 5.59},
    {'nome': 'p4', 'preco': 22},
]

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]

novos_produtos = filter(
    lambda p: p['preco'] > 10 and p['preco'] < 50,
    produtos
)

print_iter(produtos)

print_iter(novos_produtos)