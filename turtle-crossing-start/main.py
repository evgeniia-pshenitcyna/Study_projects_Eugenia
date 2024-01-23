import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")
car = CarManager()
scoreboard = Scoreboard()
a = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move(0)
    a += 1
    if a > 6:
        new_car = CarManager()
        new_car.move(0)
        scoreboard.update_scoreboard()
        a = 0
    if player.distance(car) < 20:
        print("Game over.")
        game_is_on = False
    if player.position() == (0, -280):
        car.move(10)


screen.exitonclick()
