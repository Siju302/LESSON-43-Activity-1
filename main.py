import turtle

# creating canvas
turtle.Screen().bgcolor("lightblue")

sc = turtle.Screen()
sc.setup(700, 500)

turtle.title("Welcome to the Turtle Window")

# turtle object creation
board = turtle.Turtle()

#creating a square
for i in range(4):
    board.forward(300)
    board.left(90)
    i = i+1