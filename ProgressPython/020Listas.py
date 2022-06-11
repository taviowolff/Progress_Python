'''
Lista em python
Uma lista é uma estrutura de dados composta por itens organizados de 
forma linear, na qual cada um pode ser acessado a partir de um índice, 
que representa sua posição na coleção (iniciando em zero).
Essa estrutura de dados pode armazenar, inclusive simultaneamente, 
objetos de diferentes tipos, como strings,
números e até mesmo outras listas.
'''

# aqui um exemplo de lista
lista =   [123, 'Otávio', '5.23', 'mundo']
# indices   0  ,   1    ,   2   ,    3
# essa lista pode ter seus índices acessados 

print(lista[0])
# aqui vai mostrar o "int" "123" que está no índice 0 da lista

# A lista também tem métodos embutidos em suas funcionalidades
# Para acessar esses métodos basta digitar: lista.(métodos irão aparecer)

# lista.append
# aqui podemos adicionar mais um objeto dentro da lista dando a ela um índice dentro da lista
lista2 = ['0', '1', '2','3']
lista2.append('4') # lista 2 recebera um novo objeto 
print(lista2)

# lista.insert(índice, 'objeto')
# aqui sera inserido um novo objeto no índice de desejo
lista3 = ['0', '1', '2','3']
lista3.insert(0,'nova_str') #aqui o 'nova_str' assumirá o valor de 0 nos indices
print(lista3)

# lista.pop(indice_excluído)
# aqui excluiremos um objeto a partir do seu indice
lista4 = ['0', '1', '2','3']
lista4.pop(1) # aqui estamos tirando fora o '1' localizado no indice 1
print(lista4)

# lista.remove('nome do objeto a ser removido')
# aqui haverá a exlusão do objeto uma vez, mas se houver mais de um objeto igual
# terá de se efetuar o comando de novo para excluir ele
lista5 = ['1','2','1','3']
lista5.remove('1')
print(lista5) # nesse print vai mostrar a lista com a remoção do primeiro '1'
lista5.remove('1')
print(lista5) # nesse print vai mostrar a lista com a remoção do segundo '1'

# lista.reverse()
# nesse comando temos uma reversão da lista 
lista6 = ['1','2','3','4']
lista6.reverse()
print(lista6)

# lista.sort()
# nesse comando temos uma organização de ordem crescente
lista7 = ['4','2','5','3','1']
lista7.sort()
print(lista7)

# lista.count('nome de objeto')
# conta a quantidade de vezes que o objeto aparece na lista
lista8 = ['1','1','2','3','4']
print(lista8.count('1'))
print(lista8.count('3'))

# comprimento de lista len(lista)
# temos uma contagem
lista9 = ['0','1', '2', '3'] 
print(len(lista9)) # resultado '4' mostrando o valor de objetos na lista 9

# há a possibildade de se concatenar e multiplicar listas
lista10 = ['1','2','3']
print(lista10*3) # ['1', '2', '3', '1', '2', '3', '1', '2', '3']
print(lista10+lista) # ['1', '2', '3', 123, 'Otávio', '5.23', 'mundo']