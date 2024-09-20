# Dicionário em python


# counts = {'Ester' : 2, 'Isaque' : 4,'Helio' : 1}

# x = counts.get('Isaque', 0)
# y = counts.get('Otávio',0)

# print(x)
# print(y)

# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

# for name in names:
#     counts[name] = counts.get(name,0) +1
# print(counts)

# stuff = dict()
# print(stuff['candy'])

# stuff = dict()
# print(stuff.get('candy',-1))

if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1