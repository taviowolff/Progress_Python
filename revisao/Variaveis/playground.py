print ("HELLO, WORLD!")

## Variável é um nome que aponta para um valor na memório
# idade, por exemplo, pode ser um variável
# variáveis pordem ter valores atribuídos.
# são mutáveis em momento x pode ser = 20 em outros x pode ser = 50

# idade = 27
# print(idade) # 27

# # podem ter valore reatribuídos também, exemplo abaixo:
# idade = idade + 1 # garante que o valor atribuído anteriormente some com + 1
# print(idade) # 28

## Tipos de dados que são manipuláveis.
# int - inteiros
print(type(1))
# números inteiros como 1, 10, 12315. Números que não tem casas após a vírgula, ou não apresentam víngula.

# float - números
print(type(1.0))
# número que aprensetam ponto 1.1, 120.24 e por ai vai

# Texto(Strin)
print(type('Otávio'))
# textos que são seguidos por '' simples ou "" duplas.

# Booleano(True/False)
print(type(True))
# valores que retornam True ou False, bom para construção de lógicas de sistemas.

# Listas
numeros = [1, 2, 3]
print(type(numeros))
# forma para consultar valor de listas
print(numeros[0])
# valores em listas começam por 0

# Dicionários
pessoa = {"nome": "Otávio",
          "idadde": 27}
print(type(pessoa))
# forma para consultar o valor de dados de um dicionário
print(pessoa["nome"])