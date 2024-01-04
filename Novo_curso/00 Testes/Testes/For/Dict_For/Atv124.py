perguntas = [{'pergunta' : 'Quanto é 2+2?',
              'opções' : ['3','4','5','6'],
              'resposta' : '4'},
             {'pergunta' : 'Quanto é 2x3?',
              'opções' : ['3','4','5','6'],
              'resposta' : '6'},
             {'pergunta' : 'Quanto é 10/2?',
              'opções' : ['3','4','5','6'],
              'resposta' : '5'}
            ]

qtd_acertos = 0

for pergunta in perguntas:
    print(pergunta['pergunta'])

    for i, opcao in enumerate(pergunta['opções']):
        print(f'{i})',opcao)
    print()

    escolha = input('Escolha a opção com número respectivo a resposta: ')

    acerto = False
    escolha_int = None
    qtd_opcoes = 0
