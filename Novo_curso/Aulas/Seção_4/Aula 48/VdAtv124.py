# criar uma lista de perguntas e respostas 

perguntas = [{'pergunta':'quanto é 2+2?',
            'opções':['1','3','4','5'],
            'resposta':'4'
            },

            {'pergunta':'quanto é 2 x 3?',
            'opções':['1','2','5','6'],
            'resposta':'6'
            },

            {'pergunta':'quanto é 2^4',
             'opções':['2','12','20','24'],
             'resposta': '24'
            }]


qtd_acertos = 0 

for pergunta in perguntas:
    print('Pergunta:', pergunta['pergunta'])

    opcoes = pergunta['opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}){opcao}')
    print()

    escolha = input('escolha o número correspondente a resposta: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')