import os
from time import sleep
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

caminho_arquivo = 'C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Aulas\\Seção_4\\Aula_86\\'
caminho_arquivo += 'aula86.txt'

with open(caminho_arquivo,'w+', encoding='UTF-8') as arquivo:
    arquivo.write('Esse arquivo será deletado')

sleep(3)

# os.remove(caminho_arquivo)
