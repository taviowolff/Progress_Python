"""
Faça um contador de letras 
Que ao final mostre a letra que mais se repetiu
"""
# # Contador que eu criei com base no meu conhecimento fraco sobre o laço while
# frase = 'Pato angolano'

# i = 0 

# qtd_vzs_mais_apareceu = 0

# letra_q_apareceu = ''

# while i < len(frase):
    
#     letra_da_frase = frase[i]

#     qts_vzs_letra_apareceu = frase.count(letra_da_frase)

#     print(letra_da_frase, qts_vzs_letra_apareceu)

#     i += 1


# # Usando python para fazer esse contador de letras 

# frase = input("Digite uma frase: ")
# frase = frase.replace(" ", "").lower()

# contagem_letras = {}
# indice = 0

# while indice < len(frase):
#     letra = frase[indice]
#     if letra.isalpha():
#         if letra in contagem_letras:
#             contagem_letras[letra] += 1
#         else:
#             contagem_letras[letra] = 1
#     indice += 1

# letra_mais_repetida = None
# max_contagem = 0

# for letra, contagem in contagem_letras.items():
#     if contagem > max_contagem:
#         letra_mais_repetida = letra
#         max_contagem = contagem

# if letra_mais_repetida is not None:
#     print(f"A letra que mais se repete na frase é: {letra_mais_repetida}")
# else:
#     print("Não há letras na frase.")


# Aplicação do professor Luis Otávio sobre esse 

frase = 'Eu odeio flor'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ': # esse if aqui vai fazer com que os espaços da frase não sejam contados 
        i += 1
        continue # aplicando a linha de código que faz com que continue após notar o espaço além de voltar para o início do laço 

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
    
    print(letra_atual)
    i += 1
print('')
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)