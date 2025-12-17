# 1. Definição da função (com a palavra-chave 'def')
def nome_da_funcao(parametro1, parametro2):
    """
    Docstring: Uma breve descrição do que a função faz.
    """
    # Corpo da função: Bloco de código com indentação de 4 espaços
    resultado = parametro1 * parametro2
    
    # 2. Retorno (com a palavra-chave 'return')
    return resultado

# 3. Chamada da função (execução)
saida = nome_da_funcao(5, 4) 
print(saida) # Saída: 20

## Arumento Padrao
def saudacao(nome, idioma="pt"):
    if idioma == "pt":
        return f"Olá, {nome}!"
    elif idioma == "en":
        return f"Hello, {nome}!"

# Usando o padrão (português)
print(saudacao("Maria"))    # Saída: Olá, Maria!

# Sobrescrevendo o padrão (inglês)
print(saudacao("John", idioma="en")) # Saída: Hello, John!

## Escopo de variáveis 
x = 10  # Variável Global

def minha_funcao():
    y = 5 # Variável Local
    print(f"Dentro da função, x (Global) é: {x}")
    print(f"Dentro da função, y (Local) é: {y}")

minha_funcao()

print(f"Fora da função, x (Global) é: {x}")
# print(y) # <-- ISSO GERARIA UM ERRO! 'y' não existe aqui.

## funções não podem alterar variáveis globais sem declarar explicitamente sua intenção:
contador = 0

def incrementar():
    global contador # Digo ao Python que quero modificar a variável global 'contador'
    contador = contador + 1
    
incrementar()
incrementar()
print(contador) # Saída: 2

# 4. Funções Lambda ("Anônimas")
## Funções sem nome, definidas usando a palavra lambda. 
## Usadas para tarefas rápidas onde uma função completa não é necessária.
# Ex: Função lambda que soma 10 ao argumento 'a'
adicionar_dez = lambda a: a + 10

print(adicionar_dez(5)) # Saída: 15