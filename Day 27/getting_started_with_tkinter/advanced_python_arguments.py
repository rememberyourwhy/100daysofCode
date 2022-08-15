# Arguments without Default Values:

# Arguments with Default Values:

# def my_function(a=1, b=2, c=3):
#     pass
#
#
# # Unlimited Arguments:
#
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add())

def calculate(n, **kwargs):
    result = n
    result += kwargs["add"]
    result *= kwargs["multiply"]
    print(result)


calculate(2, add=3, multiply=5)
