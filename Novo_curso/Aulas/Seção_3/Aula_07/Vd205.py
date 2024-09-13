# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2024  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# É indicado fazer um método para fazer o cálculo 
    def calcular_ano_nascimento(self):
        """Retorna o ano de nascimento baseado na idade."""
        return Pessoa.ano_atual - self.idade

# Criando instâncias
p1 = Pessoa('Carlos', 43)

# print(p1.__dict__)
# print(vars(p1))
# print(vars(Pessoa))
print(Pessoa.__dict__)