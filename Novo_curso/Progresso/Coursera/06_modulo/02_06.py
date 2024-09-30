caminho = 'C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Progresso\\Coursera\\06_modulo\\arquivo.txt'

lista = list()
counts = dict()
hora = list()

with open(caminho, 'r', encoding='utf-8') as arquivo:
    for linhas in arquivo:
        if 'From ' in linhas:
            palavras = linhas.split()
            lista.append(palavras[5])

    for tempo in lista:
        hora.append(tempo[0:2])

for tempo in hora:
    counts[tempo] = counts.get(tempo,0) + 1

# lista_tupla = list()
# for key, val in counts.items():
#     nova_tupla = (val, key)
#     lista_tupla.append(nova_tupla)

# lista_tupla = sorted(lista_tupla, reverse=True)

lista_tupla = sorted(counts.items())

for val, key in lista_tupla:
    print(val, key)

