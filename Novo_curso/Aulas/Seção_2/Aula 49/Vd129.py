# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em amos 
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^- Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2 # union retorna a uniao dos dois Sets s1 e s2
s4 = s1 & s2 # intersection retorna apenas os itens presentes em ambos os Sets
s5 = s1 - s2 # difference retorna apenas os itens diferentes do Set da esquerda (s1)
s6 = s1 ^ s2 # symmetric difference retorna os itens diferentes de ambos os Sets 

print(s3)
print(s4)
print(s5)
print(s6)

