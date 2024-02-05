import sys
# Generator expression, Iterables e Iterators em Python
iterable = ['Eu','Tenho', '__iter__']
iterator = iter(iterable)

genarator = (n for n in range(10))

print(sys.getsizeof(genarator))

for n in genarator:
    print(n)