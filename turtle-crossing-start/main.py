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
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            print("Game over.")
            scoreboard.game_over()
            game_is_on = False

    #Detect successful crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.level_up()

screen.exitonclick()
