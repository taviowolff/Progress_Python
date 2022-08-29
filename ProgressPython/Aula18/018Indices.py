"""
índices
0123456789......................33
Nesta aula vemos como usar o while para obter os indices separadamente de cada estrutura da palavra 'mundo'
Utilizando um cantador e uma variavel chamada 'nova_string'
Utilizamos o comando len(frase) para obtermos o número de caractéres dentre da palavra mundo que é = 5
e ao observarmos o laço while podemos ver que a para que ele continue rodando o tamanha_frase tem que ser maior que o contador 
A partir do momento que o contador for maior que o tamanha da frase o laço while vai parar e sair para próxima linha de código

"""
frase = 'mundo'
tamanha_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanha_frase:
    print(frase[contador], contador)

    nova_string += frase[contador]

    contador += 1
    
    print(nova_string)

print('acabou a frase')
