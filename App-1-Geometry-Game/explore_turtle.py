import turtle

# Create a canvas instance by calling the Turtle() class
myturtle = turtle.Turtle()

# pen up before moving
myturtle.penup()
# Go to a certain coordinate before starting
myturtle.goto(50, 70)

# pen down before drawing
myturtle.pendown()
myturtle.forward(100)  # Move 100 pixel forwards
myturtle.left(90)  # Turn 90 degrees to left
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()