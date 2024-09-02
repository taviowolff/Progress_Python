
# n = 5  # Número de linhas da pirâmide
# for i in range(n, 0, -1):
#     print(' ' * (n - i) + '*' * i)

n = 5  # Número de linhas da pirâmide
pyramid = [' ' * (n - i) + '*' * i for i in range(n, 0, -1)]
for row in pyramid:
    print(row)