"""
quandidade de caracteres 
len = o len vai basicamente contar a String e retornar um Inteiro
"""
"""
usuario = input('digite o nome de usuario: ')
qtd_carac =  len(usuario)
print(usuario, qtd_carac, type(qtd_carac))
"""
usuario = input('Coloque um nome de cadastro para usario: ')
qtd_permitido = len(usuario)  # aqui eu mostro a voce como utilizar 
print(qtd_permitido)

if qtd_permitido >= 6:
    print('voce foi cadastrado')
else:
    print('tente novamente')