# Nesse arquivou vou mostrar na prática a utilização de alguns metodos utilizando and, or, not

# Aqui vou definir uma senha como se já estivessa salva em um suposto banco de dados
senha_usario = '12345'

# Verificador para saber se o usuário quer entrar
entrada = input('[E]ntrar [S]sair: ')

# Aqui estaremos estaremos definindo a senha que o usuário escreveu para futuras verificações com a senha_usario
inserir_senha = input('Digite a senha: ')

# Ocorre a verificação da senha do usuário com a senha inserida
# Caso a senha também seja dado nenhuma valor
# Se um desses dois retornar True as linhas de códigos serão lidas abaixo
if inserir_senha != senha_usario or inserir_senha == '':
    print('Senha incorreta')

elif inserir_senha == senha_usario:
    print('Senha correta!')
    print('Você está logado')

else:
    print('Error!')