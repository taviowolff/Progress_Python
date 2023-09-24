"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input('Que horas são? ')

hora = horas[:2] # Fatiamos a string para extrair apenas as horas

if hora.isdigit(): # Verifica se o que a pessoa digitou é um número inteiro 

    hora = int(hora) # Após extrair a string transformamos em inteiro para analise

    if hora >= 0 and hora <= 11: # Defini os valor de 0 a 11 sendo BOM DIA
        print('Bom dia!')

    elif hora >= 12 and hora <= 18: # Defini os valor de 12 a 18 sendo BOA TARDE
        print('Boa tarde!')

    elif hora >= 19 and hora <= 23: # Defini os valor de 19 a 23 sendo BOA NOITE
        print('Boa noite!')

    else:
        print('BMO ')

elif hora.isalpha: # verifica se o que a pessoa escreveu está em String Alphabet
    print('digite um número inteiro') # Caso seja diferente retorna essa mensagem