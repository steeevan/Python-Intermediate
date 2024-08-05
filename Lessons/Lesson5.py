'''
Lesson 5: Tkinter Widgets
Objective: Learn about creating widgets such as buttons, text boxes, etc., using the Tkinter library. Create a login page.

Introduction to Tkinter

Basic window creation:
Tkinter is a standard GUI (Graphical User Interface) library for Python.
tk.Tk(): Create the main window of the application.
'''
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic Window")

# Add a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Run the application
root.mainloop()
Creating a Login Page
'''
Using Entry for text input:
Entry widget is used to accept single-line text input.
'''
import tkinter as tk

def login():
    username = entry_username.get()
    password = entry_password.get()
    print(f"Username: {username}, Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Add widgets
label_username = tk.Label(root, text="Username")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password")
label_password.pack()
entry_password = tk.Entry(root, show='*')
entry_password.pack()

button_login = tk.Button(root, text="Login", command=login)
button_login.pack()

# Run the application
root.mainloop()
