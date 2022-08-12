import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.add_move_and_delete()
    # player_and_car collision detector:
    # when abs() player.ycor() - car.ycor() <= 10 and player.distance(car) <= 25:
    # --> Game over
    for car in cars.cars_list:
        y1 = player.ycor()
        y2 = car.ycor()
        if abs(y1 - y2) <= 10 and player.distance(car) <= 25:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        scoreboard.level_up()
        player.level_up()
        cars.level_up()


screen.exitonclick()
# [done] create and move the player object
# [done] create and move the cars. also delete them from car_list
# [done]detect collision between player and car
# detect when player reach finishing line and increase the level
