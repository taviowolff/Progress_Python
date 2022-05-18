"""
While em python - aula 17
utilizado para realizar ações enquanto
uma condição for verdadeira

Requisitos: Entender condições e operadores
"""
while True:
    print()
    num_1 = input('digite um número: ')
    num_2 = input('digite outro número: ')
    operador = input('digite um operador: ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('digite um número correto.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('operador inválido')

    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break
