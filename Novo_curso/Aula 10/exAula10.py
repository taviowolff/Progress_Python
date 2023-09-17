# Entendendo as últimas aulas


# in e not in servindo como uma forma de verificação de uma lista 

# lista = ('otávio', '1', '2', '3')
# # tive que pôr os números em formato de string nessa lista pois ainda não sei verificar de maneira que não seja em string

# verificar = input('o que procura? ')

# # Essa linha de comando abaixo só será lida se retornar True
# if verificar in lista:
#     print(f'A lista é {lista}')
#     print(f'{verificar} está na lista')

# else:
#     print(f'O {verificar} não está na lista')


# Ententendo como Hexadecimal funciona 

print(f'O Hexadecimal de 100 é {100:08X}')

# print(f'O Hexadecimal de s é {'s':X}') # maneira errada de tentar descobrir o Hexadecimal de uma letra

# Maneira correta
caractere = 'A'  # Substitua 'A' pela letra que você deseja converter

valor_decimal = ord(caractere)
valor_hexadecimal = hex(valor_decimal)

print(f'O valor hexadecimal de "{caractere}" é: {valor_hexadecimal}')


# Maneira para descobrir um valor Hexadecimal de uma frase
frase = "Olá, Mundo!"  # Substitua pela frase que você deseja converter

hexadecimal = ""
for caractere in frase:
    valor_decimal = ord(caractere)
    hexadecimal += hex(valor_decimal)[2:]  # [2:] remove o prefixo '0x'


print(f'A representação hexadecimal da frase "{frase}" é: {hexadecimal}', end='.')

# Repare que eu utilizei em todos os print o f-string (formated string)
# Uma maneira mais prática e simples de se formatar as strings
# Evitei utilizar a % para formatar, pois acho muito antiquada.