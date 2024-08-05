'''
Lesson 6: Tkinter Movement
Objective: Use Tkinter to create an interactive Pong game.

Drawing and Moving Shapes in Tkinter

Creating a canvas:
Canvas widget is used to draw shapes.
'''
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Animation")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw a rectangle
rect = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

# Function to move the rectangle
def move_rect():
    canvas.move(rect, 5, 0)
    root.after(50, move_rect)

move_rect()

# Run the application
root.mainloop()
'''
Creating the Pong Game

Setting up the game window and canvas:
Create paddles and ball.
Implement game mechanics: paddle movement, ball bouncing.
'''
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Pong Game")

# Create a canvas
canvas = tk.Canvas(root, width=800, height=400, bg="black")
canvas.pack()

# Create paddles and ball
paddle1 = canvas.create_rectangle(30, 150, 50, 250, fill="white")
paddle2 = canvas.create_rectangle(750, 150, 770, 250, fill="white")
ball = canvas.create_oval(390, 190, 410, 210, fill="white")

# Variables for ball movement
ball_dx = 3
ball_dy = 3

# Function to move paddles
def move_paddle(event):
    key = event.keysym
    if key == "w":
        canvas.move(paddle1, 0, -20)
    elif key == "s":
        canvas.move(paddle1, 0, 20)
    elif key == "Up":
        canvas.move(paddle2, 0, -20)
    elif key == "Down":
        canvas.move(paddle2, 0, 20)

canvas.bind_all("<KeyPress>", move_paddle)

# Function to move the ball
def move_ball():
    global ball_dx, ball_dy
    canvas.move(ball, ball_dx, ball_dy)
    ball_pos = canvas.coords(ball)
    if ball_pos[1] <= 0 or ball_pos[3] >= 400:
        ball_dy = -ball_dy
    if ball_pos[0] <= 0 or ball_pos[2] >= 800:
        ball_dx = -ball_dx
    root.after(50, move_ball)

move_ball()

# Run the application
root.mainloop()
