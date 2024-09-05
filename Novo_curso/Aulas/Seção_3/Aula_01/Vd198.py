# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações 
# Por convenção, usamos PascalCase para nomes de
# Classes

# string = 'Otávio' # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa: # definição da classe (PascalCase)
    ...

p1 = Pessoa() # Instância da classe
# Aqui, você cria uma instância (objeto) da classe Pessoa, 
# chamada p1. A partir de agora, p1 é um objeto do tipo Pessoa
p1.nome = 'Otávio'
p1.sobrenome = 'Wolff'
# Você pode adicionar atributos ao objeto p1 dinamicamente.
#  Neste caso, p1 ganha os atributos nome e sobrenome.
print(p1.nome)
print(p1.sobrenome)
# Aqui, os atributos nome e sobrenome de p1 são acessados e impressos. 
# O mesmo ocorre com o objeto p2, que também é uma instância da classe 
# Pessoa com atributos diferentes.

p2 = Pessoa()
p2.nome = 'Nathália'
p2.sobrenome = 'Rainer'

print(p2.nome)
print(p2.sobrenome)