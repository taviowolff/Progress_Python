"Lista de tarefas criada em 2024/03/04"

import os
from time import sleep

tarefas = []

while True:
    criar_lista = input('Deseja criar uma lista? s/n: ')

    while criar_lista == 's':
            escolha = input('Deseja [1]adicionar, [2]mostrar, [3]deletar, [4]finalizar da lista? ')
           
            if escolha == '1':
                os.system('cls')
                item = input('Adicionar tarefa: ')
                tarefas.append(item)
                print('Item adicionado com sucesso!')
                sleep(2)

            elif escolha == '2':
                for tarefa in tarefas:
                    print(tarefa)
                sleep(5)
                os.system('cls')

            elif escolha == '3':
                for indice, tarefa in enumerate(tarefas):
                    print(f'{indice}:{tarefa}')    
                deletar = int(input('Escolha o indece para deletar: '))
                try:
                    del tarefas[deletar]
                except IndexError:
                    print('não tem esse indice na lista')
                sleep(2)
                os.system('cls')

            elif escolha == '4':
                for tarefa in tarefas:
                    print(tarefa)
                print('Sua lista final')    
                break

            else:
                print('Escolheu número errado')
