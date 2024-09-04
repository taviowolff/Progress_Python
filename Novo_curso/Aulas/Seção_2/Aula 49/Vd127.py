# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índexes;
# - eles não garantem ordem; 
# - eles são iteráveis (for, in, not in)

l1 = [1,2,3,4,1,2,3,3,3,3,1]
s1 = set(l1)
l2 = list(s1)
print(l2)

# s1 = {1, 2, 3, 3, 3, 3, 1}

print(s1)

for numero in s1: # os Sets são iteráveis 
    print(numero)

if 1 in s1:
    print('1 está presente')

if 5 in s1:
    print('5 está presente')

else:
    print('5 não está presente')