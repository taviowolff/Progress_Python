"""
args - argumentos não nomeados
* ou *args (empacotamento e desempacotamento)
"""
def soma(*args): # repare que esse *args é apenas para argumentos posionais
    total = 0 # definimos o total inicialmente
    for numero in args: # os argumentos passados serão jogados no laço
        total += numero # número somado com total e redefinição do total dentro do laço for
    return(f'Total = {total}')

soma(1, 2, 3, 4, 5, 6) # essa chamada não vai aparecer nada na tela devido o fato da função não ter print

soma_1_2_3 = soma(1,2,3) # chamada da função soma
# print(soma_1_2_3)

soma_4_5_6 = soma(4,5,6) # chamada da função soma
# print(soma_4_5_6)

outra_soma = soma(1,4,5,6,7,8,64,32) # chamada da função soma
# print(outra_soma)


numeros = 1,4,5,6,7,8,64,32

soma_numeros = sum(numeros)
print(f'total = {soma_numeros}')

print(soma(*numeros)) # os números são passados como argumentos para funções, só que sem o *
# esses número vão fica empacotados, acarrentando em um erro no código

print(numeros) # números empacotados dentro da tupla 
print(*numeros) # número desempacotados fora da tupla
