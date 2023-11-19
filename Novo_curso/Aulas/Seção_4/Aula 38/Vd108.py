"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcaçados.
"""
x = 1


def escopo():
    # global x
    x = 10
    print(x)
    def escopo_2():
        # global x
        x = 11
        global y
        y = 2 
        
        print(x, y)
    escopo_2()
    print(x)

print(x)
escopo()
print(x)

try:
    print(y)

except NameError:
    print('nâo é possível printar o y')