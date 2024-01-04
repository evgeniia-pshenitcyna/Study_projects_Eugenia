#import colorgram

#colors = colorgram.extract('hirst.jpg', 30)
#color_list = []

#for color in colors:
    #rgb = color.rgb
    #color_tuple = (rgb[0], rgb[1], rgb[2])
    #color_list.append(color_tuple)

#print(color_list)
import turtle as t
import random

bibi = t.Turtle()
bibi.shape("turtle")
t.colormode(255)
bibi.speed('fast')

colors_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

bibi.penup()
bibi.goto(-225, -225)
bibi.showturtle()


def draw_line():
    for a in range(10):
        new_color = random.choice(colors_list)
        bibi.color(new_color)
        bibi.dot(20)
        bibi.forward(50)


def turn_left():
    bibi.left(90)
    bibi.forward(50)
    bibi.left(90)
    bibi.forward(50)


def turn_right():
    bibi.right(90)
    bibi.forward(50)
    bibi.right(90)
    bibi.forward(50)


for line in range(5):
    draw_line()
    turn_left()
    draw_line()
    turn_right()

bibi.hideturtle()
screen = t.Screen()
screen.exitonclick()
