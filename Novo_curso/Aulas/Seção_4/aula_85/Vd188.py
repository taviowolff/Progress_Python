# Criando arquivos com Python
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


caminho_arquivo = 'C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Aulas\\Seção_4\\aula_85\\'
caminho_arquivo += 'aula85.txt'

# with open (caminho_arquivo, 'w') as arquivo:
#     print('abriu')

with open(caminho_arquivo, 'a', encoding='UTF8') as arquivo:
    arquivo.write('Atenção\n') 
    # toda vez que o programa rodar essa linha será escrita

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())