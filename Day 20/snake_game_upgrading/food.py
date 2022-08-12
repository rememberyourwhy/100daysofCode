from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Counter and big food bool
        self.count = 1
        self.is_big_food = False

        # Shape and placement
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        self.count += 1

        # big food is eaten
        if not self.is_big_food:
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.color("blue")
        # big food is coming on the way
        elif self.is_big_food:
            self.shapesize(stretch_len=2.5, stretch_wid=2.5)
            self.color("red")
            self.is_big_food = False
        else:
            pass

        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)


