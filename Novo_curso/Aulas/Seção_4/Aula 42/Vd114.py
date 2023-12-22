"""
Higher Order Functions
Funções de primeria classe
"""

def saudacao (msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'bom dia', 'Otávio')
)

print(executa(saudacao, 'boa noite', 'José'))