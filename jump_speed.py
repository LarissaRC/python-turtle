import turtle

alex = turtle.Turtle()

# A velocidade não pode ser menor do que 0 e maior que 10
alex.speed(10)

for i in range(120):
    alex.forward(100)
    alex.right(30)
    alex.left(60)
    alex.forward(50)
    alex.right(50)
    alex.right(30)

    alex.penup()
    alex.setposition(0, 0)
    alex.pendown()

    alex.right(1)

turtle.done()