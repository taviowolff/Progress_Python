# Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest 
# number of mail messages. 
# The program looks for 'From ' lines 
# and takes the second word of those lines as the 
# person who sent the mail. The program creates a 
# Python dictionary that maps the sender's 
# mail address to a count of the number 
# of times they appear in the file. After the 
# dictionary is produced, the program reads
# through the dictionary using a maximum 
# loop to find the most prolific committer.

name = 'C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Progresso\\Coursera\\05_modulo\\mbox-short.txt'
# name += 'mbox-short.txt'

lista_emails = list()
counts = dict()

with open(name, 'r', encoding='UTF-8') as arquivo: 
    for lines in arquivo:
        if 'From:' in lines:
            email = lines.split()
            lista_emails.append(email[1])


for email in lista_emails:
    counts[email] = counts.get(email,0) + 1

mais_envia = max(counts, key=counts.get)  # Encontra o email com o maior número de envios
quantidade = counts[mais_envia]           # Recupera a quantidade associada a esse email

print(f'{mais_envia} {quantidade}')

# maior_envio = max(counts.values()) # Essa forma de buscar o email e a quantidade é falha
# quem_enviou = counts[maior_envio]  # Pois o dicionário não pode ser acessado desta maneira
# print(f'{quem_enviou} {maior_envio}') # Porque a chave é o email e não a quantidade associada a ele
