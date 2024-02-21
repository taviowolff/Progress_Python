# try, excpet, else e finally
try:
    # print(1) esse aqui seria executado antes do erro
    print(8/0)
    print(1) # como esse comando é dado depois do erro, ele não é executado

except ZeroDivisionError:
    print("Erro: divisão por zero.")

else:
    print("Ainda aparece esse else")

finally:
    print(2)
