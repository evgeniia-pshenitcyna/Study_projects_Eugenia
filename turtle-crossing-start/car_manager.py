from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))
        x_pos = 280
        y_pos = random.randint(-250, 250)
        self.goto(x_pos, y_pos)

    def move(self, speed_increase):
        self.forward(MOVE_INCREMENT+speed_increase)
