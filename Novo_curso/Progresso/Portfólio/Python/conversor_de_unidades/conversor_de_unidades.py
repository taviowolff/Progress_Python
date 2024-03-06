
def conversor_temperatura(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

celsius = float(input('Qual é a temperatura em graus Celsius agora? '))
fahrenheit = conversor_temperatura(celsius)
print(f'A temperatura atual em Graus Fahrenheit é {fahrenheit}')