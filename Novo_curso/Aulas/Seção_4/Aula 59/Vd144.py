class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa("Otávio", 25)

print(dir(p))

print(hasattr(p, "nome"))

print(hasattr(p, "altura"))

print(getattr(p,"altura", "altura desconhecida"))