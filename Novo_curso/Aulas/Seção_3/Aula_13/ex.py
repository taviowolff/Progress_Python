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

    def sexo(self):
        sexo = input('Qual seu sexo? ')
        return sexo


c1 = Cachorro('Arnaldo')
print(c1.nome)
c1.idade = 8
print(c1.idade)
c1.altura = 1.71
print(c1.altura)

print(Cachorro.sexo)