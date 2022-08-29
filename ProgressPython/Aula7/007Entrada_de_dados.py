"""
entrada de dados do usuário
Para isso usaremos o comando 'input' que introduz um valor a uma variável.
Em alguma ocasiões precisamos definifir um valor final que será trazido como no primeiro exemplo. 
isso serve para Float, Bool, Int e Str.
"""
idade = int(input('qual sua idade? ')) 
# como queremos um inteiro para definir a idade precisamos definir como mostrados .int(input('idade? '))

nome = input('Qual seu nome? ')

soma = idade + idade

mult = idade * idade

print(f'olá {nome}, vocé tem {idade} anos.')

print(f'sua idade somada a ela mesma é {soma} ' f'e multiplicada por ela mesma é {mult}')