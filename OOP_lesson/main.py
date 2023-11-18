#from turtle import Turtle, Screen

#eugene = Turtle()
#print(eugene)
#eugene.shape("turtle")
#eugene.color("DeepPink2")
#eugene.forward(100)

#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Skirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

