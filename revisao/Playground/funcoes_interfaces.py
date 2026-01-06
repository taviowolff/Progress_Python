@ -1,28 +1,10 @@
import turtle
from time import sleep

# Em vez de makeTurtle, usamos turtle.Turtle()
t = turtle.Turtle()

# Agora usamos o 't' para dar comandos
# t.forward(100)

# t.left(90)

# t.forward(100)

# t.left(-90)

# t.forward(-100)

# tocar linha inicial e final
t.goto(0, 100)  # Move para o ponto (0, 100)
sleep(2)
t.goto(100, 100)  # Move para o ponto (0, 0)
sleep(2)
t.goto(100, 0)
sleep(2)
t.goto(0, 0)  # Volta para o ponto inicial (0, 0)
sleep(2)
# Importante: mantém a janela aberta
turtle.done()
