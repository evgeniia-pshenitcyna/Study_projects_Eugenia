from turtle import Turtle, Screen

bibi = Turtle()
screen = Screen()


def move_forwards():
    bibi.forward(10)


def move_backwards():
    bibi.backward(10)


def turn_left():
    new_heading = bibi.heading() + 10
    bibi.setheading(new_heading)


def turn_right():
    bibi.right(10)


def clear():
    bibi.clear()
    bibi.penup()
    bibi.home()
    bibi.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
