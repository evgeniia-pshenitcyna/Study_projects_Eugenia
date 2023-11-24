from turtle import Turtle, Screen

bibi = Turtle()
bibi.shape("turtle")
bibi.color("magenta")

#for i in range(4):
    #bibi.forward(80)
    #bibi.right(90)

for i in range(15):
    bibi.forward(10)
    bibi.up()
    bibi.forward(10)
    bibi.down()

screen = Screen()
screen.exitonclick()
