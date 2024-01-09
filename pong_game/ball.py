from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        xcor_new = self.xcor() + 10
        ycor_new = self.ycor() + 10
        self.goto(xcor_new, ycor_new)
