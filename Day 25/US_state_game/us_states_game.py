import turtle
import pandas
from screenwriter import ScreenWriter

# Create screen object, change title
screen = turtle.Screen()
screen.title("U.S. States Game")

# Import image, show it on screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screenwriter = ScreenWriter()


# import turtle
#
# def get_coor(x, y):
#     print(x, y)
#
# screen = turtle.Screen()
#
# turtle.onscreenclick(get_coor)
# screen.mainloop()
def get_mouse_click_cor(x, y):
    print(x, y)


states_data = pandas.read_csv("50_states.csv")
states_dict = states_data.to_dict()


turtle.onscreenclick(get_mouse_click_cor)

screenwriter.write("Hi", (0, 0))

screen.mainloop()








