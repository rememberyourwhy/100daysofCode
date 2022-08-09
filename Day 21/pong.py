import time
from turtle import Screen
from ball import Ball
from paddle import Paddle, PaddleComputer
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
score = ScoreBoard()
ball = Ball()
paddle = Paddle()
paddle_cp = PaddleComputer()

game_is_on = True
screen.update()
screen.listen()
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")


def ball_collision_paddle(ball, paddle):
    for segment in paddle.segments:
        if segment.distance(ball) < 20:
            return True
    return False

def ball_out(ball):
    if ball.xcor() > 450:
        return "computer"
    elif ball.xcor() < -450:
        return "player"
    else:
        return False

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.forward(20)
    ball_collision_wall = ball.collision_with_wall()
    if ball_collision_wall:
        ball.change_heading()
    if ball_collision_paddle(ball, paddle) or ball_collision_paddle(ball, paddle_cp):
        ball.change_heading_reverse()
    if ball_out(ball):
        person_who_goal = ball_out(ball)
        score.increase(person_who_goal)
        ball.refresh()
    if score.score[0] == 3 or score.score[1] == 3:
        score.game_over()
        game_is_on = False

screen.exitonclick()