from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
y_coordinate = [-100, -60, -20, 20, 60, 100]
turtle_color = ["red", "orange", "yellow", "green", "blue", "purple"]

for index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(turtle_color[index])
    tim.pu()
    tim.goto(x=-230, y=y_coordinate[index])

screen.exitonclick()