# Fazer contador de letras de uma frase
# Dar a quantidade de vezes que a letra apareceu


frase = 'Be more'

frase_n = frase.replace(' ','').lower() # converte os espaços para não ter espaços na frase e deixa todas as letras em minúsculo.

i = 0 # indíce para encerrar o laço while

qtd_letra_atual = 0 # vai mostrar a quantidade da letra atual 

letra_repetiu_mais_vezes = '' # essa variável de valor none por enquanto ainda não foi definida

while i < len(frase_n):

    letra_atual = frase_n[i] 
    
    cont_letra = frase_n.count(letra_atual)

    if qtd_letra_atual <= cont_letra:
        qtd_letra_atual = cont_letra
        letra_repetiu_mais_vezes = letra_atual

    
    print(letra_atual, cont_letra)
    i += 1

print(f'A letra que repetiu mais vezes foi "{letra_repetiu_mais_vezes.upper()}" que apareceu {qtd_letra_atual}x')