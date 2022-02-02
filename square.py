import turtle

alex = turtle.Turtle()

# "right" rotaciona a tartaruga em n graus no sentido horário
alex.forward(50)
alex.right(90)

alex.forward(50)
alex.right(90)

alex.forward(50)
alex.right(90)

alex.forward(50)

# Agora usando backward pra voltar e left para rotacionar
# no sentido anti-horário
alex.forward(50)
alex.left(90)

alex.forward(50)
alex.left(90)

alex.forward(50)
alex.left(90)

alex.forward(50)

alex.backward(50) # Voltando
alex.right(90)
alex.forward(50)

alex.right(90)
alex.forward(50)

alex.right(90)
alex.forward(50)

alex.right(90)
alex.forward(50)

# Quarto quadrado
alex.right(90)
alex.forward(100)

alex.left(90)
alex.forward(50)

alex.left(90)
alex.forward(50)

alex.left(90)
alex.forward(50)

turtle.done()