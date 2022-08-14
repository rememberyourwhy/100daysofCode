import turtle
import pandas
from rtree import index
from screenwriter import ScreenWriter

# Create screen object, change title
screen = turtle.Screen()
screen.title("U.S. States Game")

# Import image, show it on screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screenwriter = ScreenWriter()

idx = index.Index()


def find_nearest(x, y, rtree):
    global states_data_list
    hits = rtree.nearest((x, y, x, y), 1, objects=True)
    for rtree_ob in hits:
        print(rtree_ob.id)
        print(rtree_ob.bbox)
        print(states_data_list[rtree_ob.id][0])


def get_mouse_click_cor(x, y):
    turtle.onscreenclick(None)
    global idx
    find_nearest(x, y, rtree=idx)
    turtle.onscreenclick(get_mouse_click_cor)


# Convert states data so it's easier to use
states_data = pandas.read_csv("50_states.csv")
print(states_data)
states_data_list = []
for row in states_data.itertuples():
    states_data_list.append((row.state, (row.x, row.y)))
print(states_data_list)

# index to rtree object
for i in range(len(states_data_list)):
    x_cor = states_data_list[i][1][0]
    y_cor = states_data_list[i][1][1]
    idx.insert(i, (x_cor, y_cor, x_cor, y_cor))

turtle.onscreenclick(get_mouse_click_cor)

screen.mainloop()
