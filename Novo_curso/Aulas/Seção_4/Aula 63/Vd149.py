# Try, except, else e finally

# a = 18
# b = 0
# c = a + b

try: 
    a = 18
    b = f
    # print(b[0])
    c = a / b
    print(c)

# except ZeroDivisionError: # se caso b = 0
#     print('Não pode dividir por zero!')

except NameError:
    print('b não pode ser uma letra')

except (TypeError, IndexError):
    print('TypeError + Index')    

except Exception:
    print('Erro desconhecido')