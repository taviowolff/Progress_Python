"""
Repetições 
while (enquanto)
Executa uma ação enqaunto uma condição for verdadeira
Loop infinito -> Quando um não tem fim
"""
condicao = True

while condicao: # essa estrutura de repetição só será repetida se a condição tiver True
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair': # uma das formas de se quebrar a repetição
        break

print('Acabou a repetição!') # frase verificadora de quebra de repeitção