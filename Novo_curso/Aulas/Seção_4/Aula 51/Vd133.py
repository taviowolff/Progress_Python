# Funçaão lambda em Python
# A função lambda é ma funçao como qualquer outra
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única expressão

lista = [
    {'nome':'Otávio', 'sobrenome': 'Buffon'},
    {'nome':'Jorge', 'sobrenome': 'Yamaguchi'},
    {'nome':'Eduardo', 'sobrenome': 'Tavares'},
    {'nome':'Samuel', 'sobrenome': 'Mingue'},
    {'nome':'Paulo', 'sobrenome': 'Nobre'}
]

# lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['sobrenome'])
l2 = sorted(lista, key=lambda item: item['nome'])

exibir(l1)
exibir(l2)


# for nomes in lista:
#     print
# lista = [123,45,232,65,1,10]
# lista.sort(reverse=False)
# print(lista)