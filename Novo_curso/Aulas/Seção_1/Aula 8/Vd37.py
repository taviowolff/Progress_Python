# Em Python, os operadores relacionados, também conhecidos como operadores de comparação, são usados para comparar valores e expressões. Eles retornam 
# um valor booleano (True ou False) que indica se a comparação é verdadeira ou falsa. Aqui estão os principais operadores relacionados em Python:

# == (igual a): Verifica se dois valores são iguais.
# Exemplo: a == b retorna True se a for igual a b.

# != (diferente de): Verifica se dois valores são diferentes.
# Exemplo: a != b retorna True se a for diferente de b.

# < (menor que): Verifica se o valor da esquerda é menor do que o valor da direita.
# Exemplo: a < b retorna True se a for menor que b.

# > (maior que): Verifica se o valor da esquerda é maior do que o valor da direita.
# Exemplo: a > b retorna True se a for maior que b.

# <= (menor ou igual a): Verifica se o valor da esquerda é menor ou igual ao valor da direita.
# Exemplo: a <= b retorna True se a for menor ou igual a b.

# >= (maior ou igual a): Verifica se o valor da esquerda é maior ou igual ao valor da direita.
# Exemplo: a >= b retorna True se a for maior ou igual a b.

# Além desses operadores, você pode combinar expressões de comparação usando operadores lógicos, como and (e), or (ou) e not (não), 
# para criar condições mais complexas. Por exemplo:

a = int(input('Escolha um número: '))
b = int(input('Escolha outro número: '))

if a > 5 and b < 10:
    print('True')

    # Esta condição é verdadeira se 'a' for maior que 5 e 'b' for menor que 10.
