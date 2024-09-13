import json
from Ex206_a import caminho_arquivo, Pessoa, fazer_dump

with open(caminho_arquivo, 'r') as arquivo:
    pessoas = json.load(arquivo)

    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    p4 = Pessoa(**pessoas[3])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
    print(p4.nome, p4.idade)
