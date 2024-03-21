import copy
from dados import produtos
# copy, sorted, produtor.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunta)

# Ordene os produtos por preco crescene (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


# novos_produtos = copy.deepcopy(produtos) # criação da shallow copy
# novos_produtos = produtos.copy()
# print(novos_produtos,type(novos_produtos))

# for produto in novos_produtos:
#     preco = produto['preco']
#     conta = preco * 1.10
#     # produto['preco'].append(conta) Sei lá oque eu tentei aqui
#     print(f'{conta:.2f}')

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} 
    for p in copy.deepcopy(produtos)
    ]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')


produtos_ordenados_por_nome = sorted(
    produtos,
    key=lambda p: p['nome']
)


print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')



