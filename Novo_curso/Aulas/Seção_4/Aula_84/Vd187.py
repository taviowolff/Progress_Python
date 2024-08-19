# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

caminho_arquivo = 'C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Aulas\\Seção_4\\Aula_84\\'
caminho_arquivo += 'aula84.txt'
# Criação do arquivo para essa aula

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n','Linha 4\n'))

    arquivo.seek(0) 
    # garante que o cursor do python inicie na linha zero lendo todo arquivo
    print(arquivo.read())
    # print('Lendo')
    # arquivo.seek(0)
    # print(arquivo.readline(), end='')
    # print(arquivo.readline().strip())

    # print('READLINES')
    # arquivo.seek(0)
    # for linha in arquivo.readlines():
    #     print(linha.strip()) 
        # a função print já vem com um pular linha, usa-se strip para remover isso

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())