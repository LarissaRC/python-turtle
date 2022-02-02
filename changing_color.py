import turtle

alex = turtle.Turtle()

alex.pencolor("blue")

for i in range(5):
    alex.forward((i+1) * 5)
    alex.right(90)

alex.pencolor("#6534eb")

for i in range(5):
    alex.forward((i+5) * 5)
    alex.right(90)

alex.pencolor("#eb3471")

for i in range(5):
    alex.forward((i+10) * 5)
    alex.right(90)

alex.pencolor("#34eb6b")

for i in range(5):
    alex.forward((i + 15) * 5)
    alex.right(90)

alex.pencolor("#d3eb34")

for i in range(5):
    alex.forward((i + 20) * 5)
    alex.right(90)

alex.pencolor("#eb8c34")

for i in range(5):
    alex.forward((i + 25) * 5)
    alex.right(90)

alex.pencolor("#eb3434")

for i in range(5):
    alex.forward((i + 30) * 5)
    alex.right(90)

alex.pencolor("#34ebc9")

for i in range(5):
    alex.forward((i + 35) * 5)
    alex.right(90)

turtle.done()