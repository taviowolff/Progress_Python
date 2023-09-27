"""
faça um str iterável com while
"""
nome = 'Otávio Wolff'

nova_str = ''

x = 0

while x < len(nome):

    lpl = nome[x]

    nova_str += (f'-{lpl}')
    
    x += 1

    print(nova_str)
    

# print(nova_str)