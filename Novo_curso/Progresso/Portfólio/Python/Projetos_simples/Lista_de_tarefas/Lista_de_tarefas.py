""" Lista de tarefas criada em 2024/03/04
    Atualizado dia 2024/03/05               """

import os
from time import sleep

tarefas = []

while True:
    criar_lista = input('Deseja criar uma lista? s/n: ')

    while criar_lista == 's':
        escolha = input('Deseja [1]adicionar, [2]mostrar, [3]deletar, [4]finalizar a lista? ')
        
        if escolha == '1':
            os.system('cls')
            item = input('Adicionar tarefa: ')
            tarefas.append(item)
            print('Item adicionado com sucesso!')
            sleep(2)

        elif escolha == '2':
            os.system('cls')
            for tarefa in tarefas:
                print(tarefa)
            sleep(5)
            os.system('cls')

        elif escolha == '3':
            for indice, tarefa in enumerate(tarefas):
                print(f'{indice}:{tarefa}')    
           
            deletar = input('Escolha o índice para deletar: ')
            if deletar.isdigit():
                num = int(deletar)
                try:
                    del tarefas[num]

                except IndexError:
                    print('índice inválido')
            else:
                print('Escolha um número')

            # try:
            #     del tarefas[index]
            # except IndexError:
            #     print('Não tem esse índice na lista')
            # except ValueError:
            #     # if index.isalpha():
            #     print('Escolha um número como índice')
            #     # else:
            #     #     continue
            sleep(2)
            os.system('cls')

        elif escolha == '4':
            for tarefa in tarefas:
                print(tarefa)
            print('Sua lista final')    
            break

        else:
            print('Escolheu número errado')
    # else:
    #     criar_lista = input('Deseja retornar a lista? s/n: ')
      
    #     if criar_lista == 's':
    #         pass  
    #     else:
    #         print('Você não criou a lista')
    #         sleep(2)
    #         os.system('cls')
    #         break
        
