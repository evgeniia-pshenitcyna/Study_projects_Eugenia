from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []


class Snake:

    def __init__(self):
        for position in starting_position:
            my_turtle = Turtle("square")
            my_turtle.color("white")
            my_turtle.penup()
            my_turtle.goto(position)
            segments.append(my_turtle)

    def move(self):
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)
