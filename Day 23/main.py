import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
screen.exitonclick()
# create and move the player object
# create and move the cars. also delete them from car_list
# detect collision between player and car
# detect when player reach finishing line and increase the level
