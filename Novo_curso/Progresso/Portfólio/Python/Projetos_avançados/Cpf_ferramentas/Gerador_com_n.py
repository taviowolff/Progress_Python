# Função para calcular dígitos verificadores de um CPF
def calcula_digitos_verificadores(cpf_parcial):
    # Primeiro dígito verificador
    soma_1 = sum(int(cpf_parcial[i]) * (10 - i) for i in range(9))
    digito_1 = 11 - (soma_1 % 11)
    digito_1 = 0 if digito_1 >= 10 else digito_1
    
    # Segundo dígito verificador
    soma_2 = sum(int(cpf_parcial[i]) * (11 - i) for i in range(9)) + digito_1 * 2
    digito_2 = 11 - (soma_2 % 11)
    digito_2 = 0 if digito_2 >= 10 else digito_2
    
    return digito_1, digito_2

# Gerando todas as combinações de CPF possíveis com base nos 7 primeiros dígitos dados
cpf_base = "1234567" 
cpfs_possiveis = []

# Para cada possível combinação de "xx" (00 a 99)
for i in range(100):
    meio = f"{i:02d}"  # Formata o número para ter sempre 2 dígitos
    cpf_parcial = cpf_base + meio  # Concatena os 7 dígitos iniciais com os 2 do meio
    digito_1, digito_2 = calcula_digitos_verificadores(cpf_parcial)  # Calcula os dígitos verificadores
    cpf_completo = f"{cpf_parcial}{digito_1}{digito_2}"  # CPF completo com dígitos verificadores
    cpfs_possiveis.append(cpf_completo)

cpfs_possiveis[:10]  # Exibir os primeiros 10 CPFs possíveis para amostra

[print(cpf) for cpf in cpfs_possiveis]
