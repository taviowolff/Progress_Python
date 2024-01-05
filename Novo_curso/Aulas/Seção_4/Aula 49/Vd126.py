# Sets - Cib hybtis em Python (tipo set)
# conjuntos são ensinados na matemática 
# link de página de conjuntos
# Resentados graficamente pelo diagrama de Venn
# sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# criando um set
# set(interável) ou {1, 2, 3}
s1 = set('Otávio')
print(f'{type(s1)} {s1}')

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índexes;
# - eles não garantem ordem; 
# - eles são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard 

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# defiferença simétrica ^ - Itens que não estão em ambos