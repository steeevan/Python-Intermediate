'''
Lesson 1: Turtle Functions
Objective: Review the basics of the Python Turtle library by creating various shapes.

Introduction to Turtle Graphics

Turtle Library Basics:
The Turtle library is a popular way for introducing programming to kids. It provides a virtual canvas where you can draw using a turtle that moves on the screen.
Basic commands:
forward(distance): Move the turtle forward by the specified distance.
backward(distance): Move the turtle backward by the specified distance.
right(angle): Turn the turtle clockwise by the specified angle.
left(angle): Turn the turtle counterclockwise by the specified angle.
penup(): Lift the pen so that moving the turtle does not draw on the canvas.
pendown(): Lower the pen to draw when the turtle moves.


'''
import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Close the turtle graphics window
turtle.done()
'''
Activity: Draw a house using basic shapes (square and triangle).
Advanced Shapes and Custom Functions

Creating polygons with a loop:
Using loops, we can create polygons of any number of sides.
'''
import turtle

# Create a turtle object
t = turtle.Turtle()

# Function to draw a polygon
def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

# Draw a pentagon
draw_polygon(5, 100)

turtle.done()

pencolor(color) # Set the color of the pen.
fillcolor(color) # Set the color used to fill shapes.
begin_fill() # Begin filling the shape.
end_fill() # End filling the shape.

import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a filled star
t.fillcolor("yellow")
t.begin_fill()
for _ in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()

turtle.done()
