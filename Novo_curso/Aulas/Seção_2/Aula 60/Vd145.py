from time import sleep
# Generator expression, Iterables e Iterators em Python
iteravel = ['Eu','tenho','__iter__']
iterador = iter(iteravel) # tem __iter__ e __next__
print(next(iterador))
print(next(iterador))
print(next(iterador))
print()

# def counter():
#     n = 0
#     while True:
#         yield n 
#         n += 1

# gen = counter()

# for x in gen:
#     print(iter(gen))
#     sleep(1)