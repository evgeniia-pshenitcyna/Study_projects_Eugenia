import turtle as t
import random

bibi = t.Turtle()
bibi.shape("turtle")
directions = [0, 90, 180, 270]
bibi.pensize(5)
bibi.speed('fastest')
t.colormode(255)

def change_color():
    """Selects a random color for a turtle"""
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    color_tuple = (R, G, B)
    return color_tuple


for _ in range(200):
    bibi.color(change_color())
    bibi.forward(30)
    bibi.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
