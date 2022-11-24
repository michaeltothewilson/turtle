# Turtle Triforce
# Creating the Triforce from Zelda in Turtle

# Import Starter Pack
import turtle

# Screen Setup
screen = turtle.Screen()
turtle.title("Turtle Triforce")
turtle.screensize(canvwidth=400, canvheight=400, bg="dark green")

# Turtle Setup
t = turtle.Turtle()
t.fillcolor("gold")
t.pencolor("black")
t.pensize(1)
t.shape("turtle")

# Triangle Function


def equalTriangle(size):
    for i in range(3):
        t.forward(size)
        t.left(120)


# Triangle Properties
size = 200
height = 0.86602540378 * size

# Coordinates
x = [0, size * -1, (size/2) * -1]
y = [(size/2) * -1, (size/2) * -1, ((size/2) * -1) + height]

# Draw Triforce
for i in range(3):
    # Position the Turtle
    t.penup()
    t.goto(x[i], y[i])
    t.pendown()

    # Draw a Triangle
    t.begin_fill()
    equalTriangle(size)
    t.end_fill()

# Hide Turtle
# t.hideturtle()
t.penup()
t.goto(((size/2) + 100) * -1, 0)
turtle.done()
