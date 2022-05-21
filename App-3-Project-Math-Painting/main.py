from canvas import Canvas
from shape import Rectangle, Square

# Get the canvas spec from user
canvas_height = int(input("Enter canvas height: "))
canvas_width = int(input("Enter canvas width: "))

# Make a color and color code dict
colors = {"white": [255, 255, 255], "black": [0, 0, 0]}
# Get the canvas color from user
canvas_color = input("Enter canvas color (white or black): ").lower()

# canvas instantiation
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])


while True:
    shape_type = input("What do you like to draw, Square or Rectangle? And, Enter \"quit\" to quit. ")

    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green should the rectangle have? "))
        blue = int(input("How much blue should the rectangle have? "))

        # rectangle instantiation
        rectangle = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=[128, 0, 128])
        rectangle.draw(background=canvas)

    if shape_type.lower() == "square":
        sq_x = int(input("Enter x of the square: "))
        sq_y = int(input("Enter y of the square: "))
        sq_side = int(input("Enter the side length of the square: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green should the square have? "))
        blue = int(input("How much blue should the square have? "))

        # square instantiation
        square = Square(x=sq_x, y=sq_y, side=sq_side, color=[red, green, blue])
        square.draw(background=canvas)

    if shape_type.lower() == "quit":
        break


canvas.make("files/paint.png")






