import random

print('Escreva o nome dos alunos para sortear a ordem')
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista_base = [a1,a2,a3,a4]
random.shuffle(lista_base)

print(lista_base)



