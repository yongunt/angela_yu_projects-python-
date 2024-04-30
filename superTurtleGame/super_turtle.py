from turtle import Turtle
import tkinter as tk
from tkinter import ttk
import random

COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "white", "cyan", "dark blue", "grey", "pink"]

class SuperTurtle(Turtle):

    def __init__(self):
        super(SuperTurtle, self).__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()

    def put_dot(self):
        random_color = random.choice(COLORS)
        self.dot(10, random_color)

    def move_forward(self):
        self.forward(20)

    def turn_right(self):
        self.right(20)

    def turn_left(self):
        self.left(20)



class Window(tk.Tk):

    def __init__(self):
        super(Window, self).__init__()

        self.title("Super Turtle Game")
        self.geometry("480x300")

        # Label
        self.label = ttk.Label(self, text="Welcome to The Super Turtle Game", font=("Ariel", 20, "bold"))
        self.label.grid(row=0, column=0, columnspan=2)

        # Buttons
        self.start_btn = ttk.Button(self, text="Start")
        self.start_btn.grid(row=1, column=1)

        self.cancel_btn = ttk.Button(self, text="Cancel")
        self.cancel_btn.grid(row=1, column=0)

