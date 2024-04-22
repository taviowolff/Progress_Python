import random 

numero_gerado = random.randint(1,10)
tentativas = 0

while True:
    escolha = input('Adivinhe o número: ')

    if escolha.isdigit:
        tentativas += 1
        try:
            num_escolha = int(escolha)
            if num_escolha == numero_gerado:
                print(f'o número adivinhado era {numero_gerado}, você acertou! \nvocê teve {tentativas} tentativas')
                break
            
            elif (num_escolha < numero_gerado):
                print('escolha um número maior')
                
            else:
                print('escolha um número menor')
        except ValueError:
            print('escolha um número')
            
    else:
        print('escolha um número') 