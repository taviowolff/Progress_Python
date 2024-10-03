# Relações entre classes: associção, agregação e composição
# Composição é uma especialização da agregação
# Mas nela, quando o objeto "Pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
 
class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self,rua,numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Apagando--------', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando---------', self.rua, self.numero)

cliente1 = Cliente('Otávio')

cliente1.inserir_endereco('Chapot', 513)
cliente1.inserir_endereco('Saturnino', 633)
cliente1.listar_enderecos()