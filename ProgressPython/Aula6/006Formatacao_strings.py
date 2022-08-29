'''
aula de formatação de strings 
'''
nome = 'Otávio'
idade=23
altura = 1.71
e_maior = idade > 18
peso = 67
IMC = peso / (altura**2)

print(nome,'tem' , idade, ', pesa', peso,)

print(f'{nome} tem {idade}, pesa {peso}.')

print('{0} tem {1}, pesa {2}.' .format(nome, idade, peso)) 
# o que eu mais indico na hora de formatar pois vc pode definir os números nas ordes em que ele são colocados dentro dos ()
# ex : '{0} {1} {2} {1}'. format(0, 1, 2)

print('seu imc é {:.2f}' .format(IMC))