'''
Nessa aula vamo entender a questao da verificacao de variaveis 
usando os comdandos ".is(x)" ex: isdigit, isnumeric, isalpha, isalnum
onde cada um desses tem uma vereficacao diferente
'''

num1 = input('digiti um numero: ')
num2 = input('digiti um numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(f'o primeiro numero mais o segundo é = {num1 + num2}.')
else:
    print('ERRO')

