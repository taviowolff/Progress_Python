"""
Iniciar com letra, pode conter nÃºmeros, separar _, letras minÃºsculas
"""
nome = 'Otávio'
idade = 23
altura = 1.71
e_maior = idade >= 18  #  aqui temos uma condição com uma resposta booleana, se sua idade for maior ou igual a 18 aparece True 
peso = 67

print('nome', nome)
print('idade', idade)
print('altura', altura)
print('É maior', e_maior)
print('Peso', peso)

IMC = peso / (altura**2)
print('seu nome é', nome,', você tem', idade, 'anos e sua altura é', altura, 'seu peso é', peso, 'kg.')
print('seu IMC é de', IMC)
