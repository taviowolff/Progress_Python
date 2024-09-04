'''
exercício 
- peça ao usário digitar seu nome 
- peça ao usuário digitar sua idade
- se nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertid}
        seu nome contém (ou não) espaços
        se noem tem {n} na letra
        a primeira letra do seu nome é {letra}
        a última letra do seu nome é {última letra}
se nada for digitado em nome ou idade:
    exiba: "desculpa, você deixou campos vazios"
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if idade == '' or nome == '':
    print('Você deixou espaços sem preencher') 

else:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome tem espaço')
    else:
        print('seu nome não tem espaço')
        print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a última letra do seu nome é {nome[-1]}')
