"""
Fatiamento de strings 
- lembre-se que strings são iteráveis 
- elas são separadas por índices e eles podem ser manipulados

ex:
 0 1 2 3 4 5 6 7
 O l á m u n d o
-8-7-6-5-4-3-2-1

começando a partir do índice 0 se positivo 
e finalizando no índice -1 se negativo
- Isso serve para achar a palavra requisitada com coordenadas 

ex: 
texto = 'Olá mundo'
cortar_meio = texto[4:]
"""

texto = "Olá mundo"
cortar_meio_pra_frente = texto[4:]
print(cortar_meio_pra_frente)


texto = "Olá mundo"
cortar_meio_pra_tras = texto[:4]
print(cortar_meio_pra_tras)
