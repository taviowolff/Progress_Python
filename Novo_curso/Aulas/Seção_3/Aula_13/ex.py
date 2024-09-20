class Cachorro:
    def __init__(self,nome):
        self.nome = nome
        self._idade = None
        self._altura = None

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @property
    def altura(self):
        return self._idade

    @idade.setter
    def altura(self, valor):
        self._idade = valor

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        self._sexo = valor



c1 = Cachorro('Arnaldo')
print(c1.nome)
c1.idade = 8
print(c1.idade)
c1.altura = 1.71
print(c1.altura)

c1.sexo = 'm'
print(c1.sexo)
