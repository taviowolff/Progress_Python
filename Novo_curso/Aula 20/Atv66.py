# while True:

#     entrar = input('Quer calcular? (s/n): ')
    
#     while entrar != 'n':

#         x = input('escolha um tipo de cálculo +; -; /; *: ')
        
#         num1 = input(f'defina um número: ')
    
#         num2 = input(f'defina outro número: ')
        
#         if num1.isnumeric and num2.isnumeric:
       
#             num1 = int(num1)
        
#             num2 = int(num2)

#             if x == '+':
#                 soma = num1 + num2
#                 print(f'{num1} + {num2} = {soma}' )

#             if x == '-':
#                 sub = num1 - num2
#                 print(f'{num1} - {num2} = {sub}')

#             try:
#                 if x == '/':
#                     div = num1 / num2
#                     print(f'{num1} / {num2} = {div}')
            
#             except ZeroDivisionError:
#                 print('zero não divide')

#             try:
#                 if x == '*':
#                     mult = num1 * num2
#                     print(f'{num1} x {num2} = {mult}')
#             except ValueError:
#                 print('Você não digitou um número válido')
    
#         sair = input('você deseja continuar (s/n)?: ')

#     else:
#         print('Tchau, até mais.')

while True:
    entrar = input('Quer calcular? (s/n): ')

    while entrar != 'n':
        x = input('Escolha um tipo de cálculo +; -; /; *: ')
        
        if x not in ('+', '-', '/', '*'):
            print('Operador inválido. Por favor, escolha +, -, / ou *.')
            continue
        
        num1 = input('Defina um número: ')
        num2 = input('Defina outro número: ')
        
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print('Você não digitou um número válido.')
            continue

        if x == '+':
            soma = num1 + num2
            print(f'{num1} + {num2} = {soma}' )
        elif x == '-':
            sub = num1 - num2
            print(f'{num1} - {num2} = {sub}')
        elif x == '/':
            if num2 == 0:
                print('Divisão por zero não é permitida.')
            else:
                div = num1 / num2
                print(f'{num1} / {num2} = {div}')
        elif x == '*':
            mult = num1 * num2
            print(f'{num1} * {num2} = {mult}')

        sair = input('Você deseja continuar (s/n)?: ')

    else:
        print('Tchau, até mais.')

