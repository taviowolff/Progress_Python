"""
For in Python
Iterando strings com for
Aqui tem uma função de iteração muito utilizada em pyhton
Essa função é quase igual ao While porem essa tem como forma de parametro
Função range(start = 0, stop, step = 1)
A função range ela faz um range e dentro do laço For você consegue
fazer uma instancia entre os números que vc escolheu para iniciar e terminar
e fazer com que ele pule de maneiras diferentes.
"""
texto = 'mundo' # o parametro utilizado nesse laço é a STR 'mundo'.

for letra in texto:
    print(letra)

print('')

for x in range(1,6,1):  # aqui ele começa por 1 vai até 6 (mas não mostra o 6 e pula de 1 em 1)
    print(x) 
