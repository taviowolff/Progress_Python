# Controlando a quantidade de argumentos posicionais e nomeados em funções 
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados) 

# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve ser ❗APENAS❗ posicinal
# PEP 570 - Python Positional Only Parameters
# https://peps.python.org/pep-0570/

def soma (a, b, /, x, y):
    print(a + b + x + y)
soma(1, 2, 3, y=4)

# Aqui teremos uma função que ao passar (/)
# ela aceita os parâmetros nomeados e 
# não nomeados(posicionais) após a (/)
# Mas apenas posicinais antes da (/)


# 1 e 2 posicinais / 3, posicional e 4 nomeado
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗NÃO SUGA❗ valores.
# PEP 3102 - Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# Keyword-only arguments são parâmetros que só podem ser passados por \
# nome, não por posição. Eles foram introduzidos na PEP 3102 e foram 
# incluídos no Python 3.0.

# Sintaxe:
# python

def function(*, a, b):
    pass

# Tudo após o asterisco * deve ser apenas por palavra-chave (keyword).
# No exemplo acima, a e b devem ser passados como argumentos nomeados.

def saudacao(*, name="User"):
    print(f"Hello, {name}!")

saudacao(name="Alice")  # Correto
# saudacao("Alice")  # Erro, `name` deve ser passado como argumento nomeado



# UNINDO Positional-only e Keyword-only

# Você pode combinar ambos para criar funções que tenham parâmetros posicionais, 
# parâmetros que podem ser tanto posicionais quanto nomeados, e parâmetros que 
# são apenas por palavra-chave.

# Exemplo:

def func (a, b, /, c, *, d):
    pass

# Uso correto:
func(1, 2, c=3, d=4)

# argumento a -> só pode ser posicional
# argumento b -> só pode ser posicional
# argumento c -> pode ser tanto posicional quanto nomeado
# argumento d -> só pode ser nomeado

# Uso incorreto:
# func(a=1, b=2, c=3, d=4)  # Erro, `a` e `b` são somente posicionais

# Esses recursos ajudam a criar APIs mais claras e flexíveis, controlando 
# como os argumentos são passados para as funções e mantendo compatibilidade e legibilidade.



