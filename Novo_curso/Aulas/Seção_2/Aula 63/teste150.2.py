
exception_types = tuple(filter(lambda x: isinstance(vars(__import__('builtins')), type), vars(__import__('builtins'))))

try: 
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print(c)

except tuple(exception_types) as error:
    # print(mensagem)
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
