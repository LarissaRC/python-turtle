import turtle

alex = turtle.Turtle()

# Normal star spiraling
for i in range(40):
    alex.forward(i*10)
    alex.right(144)

# Exagerado agora kkkk
'''
for i in range(20):
    alex.forward(i*i)
    alex.right(144)
'''

turtle.done()