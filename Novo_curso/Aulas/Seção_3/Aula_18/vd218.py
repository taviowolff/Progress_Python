# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem Motor
# Obs: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

# 3 - Crie uma classe Fabricante (Nome)
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.modelos = []
    
    def inserir_modelos(self,modelo, ano):
        self.modelos.append(Carro(modelo, ano))

    def listar_modelos(self):
        for modelo in self.modelos:
            print(modelo.modelo, modelo.ano, self.nome)

# 1 - Crie uma classe Carro (Nome)
class Carro:
    
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
    
    # def inserir_motor(self, motor):
    #     self.motor = motor

# 2 - Crie uma classe Motor (Nome)
# class Motor:
#     def __init__(self, motor):

fabricante1 = Fabricante('Ford')
fabricante1.inserir_modelos('SUV', 2024)
fabricante1.listar_modelos()








