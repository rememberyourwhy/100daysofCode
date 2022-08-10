from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

score = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    # Detect collision with left paddle
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect paddle miss the ball
    # right paddle misses
    elif ball.xcor() > 380:
        ball.refresh()
        score.l_point()
    # left paddle misses
    elif ball.xcor() < -380:
        ball.refresh()
        score.r_point()

screen.exitonclick()


# Bookmark1: Why using 380:
# because we want to make sure that the paddle missed the ball
# if we choose a smaller number, the paddle might still have a chance
# to catch the ball, but it will be already reset
