# Nesse arquivou vou mostrar na prática a utilização de alguns metodos utilizando and, or, not

# Aqui vou definir uma senha como se já estivessa salva em um suposto banco de dados
senha_usario = '12345'

# Aqui estaremos estaremos definindo a senha que o usuário escreveu para futuras verificações com a senha_usario
inserir_senha = input('Digite a senha: ')

if inserir_senha == senha_usario:
    print('Senha correta!')
    print('Você está logado')

else:
    print('Senha incorreta!')