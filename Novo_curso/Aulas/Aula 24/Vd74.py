"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True: # Toda essa construção do laço while é para mostrar exatamente o que o laço de repetição for faz
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)