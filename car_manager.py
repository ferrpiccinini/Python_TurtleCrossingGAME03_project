COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
from turtle import *
import random

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.list_car = []

    def create_car(self):
        car = Turtle("square")
        car.shapesize(0.8,1.5)
        car.penup()
        car.color(random.choice(COLORS))
        car.goto(300,random.randint(-200,300))
        self.list_car.append(car)

