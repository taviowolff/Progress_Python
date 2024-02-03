ganho_hora = float(input('quanto você recebe po hora? '))
ganho_mensal = (40*4)*ganho_hora
deducao_ir = (ganho_mensal * 1.11) - ganho_mensal
deducao_inss = (ganho_mensal * 1.08) - ganho_mensal
deducao_sindicato = (ganho_mensal * 1.05) - ganho_mensal

print(f'Seu salário bruto é de {ganho_mensal:.2f} reais.')
print(f'Dedução IR: -{deducao_ir:.2f}')
print(f'Dedução INSS: -{deducao_inss:.2f}')
print(f'Dedução Sindicato: -{deducao_sindicato:.2f}')
print(f'Salário líquido {ganho_mensal-deducao_inss-deducao_ir-deducao_sindicato:.2f}')