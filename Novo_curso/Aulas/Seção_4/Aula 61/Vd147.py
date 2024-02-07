def generator(n=0):
    yield 1 # Pausar
    print('Continuando...')
    yield 2 # Pausar
    print('Mais um pause...')
    yield 3 # Pausar
    print('Vou terminar...')
    return 'Acabou'


gen = generator(n=0)

for g in gen:
    print(g)


# print(next(gen))
# print(next(gen))
# print(next(gen))