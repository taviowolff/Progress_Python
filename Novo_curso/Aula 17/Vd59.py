"""
Repetições 
while (enquanto)
Executa uma ação enqaunto uma condição for verdadeira
Loop infinito -> Quando um não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break

print('Acabou a repetição!')