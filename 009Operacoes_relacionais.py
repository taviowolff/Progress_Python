"""
Operadores Relacionais - aula 10
== igual
> maior que
>= maior ou igual a
<  menor que
<= menos ou igual a
!= diferente
"""
nome = input('qual é o seu nome? ')
idade = int(input('qual sua idade? '))

"""
e_maior = 18

if idade >= e_maior:
    print(f'{nome} pode pegar empréstimo')
else:
    print(f'{nome} nÃ£o pode pegar empréstimo')
"""

e_maior = 30
e_menor = 20

if idade >= e_menor and idade <= e_maior:
    print(f'{nome} pode pegar empréstimo')
else:
    print(f'{nome} nÃ£o pode pegar empréstimo')