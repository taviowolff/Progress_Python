fname = "C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Progresso\\Coursera\\04_modulo\\romeo.txt"

words_list = list()

with open(fname, 'r') as arquivo:
    for line in arquivo:
        # Dividir cada linha em uma lista de palavras
        words = line.split()
        
        # Iterar sobre as palavras e verificar se já estão na lista
        for word in words:
            if word not in words_list:
                words_list.append(word)

# Ordenando a lista de palavras
words_list.sort()

# Imprimindo o resultado
print(words_list)


        
