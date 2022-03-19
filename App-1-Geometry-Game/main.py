from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle: "Rectangle"):  # rectangle is Rectangle object instance
        """ Since the Rectangle is declared before it's created blow, so the name Rectangle doesn't yet exist.
         to solve it, we can use a string with the name.This doesn't affect how your IDE sees the declaration;
         strings are looked up once the whole module is loaded, and are resolved as a valid Python expression
         in the current context. Since the class Rectangle exists once the whole module is loaded, the string
         'Rectangle' can properly be converted to the class object. """

        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1: Point, point2: Point) -> None:  # Point class was already created before declaring
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


# It's a good practice to extend a class instead of add feature on top of it if that parent class is already well-built
# GuiRectangle (child class) inherit all attributes and methods from Rectangle (parent class)
# And we can define additional attributes and methods.
class GuiRectangle(Rectangle):

    def draw(self, canvas: turtle.Turtle):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)




# inherit Point class
class GuiPoint(Point):

    def draw(self, canvas, dot_size = 5, dot_color ="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(dot_size, dot_color)

        turtle.done()


# Create rectangle object
rectangle = GuiRectangle(Point(randint(0, 100), randint(0, 100)),
                         Point(randint(100, 200), randint(100, 200)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))


# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

myturtle = turtle.Turtle()

rectangle.draw(canvas = myturtle)
user_point.draw(canvas = myturtle)