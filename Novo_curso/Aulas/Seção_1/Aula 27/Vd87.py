'''
Introdução ao desempacotamento e empacotamento
'''

# lista = ['Otávio', 'Helena', 'Gabriela']

# nome1, nome2, nome3 = ['Otávio', 'Helena', 'Gabriela'] # pode ser utilizado assim também
# mas isso pode sugerir um erro caso a quantidade de valores e variáveis sejam diferentes


# nome1, nome2, nome3 = lista
# print(nome2)

nome0, *resto = ['Otávio', 'Helena', 'Gabriela']

print(nome0)