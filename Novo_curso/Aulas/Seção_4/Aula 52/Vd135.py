# empacotamento e desempacotamento 
a, b = 1, 2
a, b = b, a
# print(a,b)

pessoa = {
    'nome': 'Otávio',
    'Sobrebome': 'Wolff'
}

# desempacotando os argumentos
(a1, a2), (b1, b2) = pessoa.items()

# print(a1)
# print(b1,b2)

dados_pessoa = {
    'idade' : 16,
    'altura' : 1.71
}

dados_completos = {**pessoa, **dados_pessoa}

print(dados_completos)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não Nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome = 'Miguel', idade= 22)
