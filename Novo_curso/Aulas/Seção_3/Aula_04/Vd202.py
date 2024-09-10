# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'Leão' # atributo de classe

    def __init__(self,nome): # Método construtor (init)
        self.nome = nome # atributo de instância

        variavel = 'valor' # variável local só existe dentro do escopo __init__
        print(variavel) # servindo apenas para fins temporários
 
    def comendo(self,alimento): # Método de instância
        return (f'{self.nome} está comendo {alimento}') 


leao = Animal('Leão') # Criação de uma instância(Objeto)
print(leao.nome)

guaxinim = Animal('Guaxinim') # Criação de uma instância(Objeto)
print(guaxinim.nome)