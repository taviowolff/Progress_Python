import json

pessoa = {
    'nome':'Otávio Wolff',
    'sobrenome':'Buffon',
    'enderecos': [ 
        {'rua' : 'R1', 'numero' : 32},
        {'rua' : 'R2', 'numero' : 55},
    ],
    'altura' : 1.8,
    'numeros_preferidos' : (2, 4, 8, 10),
    'dev' : True,
    'nada' : None,
}

# with open('aula87.json', 'w', encoding='UTF8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo, 
#         ensure_ascii=False,
#         indent=2,
#         )

with open('aula87.json', 'r', encoding='UTF8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    print(type(pessoa['nome']))
    # print(type(pessoa))