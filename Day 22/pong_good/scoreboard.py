from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.pencolor("white")
        self.hideturtle()
        self.pu()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
