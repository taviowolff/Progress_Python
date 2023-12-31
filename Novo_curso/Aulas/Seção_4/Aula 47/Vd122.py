# Métodos úteis dos dicionários em Python
# copy - retorna uma cópia rasa (shallow copy): copiando até as alterações do dict principal
# deepcopy - retorna uma cópia profunda (deep copy): copia o dict principal, mas não sofre as alterações afetadas do restante do código
import copy

pessoa = {
    'nome' : 'Otávio',
    'idade' : '25',
    'sobrenome' : 'Buffon',
    'dado1' : [1,2,3]
}



copia1 = pessoa.copy()

copia2 = copy.deepcopy(pessoa)

copia2['idade'] = '26'
copia2['dado1'][0] = 3
copia2['dado1'][1] = 3
copia1['dado1'][1] = 0

print(copia1)
print(copia2)
print(pessoa)