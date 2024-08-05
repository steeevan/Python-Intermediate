'''
Lesson 3: Turtle and Math
Objective: Utilize the Math library to model mathematical concepts and recursive algorithms.

Introduction to the Math Library

Using math functions:
math.sin(x), math.cos(x): Return the sine and cosine of x (in radians).
math.pi: The mathematical constant π.
'''
import turtle
import math

# Create a turtle object
t = turtle.Turtle()

# Draw a sine wave
t.penup()
t.goto(-360, 0)
t.pendown()
for x in range(-360, 361):
    y = math.sin(math.radians(x)) * 100
    t.goto(x, y)

turtle.done()
'''
Recursive Algorithms with Turtle

Introduction to recursion:
Recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem.
'''
import turtle

# Create a turtle object
t = turtle.Turtle()

# Function to draw a fractal tree
def draw_tree(branch_length):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15)
        t.left(40)
        draw_tree(branch_length - 15)
        t.right(20)
        t.backward(branch_length)

t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()
draw_tree(100)

turtle.done()
