import ast

def verificar_erro(codigo, **variaveis):
    try:
        # Parseia a expressão para verificar sua sintaxe
        ast.parse(codigo, mode='eval')

        # Verifica se todas as variáveis necessárias foram fornecidas
        variaveis_necessarias = set(ast.parse(codigo).variables)  # Extrai as variáveis necessárias da expressão
        variaveis_fornecidas = set(variaveis.keys())
        if variaveis_necessarias != variaveis_fornecidas:
            variaveis_faltantes = variaveis_necessarias - variaveis_fornecidas
            return f"Variáveis necessárias faltando: {', '.join(variaveis_faltantes)}"

        # Avalia a expressão com as variáveis fornecidas
        resultado = eval(codigo, variaveis)

        return None  # Não há erro
    except SyntaxError as e:
        return f"Sintaxe inválida: {e}"
    except NameError as e:
        return f"Variável indefinida: {e}"
    except Exception as e:
        return f"Erro desconhecido: {e}"

# Exemplo de uso
codigo = 'x' + 'y' # Código a ser verificado
variaveis = {'x': 5, 'y': 10}  # Variáveis usadas no código

# Verifica se há erro no código com as variáveis fornecidas
erro = verificar_erro(codigo, **variaveis)

# Verifica se houve erro e imprime o resultado
if erro:
    print(f"Erro: {erro}")
else:
    print("Nenhum erro encontrado")
