"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. 
Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

print('Vamos descobrir se um número é par ou impar')
num1 = input('Digite um número inteiro: ')


if num1.isdigit(): # isdigit verifica se o que foi dado como objeto no input é numérico

    num1 = int(num1) # setando para int 

    par = num1 % 2 # defini a variável par com uma equação que verificará futuramente

    if par == 0: # verifica se o resto da divisão por 2 é 0, caso sim é True
        print('É par')
    
    else:
        print('É impar!')

else:
    print('Acabou o time! \nNão é um número inteiro')