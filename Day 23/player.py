from turtle import Turtle
from random import randint


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)
#the player will be able to move (user input keyboard)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        print("move y)")