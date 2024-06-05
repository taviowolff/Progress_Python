# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recuriva deve ter:
# - Um problema que possa ser divido em partes menores
# - um caso recursivo que resolve o pequeno problema
# - um caso base que para a recursão
#  - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120


def fatorial(n):
    if n == 0:
        return 1
    
    else:
        return n * fatorial(n - 1)
    

# print(fatorial(5))

def fibonacci(n):
    if n < 2:
        return n
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 
    


print(fibonacci(6)) 