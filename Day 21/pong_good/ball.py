from turtle import Turtle
from random import randint


BALL_STARTING_HEADING = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")

        random_heading_index = randint(0, 3)
        self.setheading(BALL_STARTING_HEADING[random_heading_index])
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
