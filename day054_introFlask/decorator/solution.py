import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970

# Write your code below 👇


def speed_calc_decorator(function):
    def wrapper_function():
        function()
        return time.time() - current_time

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function_speed = fast_function()
current_time = time.time()
slow_function_speed = slow_function()
print(f"fast_function run speed: {fast_function_speed}")
print(f"slow_function run speed: {slow_function_speed}")
