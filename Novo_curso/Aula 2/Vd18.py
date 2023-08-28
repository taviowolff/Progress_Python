print(12,34, sep="") #aqui o separador remove o espaço colocado por padrão no python
print(56,78, sep=' ') #nesse já o separador colocado com barra de espaço ainda está lá mas definido por nós
print(56,78, sep='.') #separado por ponto .

print(12,34, sep="-", end= '\nxx')
print(56,78, sep='-', end='x\nx') 
print(32,12, sep='.', end='\n')
print(32,24, sep="", end='.')