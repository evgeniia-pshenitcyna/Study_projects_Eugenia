from turtle import Turtle
STEP = 20


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_cor, y_cor)

    def up(self):
        new_y = self.ycor() + STEP
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - STEP
        self.goto(self.xcor(), new_y)
