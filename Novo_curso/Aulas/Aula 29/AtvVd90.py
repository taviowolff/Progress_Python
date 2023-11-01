''' 
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de íncidices inexistentes na lista.
'''

entrar = input('Vamos criar uma lista?(s/n): ')

lista_base = []

while entrar == 's' :
    
    nova_lista = lista_base

    resp1 = input('Deseja ADICIONAR algo na lista?(s/n): ')
    
    if resp1 == 's':

        add = input('adicionar: ')

        nova_lista.append(add)

        print(f'{add} adicionado a lista com êxito')

        resp1 = input('Deseja ADICIONAR algo na lista?(s/n): ')

    else:    
        print(nova_lista)
        pass


    resp2 = input('Deseja remover algo da lista?')

    if resp2 == 's':

        print(f'Essa é sua lista {nova_lista}')

        # try:
        #     enumerate(lista1)

else:
    print('Sua lista não foi feita')