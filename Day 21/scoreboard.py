from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.pencolor("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score[0]} | {self.score[1]}", align=ALIGNMENT, font=FONT)

    def increase(self, person):
        self.clear()
        if person == "player":
            self.score[0] += 1
        else:
            self.score[1] += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)