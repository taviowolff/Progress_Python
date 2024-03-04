def converter_moeda(valor, taxa):
    return valor * taxa

valor = float(input('Digite o valor da quantidade da moeda que deseja: '))
taxa = float(input('Digite a taxa de câmbia em relação a moeda de seu país: '))

resultado = converter_moeda(valor, taxa)

print(f'O valor convertido é: {resultado}')