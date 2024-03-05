def calcular_IMC(peso, altura): # Definindo uma função que retorne a conta do IMC 
    return peso / (altura ** 2)

# Recolhendo os dados 
peso = float(input('Digite seu peso: ')) 
altura = float(input('Digite sua altura em metros: '))

# Definindo a variável que receberá a função e os dados do sistema
imc = calcular_IMC(peso, altura)
print(f'Seu IMC é de {imc:.2f}') 

