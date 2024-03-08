def calcular_despesas(despesas):
    total = sum(despesas)
    return total

despesas = []

while True:
    valor = float(input('Digite o valor da despesa(0 para sair): '))
    if valor == 0:
        break
    despesas.append(valor)

total_despesas = calcular_despesas(despesas)
print(f'O valor total das despesas foi de R${total_despesas:.2f}')