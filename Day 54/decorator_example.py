import time


def speed_calc_decorator(function):
    def wrapper_function():
        pre_run = time.time()
        print(pre_run)

        function()

        after_run = time.time()
        print(after_run)

        run_time = after_run - pre_run
        print(f"Run Time: {run_time}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()