import turtle

alex = turtle.Turtle()

num_lados = 8
lado_tamanho = 70
angulo = 360.0 / num_lados

for i in range(num_lados):
    alex.forward(lado_tamanho)
    alex.right(angulo)

turtle.done()