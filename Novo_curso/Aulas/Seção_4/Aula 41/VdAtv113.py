# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult (*args):
    total = 1 # tive que colocar 1 aqui por não enteder qual número botar
    for num in args:
        total *= num
    return total

mult_1 = mult(1,2,3)
print(mult_1)

mult_2 = mult(10,2,3)
print(mult_2)



# Crie ma função que fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar

def impari(num):
    if num%2 == 0:
        return('É par')
    return ('É ímpar')

    # else: # esse else se torna redundante pois a o return em cima evita a leitura dele
    #     return('é impar')

num1 = impari(2)
num2 = impari(3)

print(num1)
print(num2)