# Usando a função input para coletar dados do usuário

# nome = input('Qual seu nome? ')
# print(f'O seu nome é {nome}')

# recomendo nao fazer essa transformaçao de dado em cima da variável 
# numero_1 = int(input('Digite um número: '))
# numero_2 = int(input('Digite outro número: '))

# print(f'A soma dos números é {numero_1+numero_2}')

# forma recomendada para facilitar futuras verificações
numero1 = input('Escreva um número: ')
numero2 = input('Escreva outro número: ')

numero1 = int(numero1)
numero2 = int(numero2)

print(f'A soma dos números é {numero1+numero2}')