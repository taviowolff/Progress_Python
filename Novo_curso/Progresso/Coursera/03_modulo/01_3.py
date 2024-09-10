

arquivo_caminho = 'C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\01_3.txt'
with open(arquivo_caminho, 'r') as arquivo:
    # count = 0
    # for numero in arquivo:
    #     count = count + 1
    # print(count) # uma forma de contar linhas em python

    linhas = arquivo.readlines()

    # print(len(linhas)) # outra forma de ler as linhas

    print(linhas[0:9]) # aqui vai ler o que tem dentro de cada linha. 
    #['1\n', '\n', '2\n', '\n', '3\n', '\n', '4\n', '\n', '5\n']

    # for numero in linhas:
    #     if numero.startswith('3'):
    #         print(f'achei o número 3 {numero}') # uma forma de achar um número dentro do arquivo'


    for linha in linhas:
        linha = linha.rstrip()
        print(linha)


    