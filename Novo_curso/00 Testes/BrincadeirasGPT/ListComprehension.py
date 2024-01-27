precos_produtos = [100, 200, 50, 60, 30]

precos_desconto_60 = [
    desconto - ( desconto * 0.5) for desconto in precos_produtos
    if desconto >= 60
]

print(precos_desconto_60)