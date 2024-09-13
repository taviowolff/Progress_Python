# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados

import json
import os

caminho_arquivo = "C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Aulas\\Seção_3\\Aula_07\\"
caminho_arquivo += "exercicio.json"

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Jorgina', 32)
p2 = Pessoa('Natalia', 25)
p3 = Pessoa('Jessica', 23)
p4 = Pessoa('Alana', 14)

lista_pessoas = [vars(p1),vars(p2),vars(p3),p4.__dict__]
# criando a lista para extração dss vars(variaveis) e __dict__
# de cada instância

def fazer_dump():
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(lista_pessoas, arquivo, ensure_ascii=False, indent=2)
    # for item in lista_pessoas:
    #     arquivo.writelines(item)