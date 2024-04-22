# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


def invert_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('parametro deve ser uma string')


inverte_string_checando_parametro = criar_funcao(invert_string)
invertida = inverte_string_checando_parametro('Otávio')
print(invertida)