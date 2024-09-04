#  if /elif      /else
#  se /se não se /se não

# entrada = input('Você quer "entrar" ou "sair"? ')

# if entrada == 'entrar':  # podemos ter um if sozinho para formar um código de condições
#     print('Você entrou no sistema')

# elif entrada == 'sair':
#     print('Você saiu do sistema')

# else:
#     print('Você não digitou nem entrar e nem sair.')


# Ao alterar uma dessas condições para o valor booleano = True
# Você ter a condição printada na sua tela
# Caso continue do jeito que está, a condição else vai ser printada 
condicao1 = False
condicao2 = False
condicao3 = False

if condicao1 == True:
    print('con1 é verdadeira') 
    print('Só um exemplo') # aqui é mostrado que pode ser colocado mais de uma linha de código dentro da condição

elif condicao2 == True:
    print('cond2 é verdadeira')

elif condicao3 == True:
    print('cond3 é verdadeira')

else:
    print('Nenhuma condição é verdadeira')