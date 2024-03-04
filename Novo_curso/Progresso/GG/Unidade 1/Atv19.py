'''
Um professor quer sortear um dos seus quatro alunos para apagar
o quadro. Faça um programa que ajude ele, lendo o nome deles e
escrevendo o nome do escolhido.
'''
import random
print('Professor vai escolher um dos 4 alunos da lista')

lista_alunos = ['Jorge', 'Otávio', 'Danilo', 'Artur']

aluno_escolhido = random.choice(lista_alunos)

print(f'O professor escolheu o {aluno_escolhido}')