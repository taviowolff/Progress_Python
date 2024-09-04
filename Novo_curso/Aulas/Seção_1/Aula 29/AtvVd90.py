''' 
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de íncidices inexistentes na lista.
'''

entrar = input('Deseja criar uma lista?(s/n): ')

lista_base = ['cebola', 'alho', 'cloro']

while entrar == 's' :
    adicionar = input('Deseja ADICIONAR algo na lista?(s/n): ')   
  
    while adicionar == 's':
        add = input('adicionar: ')
        lista_base.append(add)
        print(f'{add} adicionado a lista com êxito')
        adicionar = input('Deseja ADICIONAR algo na lista?(s/n): ')
    print(f'Sua lista foi criada\n{lista_base}')

    remover = input(f'Deseja remover algo da lista?(s/n): ')

    while remover == 's':
        for item, indice in enumerate(lista_base):
            print(item, indice)
        try:
            rmv = int(input('Escolha o número do item da lista que deseja remover: '))
            lista_base.pop(rmv)       
        except IndexError:
            print('Erou, escolha um número que há na lista')
            continue
        except ValueError:
            print('Erou, escolha apenas números na lista')
            continue

        remover = input('Deseja remover algo da lista?(s/n): ')
    
    print(f'Sua lista é essa\n{lista_base}')
    entrar = input('Deseja adicionar algo mais?(s/n): ')

if len(lista_base) >= 0:
    print(f'Sua lista é\n{lista_base}')
else:
    print('Operação finalizada com sucesso') 