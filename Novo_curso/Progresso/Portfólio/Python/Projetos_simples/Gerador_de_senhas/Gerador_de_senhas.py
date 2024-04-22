import random
import string


def gerador_de_senhas(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha 

comprimento = int(input('Digite o comprimento da senha desejada: '))
senha = gerador_de_senhas(comprimento)

print(f'Sua senha nova é {senha}')