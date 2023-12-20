# def exemplo_args(arg1, *args):
#     print("Primeiro argumento:", arg1)
#     print("Outros argumentos:", *args)

# # Chamando a função com diferentes números de argumentos
# exemplo_args(1)
# exemplo_args(1, 2)
# exemplo_args(1, 2, 3, 4)

"""
args - argumentos não nomeados
* ou *args (empacotamento e desempacotamento)
"""

# # lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4,
# print(x, y, resto) 
# # o resto sem o * ainda estará mostrando a lista dos números restantes
# print(x, y, *resto)
# # com a presença de * os números 3 e 4 são desempacotados

def soma(*args): # repare que esse *args é apenas para argumentos posionais
    total = 0 # definimos o total inicialmente
    print('Total', total)
    for numero in args: # os argumentos passados serão jogados no laço
        total = total + numero # número somado com total e redefinição do total dentro do laço for
        print('Total', total)

soma(1, 2, 3, 4, 5, 6)