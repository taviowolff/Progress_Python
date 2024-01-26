

lista = [("preco",2.5),("produto","uva"),("peso", 1)]

# dictionary comprehension 
dc = { 
    chave: valor
    for chave, valor in lista
}

print(dc)

# set comprehension 
s1 = {2**x for x in range(10)}
print(s1)