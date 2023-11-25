from turtle import Turtle, Screen
import random

bibi = Turtle()
bibi.shape("turtle")
# for i in range(15):
# bibi.forward(10)
# bibi.up()
# bibi.forward(10)
# bibi.down()


def change_color():
    """Selects a random color for a turtle"""
    R = random.random()
    G = random.random()
    B = random.random()
    bibi.color(R, G, B)


def draw_figure(sides):
    """Draws a figure based on number of sides. The length of each side is always 100 steps."""
    for _ in range(sides):
        bibi.forward(100)
        angle = 360 / sides
        bibi.right(angle)


for i in range(3, 11):
    draw_figure(i)
    change_color()

screen = Screen()
screen.exitonclick()
