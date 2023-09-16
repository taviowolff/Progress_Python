# 'in' e 'not in'
# Operadores lógicos de verificação de presença

# in - verifica se o que é pedido está dentro de uma string ou obejto
# caso estejá o valor retorno é True 

# not in - faz o inverso de 'in'
# caso haja presença do objeto ou string na lista ele retorno False,
# caso não tenha ele retorno True

# exemplos

lista = (1,2,3,4,5,6)
num = input('Digite um número: ')

num = int(num)

if num in lista:
    print(lista)
    print(f'O número {num} está na lista ')