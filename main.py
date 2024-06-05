import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

NUMBER = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

carros = CarManager()
player = Player()
scoreboard = Scoreboard()
player.move_turtle()
car_list = carros.list_car
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_ = random.randint(1,NUMBER)
    player.forward(10)
    if random_ == 2:
        carros.create_car()
    for car in car_list:
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False
        if player.distance(player.xcor(),300) < 10:
            scoreboard.add_score()
            player.goto(0,-280)
            if NUMBER != 1:
                NUMBER -= 1
        car.back(10)

screen.exitonclick()