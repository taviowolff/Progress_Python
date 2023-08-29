print(12,34, sep="") # aqui o separador remove o espaço colocado por padrão no python
print(56,78, sep=' ') # nesse já o separador colocado com barra de espaço ainda está lá mas definido por nós
print(56,78, sep='.') # separado por ponto .

print(12,34, sep="-", end= '\nxx')
print(56,78, sep='-', end='x\nx') 
print(32,12, sep='.', end='\n')
print(32,24, sep="", end='.')

# end = '' é uma forma de dizer o que vem a seguir no final do objeto 
# caso o valor dentro de '' esteja vazio, não havera nada, nem espaço.

# \n é uma quebra de linha como mostrado na linha 5,6 
# o comando do \n faz a quebra de linha jogando o x para linha de baixo
# forçando o início da linha com a letra xx e x