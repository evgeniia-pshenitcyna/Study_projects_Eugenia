# Create a ball and make it move
# Detect collision with the wall and bounce
# Detect the collision with the paddle
# Detect when paddle misses
# Keep score
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(x_cor=350, y_cor=0)
l_paddle = Paddle(x_cor=-350, y_cor=0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.15)
    screen.update()
    ball.move()

screen.exitonclick()
