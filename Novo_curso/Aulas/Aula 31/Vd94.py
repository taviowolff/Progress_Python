""" 
Lista dentro de lista
iterável dentro de iterável 
"""

salas = [ 
    ['Amanda', 'Carlos', 'Gabriel'],
    ['Silvano', 'Julia', 'Karen'],
    ['Sávio','Otávio','Isabela']
]

# print(salas)

# aluna11 = salas[1][1]
# aluno21 = salas[2][1]
# print(aluna11)

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)