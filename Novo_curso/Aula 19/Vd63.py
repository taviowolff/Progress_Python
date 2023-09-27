"""
while + while 
loop dentro de um loop
serve para fazer tarefas repetitivas
dentro de outras tarefas repetitivas
"""

x = 1

while x <= 3:
    print(f'Loop externo: {x}')

    y = 1
    while y <= 3:
        print(f'loop interno: -{y}')
        y += 1
    x += 1

print('acabou os loops')