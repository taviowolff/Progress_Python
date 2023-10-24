v1 = input('Digite algo: ')

print(f'O tpo primitivo desse valor é {type(v1)}')

print(f'Só tem espaços? {v1.isspace()}')

print(f'É um número? {v1.isnumeric()}')

print(f'É alfabético? {v1.isalpha()}')

print(f'É um alfanúmerico? {v1.isalnum()}')

print(f'Está em maiúsculo? {v1.isupper()}')

print(f'Está em minúsculo? {v1.islower()}')

print(f'Está capitalizada? {v1.istitle()}')