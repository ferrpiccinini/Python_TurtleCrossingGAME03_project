
from turtle import *
screen = Screen()

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.speed(5)
        self.goto(0,-280)

    def move_right(self):
        self.right(90)
    def move_left(self):
        self.left(90)

    def move_turtle(self):
        screen.onkey(key="a", fun=self.move_left)
        screen.onkey(key="d", fun=self.move_right)


