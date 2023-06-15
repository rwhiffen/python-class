# Rich Whiffen - 6/15/2023
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 54 - FLASK with Python
#

# decorators

import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
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
