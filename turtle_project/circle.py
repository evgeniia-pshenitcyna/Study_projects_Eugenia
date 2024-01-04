import turtle as t
import random

bibi = t.Turtle()
bibi.shape("turtle")
t.colormode(255)
bibi.speed('fastest')


def change_color():
    """Selects a random color for a turtle"""
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    color_tuple = (R, G, B)
    return color_tuple


def draw_spirograph(step):
    for _ in range(int(360/step)):
        bibi.color(change_color())
        bibi.circle(100)
        bibi.setheading(bibi.heading()+step)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
