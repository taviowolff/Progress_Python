"""
operadores lÃ³gicos - aula11
and, or, not,
in , not in

# and (comparação 1 e comparação 2)
#      verdadeira      falsa     =  falso
# or (comparação1 ou comparação2)
#    verdadeira      falsa       = verdadeiro

num1 = int(input('escolha um nomero para A: '))
num2 = int(input('escolha um nomero para B: '))

if num2 > num1:
    print('B é maior que A')
else:
    print('A é maior que B')
"""

print('Login')
usuario = input('Nome de usuario: ')
senha = input('Senha de usuario: ')

bd_usuario = 'otaviowolff'
bd_senha = '1234'

if bd_senha == senha and bd_usuario == usuario:
    print(f'seja bem vindo {bd_usuario}')
else:
    print('senha ou usuÃ¡rio incorretos')
    print('tente novamente')