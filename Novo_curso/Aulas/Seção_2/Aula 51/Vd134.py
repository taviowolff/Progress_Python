def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# as três meneiras de executar a soma
# print(executa(lambda x, y: x + y, 2, 3), 
#       executa(soma, 2, 3),
#       soma(2,3)
#     )

# duplica = cria_multiplicador(2)
duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(2))

# lamda geralmente é para coisas rápidas e fáceis como uma soma simples 
# nesse exemplo foi usado em uma função que retorna uma função o que causa uma confusão 

# def multiplica(x,y):
#     return x * y
    
print(executa(lambda x, y: x * y, 3, 2))

soma = (lambda x, y: x * y)

print(soma(2,3))

print(executa(lambda *args: sum(*args), 1,2,3,4))