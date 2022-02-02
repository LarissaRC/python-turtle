import turtle

alex = turtle.Turtle()

dot_distance = 30
width = 5
height = 7

alex.penup() # Não vai mais "riscar" a tela

for i in range(height):
    for j in range(width):
        alex.dot() # Desenha um ponto na tela
        alex.forward(dot_distance) # Anda sem tocar na tela
    # Voltar para o começo da linha
    alex.backward(dot_distance * width)
    # Descer para a próxima linha
    alex.right(90)
    alex.forward(dot_distance)
    alex.left(90)

turtle.done()