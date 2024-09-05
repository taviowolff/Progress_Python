# concatenando strings
# a = 'banana'
# b = 'split'
# c = a + ' '+ b
# print(a+b)
# print(c)

# in como operador lógico para str
# palavra = 'Banana'
# print('ana' in palavra) # True
# print('z' in palavra) # False

# operações com str
# palavra = 'cebola'
# # if palavra == 'Banana':
# #     print('Tudo certo, é bananas')

# if palavra < 'castelohibrido':
#     print(f'Sua palavra ,{palavra}, vem antes de banana.')
# elif palavra > 'banana':
#     print(f'Sua palavra,{palavra}, vem depois de banana.')
# else:
#     print('Tudo certo, é banana.')


# biblioteca str
# Para acessar a biblioteca basta você declarar uma variável como str
# e digitar um '.' logo a sua frente depois de chamá-la 
# x = 'Pular'
# x = x.upper() # dentro da biblioteca selecionei o metodo UPPER para deixar em maiúsculo
# print(x) # PULAR

# comparação com str

# buscando em str
# fruit = 'banana'
# #        012345  
# where1 = fruit.find('ba')
# where2 = fruit.find('nana')
# where3 = fruit.find('z')
# print(where1) # indice 0
# print(where2) # encontrado no indice 2
# print(where3) # Quando o elemento não é encontrado dentro da str retorna -1

# repondo um texto str
# saudacao = 'Olá Otávio'
# saudacao_nova = saudacao.replace('Otávio', 'Nathália')
# print(saudacao_nova)

# cortando espaços em branco 
# x = '   Olá, mundo!'
# x = x.lstrip() # remove espaços em branco da esquerda 
# print(x)

# y = 'Olá, Mundo!   '
# y = y.rstrip() # remove espaços em branco da direita
# print(y)

# z = '    Olá, Mundo!    '
# z = z.strip() # remove os espaços da direita e esquerda
# print(z)

# analisando e extraindo
mensagem = 'Olá seja bem vindo, seu email é otaviowolff@outlook.com.br Qui 20240905 1904'
achar1 = mensagem.find('@')
print(achar1)

achar2 = mensagem.find(' ', achar1)
print(achar2)

host_user = mensagem[achar1+1 : achar2]
print(host_user)