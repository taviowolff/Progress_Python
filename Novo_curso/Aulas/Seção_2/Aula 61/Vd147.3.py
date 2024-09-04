def contador(n):
    i = 0
    while i < n:
        yield i 
        i += 1

gen = contador(5)

for g in gen:
    print(g)