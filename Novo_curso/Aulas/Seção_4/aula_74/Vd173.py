# count é um iterador sem fim (itertools)

from itertools import count

c1 = count(0, 8)
r1 = range(10, 50)

print('c1', hasattr(c1, '__iter__'))

print('c1', hasattr(c1, '__next__'))

print('r1', hasattr(r1, '__iter__'))

print('r1', hasattr(r1, '__next__'))


print("count")
for i in c1:
    if i >= 50:
        break

    print(i)
print()
print('range')