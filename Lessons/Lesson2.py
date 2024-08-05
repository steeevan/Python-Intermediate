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
