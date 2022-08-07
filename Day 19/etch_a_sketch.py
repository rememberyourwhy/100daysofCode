from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def w():
    tim.forward(10)


def s():
    tim.backward(10)


def a():
    tim.left(15)


def d():
    tim.right(15)


def c():
    tim.pu()
    tim.clear()
    tim.home()
    tim.pd()



screen.listen()
# for kb_key in ["w", "s", "a", "d"]:
# screen.onkey(key=kb_key, fun=key_to_func_dict[kb_key])
screen.onkey(key="w", fun=w)
screen.onkey(key="s", fun=s)
screen.onkey(key="a", fun=a)
screen.onkey(key="d", fun=d)
screen.onkey(key="c", fun=c)



screen.exitonclick()