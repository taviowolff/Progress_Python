import math

# Erros comuns em Python

# 1. SyntaxError (Erro de Sintaxe)
# Ocorre quando o código não segue as regras gramaticais da linguagem.
# Exemplo: falta de dois pontos, parênteses não fechados, palavras-chave mal escritas.

# print("Olá, mundo!" # Falta fechar o parêntese
# if True # Falta os dois pontos

# 2. NameError (Erro de Nome)
# Ocorre quando você tenta usar uma variável ou função que não foi definida.

# print(variavel_nao_definida)
# minha_funcao_inexistente()

# 3. TypeError (Erro de Tipo)
# Ocorre quando uma operação é aplicada a um tipo de dado inadequado.

# print("10" + 5) # Não é possível concatenar string com int diretamente
# len(123) # len() não funciona com inteiros

# 4. IndexError (Erro de Índice)
# Ocorre quando você tenta acessar um índice que está fora dos limites de uma lista, tupla ou string.

# lista = [1, 2, 3]
# print(lista[3]) # O índice 3 não existe (vai de 0 a 2)

# 5. KeyError (Erro de Chave)
# Ocorre quando você tenta acessar uma chave que não existe em um dicionário.

# dicionario = {"nome": "João", "idade": 30}
# print(dicionario["cidade"]) # A chave "cidade" não existe

# 6. ZeroDivisionError (Erro de Divisão por Zero)
# Ocorre quando você tenta dividir um número por zero.

# resultado = 10 / 0

# 7. ValueError (Erro de Valor)
# Ocorre quando uma função recebe um argumento de tipo correto, mas com um valor inadequado.

# int("abc") # "abc" não pode ser convertido para inteiro
# import math
# math.sqrt(-1) # Não é possível calcular a raiz quadrada de um número negativo real

# 8. AttributeError (Erro de Atributo)
# Ocorre quando você tenta acessar um atributo ou método que não existe em um objeto.

# texto = "Olá"
# texto.append(" mundo") # Strings não têm

# E.1
# não é possível atribuir a um literal
# 17 = n


# E.2
# é possível atribuição de valores em múltiplas variáveis em python
# x = y = 1

# print(x)
# print(y)

# E.2.1 
# Atribuição com Tuplas
# a,b,c = 10,20,30
# print(a)
# print(b)
# print(c)

# x = 10
# y = 5

# x,y = y,x
# print(x)
# print(y)

# E.3
# É possível utilizar ; em python porém é desnecessário, até não recomendado. Servindo com o propósito de separar comando em um mesma linha exemplo x = 10;
# x = 10;y = 5;x,y = y,x;print(x);print(y)

# E.4
# Não dá para colocar um ponto final no final de um comando 
# x = 10
# y = 5

# x,y = y,x
# print(x)
# invalid syntax
# print(y).

# E.5
# Ao tentar importar libs com nomes errados o retorno é 
# ModuleNotFoundError: No module named 'maath'

pi = math.pi

print(pi)