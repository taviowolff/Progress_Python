"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
# Esse código consegue verificar o primeiro digito do cpf de uma maneira mais complexa

# cpf = input('Escreva seu cpf: ')
# lista_num = list(cpf)
# contador = 10
# nova_lista = []

# while contador >= 3:
#     for num in lista_num:
#         num = int(num)
#         mult = contador * num
#         nova_lista.append(mult)
#         contador -= 1

# # nova_lista.pop(-1)
# # nova_lista.pop(-1)
# soma_da_lista = 0

# for elemento in nova_lista:
#     soma_da_lista += elemento
# print(soma_da_lista)

# lista_mult = soma_da_lista * 10

# lista_rest = lista_mult % 11 

# if lista_rest > 9:
#     resultado = 0

# else:
#     resultado = lista_rest
# print(f'O primeiro digito do CPF é {resultado}')

# Esse que eu vou escrever daqui é a partir do que eu vi do professor

cpf = "15494868028"
nove_digitos = cpf[:9]
resultado_digito1 = 0
contador_regressivo_1 = 10

for digito_1 in nove_digitos:
    resultado_digito1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = ((resultado_digito1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)