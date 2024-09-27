# x = ('Glenn', 'Sally', 'Joseph')
# print(x[2]) # Retorno: Joseph

# y = (1, 9, 2)
# print(y) # (1, 9, 2)

# print(max(y))

# # iteravel

# for iter in y:
#     print(iter)


# mas tuplas nao sao mutaveis 
# y = 'abc'
# y[2] = 'D' # TypeError: 'tuple' object does not support item assignment

# z = (5,4,3)
# z[2] = 0 # TypeError: 'tuple' object does not support item assignment


# print(dir(tuple()))

# Tuples and Assignment 

# Tuples are comparable

# Sorting lists of tuples

# Using sorted()

# Sort by Values instead of key

# c = {'a':10, 'b':1,'c':22}

# tmp = list()
# for k,v in c.items():
#     tmp.append((v,k))
# print(tmp)

# tmp = sorted(tmp, reverse=True)
# print(tmp)

# exercicio

caminho = ('#caminhoarquivo')
counts = dict()

with open(caminho, 'r', encoding='utf-8') as arquivo:
    for line in arquivo:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key,val)

# Even shorter Version

# c = {'a':10,'b':1,'c':22}

# print(sorted([(v,k) for k,v in c.items()])) #list comprehension
