from turtle import Turtle


ALIGNMENT = "Center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("black")
        self.hideturtle()
        self.pu()
        self.level = 1
        self.goto(-260, 260)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
