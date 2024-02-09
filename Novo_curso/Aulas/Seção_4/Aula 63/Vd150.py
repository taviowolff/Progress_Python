# Try, except, else e finally

# a = 18
# b = 0
# c = a + b

try: 
    a = 18
    b = 1
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print(c)

# except ZeroDivisionError: # se caso b = 0
#     print('Não pode dividir por zero!')

except NameError:
    print('b não pode ser uma letra')

except (TypeError, IndexError) as error:
    print('TypeError + IndexError')    
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)

except Exception:
    print('Erro desconhecido')