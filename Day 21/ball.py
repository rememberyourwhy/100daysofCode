from turtle import Turtle
from random import randint
from paddle import Paddle

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

    def refresh(self):
        self.setpos(0, 0)
        random_heading_index = randint(0, 3)
        self.setheading(BALL_STARTING_HEADING[random_heading_index])

    def collision_with_wall(self):
        if self.ycor() > 280:
            return True
        elif self.ycor() < -280:
            return True
        else:
            return False

    def change_heading(self):
        if self.heading() == 45:
            self.setheading(315)
        elif self.heading() == 135:
            self.setheading(225)
        elif self.heading() == 225:
            self.setheading(135)
        elif self.heading() == 315:
            self.setheading(45)
        else:
            pass


    def change_heading_reverse(self):
        if self.heading() == 45:
            self.setheading(135)
        elif self.heading() == 135:
            self.setheading(45)
        elif self.heading() == 225:
            self.setheading(315)
        elif self.heading() == 315:
            self.setheading(225)
        else:
            pass
