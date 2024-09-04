# palavra = 'banana'

# i = 0

# Aqui temos a forma mais simplificada de se iterar em uma variável com o laço FOR
# for letra in palavra:
#     print(letra)

# Aqui temos a forma de se iterar com o laço WHILE
# while i < len(palavra):
#     print(palavra[i])
#     i += 1


# def ler_srt(*args):
#     if not args == str:

#         try:
#             args = [str(arg) for arg in args] # Converte todos os argumentos para string

#             for i in args:
#                 print(i, end='\n') # Imprime cada item com separador

#         except TypeError:
#             print('Dado inválido')

def ler_srt(*args):
    for arg in args:
        if isinstance(arg, str):  # Verifica se o argumento é uma string
            for char in arg:
                print(char, end='\n')  # Itera sobre cada caractere da string
        else:
            print(arg, end='\n')  # Imprime diretamente se não for uma string

    # for i in args:
    #     print(i, end='\n') # Imprime cada item com separador

x = (1,254,3,4,'Colher')
ler_srt(*x) # Desempacotando os valores
ler_srt(1,2,3,4,'Colher')

# ler_srt('carne')
# ler_srt(1)
# ler_srt('cinema')

print(type(x[0]))
print(type(x[-1]))