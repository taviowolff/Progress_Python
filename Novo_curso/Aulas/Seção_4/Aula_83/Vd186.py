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

caminho_arquivo = 'C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Aulas\\Seção_4\\Aula_83\\'
caminho_arquivo += 'aula83teste.txt'
print(caminho_arquivo)

# arquivo = open(caminho_arquivo, 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Aulas\\Seção_4\\Aula_83\\aula83.txt'


# arquivo = open(caminho_arquivo, 'w')
# arquivo.close() # Sempre que abrir um arquivo feche-o

with open(caminho_arquivo, 'w') as arquivo:
    print("olá, mundo!")
    print('Arquivo vai ser fechado')