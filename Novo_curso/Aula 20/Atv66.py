while True:
   
    entrar = input('Quer calcular? (s/n) ')

    while entrar != 'n':

        x = input('escolha um tipo de cálculo +; -; /; *: ')
        
        num1 = input(f'defina um número: ')
    
        num2 = input(f'defina outro número: ')

        if num1.isnumeric and num2.isnumeric:
       
            num1 = int(num1)
        
            num2 = int(num2)

            if x == '+':
                soma = num1 + num2
                print(f'{num1} + {num2} = {soma}' )

            elif x == '-':
                sub = num1 - num2
                print(f'{num1} - {num2} = {sub}')

            elif x == '/':
                div = num1 / num2
                print(f'{num1} / {num2} = {div}')

            elif x == '*':
                mult = num1 * num2
                print(f'{num1} x {num2} = {mult}')

            else:
                ('escolheu o sinal errado')

        entrar = input('Quer calcular? (s/n) ')
       
    else:
        print('Tchau até mais') 
        break
