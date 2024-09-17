fname = "C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Progresso\\Coursera\\04_modulo\\mbox-short.txt"

nova_lista = list()

with open(fname, 'r', encoding='utf-8') as arquivo:
    for line in arquivo:
        line = line.rstrip()
        if line.startswith('From '):
            email = line.split()
            # print(email)
            nova_lista.append(email[1])
            # print(nova_lista)
for emails in nova_lista:
    print(emails)

count = len(nova_lista)
print("There were", count, "lines in the file with From as the first word")

    # for emails in nova_lista:
    #     users = emails[5 : -25]
    #     print(users)

# count = len(nova_lista)
# print("There were", count, "lines in the file with From as the first word")


# nova_lista = list()

# with open(fname, 'r') as arquivo:
#     for line in arquivo:
#         line = line.rstrip()  # Remove espaços em branco à direita
#         if line.startswith('From '):
#             palavras = line.split()  # Quebra a linha em palavras
#             nova_lista.append(palavras[1])  # Adiciona o segundo item da linha (email)

# # Imprime todos os endereços de e-mail
# for email in nova_lista:
#     print(email)

# # Imprime a contagem total de linhas processadas
# count = len(nova_lista)
# print(f"There were {count} lines in the file with From as the first word.")

