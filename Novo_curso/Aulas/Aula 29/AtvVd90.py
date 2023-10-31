''' 
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de íncidices inexistentes na lista.
'''

print('Vamos criar uma lista?')

while True:
    
    lista_base = []

    resp1 = input('Deseja ADICIONAR algo na lista?(s/n): ')
    
    if resp1 == 's':

        lista1 = lista_base

        add = input('adicionar: ')

        lista1.append(add)

        print(f'{add} adicionado a lista com êxito')

        resp1 = input('Deseja ADICIONAR algo na lista?(s/n): ')

    else:    
        print(lista1)
        pass


    resp2 = input('Deseja remover algo da lista?')

    if resp2 == 's':

        print(f'Essa é sua lista {lista1}')

        # try:
        #     enumerate(lista1)