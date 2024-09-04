"""
Exercícios 
Crie funções que duplicam, triplicam e quadroplicam
o número recebido como parâmetro 
"""

# def receba_numero(*args):
#     def duplica (*args):
#         return args * 2
#     def trplica (*args):
#         return args * 3
#     def quadruplica(*args):
#         return args * 4
    
# print(receba_numero(duplica(2)))

# Uma possível variação dessa atividade
# def duplica(num):
#     return(num * 2)

# def triplica(num):
#     return(num * 3)

# def quadriplica(num):
#     return(num * 4)

# print(duplica(3),triplica(7), quadriplica(3))

def definir_multiplicador(multiplicador):
    def numero(numero):
        return multiplicador * numero
    return numero


duplica = definir_multiplicador(2)
triplica = definir_multiplicador(3)
quadruplica = definir_multiplicador(4)

print(duplica(2))
print(triplica(2))
print(quadruplica(2))

    
