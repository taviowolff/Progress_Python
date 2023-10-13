# Fazer contador de letras de uma frase
# Dar a quantidade de vezes que a letra apareceu


frase = 'aaaeeeeiiiou'

frase_n = frase.replace(' ','').lower() # converte os espaços para não ter espaços na frase e deixa todas as letras em minúsculo.

i = 0 # indíce para encerrar o laço while

qtd_letra_repetiu_mais_vezes = 0 # vai mostrar a quantidade da letra atual 

letra_repetiu_mais_vezes = '' # essa variável de valor none por enquanto ainda não foi definida

while i < len(frase_n):

    letra_atual = frase_n[i] # variável que vai passar de letra em letra que redefini a cada passada pelo final do loop
    
    qtd_letra_atual = frase_n.count(letra_atual) # count vai contar cada caractere que definimos que vai ser na letra_atual
    # então a variável qtd_atual vai receber o número de vezes que a letra aparece na frase

    if qtd_letra_repetiu_mais_vezes <= qtd_letra_atual: # Se a qtd_letra_repetiu_mais_vezes for menor ou igual a qtd_letra_atual 
        qtd_letra_repetiu_mais_vezes = qtd_letra_atual # qtd_letra_repetiu_mais_vezes se iguala qtd_letra_atual
        letra_repetiu_mais_vezes = letra_atual # iguala letra_repetiu_mais_vezes se iguala letra_atual

    """
    todo esse bloco if acima vai definir as novas variáveis a serem apresentadas
    letra_repetiu_mais_vezes - 
    qtd_letra_repetiu_mais_vezes - 
    """
    
    print(letra_atual, qtd_letra_atual)
    i += 1

print(f'A letra que repetiu mais vezes foi "{letra_repetiu_mais_vezes.upper()}" que apareceu {qtd_letra_repetiu_mais_vezes}x')