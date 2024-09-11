numlist = list()

while True:
    inp = input('Digite um número: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

media = sum(numlist) / len(numlist)
print(media)
 