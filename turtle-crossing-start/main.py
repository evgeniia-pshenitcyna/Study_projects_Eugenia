import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_1 = Player()
car_1 = CarManager()
car_2 = CarManager()
car_3 = CarManager()
car_4 = CarManager()

screen.listen()
screen.onkey(player_1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_1.move()
    car_2.move()
    car_3.move()
    car_4.move()

screen.exitonclick()
