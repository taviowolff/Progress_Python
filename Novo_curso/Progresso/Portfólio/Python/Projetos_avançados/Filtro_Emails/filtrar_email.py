fname = # caminho ou nome de arquivo

nova_lista = list()

with open(fname, 'r', encoding='utf-8') as arquivo:
    for line in arquivo:
        line = line.rstrip()
        if line.startswith('From '): # Filtra da lista as linhas que começam com From (de quem enviou)
            email = line.split()
            nova_lista.append(email[1])
for emails in nova_lista:
    print(emails)

count = len(nova_lista)
print("Há", count, "linhas que contém emails do destinatário.")