peso_peixes = float(input('Quantos kg de peixe pescou hoje? '))

if peso_peixes > 50:
    multa = (peso_peixes-50)*4.0
    print(f'Sua multa foi de {multa:.2f} reais')

else:
    print('não houve multa')