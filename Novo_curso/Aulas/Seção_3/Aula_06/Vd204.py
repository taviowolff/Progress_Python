# class Pessoa:
#     ano_atual = 2024 # atributo de class
#     # pode ser usada em outras instâncais do resto da classe
#     def __init__(self,nome,idade):
#         self.nome = nome
#         self.idade = idade
#         # self.nascimento = ano_atual - idade   
#     def data_nascimento(self):
#         return Pessoa.ano_atual - self.idade

# p1 = Pessoa('Carlos',43)
# print(p1.data_nascimento())

# class Pessoa:
#     ano_atual = 2024 # atributo de class
#     # pode ser usada em outras instâncais do resto da classe

#     def __init__(self,nome,idade):
#         self.nome = nome
#         self.idade = idade
#         self.nascimento = Pessoa.ano_atual - self.idade
#         # pode ser feito o calculo do ano de nascimento dentro da instância init
        
#     def data_nascimento(self):
#         return Pessoa.ano_atual - self.idade
#         # mas também pode ser feita dentro de uma função

# p1 = Pessoa('Carlos',43)
# print(Pessoa.ano_atual)
# print(p1.nascimento)
# print(p1.nome)
# print(p1.ano_atual - p1.idade) # possivél também fazer o calculo dentro de print
# print(p1.data_nascimento()) # Métodos de classes são acessados por objeto.funcao()

# Para um clean code

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

# Saídas
print(f"Ano atual: {Pessoa.ano_atual}")
print(f"Nome: {p1.nome}")
print(f"Ano de nascimento: {p1.calcular_ano_nascimento()}")
