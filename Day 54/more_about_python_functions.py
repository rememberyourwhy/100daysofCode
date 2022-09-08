# Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2

# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)


# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function()
#
# inner_function = outer_function()
# inner_function()

import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        print("The function is delayed")
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


def say_bye():
    print("Bye")


say_hello()

decorated_bye = delay_decorator(say_bye)
decorated_bye()

