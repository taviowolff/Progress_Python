import random

# Gera um número aleatório entre 1 e 10
number = random.randint(1, 10)

# Pede para o usuário adivinhar o número
guess = int(input("Adivinhe o número (1 a 10): "))

# Verifica se o usuário acertou
if guess == number:
  print("Parabéns, você acertou!")
else:
  print("Infelizmente, você errou. O número era", number)