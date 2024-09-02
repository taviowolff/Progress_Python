import os
import json

# Fazer um código que crie um arquivo JSON
# Escreva nesse arquivo JSON
# Seja capaz de desfazer e desfazer ações 
# tarefas = [] historico = []
# Adicionar funções de limpar tela, ler o arquivo e salvar o arquivo.










# def limpar_tela():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def adicionar_tarefa(tarefa, tarefas):
#     tarefa.append(tarefas)
#     print(f"A tarefa {tarefa} adionada")

# def apagar_tarefa(tarefas, indice):
#     if not 0 <= indice <= len(tarefas):
#         print(f'índice inválido. Nada apagado.')

#     tarefa = tarefas.pop(indice)
#     print(f"Tarefa '{tarefa}' removida.")

# def desfazer_acao(tarefas, historico):
#     if historico:
#         ultima_acao, tarefa = historico.pop()
#         if ultima_acao == "adicionar":
#             tarefas.remove(tarefa)
#             print(f"Desfazer: Tarefa '{tarefa}' removida.")
#         elif ultima_acao == "apagar":
#             tarefas.append(tarefa)
#             print(f"Desfazer: tarefa '{tarefa}' restaurada.")
#         else:
#             print('Nada desfeito.')

# def mostrar_tarefas(tarefas, caminho_arquivo):
#     dados = []
#     try:
#         with open(caminho_arquivo, 'r', encoding='UTF8') as arquivo:
#             dados = json.load(arquivo)
#     except FileExistsError:
#         print('Arquivo não existe')
#     return dados

# CAMINHO = 'aula195.json'
# tarefas = mostrar_tarefas([], CAMINHO)
# historico = []

# while True:
#     limpar_tela()
#     mostrar_tarefas()

#     print("\nComandos:")
#     print("1 - Adicionar Tarefa")
#     print("2 - Apagar Tarefa")
#     print("3 - Desfazer Ação")
#     print("4 - Limpar Tela")
#     print("5 - Sair e Salvar")

#     comando = input("\nEscolha um comando: ")

#     if comando == '1':
#         tarefa = input("Digite a tarefa: ")
#         adicionar_tarefa(tarefas, tarefa)
#         historico.append(("adicionar", tarefa))
#     elif comando == '2':
#         try:
#             indice = int(input("Digite o índice da tarefa a ser apagada: "))
#             tarefa_apagada = tarefas[indice]
#             apagar_tarefa(tarefas, indice)
#             historico.append(("apagar", tarefa_apagada))
#         except (ValueError, IndexError):
#             print("Índice inválido.")
#     elif comando == '3':
#         desfazer_acao(tarefas, historico)
#     elif comando == '4':
#         limpar_tela()
#     elif comando == '5':
#         dados = tarefas
#         with open(CAMINHO, 'w', encoding='utf8') as arquivo:
#             dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
#             break
#     else:
#         print("Comando inválido.")

#     input("\nPressione Enter para continuar...")

# # if __name__ == "__main__":
# #     main()
