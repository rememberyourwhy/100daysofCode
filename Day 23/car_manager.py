from turtle import Turtle
from random import randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_COORDINATES = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20,
                 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pu()
        self.random_color()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)

    def random_color(self):
        random_num = randint(0, len(COLORS) - 1)
        self.color(COLORS[random_num])

    def move(self, move_distance):
        new_x = self.xcor() - move_distance
        self.goto(new_x, self.ycor())

    def random_position(self):
        random_index = randint(0, len(Y_COORDINATES) - 1)
        new_y = Y_COORDINATES[random_index]
        self.goto(200, new_y)


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.delete_pending = []
        self.delay = 0
        self.move_distance = STARTING_MOVE_DISTANCE


    def add_car(self):
        new_car = Car()
        new_car.random_position()
        self.cars_list.append(new_car)

    def add_to_delete_pending(self, car_to_del):
        self.delete_pending.append(car_to_del)

    def delete_cars(self):
        for car in self.delete_pending:
            self.cars_list.remove(car)

    def add_move_and_delete(self):
        # delay manager
        self.delay += 1

        # add
        if len(self.cars_list) < 15 and self.delay >= 7:
            self.add_car()
            self.delay = 0

        # move
        for car in self.cars_list:
            car.move(self.move_distance)
            # add to delete pending
            if car.xcor() < -200:
                self.add_to_delete_pending(car)

        # delete
        delete_result = []
        for car in self.cars_list:
            if car not in self.delete_pending:
                delete_result.append(car)
            else:
                car.ht()
        self.cars_list = delete_result
        # refresh delete_pending
        self.delete_pending = []

    def level_up(self):
        self.move_distance += MOVE_INCREMENT



# create cars_list: append new element to it each time we create
# delete a car from the list when it reaches the end
# level up function that increase movement speed
