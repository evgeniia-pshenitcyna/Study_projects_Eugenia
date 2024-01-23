from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.write(f"Level: {self.level} ", True, align="center")

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.level, align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
