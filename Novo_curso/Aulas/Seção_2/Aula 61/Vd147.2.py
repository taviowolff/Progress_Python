def generator(n, maximum):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

gen = generator(n=1,maximum=10000)

for g in gen:
    print(g)
