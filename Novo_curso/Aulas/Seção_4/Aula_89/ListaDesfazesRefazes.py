import os

# Exercício - Lista de tarefas com defazer e fazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café','caminhar'] -> Adicionar caminhar 
# desfazer = ['fazer café'] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar','fazer café'] 
# refazer = todo ['fazer café']
# refazer = todo ['fazer café','caminhar']

def limpar_tela():
    # Comando para limpar a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_tarefa(tarefa, tarefas):
    tarefa.append(tarefas)
    print(f"A tarefa {tarefa} adionada")

def apagar_tarefa(tarefas, indice):
    if 0 <= indice <= len(tarefas):
        tarefa = tarefas.pop(indice)
        print(f"Tarefa '{tarefa}' removida.")

    else:
        print(f'índice inválido. Nada apagado.')

def desfazer_acao(tarefas, historico):
    if historico:
        ultima_acao, tarefa = historico.pop()
        if ultima_acao == "adicionar":
            tarefas.remove(tarefa)
            print(f"Desfazer: Tarefa '{tarefa}' removida.")
        elif ultima_acao == "apagar":
            tarefas.append(tarefa)
            print(f"Desfazer: tarefa '{tarefa}' restaurada.")
        else:
            print('Nada desfeito.')

def mostrar_tarefas(tarefas):
    if tarefas:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i}. {tarefa}")
    else:
        print("A lista de tarefas está vazia.")

def main():
    tarefas = []
    historico = []

    while True:
        limpar_tela()
        mostrar_tarefas(tarefas)

        print("\nComandos:")
        print("1 - Adicionar Tarefa")
        print("2 - Apagar Tarefa")
        print("3 - Desfazer Ação")
        print("4 - Limpar Tela")
        print("5 - Sair")

        comando = input("\nEscolha um comando: ")
        
        
        if comando == '1':
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefas, tarefa)
            historico.append(("adicionar", tarefa))
        elif comando == '2':
            try:
                indice = int(input("Digite o índice da tarefa a ser apagada: "))
                tarefa_apagada = tarefas[indice]
                apagar_tarefa(tarefas, indice)
                historico.append(("apagar", tarefa_apagada))
            except (ValueError, IndexError):
                print("Índice inválido.")
        elif comando == '3':
            desfazer_acao(tarefas, historico)
        elif comando == '4':
            limpar_tela()
        elif comando == '5':
            break
        else:
            print("Comando inválido.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
