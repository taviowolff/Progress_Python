dicionario = {
    'produto': 'Caneta-preta',
    'valor': 2.50,
    'marca': 'BIC'
}

dc = {
    chave.upper(): valor
    if isinstance(chave, str) else chave
    for chave, valor 
    in dicionario.items()
    # if chave == 'valor'   
}

print(dc)