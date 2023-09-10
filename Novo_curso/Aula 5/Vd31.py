#  formatação de strings f-strings

nome = 'otávio'
altura = 1.71
peso = 70

imc = peso / (altura ** 2)

print(nome,'Seu IMC é', imc)\

print(f'{nome}, "Seu IMC é", {imc:.2f}')
