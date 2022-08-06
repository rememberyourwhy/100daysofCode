# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)  # an object
# timmy.shape("turtle")   # use shape method to change its shape to turtle
# timmy.color("chartreuse")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)  # print the value of screen height attribute
# my_screen.exitonclick()
# # The "my_screen = Screen()" line will make turtle screen window turn off after our code finish running
# # but exitonclick method keep it open until we click on the screen

# Todo: Do coding exercise for turtle module

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)