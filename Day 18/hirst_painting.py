# import colorgram
#
# rgb_list = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     color_tuple = tuple(color.rgb)
#     rgb_list.append(color_tuple)
#
# print(rgb_list)
# rgb_list_fixed = []
# for index in range(len(rgb_list)):
#     color = rgb_list[index]
#     if not (color[0] > 200 and color[1] > 200 and color[2] > 200):
#         rgb_list_fixed.append(rgb_list[index])
#
#
# print(rgb_list_fixed)
# print(len(rgb_list_fixed))
import random
import turtle

data_color_list = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
    (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
    (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
    (176, 192, 208), (168, 99, 102)
]


def random_color():
    return data_color_list[random.randint(0, len(data_color_list) - 1)]


# create timmy object
timmy = turtle.Turtle()

# change color_mode
turtle.colormode(255)

# pen up so no arrow will be drawn
timmy.pu()

# set turtle position in the lower left corner of the screen
timmy.setposition(x=-250, y=-250)
timmy.dot(20, random_color())

x_coordinate = -250
y_coordinate = -250
run = True
while run:
    if y_coordinate == 250 and x_coordinate == 250:
        run = False
    elif x_coordinate == 250:
        timmy.sety(y_coordinate + 50)
        timmy.setx(-250)
        x_coordinate, y_coordinate = timmy.pos()
    else:
        timmy.setx(x_coordinate + 50)
        x_coordinate = timmy.pos()[0]
    timmy.dot(20, random_color())

screen = turtle.Screen()
screen.screensize(500, 500)
screen.exitonclick()
