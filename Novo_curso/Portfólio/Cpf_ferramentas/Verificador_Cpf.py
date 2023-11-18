import re
import sys

# cpf_enviado_pelo_usuario = input('Seu CPF:')
cpf = input('Digite seu CPF: ')

cpf_verificador = re.sub(
    r'[^0-9]',
    '',
    cpf
) # essa linha de código faz com que qualquer coisa que não sejam número entre 0 a 9 seja trocados por espaço vazio

entrada_e_sequencial = cpf == cpf[0] * len(cpf) # confere se há sequência

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit() # quebra de código houver dados sequenciais

nove_digitos = cpf_verificador[0:9]

contador_regressivo_1 = 10

resultado_digito1 = 0
for digito_1 in nove_digitos:
    resultado_digito1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = ((resultado_digito1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito2 = 0
for digito_2 in dez_digitos:
    resultado_digito2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = ((resultado_digito2 * 10) % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_checado = (f'{nove_digitos}{digito_1}{digito_2}')

if cpf_verificador == cpf_checado:
    print(f'{cpf}')
    print('CPF Válido')
else:
    print('CPF inválido')
