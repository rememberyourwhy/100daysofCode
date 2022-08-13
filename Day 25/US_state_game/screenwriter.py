from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 10, "normal")


class ScreenWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color("black")

    def write_on_coordinate(self, message, coordinate):
        self.goto(coordinate)
        self.write(message, align=ALIGNMENT, font=FONT)


