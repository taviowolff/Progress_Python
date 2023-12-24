"""
Closure e funções que retornam outras funções 
"""

def criar_saudacao (saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao ('bom dia')
falar_boa_tarde = criar_saudacao ('boa tarde')

for nome in ['Otávio','Jorge','Igor']:
    print(falar_boa_tarde(nome))
    print(falar_bom_dia(nome))