# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

# # Criando um dicionário vazio
# meu_dicionario = {}

# # Pedindo ao usuário para adicionar itens
# while True:
#     chave = input("Digite uma chave (ou 'sair' para parar): ")
    
#     # Verificando se o usuário quer sair
#     if chave.lower() == 'sair':
#         break
    
#     valor = input(f'Digite um valor para {chave}: ')
    
#     # Adicionando a chave e o valor ao dicionário
#     meu_dicionario[chave] = valor

# # Mostrando o dicionário final
# print("Dicionário Final:", meu_dicionario)

# # Criando um dicionário de pessoas
# pessoas = {}

# while True:
#     nome = input("Digite o nome (ou 'sair' para parar): ")
    
#     # Verificando se o usuário quer sair
#     if nome.lower() == 'sair':
#         break
    
#     sobrenome = input("Digite o sobrenome: ")
#     idade = input("Digite a idade: ")
#     endereco = input("Digite o endereço: ")

#     # Criando o dicionário da pessoa
#     pessoa = {
#         'nome': nome,
#         'sobrenome': sobrenome,
#         'idade': idade,
#         'endereco': endereco
#     }

#     # Adicionando a pessoa ao dicionário de pessoas
#     pessoas[nome] = pessoa

# # Mostrando o dicionário final de pessoas
# print("\nDicionário Final de Pessoas:")
# for nome, info in pessoas.items():
#     print(f"\nInformações de {nome}:")
#     for chave, valor in info.items():
#         print(f"{chave}: {valor}")

