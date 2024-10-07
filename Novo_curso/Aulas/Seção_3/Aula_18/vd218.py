# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem Motor
# Obs: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

# # 3 - Crie uma classe Fabricante (Nome)
# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome
#         self.modelos = []
    
#     def inserir_modelos(self,modelo, ano):
#         self.modelos.append(Carro(modelo, ano))

#     def listar_modelos(self):
#         for modelo in self.modelos:
#             print(modelo.modelo, modelo.ano, self.nome)

# # 1 - Crie uma classe Carro (Nome)
# class Carro:
    
#     def __init__(self, modelo, ano):
#         self.modelo = modelo
#         self.ano = ano
#         self.motores = []

#     def inserir_motores(self, motores):
#         self.motores.append(Motor(motor))
    
# # 2 - Crie uma classe Motor (Nome)
# class Motor:
#     def __init__(self, motor):
#         self.motor = motor


# # 1 - Crie uma classe Carro (Nome)
# class Carro:
#     def __init__(self, modelo):
#         self.modelo = modelo
#         self.motores = []

#     def inserir_motores(self, motores):
#         self.motores.append(Motor(motor))
    
# # 2 - Crie uma classe Motor (Nome)
# class Motor:
#     def __init__(self, motor):
#         self.motor = motor

# # 3 - Crie uma classe Fabricante (Nome)
# class Fabricante:
#     def __init__(self, fabricante):
#         self.fabricante = fabricante
#         self.modelos = []
    
#     def inserir_modelos(self, modelo):
#         self.modelos.append(Carro(modelo))

#     def listar_modelos(self):
#         for modelo in self.modelos:
#             print(modelo.modelo, modelo.ano, self.nome)



# 1 - Crie uma classe Carro (Nome)
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

# 2 - Crie uma classe Motor (Nome)
class Motor:
    def __init__(self, nome):
        self.nome = nome

# 3 - Crie uma classe Fabricante (Nome)
class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_v8 = Motor('V8')

fusca.fabricante = volkswagen
fusca.motor = motor_v8

print(fusca.modelo,fusca.fabricante.nome,fusca.motor.nome)

opala = Carro('Opala')
ford = Fabricante('Ford')
opala.motor = motor_v8
opala.fabricante = ford

print(opala.modelo, opala.fabricante.nome, opala.motor.nome)






