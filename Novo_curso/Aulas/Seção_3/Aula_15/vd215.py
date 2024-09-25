# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição
# Geralmente, temos uma associação quando um objeto tem 
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla 
# o ciclo de vida de outro objeto

class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property # Getter
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter # Setter
    def ferramenta(self,ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self, nome): # Definir a Ferramenta que está sendo utilizada
        self.nome = nome

    def escrever(self): # Método para dizer que Ferramenta escreve
        return f'{self.nome} está escrevendo'

escritor = Escritor('Otávio')
caneta = FerramentaDeEscrever('Caneta Bic')
teclado = FerramentaDeEscrever('Teclado')
print(escritor.nome)
print(teclado.nome)
print(caneta.escrever())


