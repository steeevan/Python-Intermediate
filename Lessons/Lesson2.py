'''
Lesson 2: Turtle and Random
Objective: Learn to create spirographs and intricate drawings with Turtle and the Random library.

Introduction to the Random Library

Generating random numbers:
random.randint(a, b): Return a random integer N such that a <= N <= b.
random.choice(sequence): Return a randomly chosen element from a non-empty sequence.
'''
import turtle
import random

# Create a turtle object
t = turtle.Turtle()

# Random walk
for _ in range(100):
    t.forward(30)
    t.right(random.randint(0, 360))

turtle.done()
'''
Creating Spirographs

Understanding spirographs and their mathematical basis:
A spirograph is a geometric drawing that produces a curve known as a hypotrochoid.
Using loops and turtle, we can create these intricate designs.
'''
import turtle
import random

# Create a turtle object
t = turtle.Turtle()
t.speed(0)

# Function to draw a spirograph
def draw_spirograph(size):
    for _ in range(int(360 / size)):
        t.pencolor(random.choice(['red', 'green', 'blue', 'yellow', 'purple']))
        t.circle(100)
        t.right(size)

draw_spirograph(10)

turtle.done()
Lesson 3: Turtle and Math
Objective: Utilize the Math library to model mathematical concepts and recursive algorithms.

Introduction to the Math Library

Using math functions:
math.sin(x), math.cos(x): Return the sine and cosine of x (in radians).
math.pi: The mathematical constant π.
python
Copy code
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
Recursive Algorithms with Turtle

Introduction to recursion:
Recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem.
python
Copy code
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
Lesson 4: Turtle Project
Objective: Apply the knowledge of Turtle graphics to create a comprehensive project.

Project Planning and Design

Brainstorming project ideas:
Choose a project that incorporates various Turtle graphics concepts learned so far.
Examples: Drawing a complex fractal, creating a scene with multiple objects.
Activity: Outline and design your Turtle project.

Turtle Project Implementation

Implementing the project step-by-step:
Break down the project into smaller tasks.
Write code for each task and test it before moving on.
Activity: Complete the Turtle project and present it.
