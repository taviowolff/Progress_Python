"""
Faça um contador de letras 
Que ao final mostre a letra que mais se repetiu
"""

# frase = 'Pato angolano'

# i = 0 

# qtd_vzs_mais_apareceu = 0

# letra_q_apareceu = ''

# while i < len(frase):
    
#     letra_da_frase = frase[i]

#     qts_vzs_letra_apareceu = frase.count(letra_da_frase)

#     print(letra_da_frase, qts_vzs_letra_apareceu)

#     i += 1


frase = input("Digite uma frase: ")
frase = frase.replace(" ", "").lower()

contagem_letras = {}
indice = 0

while indice < len(frase):
    letra = frase[indice]
    if letra.isalpha():
        if letra in contagem_letras:
            contagem_letras[letra] += 1
        else:
            contagem_letras[letra] = 1
    indice += 1

letra_mais_repetida = None
max_contagem = 0

for letra, contagem in contagem_letras.items():
    if contagem > max_contagem:
        letra_mais_repetida = letra
        max_contagem = contagem

if letra_mais_repetida is not None:
    print(f"A letra que mais se repete na frase é: {letra_mais_repetida}")
else:
    print("Não há letras na frase.")