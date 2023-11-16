"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        # print('Não vou mostrar o 6.')
        continue # omite a visualização do número 6 

    if contador >= 10 and contador <= 27: # será lido ao chegar no 10 ao 27
        # print('Não vou mostrar o', contador)
        continue # omite a visualização dos número de 10 a 27

    print(contador)

    if contador == 40:
        break # ao chegar no 40 o laço é quebrado


print('Acabou')