import os
lista = []
while True:
    resp = input('Deseja listar[l], remover[r], adicionar[a], sair[s]: ')
    if resp == 'l':
        print(lista)
    elif resp == 'r':
        os.system('cls')
        for item, indice in enumerate(lista):
            print(item, indice)
        try:
            rmv = int(input('Escolha o número do item da lista que deseja remover: '))
            lista.pop(rmv)
            os.system('cls')    
        except IndexError:
            os.system('cls')
            print('Errou, escolha um número que há na lista')
            continue
        except ValueError:
            os.system('cls')
            print('Errou, escolha apenas números na lista')
            continue         
    elif resp == 'a':
        os.system('cls')
        add = input('Adicionar: ')
        lista.append(add)
        os.system('cls')
        print(lista)
    elif resp == 's':
        if len(lista) == 0:
            os.system('cls')
            print('Processo encerrado sem lista')
            break
        else:
            os.system('cls')
            print(f'Sua lista é\n{lista}')
            break
            