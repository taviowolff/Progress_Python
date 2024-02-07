def generator(n=0):
    yield 3


gen = generator()

# for gen in range(10):
print(next(gen))
print(next(gen))
print(next(gen))