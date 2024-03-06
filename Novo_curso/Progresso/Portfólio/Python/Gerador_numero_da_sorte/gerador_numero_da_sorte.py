import random

def gerador_numero_sorteado(qtd_numeros):
    numero = random.sample(range(1,61), qtd_numeros)
    return sorted(numero)

# qtd_numeros = int(input('Digite a quantidade de números que você deseja?: ')) // definir sua própria qtd
qtd_numeros = 6
numeros_sorteados = gerador_numero_sorteado(qtd_numeros)

print(f'números da sorte: {numeros_sorteados}')