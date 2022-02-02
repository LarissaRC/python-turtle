import turtle
from getch import getch

alex = turtle.Turtle()

char = ""
while char != 'z':
    char = getch()

    if char == "a":
        alex.left(2)
    if char == "d":
        alex.right(2)
    if char == "u":
        alex.penup()
    if char == "p":
        alex.pendown()
    if char == "w":
        alex.forward(2)

turtle.done()