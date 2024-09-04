# Exemplo de uso dos Sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('você achou a letra secreta')
        break

print(len(letras))